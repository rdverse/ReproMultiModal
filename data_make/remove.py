import os
import re
import glob
import tqdm
import shutil


def remove_processed_files():

    files = [f.strip(".json") for f in os.listdir("pdfs_figures/data")]

    for file in files:

        try:
            os.remove(os.path.join("pdfsminmin", file + ".pdf"))
        except:
            print("failed to remove " + file)
            pass

        print(file + " removed")


def select_Figures():
    imagesPATH = "pdfs_figures/allimages/"
    newImagesPATH = "pdfs_figures/images/"
    allimages = glob.glob(imagesPATH + "*.png")

    for imagePATH in tqdm.tqdm(allimages):
        # All figures have Figure in their file name
        # All tables have Table in their file name
        imageName = imagePATH.split("/")[-1]
        # print(imageName)
        if re.search("Figure", imagePATH):
            shutil.copy(imagePATH, os.path.join(newImagesPATH, imageName))


if __name__ == "__main__":
    select_Figures()
