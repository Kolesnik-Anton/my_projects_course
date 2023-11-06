# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
import os


def acounting(param):
    with open(param) as f:
     lines = f.readlines()
    return len(lines)


def rewriting(file_for_writing: str, base_path, location):
    files_list = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        files_list.append([acounting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i])
    for file_from_list in sorted(files_list):
        opening_files = open(file_for_writing, 'a')
        opening_files.write(f'{file_from_list[2]}\n')
        opening_files.write(f'{file_from_list[0]}\n')
        with open(file_from_list[1], 'r') as file:
            counting = 1
            for line in file:
                opening_files.write(f'{line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()


rewriting("3.txt", "C:/Users/user/PycharmProjects/pythonProject9", "files")