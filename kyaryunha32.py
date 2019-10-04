import glob
import cv2
import random

f = open("./test1_32.txt", 'w')

for num in range(3000, 3300):
    now_filename = str(num)+".png"
    now_url = "./data_test1_blank/32/"+str(num)+".png"

    shuffled = ""
    f.write(now_filename)
    f.write("\n")
    lis = list(range(0, 256))
    random.shuffle(lis)
    for i in lis:
        shuffled = shuffled + str(i) + " "
    f.write(shuffled)
    f.write("\n")
f.close()