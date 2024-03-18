#!/usr/bin/python3
import pandas as pd
import openpyxl



class XlsxLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.workbook = None
        self.sheets = []

    def load_file(self):
        try:
            self.workbook = openpyxl.load_workbook(self.file_path)
            self.sheets = self.workbook.sheetnames
            print("File loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error loading file: {str(e)}")

# Usage example
loader = XlsxLoader('/path/to/your/file.xlsx')
loader.load_file()
print(loader.sheets)


