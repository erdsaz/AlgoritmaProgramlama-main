"""import os

liste=os.listdir(path)

os.path.join(x,y)

os.isdir(.path)

os.path.exist(path)

os.makedirs"""

import os
import json

test_dict={
    "key":"value",
    "key2":"value2",
        "key3":"value3"
}

print(test_dict["key2"])



def f(start_path,search_pattern):
    file_or_folders = os.listdir(start_path)
    for ff in file_or_folders:
        new_path = os.path.join(start_path,ff)
        if os.path.isdir(ff):
            f(start_path=new_path, search_pattern=search_pattern)
        else:
            if search_pattern in ff:
                print(ff)


print(f(start_path=".", search_pattern=".md"))