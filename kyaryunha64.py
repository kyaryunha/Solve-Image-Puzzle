import glob
import cv2
import random

images = glob.glob('./data_test1_blank/64/*.png')  # 2400 <= x <= 2699
f = open("./test1_64.txt", 'w')


images = []

for num in range(2400, 2700):
    now_filename = str(num)+".png"
    now_url = "./data_test1_blank/64/"+str(num)+".png"

    shuffled = ""
    f.write(now_filename)
    f.write("\n")
    lis = list(range(0, 64))
    random.shuffle(lis)
    for i in lis:
        shuffled = shuffled + str(i) + " "
    f.write(shuffled)
    f.write("\n")
f.close()