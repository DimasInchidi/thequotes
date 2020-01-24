from models import Quote


def handler_get_quote(update, context):
    if str(context.args[0]).isdigit():
        chat = update.effective_chat
        quote_id = int(context.args[0])
        query = Quote.select().where((Quote.id == quote_id) & (Quote.chat_id == chat.id))
        if query.exists():
            quote = query.get()
            chat.bot.forward_message(
                chat_id=chat.id,
                from_chat_id=-355145151,
                message_id=quote.stored_message_id
            )
            return
    update.message.reply_text(f'Invalid quote id.')
