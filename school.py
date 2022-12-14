from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler

from services import *


def btns(tip=None):
    bts = []
    if tip == "menu":
        bts = [
            [KeyboardButton("School 255 β"), KeyboardButton("Test Yechasizmiπ")],
            [KeyboardButton("Bog'lanish π²"), KeyboardButton("οΌ¨οΌ΅οΌ­οΌ―")],
            [KeyboardButton("Fikir bildirsh π¬")],
        ]
    elif tip == "ha":
        bts = [
            [KeyboardButton("HAπ")],
            [KeyboardButton("Orqagaπ")],
        ]
    elif tip == "baho":
        bts = [
            [KeyboardButton("Juda zoβr π")],
            [KeyboardButton("Yaxshi π")],
            [KeyboardButton("Kamchiliklar bor π")],
            [KeyboardButton("Menga yoqmadi π")],
            [KeyboardButton("Orqagaπ")],
        ]
    elif tip == "fan":
        bts = [
            [KeyboardButton("π DTM majburiy fanlardan testlar π")],
            [KeyboardButton("π Ingliz tilidan testlar yechish π")],
            [KeyboardButton("π Biologiya fanidan testlar π"), KeyboardButton("π Matematikadan testlar π")],
            [KeyboardButton("π Botni baholang π"), KeyboardButton("Orqagaπ")],
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
            [InlineKeyboardButton("Saytga tashrif β", callback_data="sayt", url=""),
             InlineKeyboardButton("Kanalπ±", callback_data="sayt", url="https://t.me/school_255")],
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
    update.message.reply_text("<b>Assalomu Alekum</b> {}  π \n \n <b>School 255 </b> botiga tashrif "
                              "uchun rahmat π€ \n\n Siz botni kezish davomida ko'proq malumot olasiz.\n\n"
                              " O'zingizga kerakli bo'lga bo'limni tanlangππ»"
                              .format(update.message.from_user.first_name),
                              reply_markup=btns("menu"), parse_mode="HTML")


def message_handler(update, context):
    user = update.message.from_user
    msg = update.message.text
    if msg == "School 255 β":
        update.message.reply_text("π² Saytga tashrif buyursangiz ko'proq malumotlarga ega bo'lasiz va bizning. \n \n "
                                  "πππ§ππ₯π π ham βοΈπππ?π§π bo'lib qo'ysangiz Hursand bo'lamiz.",
                                  reply_markup=inline_btn("btn"), parse_mode="HTML")

    # bog'lanish
    elif msg == "Bog'lanish π²":
        update.message.reply_text("Maktab <b>administratsiasi</b> bilan bog'lanish uchun shu \n<b>(Bog'lanish "
                                  "Uchun)</b> \n\n "
                                  "βοΈMalum Sabablarga ko'ra aloqa yozib olinishi mumkin...",
                                  reply_markup=inline_btn("call"), parse_mode="HTML")

    # HUMO bilan ishlanga qisim
    elif msg == "οΌ¨οΌ΅οΌ­οΌ―":
        update.message.reply_text("οΌ¨οΌ΅οΌ­οΌ― homiylar yetishmasligi sababli mavjud emas.\n\nπ¨βπ¨βπ¦βπ¦ Homiylar soni ("
                                  "1)\nπ€ Homiy bo'lishni hohlasangiz pastdagi link orqali bog'laning.\n \n οΌ¨οΌ΅οΌ­οΌ― "
                                  "nima eganligini bilish uchun  @Welkin_GR shu kanal ohirida post bilan tanishib "
                                  "chiqing sizga foydali bo'ladi degan umitdamiz.π",
                                  reply_markup=inline_btn("humo"), parse_mode="HTML")

    elif msg == "Test Yechasizmiπ":
        update.message.reply_text("Testda o'z bilimingizni tekshirishingiz mumkin agar tayyor bo'lsangiz <b>(HA)</b> "
                                  "tugmasini bosingπ",
                                  reply_markup=btns("ha"), parse_mode="HTML")

    # orqaga Back bilan ishlanga qisim
    elif msg == "Orqagaπ":
        update.message.reply_text("Tashrif uchun rahmat π", reply_markup=btns("menu"))

    elif msg == "HAπ":
        update.message.reply_photo(photo=open("Test.png", "rb"),
                                   caption="ππ» Salom do'stim ! Siz o'zingizga kerakli fandan test yechishga "
                                           "tayyormisizπ€\n\n Unda test yechishni boshlang ... \n\n O'zingizga kerakli "
                                           "bo'limni tanlang...ππ»",
                                   reply_markup=btns("fan"))

    # Fikir bildirish buttoni
    elif msg == "Fikir bildirsh π¬":
        update.message.reply_photo(photo=open("chatuchun.png", "rb"),
                                   caption="Siz o'z fikirlaringizni bildirmoqchimisiz unda \nshu yerda yozib "
                                           "qoldiring ππ»ππ»",
                                   reply_markup=inline_btn("fikir"))

    # botni baholash qismi
    elif msg == "Juda zoβr π":
        update.message.reply_text("Rahmat βΊοΈ")

    elif msg == "Yaxshi π":
        update.message.reply_text("Rahmat π")

    elif msg == "Kamchiliklar bor π":
        update.message.reply_text("Kamchiliklarni ko'rib chiqamiz π")

    elif msg == "Menga yoqmadi π":
        update.message.reply_text("Baho uchun tashakkurπ")

    elif msg == "π Botni baholang π":
        update.message.reply_text("Marhamat botimizni baholang !!!\n\n Rahmat !!!", reply_markup=btns("baho"))

    # Test ishlash qismi

    # elif msg == "π DTM majburiy fanlardan testlar π":
    #     update.message.reply_photo(document=open("dtmtest.pdf", "rb"),
    #                                caption="TEST. Asosiy va Majburiy fanlar \n Ona tili va Adabiyot \nTarix\nIngliz "
    #                                        "tili\nRus tili\nMatematika\nFizika\nBiologiya\nKimyo\nGeografiya\n"
    #                                        "\nUzizga kerakli fanlardan testlarni yeching",
    #                                reply_markup=btns("fan"))

    elif msg == "π Ingliz tilidan testlar yechish π":
        update.message.reply_text("Siz Ingliz tilidan testlarni Bot orqali ishlashingiz mumkin...\nSilka ustini "
                                  "bosing va start bosing o'z bilim darajangizni tekshirib oling π !!! \n \nIngliz "
                                  "tilidan testlar: Iltimos testni yechish uchun linklar ustiga bosing !!! π \n\n "
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
                                  "o'z bahoyingizni bildiring π ",
                                  reply_markup=btns("fan"))

    elif msg == "π Biologiya fanidan testlar π":
        update.message.reply_text("Biologiya fanidan testlar:\n\nTestlarni yechish uchun linklarni ustiga bosing: "
                                  "\n\nπ 1-testimiz: http://t.me/QuizBot?start=AfBc8Q2r \n\nRahmat !!!",
                                  reply_markup=btns("fan"))

    elif msg == "π Matematikadan testlar π":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open('matematika.pdf', 'rb'), filename='matematika.pdf',
                                  caption="Matematika fanidan  testlar π")

    if msg == "π DTM majburiy fanlardan testlar π":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open('dtmtest.pdf', 'rb'), filename='dtmtest.pdf',
                                  caption="DTM majburiy fandan testlar π agar sizga maqul bo'lgan bo'lsa Botni "
                                          "baholang va biz siz uchun yangi testlar chiqarishga harakat qilamiz.π")

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
