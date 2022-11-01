from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler

from services import *


def btns(tip=None):
    bts = []
    if tip == "menu":
        bts = [
            [KeyboardButton("School 255 ✈"), KeyboardButton("Test Yechasizmi😊")],
            [KeyboardButton("Bog'lanish 📲"), KeyboardButton("ＨＵＭＯ")],
            [KeyboardButton("Fikir bildirsh 💬")],
        ]
    elif tip == "ha":
        bts = [
            [KeyboardButton("HA🆗")],
            [KeyboardButton("Orqaga🔙")],
        ]
    elif tip == "baho":
        bts = [
            [KeyboardButton("Juda zo‘r 🌟")],
            [KeyboardButton("Yaxshi 👍")],
            [KeyboardButton("Kamchiliklar bor 📚")],
            [KeyboardButton("Menga yoqmadi 👎")],
            [KeyboardButton("Orqaga🔙")],
        ]
    elif tip == "fan":
        bts = [
            [KeyboardButton("📚 DTM majburiy fanlardan testlar 📚")],
            [KeyboardButton("📚 Ingliz tilidan testlar yechish 📚")],
            [KeyboardButton("📚 Biologiya fanidan testlar 📚"), KeyboardButton("📚 Matematikadan testlar 📚")],
            [KeyboardButton("👍 Botni baholang 👍"), KeyboardButton("Orqaga🔙")],
        ]
    return ReplyKeyboardMarkup(bts, resize_keyboard=True)


def inline_btn(btn_type=None, ctg=None, tip=None, bts=None):
    if btn_type == "call":
        btn = [
            [InlineKeyboardButton("Bog'lanish Uchun ", url="https://t.me/Welkin_Manager")],
        ]
    elif btn_type == "fikir":
        btn = [
            [InlineKeyboardButton("Chatga o'tish", url="https://t.me/chat_school255")]
        ]
    elif btn_type == "humo":
        btn = [
            [InlineKeyboardButton("Bog'lanish Uchun", url="https://link-to-tel.herokuapp.com/tel/"
                                                          "+998 (88) 007-41-81")],
        ]
    else:
        btn = [
            [InlineKeyboardButton("Saytga tashrif ✈", callback_data="sayt", url=""),
             InlineKeyboardButton("Kanal📱", callback_data="sayt", url="https://t.me/school_255")],
        ]

    return InlineKeyboardMarkup(btn)


try:
    create_table()
except Exception as e:
    pass


def start(update, context):
    user = update.message.from_user
    if get_one(user.id):
        a = update.message.from_user.first_name
        print(a)
    else:
        create_user(user_id=user.id, username=user.username)
    update.message.reply_text("<b>Assalomu Alekum</b> {}  😁 \n \n <b>School 255 </b> botiga tashrif "
                              "uchun rahmat 🤝 \n\n Siz botni kezish davomida ko'proq malumot olasiz.\n\n"
                              " O'zingizga kerakli bo'lga bo'limni tanlang👇🏻"
                              .format(update.message.from_user.first_name),
                              reply_markup=btns("menu"), parse_mode="HTML")


