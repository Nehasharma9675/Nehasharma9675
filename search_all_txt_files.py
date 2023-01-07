import os
import shutil

search_dir = r'C:\Program Files\Git'
dst_root = r'D:\temp\dst'
i = 0
for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith('.txt'):
            i = i+1
            src_path = os.path.join(root, file)
            dst_path = os.path.join(dst_root, f"A{i}.txt")
            shutil.copyfile(src_path, dst_path)
            print(dst_path)
# files.sort()
# print(files)