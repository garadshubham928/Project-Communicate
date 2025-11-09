# 💬 VSA Messenger

**VSA Messenger** is a real-time messaging application inspired by WhatsApp, designed for reliable and secure one-to-one communication.  
> _This version excludes the “Status/Story” feature by design._

---

## 🧑‍💻 Project Information

| Key Item | Details |
|-----------|----------|
| **Project Name** | VSA Messenger |
| **Developers** | Vijay Shinde, Shubham Garad, Avinash Shinde |
| **Version** | 1.0.0 |
| **License** | MIT |
| **Status** | Active Development |

---

## 📘 Overview

VSA Messenger replicates essential chat functionalities of WhatsApp, focusing on **real-time communication**, **modern UI**, and **data integrity**.  
The system supports private messaging with delivery indicators, authentication, and responsive web design.

---

## ✨ Core Features

- 🔐 **User Authentication** (Sign-Up / Login using JWT)  
- 💬 **Real-Time Messaging** (Socket.io based)  
- 📜 **Chat List & Message History**  
- 👀 **Read Receipts and Delivery Indicators**  
- 🟢 **Online / Offline User Status**  
- 👤 **User Profile Management**  
- 💻 **Responsive Web Interface**  
- 🚫 **No Status Feature** (intentionally omitted)

---

## 🧱 Technology Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | React.js, HTML5, CSS3, JavaScript |
| **Backend** | Node.js, Express.js |
| **Database** | MongoDB (Mongoose ODM) |
| **Real-Time Engine** | Socket.io |
| **Authentication** | JWT (JSON Web Tokens) |
| **Styling** | TailwindCSS / Styled Components |
| **Hosting (Optional)** | Vercel / Render / Localhost |

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/vsa-messenger.git
cd vsa-messenger
```

### 2️⃣ Install Dependencies
```bash
# Backend
cd server
npm install

# Frontend
cd ../client
npm install
```

### 3️⃣ Environment Configuration
Create a `.env` file inside the `server` directory:
```env
PORT=5000
MONGO_URI=<your_mongodb_connection_string>
JWT_SECRET=<your_jwt_secret_key>
```

### 4️⃣ Run Application
```bash
# Start backend
cd server
npm start

# Start frontend
cd ../client
npm start
```

Access the application at:  
➡️ **http://localhost:3000**

---

---

## 🔒 Security Notes

- User sessions secured using **JWT tokens**.  
- Passwords stored in **hashed form** using bcrypt.  
- No external user data shared with third-party APIs.  
- End-to-End Encryption not yet implemented (planned).

---

## 🚧 Roadmap

| Feature | Status |
|----------|---------|
| Group Chats | ⏳ In Progress |
| Media Sharing | Planned |
| Message Encryption | Planned |
| Push Notifications | Planned |
| Dark Mode | Planned |

---

## 🧾 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it for learning or commercial purposes.

---

## 🙌 Acknowledgements

Inspired by **WhatsApp Web Interface**.  
Developed as part of a learning initiative to understand **real-time communication systems** and **scalable backend design**.

---

## 📞 Contact

**Team VSA**  
Developers: Vijay Shinde • Shubham Garad • Avinash Shinde  
📧 _team.vsa.messenger@gmail.com_  
🌐 [GitHub Repository](https://github.com/<your-username>/vsa-messenger)

---