def message_handler(update, context):
    user = update.message.from_user
    msg = update.message.text
    if msg == "School 255 ✈":
        update.message.reply_text("📲 Saytga tashrif buyursangiz ko'proq malumotlarga ega bo'lasiz va bizning. \n \n "
                                  "𝐊𝐚𝐧𝐚𝐥𝐠𝐚 ham ❗️𝐎𝐛𝐮𝐧𝐚 bo'lib qo'ysangiz Hursand bo'lamiz.",
                                  reply_markup=inline_btn("btn"), parse_mode="HTML")

    # bog'lanish
    elif msg == "Bog'lanish 📲":
        update.message.reply_text("Maktab <b>administratsiasi</b> bilan bog'lanish uchun shu \n<b>(Bog'lanish "
                                  "Uchun)</b> \n\n "
                                  "❗️Malum Sabablarga ko'ra aloqa yozib olinishi mumkin...",
                                  reply_markup=inline_btn("call"), parse_mode="HTML")

    # HUMO bilan ishlanga qisim
    elif msg == "ＨＵＭＯ":
        update.message.reply_text("ＨＵＭＯ homiylar yetishmasligi sababli mavjud emas.\n\n👨‍👨‍👦‍👦 Homiylar soni ("
                                  "1)\n🤔 Homiy bo'lishni hohlasangiz pastdagi link orqali bog'laning.\n \n ＨＵＭＯ "
                                  "nima eganligini bilish uchun  @Welkin_GR shu kanal ohirida post bilan tanishib "
                                  "chiqing sizga foydali bo'ladi degan umitdamiz.😊",
                                  reply_markup=inline_btn("humo"), parse_mode="HTML")

    elif msg == "Test Yechasizmi😊":
        update.message.reply_text("Testda o'z bilimingizni tekshirishingiz mumkin agar tayyor bo'lsangiz <b>(HA)</b> "
                                  "tugmasini bosing😃",
                                  reply_markup=btns("ha"), parse_mode="HTML")

    # orqaga Back bilan ishlanga qisim
    elif msg == "Orqaga🔙":
        update.message.reply_text("Tashrif uchun rahmat 😃", reply_markup=btns("menu"))

    elif msg == "HA🆗":
        update.message.reply_photo(photo=open("Test.png", "rb"),
                                   caption="👋🏻 Salom do'stim ! Siz o'zingizga kerakli fandan test yechishga "
                                           "tayyormisiz🤔\n\n Unda test yechishni boshlang ... \n\n O'zingizga kerakli "
                                           "bo'limni tanlang...👇🏻",
                                   reply_markup=btns("fan"))

    # Fikir bildirish buttoni
    elif msg == "Fikir bildirsh 💬":
        update.message.reply_photo(photo=open("chatuchun.png", "rb"),
                                   caption="Siz o'z fikirlaringizni bildirmoqchimisiz unda \nshu yerda yozib "
                                           "qoldiring 👇🏻👇🏻",
                                   reply_markup=inline_btn("fikir"))

    # botni baholash qismi
    elif msg == "Juda zo‘r 🌟":
        update.message.reply_text("Rahmat ☺️")

    elif msg == "Yaxshi 👍":
        update.message.reply_text("Rahmat 👍")

    elif msg == "Kamchiliklar bor 📚":
        update.message.reply_text("Kamchiliklarni ko'rib chiqamiz 😊")

    elif msg == "Menga yoqmadi 👎":
        update.message.reply_text("Baho uchun tashakkur🙂")

    elif msg == "👍 Botni baholang 👍":
        update.message.reply_text("Marhamat botimizni baholang !!!\n\n Rahmat !!!", reply_markup=btns("baho"))

    # Test ishlash qismi

    # elif msg == "📚 DTM majburiy fanlardan testlar 📚":
    #     update.message.reply_photo(document=open("dtmtest.pdf", "rb"),
    #                                caption="TEST. Asosiy va Majburiy fanlar \n Ona tili va Adabiyot \nTarix\nIngliz "
    #                                        "tili\nRus tili\nMatematika\nFizika\nBiologiya\nKimyo\nGeografiya\n"
    #                                        "\nUzizga kerakli fanlardan testlarni yeching",
    #                                reply_markup=btns("fan"))

    elif msg == "📚 Ingliz tilidan testlar yechish 📚":
        update.message.reply_text("Siz Ingliz tilidan testlarni Bot orqali ishlashingiz mumkin...\nSilka ustini "
                                  "bosing va start bosing o'z bilim darajangizni tekshirib oling 😁 !!! \n \nIngliz "
                                  "tilidan testlar: Iltimos testni yechish uchun linklar ustiga bosing !!! 👇 \n\n "
                                  "1-testimiz: "
                                  "http://t.me/QuizBot?start=hLVdJo  \n\n2-testimiz:"
                                  "http://t.me/QuizBot?start=kbAsGh2y\n\n3-testimiz:"
                                  "http://t.me/QuizBot?start=SFkKhJFP\n\n4-testimiz:"
                                  "http://t.me/QuizBot?start=0XH5a6Kl\n\n5-testimiz:"
                                  "http://t.me/QuizBot?start=FW9Vse6y\n\n6-testimiz:"
                                  "http://t.me/QuizBot?start=te41vV6W\n\n7-testimiz:"
                                  "http://t.me/QuizBot?start=LcYrgNov\n\n8-testimiz:"
                                  "http://t.me/QuizBot?start=JsFtKhS7\n\n9-testimiz:"
                                  "http://t.me/QuizBot?start=lpsOVauU\n\n10-testimiz:"
                                  "http://t.me/QuizBot?start=GRBxCv9c\n\n1-testimiz:"
                                  "http://t.me/QuizBot?start=zxq7jOAK\n\n12-testimiz:"
                                  "http://t.me/QuizBot?start=ZKMdEHXS\n\n13-testimiz:"
                                  "http://t.me/QuizBot?start=eu2JsiM6\n\n14-testimiz:"
                                  "http://t.me/QuizBot?start=V52mwRY3\n\n15-testimiz:"
                                  "http://t.me/QuizBot?start=4VtNPn6p\n\n16-testimiz:"
                                  "http://t.me/QuizBot?start=ezmB0eFb\n\n17-testimiz:"
                                  "http://t.me/QuizBot?start=BH2pl4Kf\n\n18-testimiz:"
                                  "http://t.me/QuizBot?start=SXb3x6bo\n\n19-testimiz:"
                                  "http://t.me/QuizBot?start=hnWDYQ5B\n\n20-testimiz:"
                                  "http://t.me/QuizBot?start=RSu6WPsT\n\n21-testimiz:"
                                  "http://t.me/QuizBot?start=6e24ecJT\n \n Testni sizga foydasi tekgan bo'lsa botga "
                                  "o'z bahoyingizni bildiring 👇 ",
                                  reply_markup=btns("fan"))

    elif msg == "📚 Biologiya fanidan testlar 📚":
        update.message.reply_text("Biologiya fanidan testlar:\n\nTestlarni yechish uchun linklarni ustiga bosing: "
                                  "\n\n👇 1-testimiz: http://t.me/QuizBot?start=AfBc8Q2r \n\nRahmat !!!",
                                  reply_markup=btns("fan"))

    elif msg == "📚 Matematikadan testlar 📚":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open('matematika.pdf', 'rb'), filename='matematika.pdf',
                                  caption="Matematika fanidan  testlar 📚")

    if msg == "📚 DTM majburiy fanlardan testlar 📚":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open('dtmtest.pdf', 'rb'), filename='dtmtest.pdf',
                                  caption="DTM majburiy fandan testlar 📚 agar sizga maqul bo'lgan bo'lsa Botni "
                                          "baholang va biz siz uchun yangi testlar chiqarishga harakat qilamiz.😊")

def main():
    Token = "5720438402:AAGTklbR1FJLXX6ze6c1kUmnHfnMxQCiZwQ"
    updater = Updater(Token)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    # updater.dispatcher.add_handler(CallbackQueryHandler(send_document))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
