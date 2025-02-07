import os
import fnmatch
import fitz  # PyMuPDF for PDF text extraction
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
import csv

class FileSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal File Search Engine")
        self.root.geometry("600x400")

        # Labels and Entry fields
        tk.Label(root, text="Select Directory:").pack(pady=5)
        self.directory_entry = tk.Entry(root, width=50)
        self.directory_entry.pack()
        tk.Button(root, text="Browse", command=self.browse_directory).pack()

        tk.Label(root, text="Search File Type (e.g., *.pdf, *.txt, *.* for all):").pack(pady=5)
        self.file_type_entry = tk.Entry(root, width=50)
        self.file_type_entry.pack()

        tk.Label(root, text="Keyword (optional - for content search):").pack(pady=5)
        self.keyword_entry = tk.Entry(root, width=50)
        self.keyword_entry.pack()

        # Search Button
        tk.Button(root, text="Search", command=self.start_search).pack(pady=10)

        # Results Display
        self.result_text = scrolledtext.ScrolledText(root, height=10, width=70)
        self.result_text.pack(pady=10)

        # Export Button
        tk.Button(root, text="Export to CSV", command=self.export_results).pack()

        self.results = []

    def browse_directory(self):
        folder_selected = filedialog.askdirectory()
        self.directory_entry.insert(0, folder_selected)

    def search_files(self, directory, pattern, keyword=None):
        self.results = []
        for root, _, files in os.walk(directory):
            for file in fnmatch.filter(files, pattern):
                file_path = os.path.join(root, file)

                # If keyword is provided, search inside the file
                if keyword and file.endswith(".pdf"):
                    if self.search_text_in_pdf(file_path, keyword):
                        self.results.append(file_path)
                elif keyword and file.endswith((".txt", ".py", ".java", ".c")):
                    if self.search_text_in_file(file_path, keyword):
                        self.results.append(file_path)
                elif not keyword:
                    self.results.append(file_path)

        self.display_results()

    def search_text_in_pdf(self, file_path, keyword):
        try:
            with fitz.open(file_path) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
                return keyword.lower() in text.lower()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return False

    def search_text_in_file(self, file_path, keyword):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return keyword.lower() in f.read().lower()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return False

    def start_search(self):
        directory = self.directory_entry.get()
        pattern = self.file_type_entry.get()
        keyword = self.keyword_entry.get().strip()

        if not directory or not pattern:
            messagebox.showerror("Error", "Please select a directory and file type.")
            return

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Searching...\n")

        search_thread = threading.Thread(target=self.search_files, args=(directory, pattern, keyword))
        search_thread.start()

    def display_results(self):
        self.result_text.delete(1.0, tk.END)
        if self.results:
            for file in self.results:
                self.result_text.insert(tk.END, file + "\n")
        else:
            self.result_text.insert(tk.END, "No files found.\n")

    def export_results(self):
        if not self.results:
            messagebox.showerror("Error", "No search results to export!")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["File Path"])
                for result in self.results:
                    writer.writerow([result])

            messagebox.showinfo("Success", f"Results exported to {file_path}")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = FileSearchApp(root)
    root.mainloop()
