import glob
import cv2
import random
import copy

f = open("./test.txt", 'r')
grayOn = False

for num in range(3300, 3308):

    # txt파일에서 파일 이름이랑, permutation 정보 가져옴.
    filename = f.readline()
    permut = f.readline().split(' ')

    # permut.pop()

    i = 0
    print(permut)
    for x in range(0, 64):
        permut[i] = int(permut[i])
        i = i + 1
    print(permut)

    now_filename = str(num) + ".png"
    now_url = "./data_test2_blank/64/" + str(num) + ".png"

    # 프레임은 가져온 원본 이미지, ret은 저장하는 이미지.

    frame = cv2.imread(now_url, cv2.IMREAD_COLOR)
    if grayOn:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret = frame.copy()

    (img_h, img_w) = frame.shape[:2]
    grid_w = img_h / 8  # crop width
    grid_h = img_w / 8  # crop height
    range_w = (int)(img_w / grid_w)
    range_h = (int)(img_h / grid_h)

    bbox = [[[[0, 0, 0, 0]] for x in range(8)] for y in range(8)]

    for i in range(0,64):
        cv2.imshow(now_filename, ret)

        (Y,X) = i, permut[i]
        print(X, Y)

        (w, h) = int(X % 8), int(X / 8)
        x1, y1, x2, y2 = int(h * grid_h), int(w * grid_w), int((h + 1) * (grid_h)), int((w + 1) * (grid_w))

        (w, h) = int(Y % 8), int(Y / 8)
        Mx1, My1, Mx2, My2 = int(h * grid_h), int(w * grid_w), int((h + 1) * (grid_h)), int((w + 1) * (grid_w))

        ret[Mx1:Mx2, My1:My2] = frame[x1:x2, y1:y2].copy()

        print("!!")


    if grayOn:
        save_path = "./test1_64_graycrop/"
    else:
        save_path = "./data_answer/"
    save_name = save_path + "64-" + str(num) + ".jpg"
    retval = cv2.imwrite(save_name, ret)
    print('save file ' + save_name + '....')
f.close()

"""
    Shuffle                 Solved
    0 1 2 3 4 5 6           41 58 9 2 37 1 30 
    
    알 수 있는 것 : Shuffle 이미지 & Solved의 숫자 '41 58 9 2 37 1 30 '
    여기서 Solved의 이미지를 만들어 내야 한다!! 
    
"""