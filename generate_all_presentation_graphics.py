import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont

os.makedirs('generated_images', exist_ok=True)

try:
    font_title = ImageFont.truetype("arialbd.ttf", 34)
    font_subtitle = ImageFont.truetype("arialbd.ttf", 26)
    font_bold = ImageFont.truetype("arialbd.ttf", 20)
    font_regular = ImageFont.truetype("arial.ttf", 18)
    font_small = ImageFont.truetype("arial.ttf", 15)
    font_mono = ImageFont.truetype("consola.ttf", 18)
    font_monobd = ImageFont.truetype("consolab.ttf", 20)
except:
    font_title = font_subtitle = font_bold = font_regular = font_small = font_mono = font_monobd = ImageFont.load_default()

# -----------------------------------------------------------------------------
# 2. Slide 9: System Architecture Diagram (image4.jpeg: 1280 x 743)
# -----------------------------------------------------------------------------
def generate_system_architecture():
    w, h = 1280, 743
    img = Image.new('RGB', (w, h), color='#070e1b')
    draw = ImageDraw.Draw(img)

    # Top Header
    draw.rectangle([0, 0, w, 70], fill='#0b1d3a')
    draw.line([(0, 68), (w, 68)], fill='#00d2ff', width=3)
    draw.text((w//2, 35), "CRISIS INTELLIGENCE HUB: 3-TIER SYSTEM ARCHITECTURE", fill='#ffffff', font=font_title, anchor='mm')

    # Main Left Container (Core System)
    core_w = 930
    draw.rectangle([25, 85, core_w, h - 25], outline='#1e3a5f', width=2, fill='#0a1526')

    # Section 1: Presentation Layer
    draw.rectangle([40, 100, core_w - 15, 230], outline='#0284c7', width=2, fill='#0c2240')
    draw.rectangle([40, 100, core_w - 15, 132], fill='#0369a1')
    draw.text((55, 116), "1. PRESENTATION & COMMAND HUD LAYER (REACT 19 + VITE + TAILWIND // PORT 5173)", fill='#ffffff', font=font_bold, anchor='lm')
    
    hud_boxes = [
        ("Tactical War Room HUD\n• Real-Time Vector Map\n• Zulu Clock & Threat Level\n• Threat Radar Markers", 55, 142, 255, 78),
        ("Disaster Digital Twin\n• 0h-48h Iso-Contours\n• Manning Surge Sim\n• Rothermel Fire Spread", 325, 142, 260, 78),
        ("Voice SITREP & XAI\n• Web Speech Synthesizer\n• Tree-Path SHAP Modal\n• Plain-Text Action Tips", 600, 142, 255, 78),
        ("Citizen SOS & Replay\n• Offline IndexedDB Sync\n• Proximity Deduplication\n• 72x AAR CSV Export", 870, 142, 40, 78) # adjusted below
    ]
    # Re-layout presentation boxes
    p_box_w = 205
    for i, (b_title, b_desc) in enumerate([
        ("Tactical War Room HUD", "• Real-Time Vector Map\n• Zulu Military HUD\n• Multi-Hazard Markers"),
        ("Disaster Digital Twin", "• 0h-48h Surge Sim\n• Impassable Roads\n• Rothermel Wildfire"),
        ("AI Decision Support", "• Tree-Path SHAP XAI\n• Multi-Criteria A*\n• Shelter Capacity"),
        ("Citizen SOS Portal", "• Offline IndexedDB\n• Proximity Dedup\n• Voice SITREP Audio")
    ]):
        bx = 55 + i * (p_box_w + 12)
        draw.rectangle([bx, 142, bx + p_box_w, 218], fill='#081a33', outline='#38bdf8', width=1)
        draw.text((bx + 10, 155), b_title, fill='#38bdf8', font=font_bold)
        draw.text((bx + 10, 175), b_desc, fill='#cbd5e1', font=font_small)

    # Down Arrow 1
    draw.polygon([(core_w//2 - 15, 235), (core_w//2 + 15, 235), (core_w//2, 250)], fill='#00d2ff')

    # Section 2: Backend Orchestration Layer
    draw.rectangle([40, 255, core_w - 15, 475], outline='#10b981', width=2, fill='#062326')
    draw.rectangle([40, 255, core_w - 15, 287], fill='#047857')
    draw.text((55, 271), "2. BACKEND ORCHESTRATION & RELIABILITY GATEWAY (EXPRESS NODE.JS // PORT 5000)", fill='#ffffff', font=font_bold, anchor='lm')

    b_box_w = 205
    for i, (b_title, b_desc) in enumerate([
        ("Telemetry Ingestion", "• Open-Meteo Weather\n• CWC River Discharge\n• USGS Seismic Feeds\n• NASA FIRMS Satellites"),
        ("Reliability Engine", "• Exponential Backoff\n• Randomized Jitter\n• In-Memory Cache\n• Multi-Tier Attribution"),
        ("Evacuation Navigator", "• Multi-Criteria A*\n• Hazard Avoidance\n• Primary & Alternates\n• Civil Shelter Ledger"),
        ("Smart Rescue Dispatch", "• Capability Matching\n• Water Rescue / ALS\n• Trauma ICU Beds Free\n• Coordinator Sign-Off")
    ]):
        bx = 55 + i * (b_box_w + 12)
        draw.rectangle([bx, 297, bx + b_box_w, 460], fill='#041b1d', outline='#34d399', width=1)
        draw.text((bx + 10, 312), b_title, fill='#34d399', font=font_bold)
        draw.text((bx + 10, 338), b_desc, fill='#e2e8f0', font=font_small)

    # Down Arrow 2
    draw.polygon([(core_w//2 - 15, 480), (core_w//2 + 15, 480), (core_w//2, 495)], fill='#00d2ff')

    # Section 3: Python ML Microservice
    draw.rectangle([40, 500, core_w - 15, h - 40], outline='#f59e0b', width=2, fill='#251806')
    draw.rectangle([40, 500, core_w - 15, 532], fill='#b45309')
    draw.text((55, 516), "3. PYTHON FASTAPI ML & XAI PREDICTION MICROSERVICE (UVICORN // PORT 8000)", fill='#ffffff', font=font_bold, anchor='lm')

    m_box_w = 276
    for i, (b_title, b_desc) in enumerate([
        ("CalibratedClassifierCV Models", "• 150-Tree Random Forest Ensemble\n• Sigmoid Probability Calibration\n• Flood (72.0% Acc, 0.885 ROC-AUC)\n• Wildfire Model (66.9% Accuracy)"),
        ("Tree-Path Explainable AI (XAI)", "• Root-to-Leaf Path Traversal\n• Exact Feature Contribution Deltas\n• SHAP-Aligned Attributions\n• Plain-Text Commander Advice"),
        ("Physics-Based Digital Twin", "• Manning Open-Channel Hydrology\n• Rothermel Surface Fire Spread\n• Atkinson-Boore Ground Motion\n• Bounded Uncertainty (0.09 - 0.14)")
    ]):
        bx = 55 + i * (m_box_w + 17)
        draw.rectangle([bx, 542, bx + m_box_w, h - 55], fill='#1c1204', outline='#fbbf24', width=1)
        draw.text((bx + 10, 555), b_title, fill='#fbbf24', font=font_bold)
        draw.text((bx + 10, 580), b_desc, fill='#fef3c7', font=font_small)

    # Right Container: External Integrations & Data Feeds
    draw.rectangle([core_w + 15, 85, w - 25, h - 25], outline='#818cf8', width=2, fill='#11152d')
    draw.rectangle([core_w + 15, 85, w - 25, 117], fill='#4338ca')
    draw.text((core_w + 25, 101), "LIVE SENSORS & APIS", fill='#ffffff', font=font_bold, anchor='lm')

    for i, (b_title, b_desc) in enumerate([
        ("Open-Meteo Weather API", "Global Precipitation & Rain Rate"),
        ("Open-Meteo Flood GloFAS", "River Discharge & Indian Basins"),
        ("USGS Seismic Feed", "Real-Time Earthquake Catalogs"),
        ("NASA FIRMS Satellite", "VIIRS/MODIS Active Thermal Hotspots"),
        ("Grounded AI Copilot", "Natural Language SITREP Queries"),
        ("IndexedDB PWA Sync", "Offline Citizen SOS Reports"),
        ("Civil Defense Registry", "Shelters & Trauma ICU Hospital Beds")
    ]):
        sy = 127 + i * 82
        draw.rectangle([core_w + 25, sy, w - 35, sy + 72], fill='#0c0f20', outline='#a5b4fc', width=1)
        draw.text((core_w + 35, sy + 15), b_title, fill='#c7d2fe', font=font_bold)
        draw.text((core_w + 35, sy + 40), b_desc, fill='#94a3b8', font=font_small)

    img.save('generated_images/image4.jpeg', quality=95)
    print("Generated image4.jpeg")

generate_system_architecture()

# -----------------------------------------------------------------------------
# 3. Slide 10: Data Flow Between Modules (image5.png: 1672 x 941)
# -----------------------------------------------------------------------------
def generate_data_flowchart():
    w, h = 1672, 941
    img = Image.new('RGB', (w, h), color='#060c18')
    draw = ImageDraw.Draw(img)

    # Header
    draw.rectangle([0, 0, w, 80], fill='#0a1e38')
    draw.line([(0, 78), (w, 78)], fill='#00e5ff', width=3)
    draw.text((w//2, 40), "CRISIS INTELLIGENCE HUB — SYSTEM DATA FLOWCHART", fill='#ffffff', font=font_title, anchor='mm')

    col1_x = 420
    col2_x = 1250

    nodes = [
        # Col 1
        ("START", col1_x, 140, "pill", '#10b981', '#ffffff', "Initialize Command Hub & Telemetry Listeners"),
        ("Ingest Live Multi-Hazard Telemetry", col1_x, 260, "rect", '#0284c7', '#ffffff', "Open-Meteo Precipitation, CWC Basins, USGS, NASA FIRMS"),
        ("Reliability & Attribution Filter", col1_x, 380, "diamond", '#eab308', '#000000', "Validate Cache / Exponential Backoff / Tag Source"),
        ("Feature Matrix Preprocessing", col1_x, 520, "rect", '#6366f1', '#ffffff', "Normalize River Discharge, 7d Rain, Elevation, Saturation"),
        ("Calibrated ML Risk Inference", col1_x, 650, "rect", '#8b5cf6', '#ffffff', "150-Tree RF + Sigmoid Calibration (Flood / Wildfire)"),
        ("Tree-Path SHAP Decomposition", col1_x, 780, "rect", '#ec4899', '#ffffff', "Compute Feature Contribution Deltas & Plain-Text Tips"),
        
        # Col 2
        ("Disaster Digital Twin: 0h-48h Sim", col2_x, 780, "rect", '#f97316', '#ffffff', "Manning's Hydrodynamic Surge & Rothermel Fire Spread"),
        ("Multi-Criteria A* Evacuation Routing", col2_x, 650, "rect", '#06b6d4', '#ffffff', "Buffer Hazard Perimeters & Verify Civil Shelter Beds"),
        ("Smart Rescue Capability Matching", col2_x, 520, "rect", '#14b8a6', '#ffffff', "Match Water Rescue/ALS Teams & Trauma ICU Beds"),
        ("Coordinator Authorization Sign-Off?", col2_x, 380, "diamond", '#f59e0b', '#000000', "Human-in-the-Loop Audit Ledger Verification"),
        ("Command HUD & SITREP Broadcast", col2_x, 260, "rect", '#3b82f6', '#ffffff', "Update Live Map, Voice SITREP Synthesizer, PWA"),
        ("END", col2_x, 140, "pill", '#ef4444', '#ffffff', "Mission Recorded to AAR CSV Ledger")
    ]

    node_rects = {}
    for text, cx, cy, ntype, color, text_color, subtitle in nodes:
        nw, nh = 680, 75
        if ntype == "diamond":
            nw, nh = 620, 85
        x1, y1 = cx - nw//2, cy - nh//2
        x2, y2 = cx + nw//2, cy + nh//2
        node_rects[text] = (cx, cy, x1, y1, x2, y2)

        if ntype == "pill":
            draw.rounded_rectangle([x1, y1, x2, y2], radius=35, fill=color, outline='#ffffff', width=2)
            draw.text((cx, cy), text, fill=text_color, font=font_bold, anchor='mm')
        elif ntype == "diamond":
            pts = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
            draw.polygon(pts, fill=color, outline='#ffffff')
            draw.text((cx, cy - 8), text, fill=text_color, font=font_bold, anchor='mm')
            draw.text((cx, cy + 16), subtitle, fill='#1f2937', font=font_small, anchor='mm')
        else:
            draw.rounded_rectangle([x1, y1, x2, y2], radius=10, fill=color, outline='#ffffff', width=2)
            draw.text((cx, cy - 12), text, fill=text_color, font=font_bold, anchor='mm')
            draw.text((cx, cy + 14), subtitle, fill='#f1f5f9', font=font_small, anchor='mm')

    arrow_color = '#00e5ff'
    for i in range(5):
        _, cy1, _, _, _, y2 = node_rects[nodes[i][0]]
        _, cy2, _, y1_next, _, _ = node_rects[nodes[i+1][0]]
        draw.line([(col1_x, y2), (col1_x, y1_next)], fill=arrow_color, width=3)
        draw.polygon([(col1_x - 7, y1_next - 10), (col1_x + 7, y1_next - 10), (col1_x, y1_next)], fill=arrow_color)

    _, _, _, _, x2_b, _ = node_rects[nodes[5][0]]
    _, _, x1_r, _, _, _ = node_rects[nodes[6][0]]
    draw.line([(x2_b, 780), (x1_r, 780)], fill=arrow_color, width=3)
    draw.polygon([(x1_r - 10, 773), (x1_r - 10, 787), (x1_r, 780)], fill=arrow_color)

    for i in range(6, 11):
        _, cy1, _, y1_prev, _, _ = node_rects[nodes[i][0]]
        _, cy2, _, _, _, y2_next = node_rects[nodes[i+1][0]]
        draw.line([(col2_x, y1_prev), (col2_x, y2_next)], fill=arrow_color, width=3)
        draw.polygon([(col2_x - 7, y2_next + 10), (col2_x + 7, y2_next + 10), (col2_x, y2_next)], fill=arrow_color)

    img.save('generated_images/image5.png')
    print("Generated image5.png")

# -----------------------------------------------------------------------------
# 4. Slide 11: Detailed Module Design (image6.jpeg: 1280 x 807)
# -----------------------------------------------------------------------------
def generate_module_design_dfd():
    w, h = 1280, 807
    img = Image.new('RGB', (w, h), color='#070f1e')
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, w, 65], fill='#0b2247')
    draw.line([(0, 63), (w, 63)], fill='#00d2ff', width=3)
    draw.text((w//2, 32), "HIGH-LEVEL DATA FLOW (LEVEL 0) & DETAILED DATA FLOW (LEVEL 1)", fill='#ffffff', font=font_subtitle, anchor='mm')

    # Top Section: Level 0 Context DFD
    draw.rectangle([20, 75, w - 20, 260], fill='#0a182e', outline='#0284c7', width=2)
    draw.rectangle([20, 75, 340, 105], fill='#0369a1')
    draw.text((30, 90), "LEVEL 0 CONTEXT DIAGRAM", fill='#ffffff', font=font_bold, anchor='lm')

    draw.rectangle([45, 125, 290, 240], fill='#0c274c', outline='#38bdf8', width=2)
    draw.text((167, 145), "EXTERNAL SOURCES", fill='#38bdf8', font=font_bold, anchor='mm')
    draw.text((167, 185), "• Open-Meteo Weather/Floods\n• USGS Earthquake Feed\n• NASA FIRMS Satellite", fill='#e2e8f0', font=font_small, anchor='mm')

    draw.ellipse([460, 115, 820, 250], fill='#1e293b', outline='#00e5ff', width=3)
    draw.text((640, 160), "0.0 CRISIS INTELLIGENCE", fill='#ffffff', font=font_bold, anchor='mm')
    draw.text((640, 185), "COMMAND PLATFORM", fill='#00e5ff', font=font_bold, anchor='mm')
    draw.text((640, 215), "(Central Hub Engine)", fill='#94a3b8', font=font_small, anchor='mm')

    draw.rectangle([990, 125, 1235, 240], fill='#0c274c', outline='#38bdf8', width=2)
    draw.text((1112, 145), "END ACTORS", fill='#38bdf8', font=font_bold, anchor='mm')
    draw.text((1112, 185), "• Incident Commander\n• NDRF & Fire Dispatchers\n• Citizens (Offline SOS)", fill='#e2e8f0', font=font_small, anchor='mm')

    draw.line([(290, 182), (460, 182)], fill='#00e5ff', width=3)
    draw.text((375, 170), "Telemetry Feeds", fill='#7dd3fc', font=font_small, anchor='mm')
    draw.polygon([(460, 182), (445, 175), (445, 189)], fill='#00e5ff')

    draw.line([(820, 182), (990, 182)], fill='#00e5ff', width=3)
    draw.text((905, 170), "SITREP & Orders", fill='#7dd3fc', font=font_small, anchor='mm')
    draw.polygon([(990, 182), (975, 175), (975, 189)], fill='#00e5ff')

    # Bottom Section: Level 1 DFD
    draw.rectangle([20, 275, w - 20, h - 20], fill='#091426', outline='#10b981', width=2)
    draw.rectangle([20, 275, 340, 305], fill='#047857')
    draw.text((30, 290), "LEVEL 1 DETAILED DATA FLOW", fill='#ffffff', font=font_bold, anchor='lm')

    l1_procs = [
        ("1.0 Ingestion &\nReliability Cache", 140, 370),
        ("2.0 Calibrated ML\nPrediction & XAI", 390, 370),
        ("3.0 Digital Twin\nPhysics Simulation", 640, 370),
        ("4.0 Evacuation &\nResource Dispatch", 890, 370),
        ("5.0 Tactical HUD &\nAAR Replay Engine", 1140, 370)
    ]
    for p_title, px, py in l1_procs:
        draw.ellipse([px - 95, py - 45, px + 95, py + 45], fill='#0f332d', outline='#34d399', width=2)
        draw.text((px, py), p_title, fill='#ffffff', font=font_bold, anchor='mm')

    for i in range(4):
        x_from = l1_procs[i][1] + 95
        x_to = l1_procs[i+1][1] - 95
        draw.line([(x_from, 370), (x_to, 370)], fill='#34d399', width=3)
        draw.polygon([(x_to, 370), (x_to - 10, 364), (x_to - 10, 376)], fill='#34d399')

    stores = [
        ("D1 Telemetry & Caching Store", 140, 480),
        ("D2 Serialized RF & Sigmoid Models", 390, 480),
        ("D3 Digital Twin Scenario Basins", 640, 480),
        ("D4 Shelter & Asset Fleet Registry", 890, 480),
        ("D5 Coordinator Audit Sign-Off Ledger", 1140, 480)
    ]
    for s_title, sx, sy in stores:
        draw.rectangle([sx - 110, sy, sx + 110, sy + 55], fill='#182030', outline='#f59e0b', width=2)
        draw.line([(sx - 95, sy), (sx - 95, sy + 55)], fill='#f59e0b', width=2)
        draw.text((sx + 5, sy + 27), s_title, fill='#fef3c7', font=font_small, anchor='mm')
        draw.line([(sx, 415), (sx, sy)], fill='#f59e0b', width=2)

    draw.rectangle([45, 560, w - 45, h - 35], fill='#0b192e', outline='#3b82f6', width=1)
    draw.text((60, 580), "CORE ENGINEERING MECHANISMS:", fill='#38bdf8', font=font_bold)
    draw.text((60, 610), "• Process 1.0 enforces exponential backoff retry algorithms with randomized jitter and multi-tier attribution labeling.", fill='#cbd5e1', font=font_small)
    draw.text((60, 635), "• Process 2.0 decomposes random forest tree paths into SHAP-aligned feature contributions (72.0% Acc, 0.885 ROC-AUC).", fill='#cbd5e1', font=font_small)
    draw.text((60, 660), "• Process 3.0 simulates 0h-48h hazard propagation using Manning's open-channel hydrology and Rothermel wildfire equations.", fill='#cbd5e1', font=font_small)
    draw.text((60, 685), "• Process 4.0 performs multi-criteria A* hazard avoidance routing and verifies real trauma hospital ICU bed capacity.", fill='#cbd5e1', font=font_small)
    draw.text((60, 710), "• Process 5.0 enforces human-in-the-loop coordinator approval logging and provides 72x operational decision speedup.", fill='#cbd5e1', font=font_small)

    img.save('generated_images/image6.jpeg', quality=95)
    print("Generated image6.jpeg")

generate_data_flowchart()
generate_module_design_dfd()

# -----------------------------------------------------------------------------
# 5. Slide 20, Image 1: Tactical Command War Room HUD (image7.jpeg: 1392 x 662)
# -----------------------------------------------------------------------------
def generate_snapshot_1():
    w, h = 1392, 662
    img = Image.new('RGB', (w, h), color='#070d18')
    draw = ImageDraw.Draw(img)

    # Top Command Bar
    draw.rectangle([0, 0, w, 55], fill='#0b192e')
    draw.line([(0, 53), (w, 53)], fill='#00e5ff', width=2)
    draw.text((25, 27), "CRISIS INTELLIGENCE HUB  //  TACTICAL COMMAND CENTER HUD", fill='#ffffff', font=font_bold, anchor='lm')
    draw.text((w - 25, 27), "STATUS: OPERATIONAL  |  ZULU TIME: 05:45:12Z  |  SECTOR: BENGALURU-BELAGAVI", fill='#38bdf8', font=font_mono, anchor='rm')

    # Threat Banner
    draw.rectangle([0, 55, w, 95], fill='#450a0a')
    draw.line([(0, 95), (w, 95)], fill='#ef4444', width=2)
    draw.text((25, 75), "CRITICAL ALERT: CAUVERY BASIN FLASH FLOOD WARNING  (+4.8m SURGE FORECAST)  //  IMMEDIATE EVACUATION ACTIVE", fill='#fca5a5', font=font_bold, anchor='lm')

    # Left Panel: Telemetry Stream (w: 380)
    draw.rectangle([20, 110, 420, h - 20], fill='#0a1526', outline='#1e3a5f', width=2)
    draw.rectangle([20, 110, 420, 150], fill='#0f284c')
    draw.text((35, 130), "REAL-TIME TELEMETRY FEED", fill='#38bdf8', font=font_bold, anchor='lm')

    telemetry_items = [
        ("PRECIPITATION INTENSITY", "45.0 mm/h  [HEAVY TORRENTIAL]", '#ef4444', "Open-Meteo Weather API"),
        ("7-DAY CUMULATIVE RAIN", "142.5 mm  [CRITICAL THRESHOLD]", '#f97316', "State Rain Gauges"),
        ("RIVER DISCHARGE", "710 m³/s  (Danger: >650 m³/s)", '#ef4444', "GloFAS Hydrology CWC"),
        ("SOIL SATURATION", "84.2%  [NEAR TOTAL RUNOFF]", '#eab308', "Surface Wetness Index"),
        ("NASA FIRMS SATELLITE", "5 Active Thermal Hotspots (VIIRS)", '#f59e0b', "NASA S-NPP Orbit"),
        ("USGS SEISMIC FEED", "M4.2 Regional Event (52km deep)", '#10b981', "USGS Normalized Feed")
    ]
    for i, (label, val, col, src) in enumerate(telemetry_items):
        ty = 165 + i * 78
        draw.rectangle([32, ty, 408, ty + 70], fill='#0b1a30', outline='#1e293b', width=1)
        draw.text((45, ty + 16), label, fill='#94a3b8', font=font_small)
        draw.text((45, ty + 38), val, fill=col, font=font_bold)
        draw.text((45, ty + 56), f"Source: {src}", fill='#64748b', font=font_small)

    # Center Panel: Tactical Situational Map (w: 580)
    map_x1, map_x2 = 435, 1020
    draw.rectangle([map_x1, 110, map_x2, h - 20], fill='#050c17', outline='#0284c7', width=2)
    draw.rectangle([map_x1, 110, map_x2, 150], fill='#034d75')
    draw.text((map_x1 + 15, 130), "SITUATIONAL GIS RADAR & DIGITAL TWIN OVERLAY", fill='#ffffff', font=font_bold, anchor='lm')

    # Draw simulated map grid & terrain
    for gx in range(map_x1 + 40, map_x2, 60):
        draw.line([(gx, 150), (gx, h - 20)], fill='#0b1b33', width=1)
    for gy in range(180, h - 20, 60):
        draw.line([(map_x1, gy), (map_x2, gy)], fill='#0b1b33', width=1)

    # Simulated River & Flood Inundation Plume
    flood_poly = [(480, 260), (560, 310), (670, 340), (780, 420), (890, 490), (950, 560), (920, 600), (740, 520), (600, 430), (510, 360), (450, 290)]
    draw.polygon(flood_poly, fill='#083344', outline='#06b6d4')
    draw.text((680, 390), "FLOOD SURGE EXTENT (+4.8m)", fill='#22d3ee', font=font_bold, anchor='mm')

    # Impassable Highway Segment
    draw.line([(550, 480), (780, 460)], fill='#ef4444', width=5)
    draw.text((665, 450), "NH-48 CLOSED (SUBMERGED)", fill='#f87171', font=font_small, anchor='mm')

    # Evacuation Path Line
    draw.line([(520, 230), (610, 220), (750, 250), (860, 230)], fill='#10b981', width=4)
    draw.text((680, 210), "RECOMMENDED EVACUATION CORRIDOR (ELEVATED)", fill='#34d399', font=font_bold, anchor='mm')

    # Relief Shelter Marker
    draw.rectangle([860, 205, 990, 255], fill='#064e3b', outline='#10b981', width=2)
    draw.text((925, 220), "SHELTER ALPHA", fill='#6ee7b7', font=font_bold, anchor='mm')
    draw.text((925, 240), "490 Beds Free", fill='#a7f3d0', font=font_small, anchor='mm')

    # Right Panel: Drone FLIR Recon & Mission Control
    draw.rectangle([1035, 110, w - 20, h - 20], fill='#0a1526', outline='#1e3a5f', width=2)
    draw.rectangle([1035, 110, w - 20, 150], fill='#0f284c')
    draw.text((1050, 130), "DRONE FLIR RECON & ACTIONS", fill='#38bdf8', font=font_bold, anchor='lm')

    # Simulated Thermal Drone Viewport
    draw.rectangle([1050, 165, w - 35, 365], fill='#180b0b', outline='#ef4444', width=2)
    draw.text((1065, 185), "UAV TACTICAL FLIR RECON // CAM-02", fill='#fca5a5', font=font_small)
    draw.text((1065, 205), "ALT: 320m  |  BATTERY: 87%  |  NVG: ON", fill='#cbd5e1', font=font_small)
    # Crosshair
    cx, cy = (1050 + w - 35)//2, 265
    draw.line([(cx - 30, cy), (cx + 30, cy)], fill='#ef4444', width=1)
    draw.line([(cx, cy - 30), (cx, cy + 30)], fill='#ef4444', width=1)
    draw.ellipse([cx - 40, cy - 40, cx + 40, cy + 40], outline='#ef4444', width=1)
    draw.text((cx, cy + 55), "THERMAL ANOMALY: +41.8°C", fill='#f87171', font=font_small, anchor='mm')

    # Quick Action Buttons
    actions = [
        ("VOICE SITREP BRIEFING", '#0284c7', "Web Speech Synthesizer"),
        ("SCENARIO LAB (0h-48h)", '#059669', "Manning Surge Sim"),
        ("MULTI-CRITERIA ROUTING", '#7c3aed', "Shelter Allocator"),
        ("COORDINATOR LEDGER", '#d97706', "Sign-Off Dispatch")
    ]
    for i, (b_title, b_col, b_sub) in enumerate(actions):
        by = 385 + i * 62
        draw.rectangle([1050, by, w - 35, by + 52], fill=b_col, outline='#ffffff', width=1)
        draw.text((1065, by + 16), b_title, fill='#ffffff', font=font_bold)
        draw.text((1065, by + 34), b_sub, fill='#e0f2fe', font=font_small)

    img.save('generated_images/image7.jpeg', quality=95)
    print("Generated image7.jpeg")

# -----------------------------------------------------------------------------
# 6. Slide 20, Image 2: Explainable AI SHAP Decomposition Modal (image8.jpeg: 1539 x 688)
# -----------------------------------------------------------------------------
def generate_snapshot_2():
    w, h = 1539, 688
    img = Image.new('RGB', (w, h), color='#070f1f')
    draw = ImageDraw.Draw(img)

    # Modal Window Container
    draw.rectangle([30, 25, w - 30, h - 25], fill='#0b182d', outline='#0284c7', width=3)
    
    # Modal Header
    draw.rectangle([30, 25, w - 30, 95], fill='#034d75')
    draw.line([(30, 95), (w - 30, 95)], fill='#00e5ff', width=2)
    draw.text((55, 60), "EXPLAINABLE AI (XAI)  //  WHY IS THIS REGION AT CRITICAL FLOOD RISK?", fill='#ffffff', font=font_title, anchor='lm')

    # Top KPI Metrics Cards
    kpis = [
        ("PREDICTION CLASS", "CRITICAL RISK", '#ef4444', "Holdout F1: 0.7152"),
        ("CALIBRATED PROBABILITY", "92.8%", '#f97316', "Sigmoid CalibratedClassifierCV"),
        ("MODEL UNCERTAINTY", "0.11", '#10b981', "Bounded Variance (0.09-0.14)"),
        ("BASELINE LIFT", "+73.31%", '#38bdf8', "Vs Stratified Dummy (41.6%)")
    ]
    k_w = (w - 120) // 4
    for i, (k_title, k_val, k_col, k_sub) in enumerate(kpis):
        kx = 55 + i * (k_w + 12)
        draw.rectangle([kx, 115, kx + k_w, 205], fill='#071426', outline='#1e3a5f', width=2)
        draw.text((kx + 15, 135), k_title, fill='#94a3b8', font=font_small)
        draw.text((kx + 15, 168), k_val, fill=k_col, font=font_title)
        draw.text((kx + 15, 192), k_sub, fill='#64748b', font=font_small)

    # Left Section: Tree-Path Feature Contribution Bars (w: 800)
    draw.rectangle([55, 225, 870, h - 45], fill='#081426', outline='#1e3a5f', width=1)
    draw.text((75, 250), "TREE-PATH DECISION DECOMPOSITION (SHAP-ALIGNED DELTAS)", fill='#38bdf8', font=font_bold)

    factors = [
        ("River Discharge (Cauvery Basin)", "+36.8%", 36.8, "Measured: 710 m³/s (Threshold: 650 m³/s)", '#ef4444'),
        ("7-Day Cumulative Rainfall", "+28.4%", 28.4, "Measured: 142.5 mm (Seasonal Avg: 45 mm)", '#f97316'),
        ("Current Precipitation Rate", "+18.2%", 18.2, "Intensity: 45.0 mm/h torrential rain", '#eab308'),
        ("Soil Saturation Index", "+10.1%", 10.1, "Measured: 84.2% waterlogging saturation", '#3b82f6'),
        ("Terrain Elevation Delta", "-6.5%", -6.5, "Catchment basin lowland 120m AOD", '#10b981')
    ]
    for i, (fname, pct_str, val, detail, bcol) in enumerate(factors):
        fy = 285 + i * 68
        draw.text((75, fy), fname, fill='#ffffff', font=font_bold)
        draw.text((560, fy), pct_str, fill=bcol, font=font_bold)
        draw.text((75, fy + 22), detail, fill='#94a3b8', font=font_small)
        # Background bar
        draw.rectangle([640, fy + 5, 840, fy + 22], fill='#1e293b')
        # Value bar
        bar_len = int(abs(val) * 4.5)
        draw.rectangle([640, fy + 5, 640 + bar_len, fy + 22], fill=bcol)

    # Right Section: Actionable Incident Commander Guidance (w: 550)
    draw.rectangle([895, 225, w - 55, h - 45], fill='#081426', outline='#1e3a5f', width=1)
    draw.text((915, 250), "GROUNDED TACTICAL ACTION PROTOCOLS", fill='#38bdf8', font=font_bold)

    actions = [
        ("1. INITIATE MANDATORY LOWLAND EVACUATION", "Enforce 500m clearance buffer along Cauvery riverbanks. Reroute population through elevated Western Bypass.", '#ef4444'),
        ("2. PRE-POSITION DEWATERING PUMP FLEET", "Deploy 4 high-capacity pump units to NH-48 junction underpasses before forecasted +4.8m surge peak at T+12h.", '#f97316'),
        ("3. MOBILIZE WATER RESCUE ASSETS", "Dispatch NDRF 10th Battalion Zodiac rafts with flood extraction gear. Primary trauma hospital: Belagavi Civil (9 ICU beds).", '#34d399')
    ]
    for i, (atitle, adesc, acol) in enumerate(actions):
        ay = 290 + i * 115
        draw.rectangle([915, ay, w - 75, ay + 100], fill='#0b1d38', outline=acol, width=1)
        draw.text((930, ay + 18), atitle, fill=acol, font=font_bold)
        # Wrap description
        words = adesc.split()
        l1 = ' '.join(words[:7])
        l2 = ' '.join(words[7:])
        draw.text((930, ay + 45), l1, fill='#e2e8f0', font=font_regular)
        draw.text((930, ay + 68), l2, fill='#e2e8f0', font=font_regular)

    img.save('generated_images/image8.jpeg', quality=95)
    print("Generated image8.jpeg")

# -----------------------------------------------------------------------------
# 7. Slide 21, Image 3: AI-Assisted Evacuation Navigator (image9.jpeg: 1464 x 661)
# -----------------------------------------------------------------------------
def generate_snapshot_3():
    w, h = 1464, 661
    img = Image.new('RGB', (w, h), color='#070e1c')
    draw = ImageDraw.Draw(img)

    # Top Bar
    draw.rectangle([0, 0, w, 55], fill='#08253b')
    draw.line([(0, 53), (w, 53)], fill='#00e5ff', width=2)
    draw.text((25, 27), "AI-ASSISTED SAFE EVACUATION NAVIGATOR (MULTI-CRITERIA A* ROUTING)", fill='#ffffff', font=font_bold, anchor='lm')

    # Left Route Comparison Table (w: 640)
    draw.rectangle([25, 75, 680, h - 25], fill='#091629', outline='#1e3a5f', width=2)
    draw.text((45, 100), "GENERATED SAFE CORRIDORS & HAZARD PENALTIES", fill='#38bdf8', font=font_bold)

    routes = [
        ("PRIMARY ROUTE: Elevated Arterial Bypass", "3.9 km  |  6 min ETA  |  Clearance: +1.8m", "RECOMMENDED", '#10b981', '#064e3b'),
        ("ALTERNATE 1: Highway 48 East Corridor", "5.2 km  |  9 min ETA  |  Clearance: +0.6m", "CLEAR", '#0284c7', '#082f49'),
        ("ALTERNATE 2: Outer Ring Connector", "6.1 km  |  12 min ETA | Clearance: Safe", "CLEAR", '#6366f1', '#1e1b4b'),
        ("REJECTED: Valley Riverfront Parkway", "2.8 km  |  BLOCKED     | SUBMERGED (-1.2m)", "IMPASSABLE", '#ef4444', '#450a0a')
    ]
    for i, (rtitle, rstats, rbadge, rcol, rbg) in enumerate(routes):
        ry = 130 + i * 85
        draw.rectangle([40, ry, 665, ry + 75], fill=rbg, outline=rcol, width=1)
        draw.text((55, ry + 15), rtitle, fill='#ffffff', font=font_bold)
        draw.text((55, ry + 42), rstats, fill='#cbd5e1', font=font_regular)
        # Badge
        draw.rectangle([535, ry + 15, 650, ry + 45], fill=rcol)
        draw.text((592, ry + 30), rbadge, fill='#ffffff', font=font_bold, anchor='mm')

    # Shelter Capacity Ledger
    draw.rectangle([40, 480, 665, h - 45], fill='#0b1e38', outline='#10b981', width=1)
    draw.text((55, 500), "DESTINATION SHELTER VERIFICATION", fill='#34d399', font=font_bold)
    draw.text((55, 530), "• Shelter Name: Belagavi District Sports Complex Relief Hub", fill='#ffffff', font=font_regular)
    draw.text((55, 555), "• Available Capacity: 490 Beds Free / 1200 Total Beds (Occupancy: 59.2%)", fill='#a7f3d0', font=font_regular)
    draw.text((55, 580), "• On-Site Medical Post: ACTIVE  |  Auxiliary Generator: OPERATIONAL", fill='#cbd5e1', font=font_regular)
    draw.text((55, 605), "• Potable Water Supply: 72-Hour Stockpile Verified", fill='#cbd5e1', font=font_regular)

    # Right Graphical Map Visualization (w: 740)
    map_x1, map_x2 = 705, w - 25
    draw.rectangle([map_x1, 75, map_x2, h - 25], fill='#050d18', outline='#0284c7', width=2)
    draw.text((map_x1 + 20, 100), "MULTI-CRITERIA A* GRAPH OVERLAY & HAZARD CLEARANCE", fill='#38bdf8', font=font_bold)

    # Draw nodes and route paths
    # Start node
    draw.ellipse([map_x1 + 80, 480, map_x1 + 140, 540], fill='#ef4444', outline='#ffffff', width=2)
    draw.text((map_x1 + 110, 510), "ORIGIN\n(Danger)", fill='#ffffff', font=font_small, anchor='mm')

    # End node (Shelter)
    draw.rectangle([map_x2 - 190, 150, map_x2 - 40, 220], fill='#059669', outline='#ffffff', width=2)
    draw.text((map_x2 - 115, 175), "SAFE SHELTER", fill='#ffffff', font=font_bold, anchor='mm')
    draw.text((map_x2 - 115, 198), "490 Beds Free", fill='#a7f3d0', font=font_small, anchor='mm')

    # Hazard Area (Polygon)
    h_poly = [(map_x1 + 180, 360), (map_x1 + 420, 310), (map_x1 + 520, 480), (map_x1 + 320, 560)]
    draw.polygon(h_poly, fill='#1e1b4b', outline='#7c3aed')
    draw.text((map_x1 + 340, 430), "ACTIVE HAZARD ZONE\n(Inundation Surge +4.8m)", fill='#c084fc', font=font_bold, anchor='mm')

    # Recommended Safe Route (Curve around hazard)
    route_pts = [(map_x1 + 140, 500), (map_x1 + 190, 400), (map_x1 + 280, 240), (map_x1 + 500, 190), (map_x2 - 190, 185)]
    for idx in range(len(route_pts) - 1):
        draw.line([route_pts[idx], route_pts[idx+1]], fill='#10b981', width=6)
    draw.text((map_x1 + 340, 215), "Primary Route (3.9 km, 6 min) - High Clearance", fill='#34d399', font=font_bold, anchor='mm')

    # Blocked Route (Straight into hazard)
    draw.line([(map_x1 + 140, 500), (map_x1 + 340, 430)], fill='#ef4444', width=4)
    draw.line([(map_x1 + 310, 400), (map_x1 + 370, 460)], fill='#ef4444', width=6)
    draw.line([(map_x1 + 370, 400), (map_x1 + 310, 460)], fill='#ef4444', width=6)
    draw.text((map_x1 + 270, 490), "Submerged Parkway [CLOSED]", fill='#fca5a5', font=font_small, anchor='mm')

    img.save('generated_images/image9.jpeg', quality=95)
    print("Generated image9.jpeg")

# -----------------------------------------------------------------------------
# 8. Slide 21, Image 4: Smart Resource Dispatch & Coordinator Ledger (image10.jpeg: 1464 x 714)
# -----------------------------------------------------------------------------
def generate_snapshot_4():
    w, h = 1464, 714
    img = Image.new('RGB', (w, h), color='#070e1c')
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, w, 55], fill='#062c26')
    draw.line([(0, 53), (w, 53)], fill='#10b981', width=2)
    draw.text((25, 27), "SMART RESCUE RESOURCE ALLOCATION & COORDINATOR LEDGER", fill='#ffffff', font=font_bold, anchor='lm')

    # Left Container: Incident & Capability Match
    draw.rectangle([25, 75, 710, h - 25], fill='#081824', outline='#1e3a5f', width=2)
    draw.text((45, 100), "MULTI-OBJECTIVE ASSET CAPABILITY MATCHING", fill='#38bdf8', font=font_bold)

    # Incident Details Box
    draw.rectangle([40, 125, 695, 225], fill='#1c1010', outline='#ef4444', width=1)
    draw.text((55, 145), "INCIDENT TICKET #FL-2026-089  [URGENT RESCUE]", fill='#fca5a5', font=font_bold)
    draw.text((55, 172), "• Nature of Emergency: 12 Citizens Trapped on Rooftop (Water Level +2.4m)", fill='#ffffff', font=font_regular)
    draw.text((55, 195), "• Location: Cauvery Lowland Basin (15.842° N, 74.491° E)  |  Severity: CRITICAL", fill='#cbd5e1', font=font_regular)

    # Optimization Comparison Box
    draw.rectangle([40, 245, 695, 420], fill='#0b1c2e', outline='#0284c7', width=1)
    draw.text((55, 265), "OPTIMIZATION COMPARISON: BASELINE VS AI ENGINE", fill='#38bdf8', font=font_bold)
    draw.text((55, 295), "Standard Nearest-Neighbor (Baseline):", fill='#f87171', font=font_bold)
    draw.text((55, 318), "• Dispatches City Fire Tender 4 (2.1 km away)", fill='#fca5a5', font=font_regular)
    draw.text((55, 338), "• Defect: Unit lacks watercraft/zodiac boats — Result: MISSION FAILURE", fill='#fca5a5', font=font_small)

    draw.text((55, 365), "AI Capability-Matching Engine (Our Platform):", fill='#34d399', font=font_bold)
    draw.text((55, 388), "• Dispatches NDRF 10th Battalion - Water Rescue Bravo (Inflatable Zodiacs)", fill='#a7f3d0', font=font_regular)
    draw.text((55, 408), "• Travel ETA: 5 min  |  Trauma Hospital: Belagavi Civil (9 ICU beds free)", fill='#a7f3d0', font=font_small)

    # ICU Hospital Corroboration
    draw.rectangle([40, 440, 695, h - 45], fill='#0a231f', outline='#10b981', width=1)
    draw.text((55, 460), "TRAUMA CENTER BED AVAILABILITY CONFIRMATION", fill='#34d399', font=font_bold)
    draw.text((55, 490), "• Belagavi Civil Emergency Hospital (Level 1 Trauma): 9 ICU Beds FREE", fill='#ffffff', font=font_regular)
    draw.text((55, 515), "• Ambulance En Route: ALS Mobile Intensive Unit MIU-08 (Oxygen + Paramedic)", fill='#cbd5e1', font=font_regular)
    draw.text((55, 540), "• Hospital Notification: Trauma surgical suite pre-notified & on standby", fill='#cbd5e1', font=font_regular)

    # Right Container: Human-in-the-Loop Coordinator Sign-Off Ledger
    draw.rectangle([735, 75, w - 25, h - 25], fill='#081426', outline='#f59e0b', width=2)
    draw.text((755, 100), "SAFETY GOVERNANCE: COORDINATOR AUTHORIZATION LEDGER", fill='#fbbf24', font=font_bold)

    draw.rectangle([755, 130, w - 45, 250], fill='#1f1505', outline='#f59e0b', width=1)
    draw.text((775, 155), "GUARDRAIL ENFORCEMENT: AI CANNOT UNILATERALLY DISPATCH PHYSICAL ASSETS", fill='#fde68a', font=font_bold)
    draw.text((775, 185), "• Recommendation Generated at: 2026-11-20T05:33:55.140Z", fill='#cbd5e1', font=font_regular)
    draw.text((775, 210), "• Dispatch Status: AUTHORIZED & ENACTED", fill='#34d399', font=font_bold)
    draw.text((775, 230), "• Signing Officer: COORD-OFFICER-44 (Deputy Incident Commander)", fill='#cbd5e1', font=font_regular)

    # Digital Ledger Audit Table
    draw.rectangle([755, 270, w - 45, h - 45], fill='#0b182d', outline='#1e3a5f', width=1)
    draw.text((775, 290), "IMMUTABLE AUDIT TRAIL RECORD", fill='#38bdf8', font=font_bold)

    ledger_entries = [
        ("Timestamp", "Asset ID", "Target Zone", "Authorized By", "Status"),
        ("05:32:10Z", "NDRF-BRAVO-10", "Cauvery Sector 4", "COORD-OFFICER-44", "DISPATCHED"),
        ("05:28:45Z", "ALS-AMB-08", "Civil Hospital Route", "COORD-OFFICER-44", "EN ROUTE"),
        ("05:15:20Z", "PUMP-UNIT-02", "NH-48 Underpass", "COORD-OFFICER-12", "DEPLOYED"),
        ("05:02:11Z", "DRONE-FLIR-02", "Belagavi Airspace", "SYS-AUTOMATION", "MONITORING")
    ]
    for r_idx, r_data in enumerate(ledger_entries):
        ly = 325 + r_idx * 58
        bg = '#0f294a' if r_idx == 0 else ('#081729' if r_idx % 2 == 1 else '#0b1d33')
        draw.rectangle([775, ly, w - 65, ly + 48], fill=bg)
        for c_idx, text in enumerate(r_data):
            cx = 790 + c_idx * 135
            fnt = font_bold if r_idx == 0 else font_regular
            col = '#00ffff' if r_idx == 0 else ('#34d399' if c_idx == 4 else '#ffffff')
            draw.text((cx, ly + 14), text, fill=col, font=fnt)

    img.save('generated_images/image10.jpeg', quality=95)
    print("Generated image10.jpeg")

# -----------------------------------------------------------------------------
# 9. Slide 22, Image 5: Disaster Digital Twin Scenario Lab (image11.jpeg: 1757 x 655)
# -----------------------------------------------------------------------------
def generate_snapshot_5():
    w, h = 1757, 655
    img = Image.new('RGB', (w, h), color='#070f1e')
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, w, 55], fill='#1e1438')
    draw.line([(0, 53), (w, 53)], fill='#a855f7', width=2)
    draw.text((25, 27), "DISASTER DIGITAL TWIN: 0h – 48h MULTI-HAZARD SCENARIO SIMULATION LAB", fill='#ffffff', font=font_bold, anchor='lm')

    # Top Control Bar & Timeline Scrubber
    draw.rectangle([25, 75, w - 25, 160], fill='#0e172e', outline='#6366f1', width=2)
    draw.text((45, 95), "SIMULATION TIME HORIZON: T + 18.0 HOURS  [PLAYING 2x SPEED]", fill='#a5b4fc', font=font_bold)
    
    # Progress Scrubber
    draw.rectangle([45, 120, w - 200, 140], fill='#1e293b')
    draw.rectangle([45, 120, 850, 140], fill='#a855f7')
    draw.ellipse([840, 115, 860, 145], fill='#ffffff', outline='#a855f7', width=2)
    draw.text((w - 180, 130), "+18.0h / 48.0h", fill='#ffffff', font=font_bold, anchor='lm')

    # Left Container: Manning's Hydrodynamic Simulation
    draw.rectangle([25, 180, 560, h - 25], fill='#0a182c', outline='#0284c7', width=2)
    draw.text((45, 205), "HYDRODYNAMIC FLOOD SURGE (MANNING)", fill='#38bdf8', font=font_bold)
    draw.text((45, 235), "Governing Formula: Q = (1/n) * A * R^(2/3) * S^(1/2)", fill='#94a3b8', font=font_mono)

    f_stats = [
        ("Current Inundation Area", "185.4 km²  (+4.8m peak surge)"),
        ("48h Forecasted Limit", "194.4 km²  (Asymptotic Bound)"),
        ("Submerged Highways", "NH-48 Sector 3 impassable"),
        ("Population at Risk", "14,200 Citizens within perimeter")
    ]
    for i, (k, v) in enumerate(f_stats):
        draw.rectangle([40, 270 + i * 75, 545, 335 + i * 75], fill='#071629')
        draw.text((55, 285 + i * 75), k, fill='#94a3b8', font=font_small)
        draw.text((55, 310 + i * 75), v, fill='#38bdf8', font=font_bold)

    # Center Container: Rothermel Wildfire Propagation
    draw.rectangle([585, 180, 1150, h - 25], fill='#1c0f0f', outline='#ef4444', width=2)
    draw.text((605, 205), "WILDFIRE PROPAGATION (ROTHERMEL FORMULA)", fill='#f87171', font=font_bold)
    draw.text((605, 235), "Formula: R = Irx * xi * (1+phi_w+phi_s) / (rho_b * epsilon * Qig)", fill='#fca5a5', font=font_mono)

    w_stats = [
        ("24h Active Perimeter", "97.9 km  (Rothermel Spread Rate)"),
        ("Flame Front Height", "5.6 m flame length stability"),
        ("Active Thermal Radiance", "34.8 MW Fire Radiative Power (VIIRS)"),
        ("Suppression Fleet", "3 Wildfire Squads dispatched")
    ]
    for i, (k, v) in enumerate(w_stats):
        draw.rectangle([600, 270 + i * 75, 1135, 335 + i * 75], fill='#200d0d')
        draw.text((615, 285 + i * 75), k, fill='#fca5a5', font=font_small)
        draw.text((615, 310 + i * 75), v, fill='#ef4444', font=font_bold)

    # Right Container: Atkinson-Boore Seismic Attenuation
    draw.rectangle([1175, 180, w - 25, h - 25], fill='#17170a', outline='#eab308', width=2)
    draw.text((1195, 205), "SEISMIC ATTENUATION (ATKINSON-BOORE)", fill='#facc15', font=font_bold)
    draw.text((1195, 235), "Formula: ln PGA = c1 + c2*M - c3*ln R + S", fill='#fef08a', font=font_mono)

    s_stats = [
        ("Peak Ground Acceleration", "0.28g  (Severe Ground Motion)"),
        ("Liquefaction Hazard Zone", "21 km Radius around epicenter"),
        ("Modified Mercalli Class", "MMI VIII - Severe Damage"),
        ("Structural Inspection", "Priority 1 Bridges flagged")
    ]
    for i, (k, v) in enumerate(s_stats):
        draw.rectangle([1190, 270 + i * 75, w - 45, 335 + i * 75], fill='#1f1f0a')
        draw.text((1205, 285 + i * 75), k, fill='#fef08a', font=font_small)
        draw.text((1205, 310 + i * 75), v, fill='#facc15', font=font_bold)

    img.save('generated_images/image11.jpeg', quality=95)
    print("Generated image11.jpeg")

# -----------------------------------------------------------------------------
# 10. Slide 22, Image 6: Mission Replay & 72x Decision Latency Report (image12.jpeg: 1745 x 621)
# -----------------------------------------------------------------------------
def generate_snapshot_6():
    w, h = 1745, 621
    img = Image.new('RGB', (w, h), color='#070e1c')
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, w, 55], fill='#0b2247')
    draw.line([(0, 53), (w, 53)], fill='#00e5ff', width=2)
    draw.text((25, 27), "MISSION REPLAY & AFTER-ACTION ANALYTICS: 72x OPERATIONAL DECISION SPEEDUP", fill='#ffffff', font=font_bold, anchor='lm')

    # Left Container: 72x Latency Benchmark Card
    draw.rectangle([25, 75, 780, h - 25], fill='#0a182c', outline='#10b981', width=2)
    draw.text((45, 105), "QUANTITATIVE OPERATIONAL LATENCY BENCHMARK", fill='#34d399', font=font_bold)

    # Big 72x Callout
    draw.rectangle([45, 135, 760, 275], fill='#042a22', outline='#10b981', width=2)
    draw.text((65, 175), "72x FASTER DECISION LATENCY", fill='#34d399', font=font_title)
    draw.text((65, 215), "Standard Manual SOP: 130.0 minutes  --->  AI-Assisted Hub: 1.8 minutes", fill='#ffffff', font=font_bold)
    draw.text((65, 245), "Measured across 73 automated test assertions & comprehensive drill timeline.", fill='#a7f3d0', font=font_regular)

    # Detailed Comparison Bars
    comp_metrics = [
        ("Telemetry Gathering & Ingestion", "45.0 min (Manual Phone Calls)", "0.05 min (Automated Feeds)", '#ef4444', '#10b981'),
        ("Hazard Perimeter & Risk Prediction", "35.0 min (Heuristic Estimation)", "0.15 min (Calibrated ML RF)", '#ef4444', '#10b981'),
        ("Evacuation Corridor Optimization", "30.0 min (Manual Map Routing)", "0.60 min (Multi-Criteria A*)", '#ef4444', '#10b981'),
        ("Resource Dispatch & Hospital ICU Match", "20.0 min (Radio Phone Calls)", "1.00 min (Capability Matcher)", '#ef4444', '#10b981')
    ]
    for i, (mtitle, mman, mai, mcol1, mcol2) in enumerate(comp_metrics):
        my = 295 + i * 70
        draw.text((45, my), mtitle, fill='#e2e8f0', font=font_bold)
        draw.text((45, my + 24), f"Manual: {mman}", fill='#f87171', font=font_small)
        draw.text((400, my + 24), f"AI Hub: {mai}", fill='#34d399', font=font_bold)

    # Right Container: Timeline Drill Replay & AAR Export
    draw.rectangle([810, 75, w - 25, h - 25], fill='#081426', outline='#0284c7', width=2)
    draw.text((830, 105), "OPERATION FLOODSHIELD — DRILL TIMELINE STREAM", fill='#38bdf8', font=font_bold)

    events = [
        ("00:00:00", "INCIDENT TRIGGER", "Extreme precipitation detected at Cauvery Basin (45 mm/h).", '#ef4444'),
        ("00:08:12", "AI RISK ALERT", "Calibrated Random Forest flags CRITICAL flood risk (92.8% prob).", '#f97316'),
        ("00:15:30", "DIGITAL TWIN", "Manning hydrodynamic surge simulation projects +4.8m crest at T+12h.", '#a855f7'),
        ("00:22:45", "EVACUATION", "A* algorithm routes to Belagavi Sports Complex (490 beds free).", '#06b6d4'),
        ("00:35:10", "DISPATCH MATCH", "NDRF Water Rescue Bravo capability matched with 9 trauma ICU beds.", '#10b981'),
        ("00:50:00", "LEDGER SIGN-OFF", "Coordinator Officer COORD-44 authorizes orders; AAR CSV exported.", '#eab308')
    ]
    for i, (etime, etitle, edesc, ecol) in enumerate(events):
        ey = 140 + i * 68
        draw.rectangle([830, ey, w - 45, ey + 58], fill='#0b1d38', outline=ecol, width=1)
        draw.text((845, ey + 12), etime, fill='#94a3b8', font=font_mono)
        draw.text((945, ey + 12), etitle, fill=ecol, font=font_bold)
        draw.text((845, ey + 34), edesc, fill='#cbd5e1', font=font_small)

    # Export Button Callout
    draw.rectangle([w - 320, 25, w - 45, 50], fill='#10b981')
    draw.text((w - 182, 37), "DOWNLOAD AAR CSV EXPORT", fill='#ffffff', font=font_bold, anchor='mm')

    img.save('generated_images/image12.jpeg', quality=95)
    print("Generated image12.jpeg")

generate_snapshot_1()
generate_snapshot_2()
generate_snapshot_3()
generate_snapshot_4()
generate_snapshot_5()
generate_snapshot_6()
