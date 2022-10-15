from aiogram.utils import executor
from config import dp
import logging
from handlers import extra, client, callback, admin


client.register_client_handler(dp)
callback.register_callback_handler(dp)
admin.register_admin_handler(dp)
extra.register_extra_handler(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
