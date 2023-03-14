from glob import glob
import os
from typing import Tuple


def get_length_longest_string_in_list(slist: list[str]) -> int | None:
    if slist:
        lengths = [len(s) for s in slist]
        index_of_max_lengths = lengths.index(max(lengths))
        return lengths[index_of_max_lengths]


def get_filenames_in_dir(path: str) -> list:
    return [os.path.basename(x) for x in glob(f"{path}/*")]


def find_duplicate_chars(s: str) -> bool:
    uniq_chars = set(s)
    for char in uniq_chars:
        if char * 2 in s:
            return True
    return False


def get_new_filenames(path: str) -> Tuple[dict, list]:
    files = get_filenames_in_dir(path)
    len_longest_filename = get_length_longest_string_in_list(files)

    new_names = dict()
    duplicate_error = list()

    for file in files:
        if not find_duplicate_chars(file):
            new_names[file] = f"{file:_<{len_longest_filename}}"
        else:
            duplicate_error.append(file)

    return new_names, duplicate_error


