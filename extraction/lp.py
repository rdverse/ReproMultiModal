import layoutparser as lp
import cv2

model = lp.AutoLayoutModel('lp://EfficientDete/PubLayNet')
image = cv2.imread("/home/devesh/Code/ReproMultiModal/test1images/fullimgs/image0.png")
layout = model.detect(image) 

# layout = model.detect(image
# image = 