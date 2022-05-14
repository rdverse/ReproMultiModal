import os
import sys
import cv2

# The coordinates defining the square selected will be kept in this list.
select_coords = []
# While we are in the process of selecting a region, this flag is True.
selecting = False

def get_square_coords(x, y, cx, cy):
    """
    Get the diagonally-opposite coordinates of the square.
    (cx, cy) are the coordinates of the square centre.
    (x, y) is a selected point to which the largest square is to be matched.

    """

    # Selected square edge half-length; don't stray outside the image boundary.
    a = max(abs(cx-x), abs(cy-y))
    a = min(a, w-cx, cx, h-cy, cy)
    return cx-a, cy-a, cx+a, cy+a


def region_selection(event, x, y, flags, param): 
    """Callback function to handle mouse events related to region selection."""
    global select_coords, selecting, image

    if event == cv2.EVENT_LBUTTONDOWN: 
        # Left mouse button down: begin the selection.
        # The first coordinate pair is the centre of the square.
        select_coords = [(x, y)]
        selecting = True

    elif event == cv2.EVENT_MOUSEMOVE and selecting:
        # If we're dragging the selection square, update it.
        image = clone.copy()
        x0, y0, x1, y1 = get_square_coords(x, y, *select_coords[0])
        cv2.rectangle(image, (x0, y0), (x1, y1), (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP: 
        # Left mouse button up: the selection has been made.
        select_coords.append((x, y))
        selecting = False


# Load the image and get its filename without path and dimensions.
filename = sys.argv[1]
basename = os.path.basename(filename)
image = cv2.imread(filename)
h, w = image.shape[:2]
# The cropped image will be saved with this filename.
cropped_filename = os.path.splitext(filename)[0] + '_sq.png'
cropped_basename = os.path.basename(cropped_filename)
# Store a clone of the original image (without selected region annotation).
clone = image.copy() 
# Name the main image window after the image filename.
cv2.namedWindow(basename) 
cv2.setMouseCallback(basename, region_selection)

# Keep looping and listening for user input until 'c' is pressed.
while True: 
    # Display the image and wait for a keypress 
    cv2.imshow(basename, image) 
    key = cv2.waitKey(1) & 0xFF
    # If 'c' is pressed, break from the loop and handle any region selection.
    if key == ord("c"): 
        break

# Did we make a selection?
if len(select_coords) == 2: 
    cx, cy = select_coords[0]
    x, y = select_coords[1]
    x0, y0, x1, y1 = get_square_coords(x, y, cx, cy)
    # Crop the image to the selected region and display in a new window.
    cropped_image = clone[y0:y1, x0:x1]
    cv2.imshow(cropped_basename, cropped_image) 
    cv2.imwrite(cropped_filename, cropped_image)
    # Wait until any key press.
    cv2.waitKey(0)

# We're done: close all open windows before exiting.
cv2.destroyAllWindows()