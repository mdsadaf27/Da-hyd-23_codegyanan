# 📚 Library Management System

A **terminal-based Library Management System** developed using **Python** to simplify and organize daily library operations.

It provides separate **Member** and **Admin/Librarian** workflows covering registration, OTP verification, approval, memberships, book management, borrowing, returns, fines, and reports.

---

## 📌 Project Overview

### 👤 Member Side

* Register with OTP verification
* Member login
* Search books by title, author, or category
* Borrow and return books
* View borrowed books and due dates
* View membership details and fines
* Get book recommendations

### 🧑‍💼 Admin/Librarian Side

* Admin login
* Approve/reject pending members
* Add, edit, and remove books
* Manage members
* Track issues and returns
* Automatic fine calculation
* View reports and library statistics

### 🔄 Workflow

**Registration → OTP Verification → Admin Review → Membership → Login → Search → Borrow/Return**

---

## ✨ Key Features

* 🔐 OTP-based registration
* ✅ Admin approval system
* 📚 Book catalog management
* 🔎 Book search
* 📖 Borrowing and returning
* 💰 Automatic overdue fine calculation
* 👥 Membership-based borrowing limits
* 📊 Reports and statistics
* 💾 Persistent JSON data storage

---

## 💳 Membership Plans

| Plan    |     Price |   Limit | Duration |   Fine |
| ------- | --------: | ------: | -------: | -----: |
| Basic   |      Free | 3 Books |  14 Days | ₹5/day |
| Premium | ₹199/year | 5 Books |  21 Days | ₹5/day |
| Gold    | ₹499/year | 8 Books |  30 Days | ₹5/day |

---

## 🛠️ Tech Stack

* **Language:** Python
* **Application:** Terminal / CLI
* **Storage:** JSON
* **Data File:** `library_data.json`

### Project Structure

```text
Library-Management-System/
├── project.py
├── library_data.json
└── README.md
```

> If your Python file is named `library_system.py`, use that filename instead.

---

## ⚙️ Setup & Run

### Clone

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

### Check Python

```bash
python --version
```

### Run

```bash
python project.py
```

or

```bash
python3 project.py
```

If your file is `library_system.py`:

```bash
python3 library_system.py
```

---

## 🔐 Environment Variables

No environment variables or `.env` file are required for the current demo version.

OTP is displayed on screen for demonstration. A production version can use environment variables for email/SMS credentials.

```env
EMAIL_USER=your_email
EMAIL_PASSWORD=your_password
```

---

## 🗄️ Data Storage

The project uses **`library_data.json`** instead of an external database.

It stores:

* Users and memberships
* Book details and available copies
* Issue and return records
* Fine information

Data remains available after closing and reopening the application.

---

## 🔑 Demo Accounts

**Librarian**

```text
Username: admin@library.local
Password: admin123
```

**Active Student**

```text
Username: asha@example.com
Password: student123
```

**Needs Membership**

```text
Username: rahul@example.com
Password: student123
```

**Awaiting Review**

```text
Username: priya@example.com
Password: student123
```

> Demo credentials are provided only for project demonstration.

---

## 💰 Fine Calculation

The basic overdue fine is:

**₹5 per overdue day**

Membership-based fine discounts are also included.

---

## 👥 Team Contributions

### 👩 Koduri Nikhitha — Person 1

**Introduction + Member Side**

* Project introduction
* Project execution
* Member registration & OTP verification
* Pending-user workflow
* Member login and dashboard
* Book search
* Book borrowing
* Borrowed-book details
* Member-side presentation

### 👨 Mohammed Duray Sadaf — Person 2

**Admin Side + Final Closing**

* Admin/librarian login
* Pending-user approval/rejection
* Book catalog management
* Add/remove books
* Issues & returns
* Fine calculation
* Reports
* Overall workflow explanation
* Admin-side presentation
* Final project closing

---

## 🚀 Future Improvements

* Real email/SMS OTP delivery
* Multi-librarian roles
* Audit logs
* Online fine payment
* Migration from JSON to MySQL/database
* Improved authentication and password security
* Web/GUI interface

---

## 🎯 Conclusion

The **Library Management System** connects member and librarian workflows in one organized system.

Members can **register, verify, search, borrow, return, and track books**, while librarians can **approve members, manage books, monitor transactions, calculate fines, and view reports**.

### 👥 Developed By

**Koduri Nikhitha**
**Mohammed Duray Sadaf**
