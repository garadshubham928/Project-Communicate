# Project-Communicate
# 💬 VSA Messenger

A real-time chat application inspired by WhatsApp — built for seamless one-to-one communication.  
> **Note:** This clone focuses on **core messaging** features and **does not include status functionality**.

---

## 👥 Developers
- **Vijay Shinde**
- **Shubham Garad**
- **Avinash Shinde**

---

## 🚀 Project Overview
**VSA Messenger** is a modern messaging platform designed to simulate the look and feel of WhatsApp’s core chat experience.  
It enables real-time private messaging between users with an intuitive interface and secure data handling.

---

## 🧩 Features
✅ User Authentication (Sign-up / Login)  
✅ Real-Time Messaging (Socket.io or Firebase)  
✅ Chat List with Recent Messages  
✅ Message Seen / Delivered Indicators  
✅ Online / Offline Status  
✅ Profile Management (Avatar, Username)  
✅ Responsive Web UI  
🚫 **No Status / Story Feature** (by design)

---

## 🏗️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| **Frontend** | React.js / HTML / CSS / JavaScript |
| **Backend** | Node.js + Express |
| **Database** | MongoDB (with Mongoose) |
| **Real-Time Engine** | Socket.io |
| **Authentication** | JWT (JSON Web Tokens) |
| **Styling** | TailwindCSS or Styled Components |
| **Hosting** | (Optional: Render / Vercel / Localhost) |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/vsa-messenger.git
cd vsa-messenger
```

### 2️⃣ Install Dependencies
**For Backend**
```bash
cd server
npm install
```

**For Frontend**
```bash
cd ../client
npm install
```

### 3️⃣ Environment Setup
Create a `.env` file in the `server` directory with the following:
```env
PORT=5000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
```

### 4️⃣ Start the Application
**Run Backend**
```bash
cd server
npm start
```

**Run Frontend**
```bash
cd ../client
npm start
```

App will be live at **http://localhost:3000**

---

## 🖼️ Screenshots (Optional)
You can add some UI previews here later:
```
📁 assets/screenshots/
```

---

## 🔒 Security & Privacy
- End-to-end encryption is **not implemented yet** (future release).
- JWT used for authentication and user session management.

---

## 🛠️ Future Improvements
- Group Chats  
- Media Sharing (Images, Videos, Files)  
- Message Encryption  
- Notifications  
- Dark Mode  

---

## 🧾 License
This project is licensed under the **MIT License** — free to use and modify.

---

## ⭐ Acknowledgements
Inspired by **WhatsApp Web Interface** and built to learn **real-time communication systems**.

---

### 📧 Contact
For collaboration or queries:  
**Vijay Shinde**, **Shubham Garad**, **Avinash Shinde**  
📩 _Team VSA_
