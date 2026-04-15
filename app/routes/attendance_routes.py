from flask import Blueprint, session, redirect, request, render_template
from ..models.db import get_connection
from ..services.face_service import load_known_faces
from ..services.timetable_service import get_current_subject
import face_recognition
import cv2
import numpy as np
from datetime import datetime
import time
attendance_bp = Blueprint("attendance", __name__)

@attendance_bp.route("/attendance", methods=["GET", "POST"])
def attendance():
    if session.get("role") not in ["admin", "faculty"]:
        return redirect("/")

    subject = get_current_subject()
    if session.get('role') == 'faculty':
        conn = get_connection()
        c = conn.cursor()
        faculty = c.execute(
            "SELECT f.assigned_subject FROM faculty f JOIN users u ON u.id=f.user_id WHERE u.id=?",
            (session.get('user_id'),),
        ).fetchone()
        conn.close()
        if faculty and faculty[0]:
            subject = faculty[0]

    if request.method == "POST":
        subject = request.form.get("subject")

    if not subject:
        return render_template("attendance.html", subject=None)

    conn = get_connection()
    c = conn.cursor()
    students = c.execute("SELECT id, name, image FROM students").fetchall()
    known_encodings, ids, names = load_known_faces(students)

    cam = cv2.VideoCapture(0)
    time.sleep(2)

    detected_students = set()

    while True:
        ret, frame = cam.read()
        if not ret:
            continue

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, faces)

        for (top, right, bottom, left), encode in zip(faces, encodings):
            matches = face_recognition.compare_faces(known_encodings, encode)
            dist = face_recognition.face_distance(known_encodings, encode)

            if True in matches:
                index = np.argmin(dist)
                student_id = ids[index]
                name = names[index]

                detected_students.add(student_id)
                today = datetime.now().strftime("%Y-%m-%d")
                time_now = datetime.now().strftime("%H:%M:%S")

                c.execute("""
                    SELECT * FROM attendance
                    WHERE student_id=? AND subject=? AND date=?
                """, (student_id, subject, today))

                if not c.fetchone():
                    c.execute("""
                        INSERT INTO attendance(student_id, subject, date, time)
                        VALUES (?, ?, ?, ?)
                    """, (student_id, subject, today, time_now))
                    conn.commit()

                cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
                cv2.putText(frame, name, (left, top-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        cv2.putText(frame, f"Subject: {subject}", (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

        cv2.imshow("Smart Classroom Mode - Press Q to Exit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    conn.close()
    return "Attendance Recorded Successfully!"