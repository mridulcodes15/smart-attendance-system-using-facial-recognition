from flask import Blueprint, render_template, request, redirect, session
from werkzeug.security import check_password_hash, generate_password_hash
from ..models.db import get_connection
from ..services.face_service import capture_face_image
import os

auth_bp = Blueprint("auth", __name__, template_folder="../templates")

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form.get("role")
        if not role:
            role = None
        conn = get_connection()
        c = conn.cursor()

        user = c.execute(
            "SELECT id, password, role FROM users WHERE username=?",
            (username,)
        ).fetchone()

        conn.close()

        if not user:
            error = "Invalid username or password"
        elif not check_password_hash(user[1], password):
            error = "Invalid username or password"
        elif role and role not in ["student", "faculty", "admin"]:
            error = "Please select a valid role"
        elif role and role != user[2] and not (role == "faculty" and user[2] == "admin"):
            error = "Please login with the correct role"
        else:
            session["user_id"] = user[0]
            session["role"] = user[2]
            if user[2] == "student":
                return redirect("/student_dashboard")
            return redirect("/dashboard")

    return render_template("login.html", error=error)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    error = None
    message = None
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()
        role = request.form.get("role")
        name = request.form.get("name", "").strip()
        roll = request.form.get("roll", "").strip()
        department = request.form.get("department", "CSE AIML").strip()

        if not username or not password or role not in ["student", "faculty", "admin"]:
            error = "Please fill all required fields and select a role."
        else:
            conn = get_connection()
            c = conn.cursor()
            existing = c.execute("SELECT id FROM users WHERE username=?", (username,)).fetchone()
            if existing:
                error = "Username already exists. Choose another."
            else:
                hashed = generate_password_hash(password)
                c.execute("INSERT INTO users(username, password, role) VALUES (?, ?, ?)", (username, hashed, role))
                user_id = c.lastrowid
                image_path = ""
                if role == "student":
                    os.makedirs("static/faces", exist_ok=True)
                    image_path = f"static/faces/{username.replace(' ', '_')}_{user_id}.jpg"
                    c.execute("INSERT INTO students(name, roll, image, user_id) VALUES (?, ?, ?, ?)", (name or username, roll or "-", image_path, user_id))
                    conn.commit()
                    conn.close()
                    try:
                        capture_face_image(image_path)
                        message = "Registration complete. Face captured. Please login."
                    except Exception:
                        message = "Registration complete, but face capture failed. Please login and try again."
                elif role == "faculty":
                    c.execute("INSERT INTO faculty(user_id, name, department) VALUES (?, ?, ?)", (user_id, name or username, department or "CSE AIML"))
                    conn.commit()
                    conn.close()
                    message = "Faculty registration complete. Please login."
                else:
                    conn.commit()
                    conn.close()
                    message = "Admin registration complete. Please login."

    return render_template("register.html", error=error, message=message)

@auth_bp.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    error = None
    message = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        role = request.form.get("role")
        new_password = request.form.get("new_password", "").strip()
        confirm_password = request.form.get("confirm_password", "").strip()

        if not username or role not in ["student", "faculty", "admin"]:
            error = "Please enter username and select role."
        else:
            conn = get_connection()
            c = conn.cursor()
            user = c.execute("SELECT id FROM users WHERE username=? AND role=?", (username, role)).fetchone()
            if not user:
                error = "No user found with that username and role."
            elif not new_password:
                error = "Please enter a new password."
            elif new_password != confirm_password:
                error = "Passwords do not match."
            else:
                hashed = generate_password_hash(new_password)
                c.execute("UPDATE users SET password=? WHERE id=?", (hashed, user[0]))
                conn.commit()
                conn.close()
                message = "Password reset successful. Please login with your new password."
                return render_template("forgot_password.html", message=message)
            conn.close()

    return render_template("forgot_password.html", error=error, message=message)


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")