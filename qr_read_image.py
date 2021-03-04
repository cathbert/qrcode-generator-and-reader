# import required libraries

import cv2
from pyzbar.pyzbar import decode

# Read image using imread method from opencv
img = cv2.imread('code_image.png')

# Now decode image with pyzbar
decodedObjects = decode(img)

# Print objects available to use
print(decodedObjects)

"""
[Decoded(data=b'https://cartis-coding-hive.business.site', type='QRCODE', rect=Rect(left=76, top=76, 
 width=552, height=552), polygon=[Point(x=76, y=76), Point(x=76, y=628), Point(x=628, y=628), 
 Point(x=628, y=76)])]
"""
# Get data from image

for i in decodedObjects:
    print('Data: ', i.data)

Data:  b'# Get data from image'

for i in decodedObjects:
    print('Data: ', i.data)

# Result
"Data:  b'https://cartis-coding-hive.business.site'"

cv2.imshow('Image', img)
cv2.waitKey(0)


