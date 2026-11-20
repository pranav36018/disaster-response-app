import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont

os.makedirs('generated_images', exist_ok=True)

# -----------------------------------------------------------------------------
# 1. Slide 5 Image: Literature Survey Comparison Table (image3.png: 1439 x 1093)
# -----------------------------------------------------------------------------
def generate_slide5_table():
    width, height = 1439, 1093
    img = Image.new('RGB', (width, height), color='#070d18')
    draw = ImageDraw.Draw(img)

    # Header title banner
    draw.rectangle([0, 0, width, 90], fill='#0a192f')
    draw.rectangle([0, 86, width, 90], fill='#00d2ff')

    # Try default fonts
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 36)
        font_th = ImageFont.truetype("arialbd.ttf", 26)
        font_tb = ImageFont.truetype("arial.ttf", 21)
        font_tbb = ImageFont.truetype("arialbd.ttf", 21)
    except:
        font_title = font_th = font_tb = font_tbb = ImageFont.load_default()

    draw.text((width // 2, 45), "Comparative Evaluation: Disaster Management & Decision Systems", fill='#ffffff', font=font_title, anchor='mm')

    # Table layout
    headers = ["System / Platform", "Organization & Year", "Core Architecture", "Critical Limitations", "How Crisis Intelligence Hub Solves It"]
    col_widths = [240, 210, 310, 310, 369]
    col_x = [0]
    for w in col_widths:
        col_x.append(col_x[-1] + w)

    # Draw Table Header
    y_start = 110
    row_h = 65
    draw.rectangle([0, y_start, width, y_start + row_h], fill='#002060')
    for i, h in enumerate(headers):
        draw.text((col_x[i] + 15, y_start + row_h // 2), h, fill='#00ffff', font=font_th, anchor='lm')
        if i > 0:
            draw.line([(col_x[i], y_start), (col_x[i], height - 20)], fill='#1e3a5f', width=2)

    rows_data = [
        ("GDACS Multi-Hazard", "UN & EC (2020)", "Passive RSS/CAP feed aggregation with static global alert levels.", "Lacks local hydrodynamic modeling; zero route optimization or explainability.", "Ingests live feeds with calibrated local ML risk probabilities and tree-path XAI."),
        ("FEMA Hazus / NDMA", "Federal Agencies (2021)", "Desktop GIS software with post-disaster loss calculation models.", "Batch/offline calculation; non-real-time; manual shelter and asset coordination.", "Sub-second live telemetry caching, real-time Digital Twin and resource dispatch."),
        ("Google Flood Hub", "Google AI (2023)", "Gauging station LSTM neural network river discharge forecasting.", "Flood-only (single hazard); black-box predictions without operational routing.", "Multi-hazard coverage (Flood, Wildfire, Quake) with Multi-Criteria A* Evacuation."),
        ("Traditional 911 CAD", "Public Safety (2022)", "Relational incident tracking with manual radio/telephone coordination.", "Average 130-minute decision latency; high cognitive overload; unverified ICU beds.", "Capability-matched automated rescue dispatch with 72x faster decision latency (1.8m)."),
        ("Crisis Intelligence Hub\n(Our Project)", "SVIT ISE Dept.\n(2026)", "3-Tier Cloud Architecture: FastAPI ML, Node.js Gateway & React PWA.", "None — Complete multi-hazard telemetry fusion, Digital Twin & Coordinator Ledger.", "Validated ML (72% Acc, 0.885 AUC), 0h-48h Physics Twin & Offline SOS sync.")
    ]

    y = y_start + row_h
    row_heights = [170, 170, 170, 180, 200]
    for r_idx, (r_data, rh) in enumerate(zip(rows_data, row_heights)):
        bg_color = '#0c1b30' if r_idx % 2 == 0 else '#081322'
        if r_idx == 4:
            bg_color = '#0f2b48'  # Highlight our project
        draw.rectangle([0, y, width, y + rh], fill=bg_color)
        draw.line([(0, y), (width, y)], fill='#1e3a5f', width=2)

        for c_idx, text in enumerate(r_data):
            tx = col_x[c_idx] + 15
            ty = y + 15
            fnt = font_tbb if (c_idx == 0 or r_idx == 4) else font_tb
            color = '#38bdf8' if r_idx == 4 and c_idx == 0 else ('#ffffff' if r_idx == 4 else '#e2e8f0')
            if c_idx == 4:
                color = '#4ade80' if r_idx == 4 else '#93c5fd'
            
            # Simple text wrap
            words = text.split()
            lines = []
            cur_line = []
            max_char = int(col_widths[c_idx] / 12)
            for w in words:
                if '\n' in w:
                    parts = w.split('\n')
                    cur_line.append(parts[0])
                    lines.append(' '.join(cur_line))
                    cur_line = [parts[1]]
                elif len(' '.join(cur_line + [w])) <= max_char:
                    cur_line.append(w)
                else:
                    lines.append(' '.join(cur_line))
                    cur_line = [w]
            if cur_line:
                lines.append(' '.join(cur_line))

            for l_idx, line in enumerate(lines):
                draw.text((tx, ty + l_idx * 27), line, fill=color, font=fnt)

        y += rh

    draw.rectangle([0, height - 15, width, height], fill='#00d2ff')
    img.save('generated_images/image3.png')
    print("Generated image3.png")

generate_slide5_table()
