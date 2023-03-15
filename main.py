import cv2

cap = cv2.VideoCapture(0)

box_size = 80
box_x = 320 - box_size
box_y = 240 - box_size
box_speed_x = 5
box_speed_y = 5

while True:

    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    box_x += box_speed_x
    box_y += box_speed_y

    if box_x < 0 or box_x + box_size > frame.shape[1]:
        box_speed_x *= -1
    if box_y < 0 or box_y + box_size > frame.shape[0]:
        box_speed_y *= -1

    cv2.rectangle(frame, (box_x, box_y), (box_x + box_size, box_y + box_size), (0, 255, 0), 2)

    cv2.imshow("Bouncing Box", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


