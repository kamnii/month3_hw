from aiogram import types, Dispatcher
import hashlib


async def inline_wiki_handler(query: types.InlineQuery):
    text = query.query
    link = f'https://ru.wikipedia.org/wiki/{text}'

    article = [types.InlineQueryResultArticle(
        id=hashlib.md5(text.encode()).hexdigest(),
        title='Wiki search',
        url=link,
        input_message_content=types.InputMessageContent(
            message_text=f"Держи ссылку\n{link}"
        )
    )]

    await query.answer(article, cache_time=50)


def register_inline_handler(dp: Dispatcher):
    dp.register_inline_handler(inline_wiki_handler)
