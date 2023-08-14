import tkinter as tk
from tkinter import filedialog
import os
import time
from collections import defaultdict
from tabulate import tabulate

def display_banner(banner):
    print("\033[93m" + banner + "\033[0m")

banner = r'''
██████╗ ██████╗ ██╗██╗   ██╗███████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔══██╗██║██║   ██║██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██║  ██║██████╔╝██║██║   ██║█████╗      ███████╗██║     ███████║██╔██╗ ██║
██║  ██║██╔══██╗██║╚██╗ ██╔╝██╔══╝      ╚════██║██║     ██╔══██║██║╚██╗██║
██████╔╝██║  ██║██║ ╚████╔╝ ███████╗    ███████║╚██████╗██║  ██║██║ ╚████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ V1.0

- Comprehensive Drive & Folder Analyzer
'''

import time

def display_typing_message(message, color, delay=0.05):
    for char in message:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print('\033[0m')  # Reset color

def main_warning():
    warning = (
        "WARNING! -  I don't suggest to use the tool for C: Drive.\n"
        "Analyzing a directory with a substantial number of small files\n" 
        "can indeed slow down the process and potentially cause the tool\n"
        "to appear unresponsive or crash.\n"
        "\n"
        "- Rajput Shubhraj Singh \n"
        "- (Github) @Shuuubhraj  \n"
    )
    display_typing_message(warning, '\033[91m')

def convert_size(size_in_bytes):
    if size_in_bytes < 1024:
        return f"{size_in_bytes} B"
    elif size_in_bytes < 1024 ** 2:
        return f"{size_in_bytes / 1024:.2f} KB"
    elif size_in_bytes < 1024 ** 3:
        return f"{size_in_bytes / (1024 ** 2):.2f} MB"
    elif size_in_bytes < 1024 ** 4:
        return f"{size_in_bytes / (1024 ** 3):.2f} GB"
    else:
        return f"{size_in_bytes / (1024 ** 4):.2f} TB"

def analyze_drive(drive_path):
    print("\033[93m" + "Analyzing files..." + "\033[0m")
    file_info_by_type = defaultdict(lambda: {"count": 0, "size": 0})
    file_list = []
    
    for root, dirs, files in os.walk(drive_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)

    total_files = len(file_list)
    processed_files = 0
    start_time = time.time()

    for file_path in file_list:
        _, extension = os.path.splitext(file_path)
        file_size = os.path.getsize(file_path)
        file_info_by_type[extension]["count"] += 1
        file_info_by_type[extension]["size"] += file_size
        processed_files += 1
        elapsed_time = time.time() - start_time
        average_time_per_file = elapsed_time / processed_files
        remaining_files = total_files - processed_files
        estimated_remaining_time = remaining_files * average_time_per_file

        print(f"\r\033[91mAnalyzing: {processed_files}/{total_files} files - Estimated Remaining Time: {estimated_remaining_time:.2f} seconds", end="")

    total_size = 0
    table_data = []

    for extension, info in file_info_by_type.items():
        if extension:
            size_str = convert_size(info['size'])
            count_str = f"{info['count']} files"
            table_data.append([extension, count_str, size_str])
            total_size += info['size']

    total_size_str = convert_size(total_size)
    headers = ["File Type", "Files Count", "Size"]
    print("\n\033[91mResults:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print(f"\n\033[92mTotal Size: {total_size_str}")
    print(f"Analysis completed.\033[0m")

def main():
    main_warning()

    while True:
        print("\033[93m" + 'Type "1" to select any (Drive/Folder) location or Enter to exit' + "\033[0m")
        user_input = input()

        if user_input == "1":
            drive = filedialog.askdirectory(initialdir="C:/", title="Select Drive or Folder")
            if drive:
                analyze_drive(drive)
        else:
            break

if __name__ == "__main__":
    display_banner(banner)
    main()
