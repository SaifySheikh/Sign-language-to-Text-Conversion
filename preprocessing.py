import numpy as np
import cv2
import os
from image_processing import func

if not os.path.exists("data2"):
    os.makedirs("data2")

if not os.path.exists("data2/train"):
    os.makedirs("data2/train")

if not os.path.exists("data2/test"):
    os.makedirs("data2/test")

path = "data2/train"  # Update the path
path1 = "data2"
a = ['label']

for i in range(64 * 64):
    a.append("pixel" + str(i))

label = 0
var = 0
c1 = 0
c2 = 0

for (dirpath, dirnames, filenames) in os.walk(path):
    print("hello")
    for dirname in dirnames:
        print(dirname)
        for (direcpath, direcnames, files) in os.walk(os.path.join(path, dirname)):
            if not os.path.exists(os.path.join(path1, "train", dirname)):
                os.makedirs(os.path.join(path1, "train", dirname))
            if not os.path.exists(os.path.join(path1, "test", dirname)):
                os.makedirs(os.path.join(path1, "test", dirname))

            num = 100000000000000000
            i = 0
            for file in files:
                var += 1
                actual_path = os.path.join(path, dirname, file)
                actual_path1 = os.path.join(path1, "train", dirname, file)
                actual_path2 = os.path.join(path1, "test", dirname, file)
                img = cv2.imread(actual_path, 0)
                bw_image = func(actual_path)
                if i < num:
                    c1 += 1
                    cv2.imwrite(actual_path1, bw_image)
                else:
                    c2 += 1
                    cv2.imwrite(actual_path2, bw_image)

                i = i + 1

        label = label + 1

print(var)
print(c1)
print(c2)
