# 🔐 REST API with JWT Authentication

## 📌 Description
This is a simple REST API built with Flask.  
It supports user authentication using JWT tokens and task management.

## ⚙️ Technologies
- Python
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- SQLite

## 🚀 Features
- User registration
- User login
- JWT authentication
- Protected routes
- Create tasks
- Get user tasks

## 🔑 Authentication
After login, you receive a JWT token.

Use it in headers:
Authorization: Bearer <your_token>

## 📡 API Endpoints

### Register
POST /register  
Body:
```json
{
  "username": "test",
  "password": "123"
}
## ⚠️ Notes
- This is a simplified calculator
- Real cable selection depends on installation method, temperature and standards
Сейчас:

230 / 400 фиксировано

Можно добавить:

выбор 220 / 230 / 400

👉 это + к профессионализму
# ⚡ Electrical Calculator API

## 📌 Description
REST API for calculating electrical parameters.

## ⚙️ Features
- Current calculation
- Breaker selection
- Cable selection

## 📡 Endpoint

POST /calculate

### Request:
{
  "power": 5,
  "phase": 1
}

### Response:
{
  "current": 27.17,
  "breaker": 32,
  "cable_mm2": 4
}

## ▶️ Run
pip install flask
python app.py
## ⚠️ Engineering Notes
- Calculations are simplified
- Real selection depends on installation method
- Safety factor applied to breaker selection