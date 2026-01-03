from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import sqlite3
import bcrypt
from io import BytesIO
import rembg

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],    
)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


class RegisterUser(BaseModel):
    name: str
    email: str
    password: str

class LoginUser(BaseModel):
    email: str
    password: str


@app.post("/register")
def register(user: RegisterUser):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (user.email,))
    existing_user = cursor.fetchone()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                   (user.name, user.email, hashed_password))
    conn.commit()
    conn.close()

    return {"message": "User created successfully"}

@app.post("/login")
def login(user: LoginUser):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (user.email,))
    existing_user = cursor.fetchone()
    conn.close()

    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    stored_password = existing_user['password']
    
    if not bcrypt.checkpw(user.password.encode('utf-8'), stored_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"message": "Login successful"}


@app.post("/remove-background")
async def remove_background(file: UploadFile = File(...)):
    try:
        image_data = await file.read()  

        
        output = rembg.remove(image_data)

        
        image_stream = BytesIO(output)
        image_stream.seek(0)
        return StreamingResponse(image_stream, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error removing background: {e}")
