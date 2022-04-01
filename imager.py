import os
import tqdm
import shutil
import pandas as pd
import matplotlib.pyplot as plt
from pdf2image import convert_from_path

from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)

PATHsave = 'reproducibility/acm_full_pdfs/pdfs_to_imgs'
PATH = 'reproducibility/acm_full_pdfs/pdfs'


def convert_pdfs_to_images():

    for root, dirs,files in os.walk(PATH):
        
        for file in tqdm.tqdm(files):
            filePATH = os.path.join(root, file)
            try:
                images = convert_from_path(filePATH)
            except:
                print("This pdf could not be converted : {}".format(filePATH))
            for i, image in enumerate(images):
                fname = file + str(i)+'.png'
                imagePATH = os.path.joinc
    values = df.groupby('file').size().values
    plt.hist(values)
    plt.xlabel('Number of pages')
    plt.ylabel('Number of pdfs')
    plt.show()
    print(values)

if __name__=='__main__':
    df = get_converted_pdf_stats()
    plot_hist(df)