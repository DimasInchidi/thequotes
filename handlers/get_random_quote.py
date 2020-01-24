from peewee import fn

from models import Quote


def handler_get_random_quote(update, context):
    chat = update.effective_chat
    query = Quote.select().where(Quote.chat_id == chat.id)
    if query.exists():
        selected_quote = query.order_by(fn.Random()).limit(1)[0]
        chat.bot.forward_message(
            chat_id=chat.id,
            from_chat_id=-355145151,
            message_id=selected_quote.stored_message_id
        )
        return
    update.message.reply_text('Please add at least one quote first.')
