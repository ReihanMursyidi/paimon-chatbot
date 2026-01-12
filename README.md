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


## 📂 Struktur Folder

```text
.
├── main.py             # Logic Backend & Prompt Engineering
├── static/             # Aset Gambar (Icon Paimon)
├── templates/          # Frontend UI (Jinja2)
├── .env                # API Key (Tidak di-upload ke GitHub)
├── requirements.txt    # Daftar library Python
└── README.md           # Dokumentasi ini
