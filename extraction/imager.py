from json.encoder import py_encode_basestring_ascii
import os
import io
import tqdm
import shutil
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from pdf2image import convert_from_path

from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)

PATHsave = 'reproducibility/acm_full_pdfs/pdfs_to_imgs'
PATH = 'reproducibility/acm_full_pdfs/pdfs'

def get_rcParams(plt):
    plt.rcParams['font.size'] = 12
    plt.rcParams['hatch.linewidth'] = 0.25
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'Times New Roman'
    plt.rcParams['figure.dpi'] = 600
    plt.rcParams["lines.linewidth"] = 1
    plt.rcParams['hatch.linewidth'] = 0.15
    return plt

def convert_pdfs_to_images():
    count = 0
    for root, dirs, files in os.walk(PATH):
        
        for file in tqdm.tqdm(files):
            count=count+1
            filePATH = os.path.join(root, file)
            try:
                images = convert_from_path(filePATH)
            except:
                print("This pdf could not be converted : {}".format(filePATH))
                continue
            for i, image in enumerate(images):
                # create the image path to save
                fname = file + '_' + str(i) + '.png'
                imagePATH = os.path.join(PATHsave, fname)
                # Save the image 
                image.save(imagePATH)


def get_converted_pdf_stats():
    imageNames = os.listdir(PATHsave)
    # Get rid of the png extention for each image
    imageNames = [name.strip(".png") for name in imageNames]
    # split name by id and page number
    imageNames = [name.split('_') for name in imageNames]
    print(imageNames)
    df = pd.DataFrame(imageNames, columns = ["pdfName", "page"])
    pages= df.groupby('pdfName').count().values.flatten()
    return df,pages

def plot_hist(pages,plt):
    nbins=12
    plt = get_rcParams(plt)
    arr = plt.hist(pages,bins=nbins)
    plt.xlabel('Count of pages')
    plt.ylabel('Count of scholarly articles')
    for i in range(nbins):
        if int(arr[0][i])!=0:
            plt.text(arr[1][i],arr[0][i],str(int(arr[0][i])), size=8)
    fig = plt.gcf()
    fig.set_size_inches(3,3)
    plt.tight_layout()
    plt.savefig("figures/data/pageHist.png")
    plt.show()
    return None

if __name__=='__main__':
    # convert_pdfs_to_images()
    df,pages = get_converted_pdf_stats()
    plot_hist(pages,plt)