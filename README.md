# ✨ Paimon AI Chatbot (Genshin Impact Theme)

> *"Ad Astra Abyssosque! Welcome to the Adventurers' Guild!"*

Project ini adalah **AI Chatbot** berbasis web yang mensimulasikan karakter **Paimon** dari game *Genshin Impact*. Dibangun menggunakan **Python (FastAPI)** dan **Google Gemini 1.5 Flash**, chatbot ini memiliki antarmuka (UI) bertema Teyvat yang imersif dan kemampuan mengingat konteks percakapan.

![Project Screenshot](https://via.placeholder.com/800x400?text=Screenshot+Chatbot+Kamu+Disini)
*(Ganti gambar ini dengan screenshot tampilan aplikasimu nanti)*

## 🚀 Fitur Utama

* **Paimon Persona 🧚‍♀️:** Menggunakan *System Prompt Engineering* canggih agar AI berbicara dengan gaya "Orang Ketiga", memanggil user "Traveler", dan terobsesi pada makanan/Mora.
* **Genshin Impact UI Theme ⚔️:** Desain antarmuka *Glassmorphism* dengan palet warna Teyvat (Deep Blue, Gold, Cyan) menggunakan **Tailwind CSS**.
* **Context Memory 🧠:** Chatbot "mengingat" percakapan sebelumnya (Multi-turn conversation) sehingga obrolan terasa nyambung.
* **Modern Tech Stack ⚡:** Backend super cepat dengan FastAPI dan model AI terbaru (Gemini 1.5 Flash).

## 🛠️ Tech Stack

* **Backend:** Python 3.10+, FastAPI, Uvicorn
* **AI Model:** Google Gen AI SDK (`google-genai` v1.0+) - Gemini 1.5 Flash
* **Frontend:** HTML5, Jinja2 Templates, Vanilla JavaScript
* **Styling:** Tailwind CSS (via CDN), FontAwesome
* **Environment:** Python-dotenv

## 📂 Struktur Folder

```text
.
├── main.py             # Logic Backend & Prompt Engineering
├── static/             # Aset Gambar (Icon Paimon)
├── templates/          # Frontend UI (Jinja2)
├── .env                # API Key (Tidak di-upload ke GitHub)
├── requirements.txt    # Daftar library Python
└── README.md           # Dokumentasi ini
