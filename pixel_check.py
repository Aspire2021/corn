import cv2

right_clicks = list()
def mouse_callback(event, x, y, flags, params):

    if event == 2:
        global right_clicks
        right_clicks.append([x, y])

        print (right_clicks)


img = cv2.imread('F:/Aspire/3.2.2021/corn.jpeg', cv2.IMREAD_UNCHANGED)
print(img.shape)

Gray_Image =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
th, threshed = cv2.threshold(Gray_Image, 100, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

scale_width = 640 / Gray_Image.shape[1]
scale_height = 480 / Gray_Image.shape[0]
scale = min(scale_width, scale_height)
window_width = int(Gray_Image.shape[1] * scale)
window_height = int(Gray_Image.shape[0] * scale)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', window_width, window_height)

#set mouse callback function for window
cv2.setMouseCallback('image', mouse_callback)

a=Gray_Image[65,161]
print(a)
b=Gray_Image[164,12]
print(b)
c=Gray_Image[329,122]
print(c)
d=Gray_Image[230,271]
print(d)

cv2.imshow('image', Gray_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()