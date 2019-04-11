import os.path
from pathlib import Path
a=os.path.join("D:\重要文件","ssr-win","pac.txt")
print(a)

data_folder=Path("D:\重要文件\ssr-win")
file_to_open=data_folder/"pac.txt"
#pathlib可以直接读取文件而不需要open
print(file_to_open.read_text())

print(file_to_open.name)
print(file_to_open.suffix)
print(file_to_open.stem)
