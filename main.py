import cv2 as cv
import numpy as np

# https://www.nayuki.io/page/qr-code-generator-library

class QRCode:

    # https://i.stack.imgur.com/N4RFU.png
    masking_pattern = 0

    def __init__(self, file_path: str) -> None:
        self.image_path = file_path
        self.image, self.grayscale = self.process_image(self.image_path)        
        self.orientate_image()

    @staticmethod
    def process_image(image_path: str):
        img = cv.imread(image_path)
        grayscale = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
        return img, grayscale
    
    @staticmethod
    def find_contours(grayscale: cv.Mat):
        contour, _ = cv.findContours(grayscale, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        return contour

    @staticmethod
    def draw_contours(image: cv.Mat, contour: any):
        for i in range(len(contour)):
            cv.drawContours(image, contour, i, (0,0,255), 1)
            cv.waitKey(200)
            cv.imshow("output", image)


    # using masking to determine the orientation of the QR code
    # passing in the QR code to be read
    def orientate_image(self):
        
        masking, mask_grayscale = self.process_image('images/orientationMask.png')
        
        _, orientation_reference = self.process_image('images/orientation.png')

        correct_orientation = False
        rotated_image = self.image
        while not correct_orientation:
            rotated_image = cv.rotate(rotated_image, cv.ROTATE_90_CLOCKWISE)
            mask = cv.bitwise_and(masking, rotated_image)
            
            # I need to look into a more efficient way of converting types
            # here I am converting from a numpy array to a cv2 Mat
            # 'testing.png' should probably be deleted when we are done using it
            cv.imwrite('images/testing.png', mask)
            _, mask = self.process_image('images/testing.png')
            
            
            difference = cv.subtract(mask, orientation_reference)
            correct_orientation = not np.any(difference)
        
        self.image = rotated_image

    # we need to read the pixels from the image into a hash map, where the key is the simplified coordinate, and the value is 0 or 1
    def map_image(fImage: cv.Mat):

        
        pass

    # within the array we need to determine the masking pattern, then change the bits within the hash map accordingly


def main ():

    incorrect_orientation = 'images/eastOrientation.png'
    img, _ = QRCode.process_image(incorrect_orientation)
    cv.imshow('before correction', img)

    qr_code = QRCode(incorrect_orientation)
    cv.imshow('after correction', qr_code.image)
    
    cv.waitKey(0)

if __name__ == '__main__':
    main()