from PIL import ImageGrab

def shoot() -> str:
    ss_loc = '/home/gkesh/Downloads/ss.jpg'
    
    try:
        ss_area = (100, 200, 1700, 700)
        ss_img = ImageGrab.grab(ss_area)
        ss_img.save(ss_loc)
        
        return ss_loc
    except:
        return None
