# 🔍 Universal File Search Engine

## 📌 Overview
The **Universal File Search Engine** is a powerful Python-based tool that allows users to **search for files by name, extension, or content** inside text and PDF files. With a **user-friendly GUI**, this tool helps locate files efficiently in large directories.

## 🚀 Features
✅ **Search by File Name & Extension** (e.g., `.pdf`, `.txt`, `*.*` for all)  
✅ **Search Inside File Content** (PDFs, Text, Code Files)  
✅ **Recursive Search** (Looks in subdirectories)  
✅ **Multi-Threaded Search** (Fast performance)  
✅ **GUI with Tkinter** (Easy to use)  
✅ **Export Search Results to CSV** (Save results for later)  

---
## 📖 Usage Guide
#🔹 Steps to Use
1️⃣ Select the directory you want to search.
2️⃣ Enter the file type (*.pdf, *.txt, *.py, *.* for all).
3️⃣ (Optional) Enter a keyword to search inside file contents.
4️⃣ Click "Search" and view results in real-time.
5️⃣ Click "Export to CSV" to save results.
---

## 🤖 Technical Details
GUI Framework: Tkinter
File Searching: os.walk, fnmatch
PDF Text Extraction: PyMuPDF (fitz)
Multi-threading: threading module
Data Export: csv module

## 🛠 Troubleshooting
🔹 Issue: PyMuPDF Import Error (fitz not found)
Try reinstalling PyMuPDF:
```bash
pip uninstall pymupdf
pip install pymupdf
```
🔹 Issue: No Search Results
Make sure the correct directory and file type are selected.
Ensure the file contains the searched keyword (for content search).


## 🔧 Installation & Setup

### 📌 **1️⃣ Install Dependencies**
Make sure Python is installed (preferably Python 3.9+). Install required dependencies:

```bash
pip install pymupdf tk
