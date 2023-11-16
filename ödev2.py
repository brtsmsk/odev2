import cv2
import numpy as np

droidcam_ip = '192.168.137.42'
droidcam_port = '4747'

url = f'http://{droidcam_ip}:{droidcam_port}/video'

# Video akışını açın
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Kamera', frame)
    cv2.imshow('Sonuç', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
