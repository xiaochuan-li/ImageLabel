# *_*coding:utf-8 *_*
import os
from optparse import OptionParser

import cv2
import numpy as np

flag = 0
point = []


def check_empty():
    global flag
    if flag == 0:
        return True
    else:
        return False


def generate_log(img_path, log_path):
    global point
    with open(log_path, 'a') as f:
        string_log = img_path + '------'

        for x in point:
            string_log += '(' + str(int(x[0])).center(6, ' ') + " , " + str(int(x[1])).center(6, ' ') + "), "
        f.write(string_log[:-2] + '\n')


def save_mask(img_size, img_path, mask_dir, poly, color=(255, 255, 255)):
    img_name = img_path.split('.')[0]
    mask_img = np.zeros(img_size, dtype='uint8')
    cv2.fillPoly(mask_img, poly, color)
    if not os.path.isdir(mask_dir):
        os.mkdir(mask_dir)
    print(os.path.join(mask_dir, img_path))
    cv2.imwrite(os.path.join(mask_dir, img_name + '.png'), mask_img)
    return mask_img


def check_full(img, img_path, is_log=True, log_path="log.txt", mask_dir='mask', color=(0, 255, 0)):
    global point, flag
    if flag == 4:
        poly = np.array([point])
        added = save_mask(img.shape, img_path, mask_dir, poly)
        img_add = cv2.addWeighted(added, 0.3, img, 0.7, 0)
        cv2.imshow(img_path, img_add)
        cv2.waitKey()
        if is_log:
            generate_log(img_path, log_path)
        point = []
        flag = 0
        return True
    else:
        return False


def draw_circle(event, x, y, flags, params):
    global flag, point
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("ajoute point [{},{}] , the flag = {}".format(x, y, flag + 1))
        point.append((x, y))
        flag += 1

    elif event == cv2.EVENT_RBUTTONDOWN:
        if check_empty():
            print("no point to delete")
        else:
            print("delete the point {}".format(point.pop()))
            flag -= 1


def draw(img, point):
    new_img = np.array(img)
    for p in point:
        new_img = cv2.circle(new_img, p, 3, (0, 0, 255))
    return new_img


def get_args():
    parser = OptionParser()
    parser.add_option('--img_path', dest='path',
                      default="img\\video_001",
                      type='str',
                      help='path of images')
    parser.add_option('--log_name', dest='log_name', default="log.txt",
                      type='str', help='path of log file')
    parser.add_option('--mask_name', dest='mask_name', default="mask",
                      type='str', help='path of mask')
    parser.add_option('--label_class', dest='label_class', default="fond",
                      type='str', help='the name of class')
    parser.add_option('--is_log', dest='is_log', action='store_true', default=False,
                      help='whether generate log file or not')
    (options, args) = parser.parse_args()
    return options


if __name__ == "__main__":
    args = get_args()
    root = 'data'
    if not os.path.isdir(root):
        os.mkdir(root)
    label_class = os.path.join("data", args.label_class)
    if not os.path.isdir(label_class):
        os.mkdir(label_class)
    path = args.path
    mask_path = os.path.join(label_class, args.mask_name)
    if not os.path.isdir(mask_path):
        os.mkdir(mask_path)
    log_path = os.path.join(label_class, args.log_name)
    is_log = args.is_log
    for root, dir, files in os.walk(path):
        for img_path in files:
            img_ori = cv2.imread(os.path.join(path, img_path))
            cv2.namedWindow(img_path)
            cv2.setMouseCallback(img_path, draw_circle)
            while True:
                img_drawable = draw(img_ori, point)
                cv2.imshow(img_path, img_drawable)
                if cv2.waitKey(20) & 0xFF == 27 or check_full(img_drawable, img_path, log_path=log_path,
                                                              mask_dir=mask_path, is_log=is_log):
                    break
            cv2.destroyAllWindows()
