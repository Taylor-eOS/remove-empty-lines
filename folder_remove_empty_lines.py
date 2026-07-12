#!/usr/bin/env python3
import os
import sys

folder_path = input("Input folder path: ").strip()
if folder_path.startswith("file://"):
    folder_path = folder_path[7:]
if not os.path.isdir(folder_path):
    print("Invalid directory.")
    sys.exit(1)
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            while '\n\n' in text:
                text = text.replace('\n\n', '\n')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text)
        except Exception as e:
            print(f"Skipping {file_path}: {e}")
