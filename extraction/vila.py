import layoutparser as lp # For visualization 

from vila.pdftools.pdf_extractor import PDFExtractor
from vila.predictors import HierarchicalPDFPredictor
# Choose from SimplePDFPredictor,
# LayoutIndicatorPDFPredictor, 
# and HierarchicalPDFPredictor

pdf_extractor = PDFExtractor("pdfplumber")
page_tokens, page_images = pdf_extractor.load_tokens_and_image(f"test1.pdf")

vision_model = lp.EfficientDetLayoutModel("lp://PubLayNet") 
# pdf_predictor = HierarchicalPDFPredictor.from_pretrained("allenai/hvila-row-layoutlm-finetuned-docbank")
pdf_predictor = HierarchicalPDFPredictor.from_pretrained("allenai/ivila-block-layoutlm-finetuned-grotoap2")



for idx, page_token in enumerate(page_tokens):
    blocks = vision_model.detect(page_images[idx])
    page_token.annotate(blocks=blocks)
    pdf_data = page_token.to_pagedata().to_dict()
    predicted_tokens = pdf_predictor.predict(pdf_data)
    lp.draw_box(page_images[idx], predicted_tokens, box_width=0, box_alpha=0.25)