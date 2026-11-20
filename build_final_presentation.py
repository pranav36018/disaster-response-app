import os
import zipfile
import pptx
from pptx import Presentation
from pptx.util import Pt, Inches
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def build_presentation():
    prs = Presentation('phase_2_ppt_syn2sem_reference.pptx')
    print(f"Loaded reference presentation with {len(prs.slides)} slides.")

    # -------------------------------------------------------------------------
    # SLIDE 1: Title Slide
    # -------------------------------------------------------------------------
    s1 = prs.slides[0]
    # Shape 2 (TextBox 4) has the project title
    for shape in s1.shapes:
        if shape.name == 'TextBox 4' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            r = p.add_run()
            r.text = "Crisis Intelligence Hub: Autonomous Disaster Command & Real-Time AI Intelligence Engine"
            r.font.size = Pt(20)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0, 32, 96) # #002060
            print("Slide 1 updated project title.")

    # -------------------------------------------------------------------------
    # SLIDE 2: Introduction
    # -------------------------------------------------------------------------
    s2 = prs.slides[1]
    # Shape 1: Content Placeholder 2
    for shape in s2.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()
            
            p0 = tf.paragraphs[0]
            p0.alignment = PP_ALIGN.JUSTIFY
            r0_1 = p0.add_run()
            r0_1.text = "Crisis Intelligence Hub"
            r0_1.font.bold = True
            r0_1.font.size = Pt(24)
            r0_2 = p0.add_run()
            r0_2.text = " is an autonomous multi-hazard disaster command platform and real-time AI intelligence engine engineered for mission-critical emergency response. "
            r0_2.font.size = Pt(24)

            p1 = tf.add_paragraph()
            p1.alignment = PP_ALIGN.JUSTIFY
            r1 = p1.add_run()
            r1.text = "It synthesizes multi-source live telemetry from Open-Meteo weather and flood hydrology, USGS real-time seismic feeds, and NASA FIRMS thermal anomaly satellite detections. "
            r1.font.size = Pt(24)

            p2 = tf.add_paragraph()
            p2.alignment = PP_ALIGN.JUSTIFY
            r2 = p2.add_run()
            r2.text = "Many existing disaster management platforms operate as passive, retrospective alert boards that fail to provide calibrated predictive risk modeling or actionable decision support. "
            r2.font.size = Pt(24)

            p3 = tf.add_paragraph()
            p3.alignment = PP_ALIGN.JUSTIFY
            r3 = p3.add_run()
            r3.text = "Crisis Intelligence Hub integrates calibrated Random Forest classification, tree-path SHAP Explainable AI, 0h–48h physics Digital Twin simulations, and multi-criteria A* evacuation optimization to save lives. "
            r3.font.size = Pt(24)
            print("Slide 2 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 3: Problem Statement
    # -------------------------------------------------------------------------
    s3 = prs.slides[2]
    for shape in s3.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            p0 = tf.paragraphs[0]
            r0 = p0.add_run()
            r0.text = "Background of the problem:"
            r0.font.bold = True
            r0.font.size = Pt(24)

            p1 = tf.add_paragraph()
            r1 = p1.add_run()
            r1.text = "Natural disasters (flash floods, wildfires, earthquakes) inflict catastrophic loss of life and infrastructure due to fragmented data feeds and communication silos between emergency agencies."
            r1.font.size = Pt(24)

            p2 = tf.add_paragraph()
            r2 = p2.add_run()
            r2.text = "Existing issue/challenge:"
            r2.font.bold = True
            r2.font.size = Pt(24)

            p3 = tf.add_paragraph()
            r3 = p3.add_run()
            r3.text = "Incident commanders rely on manual phone calls, disconnected legacy dashboards, and uncalibrated risk heuristics, resulting in an average 130-minute operational decision latency."
            r3.font.size = Pt(24)

            p4 = tf.add_paragraph()
            r4 = p4.add_run()
            r4.text = "Most AI prototypes generate 'black-box' probabilities without explainability, lack verified civil defense shelter capacity checks, and misallocate rescue assets during multi-hazard crises."
            r4.font.size = Pt(24)

            p5 = tf.add_paragraph()
            r5 = p5.add_run()
            r5.text = "Need for the proposed system:"
            r5.font.bold = True
            r5.font.size = Pt(24)

            p6 = tf.add_paragraph()
            r6 = p6.add_run()
            r6.text = "We need an integrated command hub that combines live satellite telemetry, calibrated risk forecasting, physics-based scenario simulations, and human-in-the-loop dispatch governance to drastically reduce decision latency."
            r6.font.size = Pt(24)
            print("Slide 3 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 4: Objectives
    # -------------------------------------------------------------------------
    s4 = prs.slides[3]
    for shape in s4.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            p0 = tf.paragraphs[0]
            r0 = p0.add_run()
            r0.text = "Primary objective:"
            r0.font.bold = True
            r0.font.size = Pt(24)

            p1 = tf.add_paragraph()
            r1 = p1.add_run()
            r1.text = "Design and build an autonomous, 3-tier disaster command platform integrating multi-source real-time telemetry, calibrated predictive AI, and explainable decision optimization."
            r1.font.size = Pt(24)

            p2 = tf.add_paragraph()
            r2 = p2.add_run()
            r2.text = "Secondary objectives:"
            r2.font.bold = True
            r2.font.size = Pt(24)

            p3 = tf.add_paragraph()
            r3_1 = p3.add_run()
            r3_1.text = "Real-Time Telemetry & Attribution: "
            r3_1.font.bold = True
            r3_1.font.size = Pt(22)
            r3_2 = p3.add_run()
            r3_2.text = "Ingest Open-Meteo, USGS, and NASA FIRMS feeds with exponential backoff and transparent source tags."
            r3_2.font.size = Pt(22)

            p4 = tf.add_paragraph()
            r4_1 = p4.add_run()
            r4_1.text = "Calibrated ML & Explainable AI: "
            r4_1.font.bold = True
            r4_1.font.size = Pt(22)
            r4_2 = p4.add_run()
            r4_2.text = "Deploy 150-tree Random Forest models with Sigmoid calibration and tree-path SHAP feature contribution decomposition."
            r4_2.font.size = Pt(22)

            p5 = tf.add_paragraph()
            r5_1 = p5.add_run()
            r5_1.text = "Digital Twin & Operational Optimization: "
            r5_1.font.bold = True
            r5_1.font.size = Pt(22)
            r5_2 = p5.add_run()
            r5_2.text = "Simulate 0h–48h surge/wildfire propagation and execute multi-criteria A* routing with coordinator authorization."
            r5_2.font.size = Pt(22)

            p6 = tf.add_paragraph()
            r6 = p6.add_run()
            r6.text = "Expected outcomes:"
            r6.font.bold = True
            r6.font.size = Pt(24)

            p7 = tf.add_paragraph()
            r7 = p7.add_run()
            r7.text = "An enterprise command platform demonstrating a 72x reduction in operational decision latency (from 130 minutes down to 1.8 minutes)."
            r7.font.size = Pt(24)
            print("Slide 4 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 6: Literature Survey – Summary (Text slide)
    # -------------------------------------------------------------------------
    s6 = prs.slides[5]
    for shape in s6.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            p0 = tf.paragraphs[0]
            r0_1 = p0.add_run()
            r0_1.text = "Summary of Existing Systems: "
            r0_1.font.bold = True
            r0_1.font.size = Pt(24)
            r0_2 = p0.add_run()
            r0_2.text = "Current disaster portals (GDACS, FEMA Hazus, regional GIS dashboards) act primarily as retrospective data visualizers without real-time predictive risk modeling or automated dispatch."
            r0_2.font.size = Pt(24)

            p1 = tf.add_paragraph()
            r1_0 = p1.add_run()
            r1_0.text = "• "
            r1_0.font.size = Pt(24)
            r1_1 = p1.add_run()
            r1_1.text = "The Problem (The Gap): "
            r1_1.font.bold = True
            r1_1.font.size = Pt(24)
            r1_2 = p1.add_run()
            r1_2.text = "Emergency dashboards show raw sensor numbers without hazard risk classification, or employ uncalibrated black-box AI with zero explainability, leading to response paralysis."
            r1_2.font.size = Pt(24)

            p2 = tf.add_paragraph()
            r2_0 = p2.add_run()
            r2_0.text = "• "
            r2_0.font.size = Pt(24)
            r2_1 = p2.add_run()
            r2_1.text = "Our Solution (Crisis Intelligence Hub): "
            r2_1.font.bold = True
            r2_1.font.size = Pt(24)
            r2_2 = p2.add_run()
            r2_2.text = "We engineered a 3-tier platform that integrates real-time satellite telemetry, calibrated ML risk inference, tree-path SHAP explainability, and multi-criteria evacuation routing."
            r2_2.font.size = Pt(24)

            p3 = tf.add_paragraph()
            r3_0 = p3.add_run()
            r3_0.text = "• "
            r3_0.font.size = Pt(24)
            r3_1 = p3.add_run()
            r3_1.text = "Physics & Reliability Integration: "
            r3_1.font.bold = True
            r3_1.font.size = Pt(24)
            r3_2 = p3.add_run()
            r3_2.text = "We incorporate governing physical formulas (Manning's surge, Rothermel fire spread) and an offline-resilient IndexedDB store to ensure zero downtime during network severance."
            r3_2.font.size = Pt(24)
            print("Slide 6 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 7: System Requirement Specification-Requirements
    # -------------------------------------------------------------------------
    s7 = prs.slides[6]
    for shape in s7.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            p0 = tf.paragraphs[0]
            r0 = p0.add_run()
            r0.text = "Functional:"
            r0.font.bold = True
            r0.font.size = Pt(30)

            p1 = tf.add_paragraph()
            r1 = p1.add_run()
            r1.text = "Real-time telemetry ingestion from Open-Meteo Weather/Floods, USGS Earthquakes, and NASA FIRMS satellites."
            r1.font.size = Pt(24)

            p2 = tf.add_paragraph()
            r2 = p2.add_run()
            r2.text = "Calibrated multi-hazard ML risk classification (Flood & Wildfire) with tree-path SHAP feature contribution decomposition."
            r2.font.size = Pt(24)

            p3 = tf.add_paragraph()
            r3 = p3.add_run()
            r3.text = "0h–48h Disaster Digital Twin physics simulation with interactive time scrubbing and impassable highway detection."
            r3.font.size = Pt(24)

            p4 = tf.add_paragraph()
            r4 = p4.add_run()
            r4.text = "Multi-criteria A* hazard avoidance evacuation routing with shelter bed tracking and capability-matched rescue dispatch."
            r4.font.size = Pt(24)

            p5 = tf.add_paragraph()
            r5 = p5.add_run()
            r5.text = "Grounded AI Copilot, voice SITREP Web Speech synthesizer, and offline citizen SOS reporting with IndexedDB sync."
            r5.font.size = Pt(24)

            p6 = tf.add_paragraph()
            r6 = p6.add_run()
            r6.text = "Non-Functional:"
            r6.font.bold = True
            r6.font.size = Pt(26)

            p7 = tf.add_paragraph()
            r7 = p7.add_run()
            r7.text = "Sub-200ms cached API response latency, 72x operational decision speedup, circuit-breaker fault tolerance, and isolated execution security."
            r7.font.size = Pt(22)
            print("Slide 7 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 8: System Requirement Specification – Environment
    # -------------------------------------------------------------------------
    s8 = prs.slides[7]
    for shape in s8.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            p0 = tf.paragraphs[0]
            r0 = p0.add_run()
            r0.text = "Operating System: "
            r0.font.bold = True
            r0.font.size = Pt(26)

            p1 = tf.add_paragraph()
            r1 = p1.add_run()
            r1.text = "Windows 10/11, Linux (Ubuntu 22.04 LTS), or macOS."
            r1.font.size = Pt(24)

            p2 = tf.add_paragraph()
            r2 = p2.add_run()
            r2.text = "Runtime Platforms: "
            r2.font.bold = True
            r2.font.size = Pt(26)

            p3 = tf.add_paragraph()
            r3 = p3.add_run()
            r3.text = "Node.js (v20.0+ / Express 5), Python (3.11+ / FastAPI, Uvicorn)."
            r3.font.size = Pt(24)

            p4 = tf.add_paragraph()
            r4 = p4.add_run()
            r4.text = "ML & Scientific Stack: "
            r4.font.bold = True
            r4.font.size = Pt(26)

            p5 = tf.add_paragraph()
            r5 = p5.add_run()
            r5.text = "Scikit-learn (CalibratedClassifierCV, RandomForest), NumPy, Pandas, Joblib, SciPy."
            r5.font.size = Pt(24)

            p6 = tf.add_paragraph()
            r6 = p6.add_run()
            r6.text = "Frontend Stack: "
            r6.font.bold = True
            r6.font.size = Pt(26)

            p7 = tf.add_paragraph()
            r7 = p7.add_run()
            r7.text = "React 19, Vite 8, Tailwind CSS, Lucide React, Chart.js, React Three Fiber, PWA Service Worker."
            r7.font.size = Pt(24)

            p8 = tf.add_paragraph()
            r8 = p8.add_run()
            r8.text = "Hardware Requirements: "
            r8.font.bold = True
            r8.font.size = Pt(26)

            p9 = tf.add_paragraph()
            r9 = p9.add_run()
            r9.text = "Intel Core i5 / AMD Ryzen 5 or higher, minimum 8 GB RAM (16 GB recommended), 2 GB storage."
            r9.font.size = Pt(24)
            print("Slide 8 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 12: Detailed Module Design (Text slide)
    # -------------------------------------------------------------------------
    s12 = prs.slides[11]
    for shape in s12.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            p0 = tf.paragraphs[0]
            r0_1 = p0.add_run()
            r0_1.text = "Telemetry & Reliability Ingestion: "
            r0_1.font.bold = True
            r0_1.font.size = Pt(24)
            r0_2 = p0.add_run()
            r0_2.text = "Continuously ingests live satellite thermal hotspots, river hydrology, and seismic feeds with exponential-backoff retries, in-memory caching, and strict multi-tier source attribution labeling."
            r0_2.font.size = Pt(24)

            p1 = tf.add_paragraph()
            r1_1 = p1.add_run()
            r1_1.text = "Calibrated ML & XAI Engine: "
            r1_1.font.bold = True
            r1_1.font.size = Pt(24)
            r1_2 = p1.add_run()
            r1_2.text = "Executes 150-tree Random Forest models with Sigmoid probability calibration, outputting bounded uncertainty scores (0.09–0.14) and exact tree-path SHAP feature contribution deltas."
            r1_2.font.size = Pt(24)

            p2 = tf.add_paragraph()
            r2_1 = p2.add_run()
            r2_1.text = "Disaster Digital Twin Simulator: "
            r2_1.font.bold = True
            r2_1.font.size = Pt(24)
            r2_2 = p2.add_run()
            r2_2.text = "Computes dynamic flood inundation via Manning's hydrology, wildfire spread via Rothermel formulation, and peak ground acceleration via Atkinson-Boore across a 48-hour forward horizon."
            r2_2.font.size = Pt(24)

            p3 = tf.add_paragraph()
            r3_1 = p3.add_run()
            r3_1.text = "Evacuation & Resource Dispatcher: "
            r3_1.font.bold = True
            r3_1.font.size = Pt(24)
            r3_2 = p3.add_run()
            r3_2.text = "Executes multi-criteria A* hazard avoidance routing, verifies shelter capacities and trauma ICU beds, and enforces a mandatory human-in-the-loop coordinator approval ledger."
            r3_2.font.size = Pt(24)
            print("Slide 12 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 13: Project Modules
    # -------------------------------------------------------------------------
    s13 = prs.slides[12]
    for shape in s13.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            modules = [
                ("Module 1 – Tactical Command War Room HUD: ", "Interactive full-screen situational map with real-time hazard markers, FLIR drone recon, and military Zulu time HUD."),
                ("Module 2 – Multi-Source Telemetry & Reliability Gateway: ", "Express and Axios gateway with circuit breakers, Open-Meteo, USGS, and NASA FIRMS integration."),
                ("Module 3 – Calibrated Machine Learning & XAI Microservice: ", "Python FastAPI service hosting calibrated flood and wildfire models with genuine metrics and SHAP explainability."),
                ("Module 4 – Disaster Digital Twin Scenario Lab: ", "0h–48h hydrodynamic and fire propagation engine with interactive timeline scrubbers and impassable road detection."),
                ("Module 5 – Evacuation, Dispatch & Citizen SOS Engine: ", "Graph-based A* routing, capability-matching rescue fleet allocator, and offline IndexedDB citizen report store.")
            ]
            for idx, (m_title, m_desc) in enumerate(modules):
                p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
                r1 = p.add_run()
                r1.text = m_title
                r1.font.bold = True
                r1.font.size = Pt(22)
                r2 = p.add_run()
                r2.text = m_desc
                r2.font.size = Pt(22)
            print("Slide 13 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 14: Implementation – Translation Pipeline (Heading stays exact!)
    # -------------------------------------------------------------------------
    s14 = prs.slides[13]
    for shape in s14.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            pipeline_steps = [
                "Multi-hazard telemetry (Open-Meteo weather, river hydrology, USGS earthquakes, NASA FIRMS) is ingested continuously and normalized into uniform GeoJSON schema.",
                "An exponential backoff reliability manager with randomized jitter prevents rate-limiting and engages missing-data handlers if upstream APIs fail.",
                "Telemetry payloads are deterministically tagged with transparent source labels: Live observation, Near-real-time observation, Forecast, Historical, or Simulated.",
                "The Express API gateway proxies feature payloads to the Python FastAPI ML microservice for sub-50ms inference, with automated physics fallbacks if the service is offline.",
                "Verified risk classifications, simulation contours, and emergency alerts are pushed to the React HUD for instantaneous tactical situational awareness."
            ]
            for idx, step in enumerate(pipeline_steps):
                p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
                r = p.add_run()
                r.text = step
                r.font.size = Pt(24)
            print("Slide 14 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 15: Implementation – AST Parsing & Type Inference (Heading stays exact!)
    # -------------------------------------------------------------------------
    s15 = prs.slides[14]
    for shape in s15.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            ml_steps = [
                "Raw hydrological and meteorological readings are preprocessed into structured feature vectors: rainfall intensity, 7-day cumulative precipitation, river discharge, elevation, and soil saturation.",
                "Base 150-tree Random Forest classifiers are wrapped in CalibratedClassifierCV(method='sigmoid') to map ensemble decision votes into true posterior probabilities.",
                "Model uncertainty is computed across tree variance, guaranteeing bounded uncertainty scores (0.09 – 0.14) to prevent high-stakes emergency false alarms.",
                "A recursive tree-path decomposition algorithm traverses all 150 decision trees from root to leaf to calculate exact SHAP-aligned feature contribution deltas.",
                "Mathematical feature contributions are dynamically translated into plain-language tactical advice for incident commanders and field teams."
            ]
            for idx, step in enumerate(ml_steps):
                p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
                r = p.add_run()
                r.text = step
                r.font.size = Pt(24)
            print("Slide 15 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 16: Implementation – Semantic Lowering & Idiom Normalization (Heading stays exact!)
    # -------------------------------------------------------------------------
    s16 = prs.slides[15]
    for shape in s16.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            opt_steps = [
                ("Hydrodynamic Surge Modeling: ", "Solves Manning's open-channel formula (Q = 1/n * A * R^(2/3) * S^(1/2)) to project water depth contours and submerge low-lying road networks over 48 hours."),
                ("Wildfire Surface Propagation: ", "Evaluates Rothermel's rate-of-spread equations (incorporating fuel moisture, wind velocity, and terrain slope) to project fire boundary growth."),
                ("Seismic Attenuation: ", "Calculates Peak Ground Acceleration via Atkinson-Boore formulations to demarcate structural hazard rings and liquefaction zones."),
                ("Multi-Criteria A* Pathfinding: ", "Penalizes active hazard buffers to compute primary and alternate evacuation corridors with verified shelter capacity."),
                ("Coordinator Authorization Ledger: ", "Enforces a human-in-the-loop sign-off protocol before emergency resource dispatches are enacted and recorded to the mission ledger.")
            ]
            for idx, (lbl, desc) in enumerate(opt_steps):
                p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
                r1 = p.add_run()
                r1.text = lbl
                r1.font.bold = True
                r1.font.size = Pt(22)
                r2 = p.add_run()
                r2.text = desc
                r2.font.size = Pt(22)
            print("Slide 16 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 17: Test cases (1. Unit Testing)
    # -------------------------------------------------------------------------
    s17 = prs.slides[16]
    for shape in s17.shapes:
        if shape.has_table:
            t = shape.table
            unit_tests = [
                ("Open-Meteo & Flood Hydrology Ingestion", "Query (12.9716, 77.5946) telemetry via API", "Temperature, rain rate, and discharge (45 m³/s) parsed with source tags (PASS)"),
                ("USGS & NASA FIRMS Normalization", "Ingest active seismic and satellite thermal feeds", "Normalized GeoJSON schema with distance filtering and coordinates check (PASS)"),
                ("Calibrated ML Risk Inference", "Evaluate flood feature payload on ML gateway", "Classifies risk (CRITICAL), returns calibrated prob (92.8%), uncertainty 0.11 (PASS)"),
                ("Tree-Path SHAP XAI Explanation", "Post prediction vector to /api/explain endpoint", "Returns top 3 contributing factors, feature deltas, and actionable recommendations (PASS)"),
                ("Empirical Model Evaluation Metrics", "Query /api/ml/metrics for holdout metrics", "Returns genuine holdout metrics: 72.0% Acc, 0.7152 F1, 0.8851 ROC-AUC, 4x4 matrix (PASS)")
            ]
            for r_idx, (tc, wd, er) in enumerate(unit_tests, start=1):
                t.cell(r_idx, 0).text = tc
                t.cell(r_idx, 1).text = wd
                t.cell(r_idx, 2).text = er
            print("Slide 17 unit test table updated.")

    # -------------------------------------------------------------------------
    # SLIDE 18: Test cases (2. Integration Testing)
    # -------------------------------------------------------------------------
    s18 = prs.slides[17]
    for shape in s18.shapes:
        if shape.has_table:
            t = shape.table
            int_tests = [
                ("Evacuation Route Optimization", "Request route between hazard zone & shelter", "Generates primary & 3 alternate routes, verifies 490 available beds at destination (PASS)"),
                ("Capability-Matched Resource Dispatch", "Optimize dispatch for flood rescue crisis", "Matches NDRF Water Rescue team, verifies 9 trauma ICU beds, calculates 5 min ETA (PASS)"),
                ("Human-in-the-Loop Safety Guardrail", "Attempt physical asset dispatch without sign-off", "Enforces PENDING_APPROVAL; requires coordinator approval before physical enactment (PASS)"),
                ("Mission Replay & 72x Latency Benchmark", "Replay drill timeline events 00:00 to 00:50", "Calculates decision latency: 130 min baseline vs 1.8 min AI (72x speedup), exports AAR CSV (PASS)"),
                ("Grounded Copilot & Voice SITREP", "Submit query: 'Hospital ICU bed availability'", "Returns verified trauma beds; refuses unauthorized operational commands without sign-off (PASS)")
            ]
            for r_idx, (tc, wd, er) in enumerate(int_tests, start=1):
                t.cell(r_idx, 0).text = tc
                t.cell(r_idx, 1).text = wd
                t.cell(r_idx, 2).text = er
            print("Slide 18 integration test table updated.")

    # -------------------------------------------------------------------------
    # SLIDE 19: Test cases (3. System Testing)
    # -------------------------------------------------------------------------
    s19 = prs.slides[18]
    for shape in s19.shapes:
        if shape.has_table:
            t = shape.table
            sys_tests = [
                ("Full End-to-End Operational Flow", "Ingest live data -> predict -> evacuate -> dispatch", "Complete workflow executes seamlessly across all 3 tiers with sub-2s total latency (PASS)"),
                ("Offline SOS & IndexedDB Sync", "Disconnect network, submit citizen emergency reports", "Persists in IndexedDB, auto-syncs on reconnect, proximity deduplication eliminates spam (PASS)"),
                ("Digital Twin 48h Simulation Stability", "Run Manning's flood & Rothermel fire models", "Inundation curves and fire perimeters obey physical bounds without numeric instability (PASS)"),
                ("Failover & Resiliency Verification", "Terminate Python FastAPI microservice daemon", "Express gateway intercepts error, activates local calibrated physics model without crash (PASS)"),
                ("Cross-Browser PWA Performance", "Load on Chrome/Edge with simulated 3G network", "PWA service worker caches shell, interactive live map responsive under 60fps rendering (PASS)")
            ]
            for r_idx, (tc, wd, er) in enumerate(sys_tests, start=1):
                t.cell(r_idx, 0).text = tc
                t.cell(r_idx, 1).text = wd
                t.cell(r_idx, 2).text = er
            print("Slide 19 system test table updated.")

    # -------------------------------------------------------------------------
    # SLIDE 23: Conclusion
    # -------------------------------------------------------------------------
    s23 = prs.slides[22]
    for shape in s23.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            conc_points = [
                "Crisis Intelligence Hub resolves the critical vulnerabilities of contemporary emergency management: fragmented telemetry feeds, uncalibrated 'black-box' AI models, and crippling manual decision latency.",
                "By fusing multi-source satellite and hydrological telemetry with calibrated machine learning, tree-path explainability, and physics-driven digital twins, the platform transforms raw hazard data into verified, actionable intelligence.",
                "Demonstrating a verified 72x reduction in operational decision latency (from 130 minutes down to 1.8 minutes), it empowers incident commanders to protect communities, optimize resource dispatch, and save lives during major catastrophes."
            ]
            for idx, pt in enumerate(conc_points):
                p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
                r = p.add_run()
                r.text = pt
                r.font.size = Pt(24)
            print("Slide 23 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 24: Future Enhancements
    # -------------------------------------------------------------------------
    s24 = prs.slides[23]
    for shape in s24.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            p0 = tf.paragraphs[0]
            r0_1 = p0.add_run()
            r0_1.text = "Current Limitations: "
            r0_1.font.bold = True
            r0_1.font.size = Pt(24)
            r0_2 = p0.add_run()
            r0_2.text = "Regional satellite resolution relies on public 375m VIIRS passes; routing uses topological centroids rather than dynamic lane-level street closures."
            r0_2.font.size = Pt(24)

            p1 = tf.add_paragraph()

            p2 = tf.add_paragraph()
            r2 = p2.add_run()
            r2.text = "Future Enhancements: "
            r2.font.bold = True
            r2.font.size = Pt(36)

            p3 = tf.add_paragraph()
            r3_1 = p3.add_run()
            r3_1.text = "1: "
            r3_1.font.bold = True
            r3_1.font.size = Pt(32)
            r3_2 = p3.add_run()
            r3_2.text = "Integration with real-time autonomous drone swarm mesh networks for ultra-high-resolution millimeter-wave flood depth and LiDAR terrain reconstruction."
            r3_2.font.size = Pt(32)

            p4 = tf.add_paragraph()
            r4_1 = p4.add_run()
            r4_1.text = "2: "
            r4_1.font.bold = True
            r4_1.font.size = Pt(32)
            r4_2 = p4.add_run()
            r4_2.text = "Deployment of physics-informed neural operators (PINNs) for real-time 3D Navier-Stokes urban flood hydrodynamics and atmospheric smoke dispersion."
            r4_2.font.size = Pt(32)
            print("Slide 24 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 25: References
    # -------------------------------------------------------------------------
    s25 = prs.slides[24]
    for shape in s25.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            refs = [
                ("[1] ", "National Disaster Management Authority (NDMA) (2024). ", "\"National Disaster Management Plan and Standard Operating Procedures for Emergency Operations.\" Government of India."),
                ("[2] ", "Open-Meteo & ECMWF (2026). ", "\"Global Flood Awareness System (GloFAS) River Discharge Hydrology API Documentation.\""),
                ("[3] ", "U.S. Geological Survey (USGS) (2026). ", "\"Real-time Earthquake Hazards Program Feed and Ground Motion Attenuation Models.\" https://earthquake.usgs.gov/"),
                ("[4] ", "NASA FIRMS Authors (2026). ", "\"VIIRS 375m and MODIS Active Thermal Fire Anomaly Satellite Products.\" NASA Earthdata."),
                ("[5] ", "Niculescu-Mizil, A., & Caruana, R. (2005). ", "\"Predicting Good Probabilities With Supervised Learning (CalibratedClassifierCV).\" ICML 2005, pp. 625–632."),
                ("[6] ", "Lundberg, S. M., & Lee, S. I. (2017). ", "\"A Unified Approach to Interpreting Model Predictions (Tree SHAP).\" NeurIPS 30, pp. 4765–4774.")
            ]
            for idx, (num, auth, title) in enumerate(refs):
                p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
                r1 = p.add_run()
                r1.text = num
                r1.font.size = Pt(22)
                r2 = p.add_run()
                r2.text = auth
                r2.font.bold = True
                r2.font.size = Pt(22)
                r3 = p.add_run()
                r3.text = title
                r3.font.size = Pt(22)
            print("Slide 25 updated.")

    # -------------------------------------------------------------------------
    # SLIDE 26: Paper Publication details
    # -------------------------------------------------------------------------
    s26 = prs.slides[25]
    for shape in s26.shapes:
        if shape.name == 'Content Placeholder 2' and shape.has_text_frame:
            tf = shape.text_frame
            tf.clear()

            p0 = tf.paragraphs[0]
            r0_1 = p0.add_run()
            r0_1.text = "Paper Title: "
            r0_1.font.bold = True
            r0_1.font.size = Pt(24)
            r0_2 = p0.add_run()
            r0_2.text = "Autonomous Disaster Command & Real-Time AI Intelligence Engine: Calibrated Hazard Modeling and Explainable Evacuation Optimization"
            r0_2.font.size = Pt(24)

            p1 = tf.add_paragraph()
            r1_1 = p1.add_run()
            r1_1.text = "   Authors: "
            r1_1.font.bold = True
            r1_1.font.size = Pt(28)
            r1_2 = p1.add_run()
            r1_2.text = "Praveen H S, Ullas Jain M S, Vijay Kumar A, Nandish K"
            r1_2.font.size = Pt(28)

            p2 = tf.add_paragraph()
            r2_1 = p2.add_run()
            r2_1.text = "  Guides: "
            r2_1.font.bold = True
            r2_1.font.size = Pt(28)
            r2_2 = p2.add_run()
            r2_2.text = "Prof. Pratibha Pujari, Dr. Vrinda Shetty"
            r2_2.font.size = Pt(28)

            p3 = tf.add_paragraph()
            r3_1 = p3.add_run()
            r3_1.text = "Department & College: "
            r3_1.font.bold = True
            r3_1.font.size = Pt(24)
            r3_2 = p3.add_run()
            r3_2.text = "Dept. of Information Science & Engineering, "
            r3_2.font.size = Pt(24)

            p4 = tf.add_paragraph()
            r4 = p4.add_run()
            r4.text = "   Sai Vidya Institute of Technology, Bengaluru"
            r4.font.size = Pt(24)

            p5 = tf.add_paragraph()
            r5_1 = p5.add_run()
            r5_1.text = "Publication Status: "
            r5_1.font.bold = True
            r5_1.font.size = Pt(24)
            r5_2 = p5.add_run()
            r5_2.text = "Applied (Paper ID: 1277) , Still not received any response from them."
            r5_2.font.size = Pt(24)
            print("Slide 26 updated.")

    temp_pptx = 'temp_updated_presentation.pptx'
    prs.save(temp_pptx)
    print(f"Saved text-updated presentation to {temp_pptx}.")

    # -------------------------------------------------------------------------
    # MEDIA REPLACEMENT: Replace images inside PPTX ZIP with generated images
    # -------------------------------------------------------------------------
    final_output = 'Project_Final_Presentation.pptx'
    
    media_replacements = {
        'ppt/media/image3.png': 'generated_images/image3.png',
        'ppt/media/image4.jpeg': 'generated_images/image4.jpeg',
        'ppt/media/image5.png': 'generated_images/image5.png',
        'ppt/media/image6.jpeg': 'generated_images/image6.jpeg',
        'ppt/media/image7.jpeg': 'generated_images/image7.jpeg',
        'ppt/media/image8.jpeg': 'generated_images/image8.jpeg',
        'ppt/media/image9.jpeg': 'generated_images/image9.jpeg',
        'ppt/media/image10.jpeg': 'generated_images/image10.jpeg',
        'ppt/media/image11.jpeg': 'generated_images/image11.jpeg',
        'ppt/media/image12.jpeg': 'generated_images/image12.jpeg'
    }

    with zipfile.ZipFile(temp_pptx, 'r') as zin:
        with zipfile.ZipFile(final_output, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename in media_replacements and os.path.exists(media_replacements[item.filename]):
                    print(f"Replacing media: {item.filename} with {media_replacements[item.filename]}")
                    with open(media_replacements[item.filename], 'rb') as f:
                        zout.writestr(item, f.read())
                else:
                    zout.writestr(item, zin.read(item.filename))

    print(f"\n=======================================================")
    print(f"SUCCESS: Project presentation built cleanly as {final_output}")
    print(f"File size: {os.path.getsize(final_output):,} bytes")
    print(f"=======================================================")

if __name__ == '__main__':
    build_presentation()
