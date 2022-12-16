import cv2 as cv
import matplotlib.pyplot as plt

# https://www.nayuki.io/page/qr-code-generator-library

def main ():

    imgOne = cv.imread('images/frame.png')
    imgTwo = cv.imread('images/frameTwo.png')

    grayScl = cv.cvtColor(imgOne, cv.COLOR_BGR2GRAY)
    cont, _ = cv.findContours(grayScl, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    
    
    # not sure if I need to be finding all of the contours
    # might be easier to assume the QR code is always in the correct orientation, and check pixels in a grid

    
    for i in range(len(cont)):
        
        cv.drawContours(imgOne, cont, i, (0,0,255), 1)
        cv.imshow('test', imgOne)
        print(cont[i])
        cv.waitKey(200)

    cv.waitKey(0)

if __name__ == '__main__':
    main()