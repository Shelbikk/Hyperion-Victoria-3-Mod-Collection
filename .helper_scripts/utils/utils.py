import os
import sys

output_path = os.path.join(os.path.dirname(sys.argv[0]), "outputs")

def save_file(filename, text):
    full_path = os.path.join(output_path, filename)
    with open(
        full_path,
        "w",
        encoding="utf-8-sig",
    ) as f:
        f.write(text)
