import os

def search_files(path):
    file_dict = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            file_dict[file] = os.path.join(root, file)
    return file_dict

def main():
    path = "C:/"
    file_dict = search_files(path)
    for file, path in file_dict.items():
        print(f"File: {file}, Path: {path}")

if __name__ == "__main__":
    main()
