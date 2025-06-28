from PIL import ImageGrab
from os import getenv

def shoot() -> str:
    ss_loc = getenv("SCREENSHOT_LOC")
    
    try:
        ss_area = (100, 200, 1700, 700)
        ss_img = ImageGrab.grab(ss_area)
        ss_img.save(ss_loc)
        
        return ss_loc
    except:
        return None
