# These are my hobby project codes developed in python using OpenCV.
# Some of the projects are tested on Mac, Some on Raspberry Pi
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#

# imports
import os
#from week1a import imread_lesson as imLesson1
from week1a import drawing_lesson as dl1

__author__ = 'kishwarkumar'
__date__ = '7/2/16' '6:43 PM'

if __name__ == "__main__":

    # Current Path
    CurrPath = os.path.dirname(__file__)
    '''
    # declare object, update path, call for display
    imreadObj = imLesson1.Imread_lesson(CurrPath + "/week1a/image3.jpg")
    imreadObj.DisplayIt()
    imreadObj.DisplayUpperLeft()
    imreadObj.DisplayCorners()
    imreadObj.image_tl_green()
    '''

    # declare object, update path, call for display
    dlObj = dl1.Drawing_lesson(CurrPath + "/week1a/image3.jpg")
    dlObj.drawit()