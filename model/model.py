
from transformers import ViltProcessor, ViltModel
from PIL import Image
import requests
import os
# prepare image and text
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)
text = "hello world"

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-mlm")
model = ViltModel.from_pretrained("dandelin/vilt-b32-mlm")

inputs = processor(image, text, return_tensors="pt")
outputs = model(**inputs)



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
    
# last_hidden_states = outputs.last_hidden_state,