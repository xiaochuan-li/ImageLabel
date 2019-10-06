# *_*coding:utf-8 *_*
import os

import cv2


def split_video(path_video, dir_img):
    if not os.path.isfile(path_video):
        print(" Invalid path")
        exit()
    if not os.path.isdir(dir_img):
        os.mkdir(dir_img)
    cap = cv2.VideoCapture(path_video)
    count = 0
    if cap.isOpened():  # 判断是否正常打开
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
        count += 1
        ret, frame = cap.read()
        if count % 10 == 0:
            print(" the {}th picture ...".format(str(count // 10).zfill(4)))
            cv2.imwrite(os.path.join(dir_img, str(count // 10).zfill(4) + '.png'), frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    path_video = "video\\video_001.mp4"
    video_name = os.path.split(path_video)[-1].split('.')[0]
    dir_img = os.path.join("img", video_name)

    split_video(path_video, dir_img)
