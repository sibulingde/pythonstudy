import os
import cv2 as cv
import numpy as np
import serial
import multiprocessing as mul

pipe=mul.Pipe()
pipe1=mul.Pipe()
port=mul.Pipe()


def port_do(pipe):
    port=serial.Serial('/dev/ttyS3',115200)
    while True:
        a=pipe.recv().encode()
        port.write()


def camera_run(pipe):
    pp = cv.VideoCapture(700)
    while True:
        p,imh=pp.read()
        pipe.send(imh)
        #print("2222")
        #pipe.send(cv.imread("D:/test.jpg"))




def gay_img_f(pipe,pipe1):
    while True:
        planets = pipe.recv()
        try:
            gay_img = cv.cvtColor(planets, cv.COLOR_BGRA2GRAY)
            img = gay_img
            img = cv.medianBlur(gay_img, 7)  # 进行中值模糊，去噪点
            pipe1.send(img)
        except:
            print("e")



def img_doCircle(pipe1):
    circle = []
    port=None
    while True:
        time = 5
        img=pipe1.recv()
        j = 0
        circle=[]
        try:
            circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 2, 768)
            circles = np.uint16(np.around(circles))
            circle.extend(list(circles[0]))
            while time:
                circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 2, 768, minRadius=circle[j][2]+5)
                circles = np.uint16(np.around(circles))
                circle.extend(list(circles[0]))
                j += 1
                time-=1
        except Exception as e:
            print(e)
        time=5
        try:
            circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 2, 768)
            circles = np.uint16(np.around(circles))
            circle.extend(list(circles[0]))
            while time:
                circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 2, 768, maxRadius=circle[j][2]-5)
                circles = np.uint16(np.around(circles))
                circle.extend(list(circles[0]))
                j += 1
                time-=1
        except Exception as e:
            print(e)
        for i in circle:  # 遍历矩阵每一行的数据
            cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
        cv.imshow("gay_img", img)
        if cv.waitKey(100) & 0xFF == ord('q'):
            break

if __name__=="__main__":
    p1=mul.Process(target=camera_run,args=(pipe[0],))
    p2=mul.Process(target=img_doCircle,args=(pipe1[1],))
    p3 = mul.Process(target=gay_img_f, args=(pipe[1],pipe1[0]))
    p1.start()
    p2.start()
    p3.start()
