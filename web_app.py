from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

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
            .container { max-width: 900px; margin: auto; background: #1e293b; padding: 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
            h1 { color: #38bdf8; text-align: center; }
            .card { background: #334155; padding: 20px; margin: 15px 0; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; }
            .btn { background: #10b981; color: white; border: none; padding: 12px 24px; border-radius: 6px; cursor: pointer; font-size: 16px; font-weight: bold; }
            .btn:hover { background: #059669; }
            .status-ok { color: #4ade80; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>لوحة تحكم بوت مراجحة سولانا</h1>
            <div class="card">
                <div>
                    <h3>حالة المحفظة</h3>
                    <p id="wallet-status">الحالة: غير متصلة</p>
                </div>
                <button class="btn" onclick="connectWallet()">ربط المحفظة</button>
            </div>
            <div class="card">
                <div>
                    <h3>تفاصيل أداء البوت</h3>
                    <p>الحالة التشغيلية: <span class="status-ok">نشط ويعمل</span></p>
                    <p>عدد المجمعات المراقبة: 10 مجمعات (Raydium, Orca, Meteora ...)</p>
                    <p>آخر فارق سعري مرصود: <span id="spread">0.42%</span></p>
                    <p>إجمالي الأرباح: <span id="profit">0.045 SOL</span></p>
                </div>
            </div>
        </div>
        <script>
            function connectWallet() {
                document.getElementById('wallet-status').innerText = "العنوان: 7xKX...SolanaWalletMock";
                alert("تم ربط المحفظة بنجاح!");
            }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
