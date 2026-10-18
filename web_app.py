fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import random

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    return """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>لوحة تحكم بوت مراجحة سولانا</title>
        <style>
            body { font-family: Tahoma, sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }
            .container { max-width: 
