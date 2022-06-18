import cv2

cap = cv2.VideoCapture(0) # cap capture dan türetilmiştir.Geleneksel olarak bu kullanılıyormuş

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.imshow("Webcam",frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()

cv2.destroyAllWindpws()