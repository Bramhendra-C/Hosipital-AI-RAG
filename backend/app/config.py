from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data Directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
CHUNKS_DIR = DATA_DIR / "chunks"
VECTORSTORE_DIR = DATA_DIR / "vectorstore"

# Files
PDF_PATH = RAW_DIR / "TMH_Patient_Booklet_2026.pdf"
VECTOR_DB_PATH = VECTORSTORE_DIR / "faiss_index"

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-3.5-flash"

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found.")