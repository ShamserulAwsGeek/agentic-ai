import csv
from pathlib import Path
from typing import List, Dict, Any
from typing_extensions import Doc
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_community.document_loaders import JSONLoader

def load_all_documents(data_dir: str) -> List[Any]:
    """
    Load all supported files from the data directory and convert to LangChain document structure.
    Supported: PDF, TXT, CSV, Excel, Word, JSON
    """
    #use project root path to load data files
    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data path: {data_path}")
    documents = []

    #PDF files:
    pdf_files = list(data_path.glob("**/*.pdf"))
    print(f"[DEBUG] Found {len(pdf_files)} PDF files:{[str(f) for f in pdf_files]}")
    for pdf_file in pdf_files:
        print(f"[DEBUG] Loading PDF file: {pdf_file}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            loader = loader.load()
            print(f"[DEBUG] Loaded {len(loader)} pages from PDF file: {pdf_file}")
            documents.extend(loader)
        except Exception as e:
            print(f"[ERROR] Failed to load PDF file {pdf_file}: {e}")
      
    #TXT files:
    txt_files = list(data_path.glob("**/*.txt"))
    print(f"[DEBUG] Found {len(txt_files)} TXT files:{[str(f) for f in txt_files]}")
    for txt_file in txt_files:
        print(f"[DEBUG] Loading TXT file: {txt_file}")
        try:
            loader = TextLoader(str(txt_file))
            loader = loader.load()
            print(f"[DEBUG] Loaded {len(loader)} pages from TXT file: {txt_file}")
            documents.extend(loader)
        except Exception as e:
            print(f"[ERROR] Failed to load TXT file {txt_file}: {e}")

    #CSVfiles:
    csv_files = list(data_path.glob("**/*.csv"))
    print(f"[DEBUG] Found {len(csv_files)} CSV files:{[str(f) for f in csv_files]}")
    for csv_file in csv_files:
        print(f"[DEBUG] Loading CSV file: {csv_file}")
        try:
            loader = CSVLoader(str(csv_file))
            loader = loader.load()
            print(f"[DEBUG] Loaded {len(loader)} pages from CSV file: {csv_file}")
            documents.extend(loader)
        except Exception as e:
            print(f"[ERROR] Failed to load CSV file {csv_file}: {e}")

    #Excel files:
    xlsx_files = list(data_path.glob("**/*.xlsx"))
    print(f"[DEBUG] Found {len(xlsx_files)} Excel files:{[str(f) for f in xlsx_files]}")
    for xlsx_file in xlsx_files:
        print(f"[DEBUG] Loading Excel file: {xlsx_file}")
        try:
            loader = UnstructuredExcelLoader(str(xlsx_file))
            loader = loader.load()
            print(f"[DEBUG] Loaded {len(loader)} pages from Excel file: {xlsx_file}")
            documents.extend(loader)
        except Exception as e:
            print(f"[ERROR] Failed to load Excel file {xlsx_file}: {e}")

    #Word files:
    docx_files = list(data_path.glob("**/*.docx"))
    print(f"[DEBUG] Found {len(docx_files)} Word files:{[str(f) for f in docx_files]}")
    for docx_file in docx_files:
        print(f"[DEBUG] Loading Word file: {docx_file}")
        try:
            loader = Docx2txtLoader(str(docx_file))
            loader = loader.load()
            print(f"[DEBUG] Loaded {len(loader)} pages from Word file: {docx_file}")
            documents.extend(loader)
        except Exception as e:
            print(f"[ERROR] Failed to load Word file {docx_file}: {e}")


    #JSON files:
    json_files = list(data_path.glob("**/*.json"))
    print(f"[DEBUG] Found {len(json_files)} JSON files:{[str(f) for f in json_files]}")
    for json_file in json_files:   
        print(f"[DEBUG] Loading JSON file: {json_file}")
        try:
            loader = JSONLoader(str(json_file))
            loader = loader.load()
            print(f"[DEBUG] Loaded {len(loader)} pages from JSON file: {json_file}")
            documents.extend(loader)
        except Exception as e:
            print(f"[ERROR] Failed to load JSON file {json_file}: {e}")
    


#Example usage:
# if __name__ == "__main__":
#     docs = load_all_documents("data")
#     print(f"Loaded {len(docs)} documents.")
#     print("Example document:", docs[0] if docs else None)