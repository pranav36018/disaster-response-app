import pptx
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

prs = Presentation('phase_2_ppt_syn2sem_reference.pptx')
print(f"Slide width: {prs.slide_width}, height: {prs.slide_height}")
print(f"Total slides: {len(prs.slides)}\n")

for idx, slide in enumerate(prs.slides):
    print(f"==================================================")
    print(f"SLIDE {idx+1}")
    print(f"==================================================")
    for s_idx, shape in enumerate(slide.shapes):
        st = shape.shape_type
        print(f"Shape {s_idx}: Name='{shape.name}', Type={st}, Left={shape.left}, Top={shape.top}, W={shape.width}, H={shape.height}")
        if shape.has_text_frame:
            tf = shape.text_frame
            for p_idx, p in enumerate(tf.paragraphs):
                p_text = p.text
                font_names = set(r.font.name for r in p.runs if r.font.name)
                font_sizes = set(r.font.size.pt for r in p.runs if r.font.size)
                colors = []
                for r in p.runs:
                    if r.font.color and r.font.color.type:
                        try:
                            colors.append(str(r.font.color.rgb))
                        except Exception:
                            colors.append("theme")
                print(f"  [P{p_idx}] (Fonts={font_names}, Sizes={font_sizes}, Colors={set(colors)}, Bullet={p.level}) : {p_text}")
        if shape.has_table:
            t = shape.table
            print(f"  [TABLE] {len(t.rows)} rows x {len(t.columns)} cols")
            for r_idx, row in enumerate(t.rows):
                vals = [c.text.strip().replace('\n', ' ') for c in row.cells]
                print(f"    R{r_idx}: {vals}")
        if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
            print(f"  [PICTURE] Content type: {shape.image.content_type}, Size: {len(shape.image.blob)} bytes")
