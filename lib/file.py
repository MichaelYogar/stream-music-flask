import os


# TODO: implement
def normalize(filename):
    return filename

def read_files(folder_path):
    full_path = os.getcwd() + folder_path
    onlyfiles = [f for f in os.listdir(full_path) if os.path.isfile(os.path.join(full_path, f))]
    print(onlyfiles)
    return onlyfiles
