'''
This script is to convert the whole images to feature vectors into a json dataset format
Currently it is hardcoded to taking first page of the pdf
Change _0.png to desired page
'''
import os
import tqdm
import json
import pandas as pd
import numpy as np
from PIL import Image

PATHImages = 'reproducibility/acm_full_pdfs/pdfs_to_imgs'
PATH = 'reproducibility/acm_full_pdfs/pdfs'
labelFileName = "labelData.csv"

def save_image_file_json():
    labeldf = pd.read_csv(labelFileName)
    print(labeldf.columns)
    files = labeldf["fileName"].values
    labels = labeldf.drop(columns = "fileName").values
    
    images = list()
    for fileName in tqdm.tqdm(files):
        image = np.asarray(Image.open(os.path.join(PATHImages, fileName + "_0.png")))
        image = image.tolist()
        images.append(list(image))

    saveData = dict()
    saveData["labels"] = labels
    saveData["values"] = images
    saveData["classes"] = labeldf.drop(columns = "fileName").columns.values
    
    with open("reproducibility_firstpage.json", "w") as jsonFile:
        json.dump(saveData, jsonFile)   

if __name__=='__main__':
    save_image_file_json()