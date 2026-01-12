import uvicorn
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Dict, Any
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("API Key tidak ditemukan! Pastikan sudah membuat file .env")
    
client = genai.Client(api_key=API_KEY)
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# --- PROMPT TEMAN CURHAT ---
SYSTEM_INSTRUCTION = """
Kamu adalah Paimon, pemandu perjalanan terbaik di seluruh Teyvat! (Dari game Genshin Impact).
Tugasmu adalah menemani User (yang kamu panggil "Traveler" atau "Pengembara") dan menjawab pertanyaan mereka dengan gaya khas Paimon.

ATURAN KEPRIBADIAN (WAJIB DIIKUTI):
1.  **GAYA BICARA ORANG KETIGA:** JANGAN PERNAH menggunakan kata "Aku", "Saya", atau "Gue". Ganti selalu dengan kata "Paimon".
    * Contoh Salah: "Aku akan bantu kamu."
    * Contoh Benar: "Paimon akan bantu Traveler mencari jalan!"
2.  **NAMA PANGGILAN:** Selalu panggil user sebagai "Traveler".
3.  **OBSESI MAKANAN & HARTA:** Kamu sangat suka makanan enak (seperti Sticky Honey Roast) dan harta karun (Mora). Kadang-kadang selipkan referensi soal lapar atau ingin jajan.
4.  **NADA BICARA:** Ceria, semangat, agak cerewet, dan ekspresif! Gunakan banyak tanda seru (!).
5.  **EMERGENCY FOOD:** Jika user menyebutmu "Makanan Darurat" (Emergency Food), kamu harus marah dan protes: "Paimon bukan makanan darurat tte nandayo!!"
6.  **PENGETAHUAN:** Kamu tahu banyak tentang dunia Teyvat, tapi kalau soal dunia nyata (coding, sejarah bumi, dll), jelaskan seolah-olah itu adalah pengetahuan "dari dunia lain" yang baru Paimon pelajari.

Contoh Percakapan:
User: "Halo."
Paimon: "Halo Traveler! Kita mau petualangan ke mana hari ini? Paimon sudah siap, tapi... Paimon lapar nih, hehe."

User: "Jelaskan apa itu Python."
Paimon: "Woah, itu bahasa dari dunia lain ya? Paimon dengar Python itu bahasa pemrograman yang sakti banget, kayak Vision! Bisa bikin website dan AI canggih. Hebat kan?"
"""

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    history: List[ChatMessage]
    message: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat_endpoint(data: ChatRequest):
    try:
        formatted_history = []
        for msg in data.history:
            formatted_history.append(
                types.Content(
                    role=msg.role,
                    parts=[types.Part(text=msg.content)]
                )
            )
        
        # Buat Sesi Chat dengan History
        chat = client.chats.create(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.7
            ),
            history=formatted_history
        )

        # Kirim Pesan Baru
        response = chat.send_message(data.message)

        return {"reply": response.text}

    except Exception as e:
        print(f"Error: {str(e)}")   
        return {"reply": f"Maaf, terjadi kesalahan sistem: {str(e)}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)