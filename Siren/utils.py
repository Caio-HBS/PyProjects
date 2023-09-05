import os
import json
import shutil

from difPy import dif

def change_duplicates_directory(
        list_of_paths_of_duplicates: list, 
        new_directory_for_duplicates
):
    """
    Takes the list of file paths provided by difPy and changes those files to a 
    new folder.
        Args:
            list_of_paths_of_duplicates: list of duplicates provided by difPy;
            new_directory_for_duplicates: path for the new directory where 
            duplicates will be stored.
    """
    for single_file_path in list_of_paths_of_duplicates:
        file_name = os.path.basename(single_file_path)
        new_directory_path = os.path.join(new_directory_for_duplicates, file_name)
        shutil.move(single_file_path, new_directory_path)
