import os
def load_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        files = [os.path.join(root, name) for name in dirs]
    return files
def load_files(path):
    for root, dirs, files in os.walk(path, topdown=False):
        files = [os.path.join(root, name) for name in files
    return files
