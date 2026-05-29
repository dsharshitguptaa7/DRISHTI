import cv2
import time

from detector import detect_objects, summarize_objects
from speech import speak

cap = cv2.VideoCapture(0)

last_spoken_time = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("DRISHTI Webcam", frame)

    current_time = time.time()

    # Every 5 seconds
    if current_time - last_spoken_time > 5:

        temp_image = "temp.jpg"

        cv2.imwrite(temp_image, frame)

        objects = detect_objects(temp_image)

        summary = summarize_objects(objects)

        if summary:

            speech_text = ". ".join(summary)

            print("\n", speech_text)

            speak(speech_text)

        last_spoken_time = current_time

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()