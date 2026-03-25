# Employee Record Management System (ERMS)

A Python-based desktop application designed to efficiently manage employee records using a modern GUI and a MySQL database. The system simplifies employee data handling by providing secure, fast, and user-friendly CRUD operations.

---

##  Project Overview

Many small and medium-sized organizations still rely on manual registers or scattered spreadsheets to manage employee data. This often leads to data inconsistency, human errors, and poor accessibility. The **Employee Record Management System (ERMS)** provides a centralized and structured solution that allows administrators to manage employee records digitally with ease.

---

## ✨ Features

- 🔐 Secure login system
- ➕ Add new employee records
- ✏️ Update existing employee details
- ❌ Delete individual or all employee records
- 🔍 Search employees by ID, Name, Contact, Gender, Role, or Salary
- 📊 View employee data in a tabular format
- ⚠️ Input validation and error handling
- 🔄 Real-time UI updates synced with database

---

## 🛠️ Technology Stack

### Frontend
- Python
- CustomTkinter (modern GUI framework)

### Backend
- Python

### Database
- MySQL
- PyMySQL

### Tools
- VS Code
- Git & GitHub

---

## 🧩 Project Structure

```
employee-record-system/
│
├── login.py          # Login interface
├── ems.py            # Employee management system UI and logic
├── database.py       # Database connection and CRUD operations
├── cover.jpg         # Background image for login screen
├── .gitignore        # Ignored files (venv, cache, etc.)
├── README.md         # Project documentation
└── venv/             # Virtual environment (not pushed to GitHub)
```

---

## 🏗️ System Architecture

```
Login Module
    ↓
Employee Management System (UI + Logic)
    ↓
MySQL Database
```

- Modular design
- Clear separation of UI, logic, and database
- Easy to maintain and extend

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<username>/<repository>.git
cd employee-record-system
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install customtkinter pymysql pillow
```

### 4️⃣ Configure MySQL

- Ensure MySQL server is running
- Update credentials in `database.py` if required

### 5️⃣ Run the Application

```bash
python login.py
```

---

## 🧪 Validations Implemented

- Mandatory field checks
- Unique employee ID validation
- ID format validation
- Confirmation before delete operations
- Safe database queries using parameterized SQL

---

## ⚠️ Assumptions & Limitations

- Single-user (admin) system
- Desktop-based application
- Basic authentication (credentials are hardcoded for demo)
- Salary stored as text (can be optimized in future)

---

## 🚀 Future Enhancements

- Role-based authentication (Admin / HR / Manager)
- Password encryption and secure authentication
- Cloud database integration
- Employee analytics dashboard
- Attendance and payroll modules
- Multi-user access

---

## 🎯 Use Cases

- Small & Medium Enterprises
- HR Departments
- Educational Institutions
- Startups
- Training Centers

---

## 👩‍💻 Contributor

**Kavya Sharma**  
B.Tech CSE (AIML)  
Python | MySQL | UI Development

---

## 📜 License

This project is developed for educational and hackathon purposes.

---

⭐ **If you find this project useful, feel free to star the repository!**

---
