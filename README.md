# 🎓 Smart Attendance System Using Facial Recognition

A real-time, AI-powered attendance management system built using **Python, OpenCV, Flask, and facial recognition** to automate student attendance and reduce the limitations of traditional manual attendance systems.

The system detects and recognizes registered students through a live camera feed, automatically records their attendance, maps attendance to the appropriate subject, and provides structured attendance records and reports through a web-based interface.

---

## 🚀 Overview

Traditional attendance systems are time-consuming and can be prone to manual errors and proxy attendance.

The **Smart Attendance System Using Facial Recognition** was developed to automate this process using Computer Vision.

The system captures a live video feed, detects faces, compares them with registered student data, and automatically records attendance when a student is successfully recognized.

The project combines **Computer Vision, Machine Learning, backend development, database management, and automation** into a complete attendance management system.

---

## ✨ Key Features

### 👤 Real-Time Face Detection & Recognition
- Detects faces through a live camera feed
- Recognizes registered students in real time
- Automatically marks attendance after successful recognition
- Prevents duplicate attendance entries during the same session

### 📝 Automated Attendance Management
- Automatically stores attendance records
- Records student name, date, time, and subject
- Reduces the need for manual attendance entry
- Maintains structured attendance data

### 📚 Subject-Based Attendance
- Supports subject selection and subject-wise attendance
- Maps attendance records to the selected subject
- Makes it easier for faculty to manage attendance across different classes

### 📊 Attendance Reports
- Generates structured attendance records
- Supports Excel-based attendance reporting
- Provides downloadable attendance data
- Helps faculty review attendance history

### ⚠️ Attendance Monitoring
- Tracks student attendance percentages
- Identifies students whose attendance falls below the required threshold
- Supports automated attendance alerts/reporting

### 🌐 Web-Based Interface
- Flask-based web application
- Interfaces for managing attendance and viewing records
- Designed to make the system easier for faculty and students to use

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **OpenCV** | Image processing and real-time video handling |
| **Face Recognition** | Facial feature encoding and recognition |
| **NumPy** | Numerical and image data processing |
| **Flask** | Backend and web application |
| **SQLite** | Structured data storage |
| **HTML/CSS** | Web interface |
| **Excel** | Attendance reports and exports |

---

## 🧠 How It Works

The system follows the following pipeline:

```text
Live Camera Feed
        ↓
Face Detection
        ↓
Face Encoding
        ↓
Compare With Registered Faces
        ↓
Student Recognition
        ↓
Duplicate Check
        ↓
Subject Mapping
        ↓
Attendance Recorded
        ↓
Database / Excel Report
```

### 1. Student Registration

Student details and facial data are registered in the system.

### 2. Face Detection

OpenCV processes frames from the live camera feed and identifies faces.

### 3. Face Recognition

Facial features are extracted and compared with stored face encodings of registered students.

### 4. Attendance Verification

When a registered student is recognized, the system checks whether attendance has already been recorded for that session.

### 5. Attendance Recording

Valid attendance is automatically recorded along with relevant information such as:

- Student name
- Date
- Time
- Subject

### 6. Reporting

Attendance records can then be viewed and exported for further analysis and reporting.

---

## 📂 Project Structure

A typical project structure is:

```text
smart-attendance-system/
│
├── app.py
├── images/
│   └── registered_student_images
│
├── templates/
│   └── HTML templates
│
├── static/
│   └── CSS / frontend assets
│
├── attendance.xlsx
│
└── README.md
```

> The exact structure may vary depending on the current version of the project.

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/mridulcodes15/smart-attendance-system-using-facial-recognition.git
```

### 2. Navigate to the project directory

```bash
cd smart-attendance-system-using-facial-recognition
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 5. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Open the local Flask URL displayed in the terminal in your browser.

---

## 🎯 Project Objectives

The project was developed with the following objectives:

- Automate classroom attendance using Computer Vision
- Reduce manual attendance effort
- Minimize duplicate or incorrect attendance records
- Provide structured digital attendance data
- Explore practical applications of facial recognition
- Build an end-to-end AI-powered application

---

## 🔬 Research

The work associated with this system was also developed into a research paper:

**Smart Attendance System Using Facial Recognition**

Published in the **International Research Journal of Innovations in Engineering and Technology (IRJIET)**.

The research explores the use of facial recognition for automated attendance management and evaluates the system in a classroom-oriented environment.

---

## 👥 Developers & Contributors

This project was collaboratively developed by:

### Mridul Paradkar
**Developer & Contributor**

### Sunaina Sahu
**Developer & Contributor**

### Harshal Salekar
**Developer & Contributor**

### Diya Singh
**Developer & Contributor**

All four team members contributed to the development and implementation of the project.

---

## 🔮 Future Improvements

Potential improvements include:

- Improved recognition under different lighting conditions
- More robust anti-spoofing mechanisms
- Larger-scale face datasets
- Improved recognition performance for crowded environments
- Cloud-based attendance synchronization
- Mobile integration
- Advanced attendance analytics
- Deployment across multiple classrooms

---

## 📌 Use Cases

The system can potentially be adapted for:

- Colleges and universities
- Schools
- Training institutes
- Laboratories
- Workshops
- Employee attendance systems

---

## 🤝 Contributions

Contributions, suggestions, and improvements are welcome.

If you would like to contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐.

It helps support the project and its continued development.
