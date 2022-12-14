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
    about = "Quyida 'Pay IT Forward' website๐ haqida qisqacha ma'lumot beriladi. \n" \
            "1. Loyihaning asosiy maqsadi๐ฅ: \n" \
            "Bu loyiha veb dasturlashga qiziquvchi 7 yoshdan ๐ง๐ป๐ฆ 70 yoshgacha ๐ฉ๐ป๐ง๐ป bo'lgan yigit-qiz, erkak-ayollarni ๐ต๐ผ๐ด๐ป to'plab, ularga yo'l-yo'riq, ko'rsatmalar berib, dasturchilar safini kengaytirishga qaratilgandir. \n" \
            "2. Biz bilan dasturlashni o'rganish ๐ va 'to'lov' tartibi ๐ธ: \n" \
            "Dasturlashni o'rganish 'Piramida sxemasi' asosida bo'ladi. Yo'q, bu siz bir paytlar katta pul tikib, keyin afsus qilib qolgan Piramida sxemasi emas๐. Bu saytda dasturchilar daraxti shakllangan bo'lib, u piramida ko'rinishida. \n" \
            "๐๏ธ Siz daraxtdan birorta dasturchi bilan bog'lanib uning jamoasiga qo'shilasiz. \n" \
            "๐๏ธ Jamoa bilan birga bir xil mavzularni o'zlashtirib borasiz. \n" \
            "๐ Qiziqarli vazifalar, har kunlik Stand-up lar va Haftalik Retrolarda ishtirok etasiz. \n" \
            "To'lov tartibi mutlaqo tekin, lekin bu biroz qimmatga tushishi mumkin๐ค. Sababi darslar nihoyasiga yetgandan keyin, o'zingiz kamida 3 (uch) dona shogird topib ularni o'zingiz qanday o'rgangan bo'lsangiz, shunday tartibda o'qitasiz va ularga ham shu 'narx'ni aytasiz. \n" \
            "3. Nimalarni o'rgatamiz๐: \n" \
            "Asosan Veb-dasturlashning Front-end qismini, yani internet foydalanuvchilarga ko'rinadigan qismini tuzishni o'rganamiz. \n" \
            "Bunda bizga HTML, CSS, JAVASCRIPT, BOOTSTRAP, REACT kabi bir qancha texnologiyalar kerak bo'ladi. \n" \
            "4. Darslar qachon yakunlanadi๐: \n" \
            "Siz qo'shilgan jamoa a'zolari hamma har xil muddatda darslarni tugatishi mumkin. Biz ko'rsatgan yoโl xaritasini tugatib (bunga taxminan 1 yil ketadi), biror maoshli ishga kirib olgandan keyingina darslarni yakunladingiz deyishimiz mumkin. \n" \
            "5. Hozirgi jamoa haqida๐ฅ: \n" \
            "Bahriddin Abdiev jamoa sardori ๐ช๐ผ: \n" \
            "Avstralianing Ferocia kompaniyasi senior dasturchisi. 7 yillik tajribaga ega. Hobbiylar: yugurish, stol tennisi, velosiped haydash, bog'dorchilik, Arduino bilan Hardware+Software loyihachalar qilish. \n" \
            "Otabek Kadirov: \n" \
            "Ingliz tili o'qituvchisi, Front-end dasturchi. Hobbiylari: kino, stol tennisi, video oโyinlar. Maqsadi: - kuchli dasturchi bo'lib, FAANG kompaniyalarida tajriba orttirish. \n" \
            "Oybek Turaev: \n" \
            "Frontend dasturchi. Hozirgi ish faoliyati Assalam Group kompaniyasida frontendchi sifatida. Qiziqishlari: - til o'rganish. Maqsadi: - MERN stack dasturchisi bo'lish. \n" \
            "Eldor Ergashov: \n" \
            "TATU talabasi, Frontend dasturchi, Informtech uz youtube kanali asoschisi, qiziqqan sport turi shaxmat. Maqsadi: Full Stack dasturchi bo'lish. \n" \
            "Husan Eshonqulov: \n" \
            "Frontend dasturchi, TDTU talabasi. Foydalanadigan dasturlash tili - JavaScript. Qiziqishlari: xotira va aqliy o'yinlar. Maqsadi: kuchli va O'zbekistonga foydasi tegadigan dasturchi bo'lish. \n" \
            "6. Boโlajak shogirdlarga talablarimizโ๏ธ: \n" \
            "1. Sizda eng avvalo ichki qiziquvchanlik ๐ฅ va xohish kuchli bo'lishi kerak. Dasturchilikni tekin manbalardan o'rganish mumkin, lekin buni birovning undovi bilan o'rganib bo'lmaydi. \n" \
            "2. Manbalarning ko'pchiligi ingliz tilida bo'lganligi sababli, sizda ingliz tili ๐ด๓?ง๓?ข๓?ฅ๓?ฎ๓?ง๓?ฟ eng kamida pre-intermediate darajasida bo'lishi kerak. Rus tili ham albatta asqotadi. \n" \
            "3. Albatta hech bir ishga mas'uliyat ๐ง bilan qaralmasa u ish chala bo'lishi yoki umuman bo'lmasligi ham mumkin. Shuning uchun sizdan mas'ulayat ham talab qilinadi. \n" \
            "4. Sabrโ๏ธ๐. Dasturchilikni hamma ham tanlamasligining eng asosiy sababi mana shu talabda. Dasturchilik bu xuddi zargarlik ishiga o'xshaydi. Uning har bir mayda detallariga e'tibor qaratmasangiz bo'lmaydi. Hatto eng qo'pol va xunuk sayt tayyorlash uchun ham eng mayda piksel, millimetrlarni hisobga olish kerak bo'ladi. \n" \
            "Barchaga omad! \n"
    await message.answer(about)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)