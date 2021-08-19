import cv2 as cv
import numpy as np
import time
from scipy import signal

nurcle = np.array([[1, 0], [0, -1]])
nurcle1 = np.array([[0, 1], [-1, 0]])
nurcle2 = np.array([[-1, 0], [0, 1]])
nurcle3 = np.array([[0, -1], [1, 0]])
nurcle3 = np.array([[0, -1], [1, 0]])
pp = cv.VideoCapture(700)
while True:
    a=time.time()
    re,img=pp.read()
    planets = img
    circle=[]
    gay_img = cv.cvtColor(planets, cv.COLOR_BGRA2GRAY)
    img = cv.medianBlur(gay_img, 7)  # 进行中值模糊，去噪点`
    cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    img1=cv.filter2D(img, -1,nurcle)
    img2=cv.filter2D(img, -1,nurcle1)
    img3=cv.filter2D(img, -1,nurcle2)
    img4=cv.filter2D(img, -1,nurcle3)
    img1=img1+img2+img3+img4
    lines = cv.HoughLinesP(img1, 2, np.pi / 180, 100,100,50)
    for hu in lines:
        for x1, y1, x2, y2 in hu:
            cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    b = time.time()
    cv.imshow("gay_imd",img1)
    cv.imshow("gay_imd1", img)
    """print(1/(b-a))"""
    if cv.waitKey(100) & 0xFF == ord('q'):
        break
