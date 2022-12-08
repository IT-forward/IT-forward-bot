import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5809270798:AAHFrz-2ZnF3Yhu8bfTw6e_QQMToIQlot7M'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Pay IT Fprward botiga xush kelibsiz!")

@dp.message_handler(commands=['about'])
async def send_about(message: types.Message):
    about = "Quyida 'Pay IT Forward' website🌐 haqida qisqacha ma'lumot beriladi. \n" \
            "1. Loyihaning asosiy maqsadi🥅: \n" \
            "Bu loyiha veb dasturlashga qiziquvchi 7 yoshdan 👧🏻👦 70 yoshgacha 👩🏻🧔🏻 bo'lgan yigit-qiz, erkak-ayollarni 👵🏼👴🏻 to'plab, ularga yo'l-yo'riq, ko'rsatmalar berib, dasturchilar safini kengaytirishga qaratilgandir. \n" \
            "2. Biz bilan dasturlashni o'rganish 📚 va 'to'lov' tartibi 💸: \n" \
            "Dasturlashni o'rganish 'Piramida sxemasi' asosida bo'ladi. Yo'q, bu siz bir paytlar katta pul tikib, keyin afsus qilib qolgan Piramida sxemasi emas😄. Bu saytda dasturchilar daraxti shakllangan bo'lib, u piramida ko'rinishida. \n" \
            "👉️ Siz daraxtdan birorta dasturchi bilan bog'lanib uning jamoasiga qo'shilasiz. \n" \
            "👉️ Jamoa bilan birga bir xil mavzularni o'zlashtirib borasiz. \n" \
            "👉 Qiziqarli vazifalar, har kunlik Stand-up lar va Haftalik Retrolarda ishtirok etasiz. \n" \
            "To'lov tartibi mutlaqo tekin, lekin bu biroz qimmatga tushishi mumkin🤑. Sababi darslar nihoyasiga yetgandan keyin, o'zingiz kamida 3 (uch) dona shogird topib ularni o'zingiz qanday o'rgangan bo'lsangiz, shunday tartibda o'qitasiz va ularga ham shu 'narx'ni aytasiz. \n" \
            "3. Nimalarni o'rgatamiz📝: \n" \
            "Asosan Veb-dasturlashning Front-end qismini, yani internet foydalanuvchilarga ko'rinadigan qismini tuzishni o'rganamiz. \n" \
            "Bunda bizga HTML, CSS, JAVASCRIPT, BOOTSTRAP, REACT kabi bir qancha texnologiyalar kerak bo'ladi. \n" \
            "4. Darslar qachon yakunlanadi🔚: \n" \
            "Siz qo'shilgan jamoa a'zolari hamma har xil muddatda darslarni tugatishi mumkin. Biz ko'rsatgan yo‘l xaritasini tugatib (bunga taxminan 1 yil ketadi), biror maoshli ishga kirib olgandan keyingina darslarni yakunladingiz deyishimiz mumkin. \n" \
            "5. Hozirgi jamoa haqida👥: \n" \
            "Bahriddin Abdiev jamoa sardori 💪🏼: \n" \
            "Avstralianing Ferocia kompaniyasi senior dasturchisi. 7 yillik tajribaga ega. Hobbiylar: yugurish, stol tennisi, velosiped haydash, bog'dorchilik, Arduino bilan Hardware+Software loyihachalar qilish. \n" \
            "Otabek Kadirov: \n" \
            "Ingliz tili o'qituvchisi, Front-end dasturchi. Hobbiylari: kino, stol tennisi, video o‘yinlar. Maqsadi: - kuchli dasturchi bo'lib, FAANG kompaniyalarida tajriba orttirish. \n" \
            "Oybek Turaev: \n" \
            "Frontend dasturchi. Hozirgi ish faoliyati Assalam Group kompaniyasida frontendchi sifatida. Qiziqishlari: - til o'rganish. Maqsadi: - MERN stack dasturchisi bo'lish. \n" \
            "Eldor Ergashov: \n" \
            "TATU talabasi, Frontend dasturchi, Informtech uz youtube kanali asoschisi, qiziqqan sport turi shaxmat. Maqsadi: Full Stack dasturchi bo'lish. \n" \
            "Husan Eshonqulov: \n" \
            "Frontend dasturchi, TDTU talabasi. Foydalanadigan dasturlash tili - JavaScript. Qiziqishlari: xotira va aqliy o'yinlar. Maqsadi: kuchli va O'zbekistonga foydasi tegadigan dasturchi bo'lish. \n" \
            "6. Bo‘lajak shogirdlarga talablarimiz❗️: \n" \
            "1. Sizda eng avvalo ichki qiziquvchanlik 🔥 va xohish kuchli bo'lishi kerak. Dasturchilikni tekin manbalardan o'rganish mumkin, lekin buni birovning undovi bilan o'rganib bo'lmaydi. \n" \
            "2. Manbalarning ko'pchiligi ingliz tilida bo'lganligi sababli, sizda ingliz tili 🏴󠁧󠁢󠁥󠁮󠁧󠁿 eng kamida pre-intermediate darajasida bo'lishi kerak. Rus tili ham albatta asqotadi. \n" \
            "3. Albatta hech bir ishga mas'uliyat 🧐 bilan qaralmasa u ish chala bo'lishi yoki umuman bo'lmasligi ham mumkin. Shuning uchun sizdan mas'ulayat ham talab qilinadi. \n" \
            "4. Sabr☝️😌. Dasturchilikni hamma ham tanlamasligining eng asosiy sababi mana shu talabda. Dasturchilik bu xuddi zargarlik ishiga o'xshaydi. Uning har bir mayda detallariga e'tibor qaratmasangiz bo'lmaydi. Hatto eng qo'pol va xunuk sayt tayyorlash uchun ham eng mayda piksel, millimetrlarni hisobga olish kerak bo'ladi. \n" \
            "Barchaga omad! \n"
    await message.answer(about)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)