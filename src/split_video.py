# *_*coding:utf-8 *_*
import os
from optparse import OptionParser

import cv2


def split_video(path_video, dir_img, frames):
    if not os.path.isfile(path_video):
        print(" Invalid path")
        exit()
    if not os.path.isdir(dir_img):
        os.makedirs(dir_img)
    cap = cv2.VideoCapture(path_video)
    count = 0
    if cap.isOpened():  # 判断是否正常打开
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
        count += 1
        ret, frame = cap.read()
        if count % frames == 0:
            print(" the {}th picture ...".format(str(count // frames).zfill(4)))
            cv2.imwrite(os.path.join(dir_img, str(count // frames).zfill(4) + '.png'), frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def get_args():
    parser = OptionParser()
    parser.add_option('--video_path', dest='video_path',
                      default="video\\video_001.mp4",
                      type='str',
                      help='path of video')
    parser.add_option('--number_frames', dest='frames', default=10,
                      type='int', help='number of frames')
    (options, args) = parser.parse_args()
    return options


'''
if __name__ == "__main__":
    args = get_args()
    frames = args.frames
    path_video = args.video_path
    video_name = os.path.split(path_video)[-1].split('.')[0]
    dir_img = os.path.join("img", video_name)
    split_video(path_video, dir_img, frames)
'''
