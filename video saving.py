import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
fileName = "C:\Users\mahmu\PycharmProjects\OpenCVBASLANGIC\webcam.avi"
codec = cv2.VideoWriter_fourcc("W","M","V","2")
frameRate = 30
resolution = (640,480)
videoFileOutput = cv2.VideoWriter(fileName,codec)
while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.imshow("Webcam Live",frame)
    videoFileOutput.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()