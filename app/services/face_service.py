import face_recognition
import cv2
import numpy as np


def capture_face_image(filename):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Capture Student Face")

    instructions = "Press SPACE to capture face, ESC to cancel"
    while True:
        ret, frame = cam.read()
        if not ret:
            continue

        cv2.putText(frame, instructions, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow("Capture Student Face", frame)

        key = cv2.waitKey(1)
        if key % 256 == 27:  # ESC
            break
        elif key % 256 == 32:  # SPACE
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            locations = face_recognition.face_locations(rgb)
            if len(locations) == 0:
                cv2.putText(frame, "No face detected. Try again.", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                cv2.imshow("Capture Student Face", frame)
                cv2.waitKey(1000)
                continue
            elif len(locations) > 1:
                cv2.putText(frame, "Multiple faces detected. Try again.", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                cv2.imshow("Capture Student Face", frame)
                cv2.waitKey(1000)
                continue
            cv2.imwrite(filename, frame)
            break

    cam.release()
    cv2.destroyAllWindows()


def load_known_faces(students):
    encodings = []
    ids = []
    names = []

    for s in students:
        try:
            img = face_recognition.load_image_file(s[2])
            enc_list = face_recognition.face_encodings(img)
            if len(enc_list) == 0:
                continue
            enc = enc_list[0]
            encodings.append(enc)
            ids.append(s[0])
            names.append(s[1])
        except Exception:
            continue

    return encodings, ids, names