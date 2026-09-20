#!/usr/bin/env python3
import csv, hashlib, json, os, re, subprocess, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "jane-standards-library"
DOCS = ROOT / "public"
DOCS.mkdir(parents=True, exist_ok=True)

ITEMS = [
  ("DMT-01", "Community Facility Planning Standards", "https://www.dmt.gov.ae/-/media/Project/DMT/DMT/E-Library/10-24/02/DMT_Community-Facility-Planning-Standards_EN_Interactive_2_Map-Update.pdf"),
  ("DMT-02", "Abu Dhabi Public Toilet Planning and Regulation Manual", "https://dmt.gov.ae/-/media/Project/DMT/DMT/E-Library/05-25/Abu-Dhabi-Public-Toilet-Planning-and-Regulation-Manual-EN.pdf"),
  ("DMT-03", "Abu Dhabi Waste Bin Planning and Regulation Manual Part 1", "https://www.dmt.gov.ae/-/media/Project/DMT/DMT/E-Library/10-24/20220713_Abu-Dhabi-Waste-Bin-Planning-and-Regulation-Manual_Part-1.pdf"),
  ("DMT-04", "Abu Dhabi Urban Street Design Manual", "https://www.dmt.gov.ae/-/media/Project/DMT/DMT/E-Library/0001-Manuals/Abu-Dhabi-Urban-Street-Design-Manual.pdf"),
  ("DMT-05", "Unified As-Built GeoSpatial Data Submission Standards", "https://admobility.gov.ae/services/-/media/As-Built-Data-Submission-Standards.pdf"),
  ("ISGL-00", "Infrastructure Standards and Guidelines", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL.pdf"),
  ("ISGL-CATALOG", "ISGL List", "https://qcc.gov.ae/-/media/Project/QCC/QCC/Documents/opendata/STANDARDS/ISGL-List.pdf"),
  ("ISGL-01", "ISGL Appendix III", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/Appendix-III.pdf"),
  ("ISGL-02", "ISGL Chapter 05", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/Ch.05.pdf"),
  ("ISGL-03", "DP-301", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/DP-301.pdf"),
  ("ISGL-04", "DP-304", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/DP-304.pdf"),
  ("ISGL-05", "DP-306", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/DP-306.pdf"),
  ("ISGL-06", "GA-904", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/GA-904.pdf"),
  ("ISGL-07", "GA-905", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/GA-905.pdf"),
  ("ISGL-08", "TR-506-4", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/TR-506-4.pdf"),
  ("ISGL-09", "TR-508", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/TR-508.pdf"),
  ("ISGL-10", "TR-511", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/TR-511.pdf"),
  ("ISGL-12", "ROW-601", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/ROW-601.pdf"),
  ("ISGL-13", "WA-705", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/WA-705.pdf"),
  ("ISGL-14", "WA-726-1", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/WA-726-1.pdf"),
  ("ISGL-15", "EN-804", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/EN-804.pdf"),
  ("ISGL-16", "EN-816", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/EN-816.pdf"),
  ("ISGL-17", "TE-1102", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/TE-1102.pdf"),
  ("ISGL-18", "WM-1213", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/WM-1213.pdf"),
  ("ISGL-19", "DC-1003", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ISGL/ISGL-LIST/DC-1003.pdf"),
  ("ADM-03", "ADG-005-2017", "https://jawdah.qcc.abudhabi.ae/en/Registration/QCCServices/Services/STD/ADG/ADG-005-2017-En.pdf"),
  ("ADM-04", "ADG-15 Industrial Lands Mussafah", "https://www.qcc.gov.ae/-/media/Project/QCC/QCC/Documents/Quality-Infrastructure-Documents/Abu-Dhabi-Specification/Abu-Dhabi-Guideline/ADG-15---Development-And-Organization-of-Industrial-Lands-Guideline-for-Mussafah-Region.pdf"),
  ("TAQA-04", "AADC GL.AM.01", "https://www.aadc.ae/docs/GL.AM.01.pdf"),
  ("TAQA-05", "AADC public standard", "https://www.aadc.ae/img/394bc1b2-e24c-475d-9a01-c4d31ee122cc.pdf"),
  ("DOE-01", "Customer Metering Regulations Second Edition", "https://doe.gov.ae/-/media/Project/DOE/Department-Of-Energy/Media-Center-Publications/Regulations/English/the-customer-metering-regulations-second-edition.pdf"),
  ("DOE-02", "Recycled Water and Biosolids Regulations 2021 Edition 3", "https://www.doe.gov.ae/-/media/Project/DOE/Department-Of-Energy/Media-Center-Publications/Regulations/English/Recycled-Water--Biosolids-Regulations-2021-Edition-3.pdf"),
  ("DOE-03", "Water Quality Regulation 2025", "https://www.doe.gov.ae/-/media/Project/DOE/Department-Of-Energy/Media-Center-Publications/Water-Quality-Regulation-2025.pdf"),
  ("ESTIDAMA-02", "Pearl Rating System for Communities Version 1.0", "https://www.dmt.gov.ae/-/media/Project/DMT/DMT/E-Library/0001-Manuals/PRRS/PRRS-Version-10.pdf"),
  ("ESTIDAMA-03", "Pearl Rating System for Villas Version 1.0", "https://dmt.gov.ae/-/media/Project/DMT/DMT/E-Library/0001-Manuals/PVRS/PVRS-Version-10.pdf"),
  ("ADCDA-01", "ADG 45 2024 Temporary Buildings Fire Safety", "https://srv.adcda.gov.ae/ar/Doc/Guidelines%20Manual%20temp%20building.pdf"),
]

def safe_name(s):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", s).strip("-")[:110]

def pdfinfo(path):
    try:
        p = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True, timeout=60)
        info = {}
        for line in p.stdout.splitlines():
            if ":" in line:
                k,v=line.split(":",1); info[k.strip().lower()] = v.strip()
        return info, p.returncode
    except Exception:
        return {}, 99

def acquire(item):
    ident, title, url = item
    path = DOCS / f"{ident}__{safe_name(title)}.pdf"
    status="downloaded"
    error=""
    try:
        req=urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 Jane-Standards-Library/1.0"})
        with urllib.request.urlopen(req, timeout=45) as src, open(path, "wb") as dst:
            while True:
                chunk=src.read(1024*1024)
                if not chunk: break
                dst.write(chunk)
        if path.stat().st_size < 100 or path.read_bytes()[:5] != b"%PDF-":
            status="invalid-response"
    except Exception as e:
        status="failed"; error=f"{type(e).__name__}: {e}"
    info, rc = pdfinfo(path) if path.exists() else ({}, 99)
    if status == "downloaded" and rc != 0:
        status="invalid-pdf"
    sha=""
    size=path.stat().st_size if path.exists() else 0
    if path.exists():
        sha=hashlib.sha256(path.read_bytes()).hexdigest()
    row = {
      "id":ident,"catalogue_title":title,"source_url":url,"retrieval_status":status,
      "retrieved_utc":__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),
      "file_name":path.name,"file_size_bytes":size,"sha256":sha,
      "pdf_title":info.get("title", ""),"author":info.get("author", ""),
      "creation_date":info.get("creationdate", ""),"pages":info.get("pages", ""),
      "encrypted":info.get("encrypted", ""),"error":error,
    }
    print(f"{ident}: {status} {size} bytes {info.get('pages','?')} pages", flush=True)
    return row

rows=[]
with ThreadPoolExecutor(max_workers=6) as pool:
    futures=[pool.submit(acquire, item) for item in ITEMS]
    for future in as_completed(futures):
        rows.append(future.result())
rows.sort(key=lambda r: r["id"])

fields=list(rows[0].keys())
with open(ROOT/"verified-download-manifest.csv", "w", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
with open(ROOT/"verified-download-manifest.json", "w", encoding="utf-8") as f:
    json.dump(rows,f,indent=2,ensure_ascii=False)
ok=sum(r["retrieval_status"]=="downloaded" for r in rows)
print(f"SUMMARY downloaded={ok} failed_or_invalid={len(rows)-ok} total={len(rows)}")
sys.exit(0 if ok else 1)
