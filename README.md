# Student Management System

A robust Python console application designed to handle student data management using text files as a local flat-file database. Built as a foundational portfolio piece demonstrating clean code principles, edge-case data validation, and secure file manipulation.

## 🚀 Key Features
* **View Student Records:** Parses text files cleanly into readable, styled terminal profiles.
* **Smart Search System:** Search records dynamically by student name with case-insensitivity.
* **Safe Entry Deletion:** Rewrites flat-file entries safely using optimized name-matching logic.
* **Edge-Case Validation:** Employs defensive programming via data sanitization (`.strip()` and `.lower()`) and custom line filters (`if not record.strip(): continue`) to handle accidental trailing newlines and trailing white space without application crashes.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Database:** Local Text Database (`students.txt`)

## 📋 How To Run
1. Ensure you have Python installed on your local environment.
2. Clone or download this repository.
3. Open your terminal/command prompt inside the project directory and execute:
   ```bash
   python SchoolManagement.py
   ```
