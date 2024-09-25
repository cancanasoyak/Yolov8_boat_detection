import shutil


def move_data(source:str, destination, ends_with:str):
    """
    Move files from source to destination if the file ends with a certain string.

    :param source: Source directory
    :param destination: Destination directory
    :param ends_with: String that the file should end with
    """
    for file in source.iterdir():
        if file.is_file() and file.name.endswith(ends_with):
            shutil.move(file, destination)
            print(f'Moved {file.name} to {destination}')
            
if __name__ == "__main__":
    source = r"SourceDirectory"
    destination = r"DestinationDirectory"
    ends_with = ".npz"
    move_data(source, destination, ends_with)