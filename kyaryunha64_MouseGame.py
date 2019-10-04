import cv2
import random

grayOn = False

f = open("./test1_64.txt", 'a')

cnt, Cx1, Cy1, Cx2, Cy2 = 0, 0, 0, 0, 0


def Clicking(event, x, y, flags, param):
    global cnt, Cx1, Cy1, Cx2, Cy2
    if event == cv2.EVENT_LBUTTONDOWN:
        if cnt == 0:
            Cx1 = x
            Cy1 = y
            cnt = cnt + 1
        elif cnt == 1:
            Cx2 = x
            Cy2 = y
            cnt = cnt + 1


########################################################################
# Starting

for num in range(2400, 2401):

    # txt 파일 파일명 적어줌. 2400.png 이런거
    now_filename = str(num) + ".png"
    now_url = "./data_test1_blank/64/" + str(num) + ".png"
    f.write(now_filename)
    f.write("\n")

    while True:
        permut = list(range(0, 64))
        # random.shuffle(permut)
        print(permut)

        img_filename = str(num) + ".png"
        img_url = "./data_test1_blank/64/" + str(num) + ".png"

        # 프레임은 가져온 원본 이미지, ret은 저장하는 이미지.
        frame = cv2.imread(img_url, cv2.IMREAD_COLOR)
        if grayOn:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        ret = frame.copy()
        (img_h, img_w) = frame.shape[:2]

        ############################################################################
        # 에지처리하는 그레이 이미지용 코드들 ( 지금은 쓸모 없음.. 언젠가 휴리스틱하면 쓰게 될지도 ? )
        if grayOn:
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            frame = clahe.apply(frame)
            frame = cv2.Laplacian(frame, ddepth=cv2.CV_8U, ksize=3, scale=1, delta=0)
            frame = cv2.bilateralFilter(frame, 13, 50, 50)
            (_, frame) = cv2.threshold(frame, 55, 255, cv2.THRESH_BINARY)

        ############################################################################
        # 전처리
        grid_w = img_h / 8  # crop width
        grid_h = img_w / 8  # crop height
        range_w = (int)(img_w / grid_w)
        range_h = (int)(img_h / grid_h)

        bbox = [[[[0, 0, 0, 0]] for x in range(8)] for y in range(8)]
        """
        i = 0
        for w in range(range_w):
            for h in range(range_h):
                x1, y1, x2, y2 = int(h * grid_h), int(w * grid_w), int((h + 1) * (grid_h)), int((w + 1) * (grid_w))
                bbox[int(i % 8)][int(i / 8)] = [x1, x2, y1, y2]
                i = i + 1
        i = 0
        for w in range(range_w):
            for h in range(range_h):
                x1, y1, x2, y2 = int(h * grid_h), int(w * grid_w), int((h + 1) * (grid_h)), int((w + 1) * (grid_w))
                Mx1, Mx2, My1, My2 = bbox[int(permut[i] % 8)][int(permut[i] / 8)]
                roi = frame[x1:x2, y1:y2]
                ret[Mx1:Mx2, My1:My2] = roi
                i = i + 1
        """

        ###################################################################
        # Gaming
        cv2.namedWindow(now_filename)
        cv2.setMouseCallback(now_filename, Clicking)
        while True:
            cv2.imshow(now_filename, ret)

            if cnt == 2:
                X = int(Cx1/64) + int(Cy1/64)*8
                Y = int(Cx2/64) + int(Cy2/64)*8

                print(X,Y)

                permut[X], permut[Y] = permut[Y], permut[X]

                (w,h) = int(X%8), int(X/8)
                x1, y1, x2, y2 = int(h * grid_h), int(w * grid_w), int((h + 1) * (grid_h)), int((w + 1) * (grid_w))

                (w,h) = int(Y%8), int(Y/8)
                Mx1, My1, Mx2, My2 = int(h * grid_h), int(w * grid_w), int((h + 1) * (grid_h)), int((w + 1) * (grid_w))

                tmp = ret[x1:x2, y1:y2].copy()
                ret[x1:x2, y1:y2] = ret[Mx1:Mx2, My1:My2].copy()
                ret[Mx1:Mx2, My1:My2] = tmp.copy()

                print("!!")

                cnt = 0

            if cv2.waitKey(1) & 0xFF == ord('n'):
                ###################################################################
                # Permutation Saving
                print(permut)
                shuffled = ""
                for i in permut:
                    shuffled = shuffled + str(i) + " "
                f.write(shuffled)
                f.write("\n")
                break

        ###################################################################
        # Game Finishing

        if grayOn:
            save_path = "./test1_64_graycrop/"
        else:
            save_path = "./data_answer/"



        ###################################################################
        # Image Saving

        save_name = save_path + "64-" + str(num) + ".png"
        retval = cv2.imwrite(save_name, ret)
        print('save file ' + save_name + '....')

        break

f.close()


