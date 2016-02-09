# These are my hobby project codes developed in python using OpenCV.
# Some of the projects are tested on Mac, Some on Raspberry Pi
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#

__author__ = 'kishwarkumar'
__date__ = '7/2/16' '11:11 PM'

# imports
import cv2
import numpy as np
import imutils

class ImageProcessingOperations_lesson:

    # define constructor
    def __init__(self, path):
        self.Image = path
        return

    # Translation
    def translationOp(self):
        # read image
        im = cv2.imread(self.Image)

        # NOTE: Translating (shifting) an image is given by a NumPy matrix in
        # the form:
        # [[1, 0, shiftX], [0, 1, shiftY]]
        # You simply need to specify how many pixels you want to shift the image
        # in the X and Y direction -- let's translate the image 25 pixels to the
        # right and 50 pixels down
        M = np.float32([[1, 0, 25], [0, 1, 50]])
        shifted = cv2.warpAffine(im, M, (im.shape[1], im.shape[0]))

        # show shifted image and wait for key press
        cv2.imshow("Image", shifted)
        cv2.waitKey(0)

        # now, let's shift the image 50 pixels to the left and 90 pixels up, we
        # accomplish this using negative values
        M = np.float32([[1, 0, -50], [0, 1, -90]])
        shifted = cv2.warpAffine(im, M, (im.shape[1], im.shape[0]))
        cv2.imshow("Shifted Up and Left", shifted)
        cv2.waitKey(0)

        # shift down
        shifted = imutils.translate(im, 0, 100)
        cv2.imshow("shifted down", shifted)
        cv2.waitKey(0)

        return

    # Rotation
    def rotationOp(self):
        # read image
        im = cv2.imread(self.Image)

        # grab the dimension of the image
        (h, w) = im.shape[:2]
        (cX, cY) = (w/2, h/2)

        # rotate image by 45 degrees
        M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
        rotated = cv2.warpAffine(im, M, (w,h))
        cv2.imshow("Rotated by 45 degrees", rotated)
        cv2.waitKey(0)

        # rotate our image by -90 degrees
        M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
        rotated = cv2.warpAffine(im, M, (w, h))
        cv2.imshow("Rotated by -90 Degrees", rotated)
        cv2.waitKey(0)

        # using imutils
        rotated = imutils.rotate(im, 180)
        cv2.imshow("Rotated by 180 degrees using imutils", rotated)
        cv2.waitKey(0)

        rotated = imutils.rotate(im, -110)
        (b, g, r) = rotated[136, 312]
        print("red=%d, green=%d, blue=%d" % (r,g,b))


        M = cv2.getRotationMatrix2D((50, 50), -88, 1.0)
        rotated = cv2.warpAffine(im, M, (w, h))
        cv2.imshow("Rotated by -88 Degrees with offset (50,50)", rotated)
        (b, g, r) = rotated[10, 10]
        print("red=%d, green=%d, blue=%d" % (r,g,b))
        cv2.waitKey(0)

        return

    # Resizing
    def resizingOp(self):
        # read image
        im = cv2.imread(self.Image)

        # show original image
        cv2.imshow("Original", im)

        # we need to keep in mind aspect ratio so the image does not look skewed
        # or distorted -- therefore, we calculate the ratio of the new image to
        # the old image. Let's make our new image have a width of 150 pixels
        # shape[0] = width
        r = 150.0 / im.shape[1]
        dim = (150, int(im.shape[0] * r))
        print dim, im.shape[0], im.shape[1], im.shape[:2]

        # perform the actual resizing of the image
        resized = cv2.resize(im, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow("Resized (Width)", resized)

        # of course, calculating the ratio each and every time we want to resize
        # an image is a real pain -- let's create a  function where we can specify
        # our target width or height, and have it take care of the rest for us.
        resized = imutils.resize(im, width=100, inter=cv2.INTER_NEAREST)
        cv2.imshow("Resized via Function", resized)
        (b, g, r) = resized[74, 20]
        print("red=%d, green=%d, blue=%d" % (r,g,b))
        print resized.shape[:2]


        resized = imutils.resize(im, width=im.shape[1]*2, inter=cv2.INTER_CUBIC)
        cv2.imshow("Resized via Function", resized)
        (b, g, r) = resized[367, 170]
        print("red=%d, green=%d, blue=%d" % (r,g,b))
        print resized.shape[:2]
        cv2.waitKey(0)

        return

    # Flipping
    def flippingOp(self):
        # read image
        im = cv2.imread(self.Image)

        # flip the image horizontally
        flipped = cv2.flip(im, 1)
        cv2.imshow("Flipped Horizontally", flipped)
        (b, g, r) = flipped[235, 259]
        print("red=%d, green=%d, blue=%d" % (r,g,b))
        cv2.waitKey(0)

        # flip the image vertically
        flipped = cv2.flip(im, 0)
        cv2.imshow("Flipped Vertically", flipped)
        cv2.waitKey(0)

        # flip on both axis
        flipped = cv2.flip(im, -1)
        cv2.imshow("Flipped on both axis", flipped)
        cv2.waitKey(0)

        flipped = cv2.flip(im, 1)
        cv2.imshow("1", flipped)
        cv2.waitKey(0)
        rotated = imutils.rotate(flipped, 45)
        cv2.imshow("2", rotated)
        cv2.waitKey(0)
        flippedAgain = cv2.flip(rotated, 0)
        cv2.imshow("3", flippedAgain)
        cv2.waitKey(0)
        (b, g, r) = flippedAgain[189, 441]
        print("red=%d, green=%d, blue=%d" % (r,g,b))

        return

    # Cropping
    def croppingOp(self):
        # read image
        im = cv2.imread(self.Image)
        cv2.imshow("Original", im)
        #cv2.waitKey(0)

        # face
        face = im[85:250, 85:220]
        cv2.imshow("Face", face)
        #cv2.waitKey(0)

        # ...and now let's crop the entire body
        body = im[90:450, 0:290]
        cv2.imshow("Body", body)
        #cv2.waitKey(0)

        # people
        people = im[173:235, 13:81]
        cv2.imshow("People", people)

        # boat
        people = im[124:212, 225:380]
        cv2.imshow("Boat", people)
        cv2.waitKey(0)

        return

    # Image Arithmetic
    def arithmeticOp(self):
        # read image
        im = cv2.imread(self.Image)

        # images are NumPy arrays, stored as unsigned 8 bit integers -- this
        # implies that the values of our pixels will be in the range [0, 255]; when
        # using functions like cv2.add and cv2.subtract, values will be clipped
        # to this range, even if the added or subtracted values fall outside the
        # range of [0, 255]. Check out an example:
        print "max of 255: " + str(cv2.add(np.uint8([200]), np.uint8([100])))
        print "min of 0: " + str(cv2.subtract(np.uint8([1]), np.uint8([251])))

        # NOTE: if you use NumPy arithmetic operations on these arrays, the value
        # will be modulos (wrap around) instead of being  clipped to the [0, 255]
        # range. This is important to keep in mind when working with images.
        print "wrap around (unsigned): " + str(np.uint8([200]) + np.uint8([68]))
        print "wrap around (signed): " + str(np.int8([200]) + np.int8([68]))
        print "wrap around (unsigned): " + str(np.uint8([1]) - np.uint8([251]))

        # let's increase the intensity of all pixels in our image by 100 -- we
        # accomplish this by constructing a NumPy array that is the same size of
        # our matrix (filled with ones) and the multiplying it by 100 to create an
        # array filled with 100's, then we simply add the images together; notice
        # how the image is "brighter"
        M = np.ones(im.shape, dtype = "uint8") * 75
        added = cv2.add(im, M)
        cv2.imshow("Added", added)
        (b, g, r) = added[152, 61]
        print("red=%d, green=%d, blue=%d" % (r,g,b))
        cv2.waitKey(0)

        # similarly, we can subtract 50 from all pixels in our image and make it
        # darker
        M = np.ones(im.shape, dtype = "uint8") * 50
        subtracted = cv2.subtract(im, M)
        cv2.imshow("Subtracted", subtracted)
        cv2.waitKey(0)

        return

    # Bitwise Operations
    def bitwiseOp(self):
        # read image
        im = cv2.imread(self.Image)

        # first, let's draw a rectangle
        rectangle = np.zeros((300, 300), dtype = "uint8")
        cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
        cv2.imshow("Rectangle", rectangle)

        # secondly, let's draw a circle
        circle = np.zeros((300, 300), dtype = "uint8")
        cv2.circle(circle, (150, 150), 150, 255, -1)
        cv2.imshow("Circle", circle)

        # A bitwise 'AND' is only True when both rectangle and circle have
        # a value that is 'ON.' Simply put, the bitwise AND function
        # examines every pixel in rectangle and circle. If both pixels
        # have a value greater than zero, that pixel is turned 'ON' (i.e
        # set to 255 in the output image). If both pixels are not greater
        # than zero, then the output pixel is left 'OFF' with a value of 0.
        bitwiseAnd = cv2.bitwise_and(rectangle, circle)
        cv2.imshow("AND", bitwiseAnd)
        cv2.waitKey(0)

        # A bitwise 'OR' examines every pixel in rectangle and circle. If
        # EITHER pixel in rectangle or circle is greater than zero, then
        # the output pixel has a value of 255, otherwise it is 0.
        bitwiseOr = cv2.bitwise_or(rectangle, circle)
        cv2.imshow("OR", bitwiseOr)
        cv2.waitKey(0)

        # The bitwise 'XOR' is identical to the 'OR' function, with one
        # exception: both rectangle and circle are not allowed to BOTH
        # have values greater than 0.
        bitwiseXor = cv2.bitwise_xor(rectangle, circle)
        cv2.imshow("XOR", bitwiseXor)
        cv2.waitKey(0)

        # Finally, the bitwise 'NOT' inverts the values of the pixels. Pixels
        # with a value of 255 become 0, and pixels with a value of 0 become
        # 255.
        bitwiseNot = cv2.bitwise_not(circle)
        cv2.imshow("NOT", bitwiseNot)

        cv2.waitKey(0)
        return

    # Masking Operations
    def maskingOp(self):
        # read image
        im = cv2.imread(self.Image)

        # Masking allows us to focus only on parts of an image that interest us.
        # A mask is the same size as our image, but has only two pixel values,
        # 0 and 255. Pixels with a value of 0 are ignored in the orignal image,
        # and mask pixels with a value of 255 are allowed to be kept. For example,
        # let's construct a rectangular mask that displays only the person in
        # the image
        mask = np.zeros(im.shape[:2], dtype="uint8")
        cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
        cv2.imshow("Mask", mask)

        # Apply our mask -- notice how only the person in the image is cropped out
        masked = cv2.bitwise_and(im, im, mask=mask)
        cv2.imshow("Mask Applied to Image", masked)
        cv2.waitKey(0)

        # Now, let's make a circular mask with a radius of 100 pixels and apply the
        # mask again
        mask = np.zeros(im.shape[:2], dtype="uint8")
        cv2.circle(mask, (145, 200), 100, 255, -1)
        masked = cv2.bitwise_and(im, im, mask=mask)
        cv2.imshow("Mask", mask)
        cv2.imshow("Mask Applied to Image", masked)
        cv2.waitKey(0)

        return

    # Split and Merge Operations
    def splitmergeOp(self):
        # read image
        im = cv2.imread(self.Image)

        (B, G, R) = cv2.split(im)
        print(G[5, 80])

        # show each channel individually
        cv2.imshow("Red", R)
        cv2.imshow("Green", G)
        cv2.imshow("Blue", B)
        cv2.waitKey(0)

        # merge the image back together again
        merged = cv2.merge([B, G, R])
        cv2.imshow("Merged", merged)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # visualize each channel in color
        zeros = np.zeros(im.shape[:2], dtype = "uint8")
        cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
        cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
        cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
        cv2.waitKey(0)

        return