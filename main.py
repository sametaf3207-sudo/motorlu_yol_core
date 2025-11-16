from fastapi import FastAPI

app = FastAPI(title="motorlu_yol_core", version="1.0.0")

@app.get("/")
async def root():
    return {
        "cekirdek": "motorlu_yol_core",
        "durum": "AKTIF",
        "versiyon": "1.0.0",
        "mesaj": "Kurye sistemi çekirdeği çalışıyor."
    }
