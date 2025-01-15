import telebot

BOT_TOKEN = "5124149668:AAGVQmd9ywi_PcF77Dwq60uf6VjXIFTdVlI"  # Замените на токен вашего бота
CHAT_ID = "1379579817"  # Замените на ваш Chat ID

bot = telebot.TeleBot(BOT_TOKEN)

def handler(request):
    try:
        # Отправка сообщения через бота
        bot.send_message(CHAT_ID, "Таймер завершился! Проверь WhatsApp.")
        return {
            "statusCode": 200,
            "body": "Уведомление отправлено",
        }
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")
        return {
            "statusCode": 500,
            "body": "Ошибка при отправке уведомления",
        } 
