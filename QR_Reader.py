import cv2
from pyzbar.pyzbar import decode

###🧪 It supports:
##QR codes

#EAN-13, UPC-A, Code 128, and many more barcode types

# Load image
img = cv2.imread('bar.png')

# Decode barcodes
decoded_objects = decode(img)

# Loop through detected codes
for obj in decoded_objects:
    print("Type:", obj.type)
    print("Data:", obj.data.decode('utf-8'))
    # Draw rectangle
    points = obj.polygon
    pts = [(p.x, p.y) for p in points]
    pts = pts + [pts[0]]
    for i in range(len(pts)-1):
        cv2.line(img, pts[i], pts[i+1], (255,0,0), 2)

# Show result
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
