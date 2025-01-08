import os

def ListFiles_Folder(xfolder_path):

# List to store file names
    file_names = []

# Iterate through the files in the folder
    for file in os.listdir(xfolder_path):
    # Check if it's a file (not a directory)
        if os.path.isfile(os.path.join(xfolder_path, file)):
            file_names.append(file)
    return file_names

# Print the list of file names
#print(file_names)
