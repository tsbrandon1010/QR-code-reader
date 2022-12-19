import cv2 as cv
import numpy as np

# https://www.nayuki.io/page/qr-code-generator-library

def processImage(fImagePath: str):
    img = cv.imread(fImagePath)
    grayScale = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
    
    return img, grayScale

def findContours(fGrayScale: cv.Mat):
    contour, _ = cv.findContours(fGrayScale, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    return contour

def drawContours(fImage: cv.Mat, fContour: any):
    for i in range(len(fContour)):
        cv.drawContours(fImage, fContour, i, (0,0,255), 1)
        cv.waitKey(200)
        cv.imshow("output", fImage)


# using masking to determine the orientation of the QR code
# passing in the QR code to be read
def orientateImage(fImage: cv.Mat) -> cv.Mat:
    
    masking, grayScale = processImage('images/orientationMask.png')
    
    _, orientation = processImage('images/orientation.png')

    correctOrientation = False
    while not correctOrientation:
        fImage = cv.rotate(fImage, cv.ROTATE_90_CLOCKWISE)
        mask = cv.bitwise_and(masking, fImage)
        
        # I need to look into a more efficent way of converting types
        # here I am converting from a numpy array to a cv2 Mat
        cv.imwrite('images/testing.png', mask)
        _, mask = processImage('images/testing.png')
        difference = cv.subtract(mask, orientation)
        correctOrientation = not np.any(difference)
    
    return fImage


def main ():

    
    # not sure if I need to be finding all of the contours
    # might be easier to assume the QR code is always in the correct orientation, and check pixels in a grid

    incorrectOrientation = 'images/eastOrientation.png'
    
    processedImage, grayScal = processImage(incorrectOrientation)
    
    cv.imshow('before-orientation', processedImage)

    correctOrientation = orientateImage(processedImage)
    cv.imshow('after-orientation', correctOrientation)

    cv.waitKey(0)

if __name__ == '__main__':
    main()