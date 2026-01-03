
# Background Remover

A full‑stack web application that allows users to register, log in, upload images, and remove the background with a single click using an AI‑powered backend. This project demonstrates modern web development with authentication, image processing, and a clean UI.

---

## 🔍 Overview

This application enables users to:

💡 **Register and log in** using email and password
🖼️ **Upload images** by drag & drop or file selection
🧠 **Remove the image background** using a Python backend powered by `rembg` (AI‑based background removal)
⬇️ **Download the processed image** with transparent background

The backend is built with **FastAPI**, and the frontend uses simple yet effective **HTML, CSS, and Vanilla JavaScript**.

---

## 🚀 Features

✔ User authentication with hashed passwords (using `bcrypt`)
✔ Fast background removal via a Python endpoint (`/remove‑background`)
✔ Drag & drop or click‑to‑upload UX
✔ Responsive UI and modern design
✔ Simple download option for processed images

---

## 🛠️ Tech Stack

| Layer            | Technology                        |
| ---------------- | --------------------------------- |
| Backend          | FastAPI                           |
| Image Processing | rembg (u2net model) ([GitHub][1]) |
| Authentication   | Python `bcrypt`                   |
| Database         | SQLite                            |
| Frontend         | HTML, CSS, JavaScript             |
| Deployment       | uvicorn (ASGI server)             |

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/giboiq200/Background-remover.git
cd Background-remover
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # Linux & macOS
venv\Scripts\activate           # Windows
```

3. **Install backend dependencies**

```bash
pip install fastapi uvicorn bcrypt rembg[cpu]
```

4. **Run the FastAPI server**

```bash
uvicorn main:app --reload
```

5. **Open the frontend**

* Open `register.html` and `login.html` in your browser
* After logging in, the app redirects to `main.html`

---

## 🧑‍💻 Usage

1. **Register** a new user or login with the test account
2. **Upload an image** via drag & drop or click
3. Click **Remove Background** to process the image
4. After processing, click **Download Image**

---

## 📁 Folder Structure

```
├── backend/                  # FastAPI server code
│   └── main.py
├── frontend/                 # Frontend UI files
│   ├── register.html
│   ├── login.html
│   ├── main.html
|   ├── styles.css
|   ├── main.css
│   └── style.css
├── database.db               # SQLite database (optional)
└── README.md
```

---

## 🧠 How It Works

### 🗄️ Authentication

User details are stored in a SQLite database, with passwords hashed using `bcrypt` before storage.

### 🖼️ Image Processing

Images are sent from the frontend via `fetch` and processed on the backend using the `rembg` library — a Python package that removes image backgrounds via pre‑trained segmentation models.

---

## 🧪 Demo Test Credentials

You can use the following sample credentials (if included in the sample database):

```
Email: user@example.com
Password: password123
```

