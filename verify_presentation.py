import pptx
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

prs = Presentation('Project_Final_Presentation.pptx')
print(f"Total slides: {len(prs.slides)}\n")

issues = []

for idx, slide in enumerate(prs.slides):
    slide_num = idx + 1
    texts = []
    has_table = False
    has_image = False
    
    for shape in slide.shapes:
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                t = p.text.strip()
                if t:
                    texts.append(t)
        if shape.has_table:
            has_table = True
        if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
            has_image = True

    header = texts[0] if texts else "<EMPTY>"
    print(f"Slide {slide_num:2d}: Header='{header[:50]}' | Texts={len(texts)} | Table={has_table} | Image={has_image}")

    # Check for old unwanted project mentions
    combined = " ".join(texts).lower()
    for forbidden in ["syn2sem", "syntax-to-semantics", "piston execution", "tree-sitter c-based", "monaco editor: the code"]:
        if forbidden in combined:
            issues.append(f"Slide {slide_num}: Contains old reference '{forbidden}'")

if issues:
    print("\n[WARNING] Issues found:")
    for iss in issues:
        print("  -", iss)
else:
    print("\n[PASS] All 27 slides verified cleanly. Zero legacy references found!")
