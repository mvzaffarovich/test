from aiogram import Bot , Dispatcher , F
from asyncio import run
from aiogram.types import Message 

bot = Bot (token = "8106967102:AAF5q0GMHyPwvnF0G8CnZ-P3iIRXsdb2azk")

db = Dispatcher ()

@db.message(F.photo)
async def photo (xabar: Message ):
    await xabar.answer (f"Siz rasm yubordiz")

async def main():
    await db.start_polling(bot)


if __name__ == '__main__':
    run(main())