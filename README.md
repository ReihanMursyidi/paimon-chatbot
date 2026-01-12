# ✨ Paimon AI Chatbot (Genshin Impact Theme)

> *"Ad Astra Abyssosque! Welcome to the Adventurers' Guild!"*

Project ini adalah **AI Chatbot** berbasis web yang mensimulasikan karakter **Paimon** dari game *Genshin Impact*.
Dibangun menggunakan **Python (FastAPI)** dan **Google Gemini 2.5 Flash**.

![Project Screenshot](https://github.com/ReihanMursyidi/paimon-chatbot/blob/main/Screenshot%202026-01-12%20195040.png)

## 🚀 Fitur Utama

* **Paimon Persona 🧚‍♀️:** Menggunakan *System Prompt Engineering* canggih agar AI berbicara dengan gaya "Orang Ketiga", memanggil user "Traveler", dan terobsesi pada makanan/Mora.
* **Genshin Impact UI Theme ⚔️:** Desain antarmuka *Glassmorphism* dengan palet warna Teyvat (Deep Blue, Gold, Cyan) menggunakan **Tailwind CSS**.
* **Context Memory 🧠:** Chatbot "mengingat" percakapan sebelumnya (Multi-turn conversation) sehingga obrolan terasa nyambung.
* **Modern Tech Stack ⚡:** Backend super cepat dengan FastAPI dan model AI terbaru (Gemini 2.5 Flash).

## 🛠️ Tech Stack

* **Backend:** Python 3.10+, FastAPI, Uvicorn
* **AI Model:** Google Gen AI SDK (`google-genai` v1.0+) - Gemini 2.5 Flash
* **Frontend:** HTML5, Jinja2 Templates, Vanilla JavaScript
* **Styling:** Tailwind CSS (via CDN), FontAwesome
* **Environment:** Python-dotenv

## 💻 Instalasi & Penggunaan

Ikuti langkah-langkah di bawah ini untuk menjalankan **Paimon Chatbot** di komputer lokal Anda.

### 1. Prasyarat (Prerequisites)
Pastikan Anda sudah menginstall:
* [Python](https://www.python.org/downloads/) (Versi 3.10 ke atas)
* [Git](https://git-scm.com/downloads)

### 2. Clone Repository
Buka terminal (CMD/PowerShell/Terminal) dan jalankan perintah ini:

```bash
git clone https://github.com/ReihanMursyidi/paimon-chatbot.git
cd paimon-chatbot
```

### 3. Setup Virtual Environment (Disarankan)
Agar library tidak berantakan, gunakan lingkungan virtual:

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
Install semua library yang diperlukan (FastAPI, Google GenAI, dll):
```bash
pip install -r requirements.txt
```

### 5. Konfigurasi API Key
Project ini membutuhkan Gemini API Key agar berfungsi.
1. Dapatkan API Key gratis di Google AI Studio.
2. Duplikasi file .env.example menjadi .env (jika ada), atau buat file baru bernama .env.
3. Isi file .env dengan format berikut:

```
GEMINI_API_KEY=Tempel_API_Key_Google_Kamu_Disini
```

### 6. Jalankan Server
Jalankan perintah berikut untuk menyalakan server lokal:
```bash
python main.py
```
Jika berhasil, akan muncul pesan: Uvicorn running on http://127.0.0.1:8000


## 📂 Struktur Folder

```text
.
├── main.py             # Logic Backend & Prompt Engineering
├── static/             # Aset Gambar (Icon Paimon)
├── templates/          # Frontend UI (Jinja2)
├── .env                # API Key (Tidak di-upload ke GitHub)
├── requirements.txt    # Daftar library Python
└── README.md           # Dokumentasi ini
