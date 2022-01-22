# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import cv2
import numpy as np

# print(cv2.__version__)
#
# print(cv2.cuda.getCudaEnabledDeviceCount())
#
# img = cv2.imread("CHER.jpg")
#
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#
# lower_mask = np.array([0,0,30])
# higher_mask = np.array([180,30,255])
#
# mask = cv2.inRange(img,lower_mask,higher_mask)
#
#
# cv2.imshow("Eroded", mask)
# cv2.waitKey(0)


import cv2
import numpy as np


def barcode_cnt(src, cx, cy, distance):
    barcode_x1 = cx - distance
    barcode_x2 = cx - distance
    barcode_x3 = cx + distance
    barcode_x4 = cx + distance

    barcode_y1 = cy + distance
    barcode_y2 = cy - distance
    barcode_y3 = cy - distance
    barcode_y4 = cy + distance
    rectangle_barcode = cv2.rectangle(src, (barcode_x1, barcode_y1), (barcode_x3, barcode_y3), (0, 255, 0), 3)

    barcode_roi = src[barcode_y3:barcode_y1, barcode_x1:barcode_x3]

    return barcode_roi
    # count = cv2.countNonZero(barcode_roi)
    # cv2.putText(img, "TOTAL: {}".format(count), (10, 550), 0, 1.2, (60, 60, 60), 2)
    #
    #
    # cv2.imshow("new", barcode_roi)


#
# def empty(a):
#     pass
#
#
# path = "CHER.jpg"
# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",640,240)
# cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
# cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
# cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
# cv2.createTrackbar("Sat Max","TrackBars",21,255,empty)
# cv2.createTrackbar("Val Min","TrackBars",185,255,empty)
# cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
#
# while True:
#     img = cv2.imread(path)
#     imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
#     h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
#     s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
#     s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
#     v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
#     v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
#     lower = np.array([h_min,s_min,v_min])
#     upper = np.array([h_max,s_max,v_max])
#     mask = cv2.inRange(imgHSV,lower,upper)
#
#     cv2.imshow("Original",img)
#     cv2.imshow("HSV",imgHSV)
#     cv2.imshow("mask", mask)
#     cv2.waitKey(1)
#


def label_identify(src):
    img = cv2.imread(src)

    lb_window = barcode_cnt(img, 482, 320, 120)
    imgHSV = cv2.cvtColor(lb_window, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 0, 185])
    upper = np.array([179, 21, 255])
    mask = cv2.inRange(imgHSV, lower, upper)

    count = cv2.countNonZero(mask)
    if count > 20000:

        cv2.putText(lb_window, "PASS".format(count), (40, 50), 0, 1.2, (255, 60, 60), 2)
    else:
        cv2.putText(lb_window, "No LABeL".format(count), (40, 50), 0, 1.2, (0, 0, 255), 2)

    cv2.imshow("new", lb_window)


# imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgblur = cv2.GaussianBlur(imggray,(81,81),1)
# imgThreshold = cv2.adaptiveThreshold(imgblur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)


label_identify("1.jpg")

if cv2.waitKey(0) & 0xFF == 27:
    cv2.waitKey(0)
