# These are my hobby project codes developed in python using OpenCV.
# Some of the projects are tested on Mac, Some on Raspberry Pi
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#

# imports
import os
# from week1a import imread_lesson as imLesson1
# from week1a import drawing_lesson as dl1
# from week1a import ImageProcessingOperations_lesson as imOp
# from week1a import MorphologicalOp as mp
# from week1a import SmoothAndBlur as sb
# from week1a import Thresholding as th
# from week1a import Gradient as gr
from week1a import Edge as edg

__author__ = 'kishwarkumar'
__date__ = '7/2/16' '6:43 PM'

if __name__ == "__main__":

    # Current Path
    CurrPath = os.path.dirname(__file__)
    '''
    # declare object, update path, call for display
    imreadObj = imLesson1.Imread_lesson(CurrPath + "/week1a/images/image3.jpg")
    imreadObj.DisplayIt()
    imreadObj.DisplayUpperLeft()
    imreadObj.DisplayCorners()
    imreadObj.image_tl_green()
    '''

    '''
    # declare object, update path, call for display
    dlObj = dl1.Drawing_lesson(CurrPath + "/week1a/images/image3.jpg")
    dlObj.drawit()
    '''

    '''
    # declare object, update path, call for different operations
    imOpObj = imOp.ImageProcessingOperations_lesson(CurrPath + "/week1a/images/image23.png")
    #imOpObj.translationOp()
    imOpObj.rotationOp()
    imOpObj.resizingOp()
    imOpObj.flippingOp()
    imOpObj.croppingOp()
    imOpObj.arithmeticOp()
    imOpObj.bitwiseOp()
    imOpObj.maskingOp()
    imOpObj.splitmergeOp()
    '''

    '''
    # declare object, update path, call for different operations
    imOpObj = mp.MorphologicalOp(CurrPath + "/week1a/images/image10.png")
    imOpObj.ErodeOp()
    imOpObj.DiluteOp()
    imOpObj.OpenOp()
    imOpObj.ClosingOp()
    imOpObj.Gradient()
    imOpObj.WhiteHat()
    '''

    '''
    # declare object, update path, call for different operations
    imOpObj = sb.SmoothNBlur(CurrPath + "/week1a/images/image3.jpg")
    imOpObj.BlurAvg()
    imOpObj.Blurgaus()
    imOpObj.Blurmed()
    imOpObj.Blurbil()
    '''

    '''
    # declare object, update path, call for different operations
    imOpObj = th.Thresholding(CurrPath + "/week1a/images/image17.png")
    imOpObj.Simple_Thresholding()
    imOpObj.Otsu_Thresholding()
    imOpObj.Adaptive_Thresholding()
    '''

    '''
    # declare object, update path, call for different operations
    imOpObj = gr.Gradient(CurrPath + "/week1a/images/image19.png")
    imOpObj.Gradient_Sobel()
    '''

    # declare object, update path, call for different operations
    imOpObj = edg.Edge(CurrPath + "/week1a/images/image25.jpg")
    #imOpObj.Edge_Canny()
    imOpObj.Edge_Canny_auto()