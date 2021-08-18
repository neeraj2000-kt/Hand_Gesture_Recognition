import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)
    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    index = False
    middle = False
    ring = False
    pinky = False
    thumb = False
    if results.multi_hand_landmarks:
      for hand in results.multi_hand_landmarks:
        # mp_drawing.draw_landmarks(
        #     image, hand, mp_hands.HAND_CONNECTIONS)
        if hand.landmark[8].x < hand.landmark[6].x  and hand.landmark[7].x < hand.landmark[6].x:
          if hand.landmark[8].y < hand.landmark[6].y  and hand.landmark[7].y < hand.landmark[6].y:
              index = True
        if hand.landmark[12].x < hand.landmark[10].x  and hand.landmark[11].x < hand.landmark[10].x:
          if hand.landmark[12].y < hand.landmark[10].y  and hand.landmark[11].y < hand.landmark[10].y:
              middle = True
        if hand.landmark[16].x < hand.landmark[14].x  and hand.landmark[15].x < hand.landmark[14].x:
          if hand.landmark[16].y < hand.landmark[14].y  and hand.landmark[15].y < hand.landmark[14].y:
              ring = True
        if hand.landmark[20].x < hand.landmark[18].x  and hand.landmark[19].x < hand.landmark[18].x:
          if hand.landmark[20].y <= hand.landmark[18].y  and hand.landmark[19].y <= hand.landmark[18].y:
              pinky = True
        if hand.landmark[4].x < hand.landmark[2].x  and hand.landmark[3].x < hand.landmark[2].x:
          if hand.landmark[4].y <= hand.landmark[2].y  and hand.landmark[3].y <= hand.landmark[2].y:
              thumb = True
        if index==True  and middle==False and ring==False and pinky==False and thumb==False:
            cv2.putText(image, 'ONE', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0))
        if index==True  and middle==True and ring==False and pinky==False and thumb==False:
            cv2.putText(image, 'TWO', (10,100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0))
        if index==True  and middle==True and ring==True and pinky==False and thumb==False:
            cv2.putText(image, 'THREE', (10,100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0))
        if index==True  and middle==True and ring==True and pinky==True and thumb==False:
            cv2.putText(image, 'FOUR', (10,100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0))
        if index==True  and middle==True and ring==True and pinky==True and thumb==True:
            cv2.putText(image, 'FIVE', (10,100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0))
        if index==False  and middle==True and ring==True and pinky==True and thumb==False:
            cv2.putText(image, 'SUPER', (10,100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0))
    # print(index)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
cv2.destroyAllWindows()
