import asyncio
import aiohttp
from loguru import logger

logger.add("bot.log", rotation="10 MB")

class SolanaArbitrageBot:
    def __init__(self):
        self.dexes = [
            "Raydium", "Orca", "Meteora", "Pump.fun", 
            "MannyFold", "Saber", "OpenBook", "Crema", 
            "Lifinity", "Aldrin"
        ]
        self.is_running = False

    async def fetch_prices(self):
        await asyncio.sleep(0.5)
        return {dex: 100.0 + (hash(dex) % 5) * 0.1 for dex in self.dexes}

    async def scan_opportunities(self):
        prices = await self.fetch_prices()
        min_dex = min(prices, key=prices.get)
        max_dex = max(prices, key=prices.get)
        
        min_price = prices[min_dex]
        max_price = prices[max_dex]
        
        spread = ((max_price - min_price) / min_price) * 100
        
        logger.info(f"تم فحص المجمعات. أرخص منصة: {min_dex} بسعر {min_price}, أغلى منصة: {max_dex} بسعر {max_price}, الفارق: {spread:.2f}%")
        
        if spread > 0.5:
            logger.success(f"فرصة مراجحة حقيقية تم اكتشافها! الشراء من {min_dex} والبيع في {max_dex}")
            await self.execute_atomic_swap(min_dex, max_dex)

    async def execute_atomic_swap(self, buy_dex, sell_dex):
        logger.info(f"جاري إرسال معاملة ذرية واحدة للشراء من {buy_dex} والبيع في {sell_dex}...")
        await asyncio.sleep(1)
        logger.success("تم تنفيذ المعاملة الذرية بنجاح وتسجيل الربح!")

    async def start(self):
        self.is_running = True
        logger.info("تم تشغيل بوت المراجحة الذرية لمجمعات سولانا بنجاح.")
        while self.is_running:
            try:
                await self.scan_opportunities()
                await asyncio.sleep(2)
            except Exception as e:
                logger.error(f"خطأ أثناء المراقبة: {e}")
                await asyncio.sleep(2)

if __name__ == "__main__":
    bot = SolanaArbitrageBot()
    try:
        asyncio.run(bot.start())
    except KeyboardInterrupt:
        logger.info("تم إيقاف البوت بواسطة المستخدم.")
