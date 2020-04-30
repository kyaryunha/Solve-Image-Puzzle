import cv2
import numpy as np
for num in range(3300, 3301):
    shuffle_filename = str(num) + ".png"
    shuffle_url = "./data_test2_blank/64/" + str(num) + ".png"
    answer_filename = str(num) + ".png"
    answer_url = "./data_answer/" + "64-" + str(num) + ".png"

    shuffle = cv2.imread(shuffle_url, cv2.IMREAD_COLOR)
    answer = cv2.imread(answer_url, cv2.IMREAD_COLOR)

    cv2.imshow('sh', shuffle)
    cv2.imshow('an', answer)
    cv2.waitKey(0)

    shuffle_permut = list(range(0, 64))

    ### This Program's goal is Know about answer's perm

    ### Get a bbox
    (img_h, img_w) = shuffle.shape[:2]
    grid_w = img_h / 8  # crop width
    grid_h = img_w / 8  # crop height
    range_w = (int)(img_w / grid_w)
    range_h = (int)(img_h / grid_h)

    ### Matching ~

    used = [False] * 64
    answer_str = ""

    for i in range(0, 64):

        X = i

        sx = int(i / 8)
        sy = i % 8

        found = False

        # print("!!!!!!!!!!!!!!!!!!!!!11")
        mini_num = 10000000000
        mini_who = X
        mini_idx = -1

        for j in range(0, 64):

            if used[j]:
                continue

            Y = int(j / 8) * 8 + (j % 8)

            rx = int(j / 8)
            ry = j % 8

            # print(X, Y)

            (w, h) = int(X % 8), int(X / 8)
            x1, y1, x2, y2 = int(h * grid_h), int(w * grid_w), int((h + 1) * (grid_h)), int((w + 1) * (grid_w))

            (w, h) = int(Y % 8), int(Y / 8)
            Mx1, My1, Mx2, My2 = int(h * grid_h), int(w * grid_w), int((h + 1) * (grid_h)), int((w + 1) * (grid_w))

            shuffle_roi = shuffle[x1:x2, y1:y2].copy()
            ret_roi = answer[Mx1:Mx2, My1:My2].copy()

            diff = 0
            for fir in range(0,15):
                for sec in range(0,15):
                    for thi in range(0,3):
                        cha = -1
                        if shuffle_roi[fir][sec][thi] > ret_roi[fir][sec][thi]:
                            cha = shuffle_roi[fir][sec][thi] - ret_roi[fir][sec][thi]
                        else:
                            cha = ret_roi[fir][sec][thi] - shuffle_roi[fir][sec][thi]
                        if cha <= 3:
                            diff = diff + 1

            if mini_num > diff:
                mini_num = diff
                mini_who = Y
                mini_idx = j
        used[mini_idx] = True
        print(mini_who)
        answer_str = answer_str + str(mini_who) + " "
    print("ans", answer_str)

