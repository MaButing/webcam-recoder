import numpy as np
import cv2

WIDTH = 1280
HEIGHT = 720

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
print(cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

# https://github.com/cisco/openh264/releases/tag/v1.8.0
fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('output.avi', fourcc, fps, (WIDTH, HEIGHT))


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #do sth
    frame = cv2.flip(frame, 0)
    
    # write the frame
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
