with open(
    "/home/kai/learning/Python_Foundation/notebooks/ch10_Files and Exceptions/text_files/pi_digits.txt"
) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

from pathlib import Path

print(Path.cwd())
