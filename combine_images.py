"""combine images"""
import argparse
import glob
import os
import cv2
import numpy as np

def main(args):
    files = []
    exts = ['jpg', 'jpeg', 'png']
    for ext in exts:
        path = os.path.join(args.in_path, '*.{}'.format(ext))
        files.extend(glob.glob(path))
    file_num = len(files)

    if file_num <= 1:
        print("Please set 'in_path' directory where contains images more than 1.")
        exit(0)

    it = 1
    count = 1

    for file in files:
        input_img = cv2.imread(file)

        size = input_img.shape
        if it > 2:
            if size != prev_size:
                print("Please select the images of the same size")
                exit(0)
        prev_size = size

        if it == file_num:
            if count != 1:
                if (args.config == 0):
                        next_img = cv2.hconcat([prev_img, input_img])
                else:
                    next_img = cv2.hconcat([input_img, prev_img])
                prev_img = next_img
                if it % args.horizontal_num != 0:
                    black = np.zeros(input_img.shape, np.uint8)
                    for _ in range(args.horizontal_num - count):
                        if args.config == 0:
                            next_img = cv2.hconcat([prev_img, black])
                        else:
                            next_img = cv2.hconcat([black, prev_img])
                        prev_img = next_img
                dst = cv2.vconcat([tmp, next_img])
            else:
                prev_img = input_img
                black = np.zeros(input_img.shape, np.uint8)
                for _ in range(args.horizontal_num - count):
                    if args.config == 0:
                        next_img = cv2.hconcat([prev_img, black])
                    else:
                        next_img = cv2.hconcat([black, prev_img])
                    prev_img = next_img
                dst = cv2.vconcat([tmp, next_img])
            break
        elif it == 1:
            prev_img = input_img
            it += 1
            count += 1
        elif count == 1:
            prev_img = input_img
            it += 1
            count += 1
        elif count != args.horizontal_num:
            if args.config == 0:
                next_img = cv2.hconcat([prev_img, input_img])
            else:
                next_img = cv2.hconcat([input_img, prev_img])

            prev_img = next_img
            it += 1
            count += 1
        elif it == count:
            if args.config == 0:
                tmp = cv2.hconcat([prev_img, input_img])
            else:
                tmp = cv2.hconcat([input_img, prev_img])
            it += 1
            count = 1
        elif count == args.horizontal_num:
            if args.config == 0:
                next_img = cv2.hconcat([prev_img, input_img])
            else:
                next_img = cv2.hconcat([input_img, prev_img])
            tmp_v = cv2.vconcat([tmp, next_img])
            tmp = tmp_v
            it += 1
            count = 1

    dst_path = os.path.join(args.out_path, args.save_name + '.png')
    try:
        os.makedirs(args.out_path)
    except OSError as e:
        if e.errno != 17:
            raise
    cv2.imwrite(dst_path, dst)
    print("output file:", dst_path)
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_path', type=str, default='data')
    parser.add_argument('--out_path', type=str, default='results')
    parser.add_argument('--save_name', type=str, default='combine')
    parser.add_argument('--horizontal_num', type=int, default=3)
    parser.add_argument('--config', type=int, default=0)

    args = parser.parse_args()
    main(args)
