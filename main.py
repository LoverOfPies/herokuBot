import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import time
import random


links = 'https://metanit.com/python/django/ - Руководство по веб-фреймворку Django \n' \
    'https://habr.com/ru/post/181556/ - Простой блог с комментариями на Django \n' \
    'https://habr.com/ru/company/ruvds/blog/429552/ - Руководство по JavaScript \n' \
    'https://habr.com/ru/company/ruvds/blog/432636/ - Учебный курс по React \n' \
    'https://html5book.ru/ - Сайт для тех, кто изучает веб-технологии и создает сайты \n' \
    'https://habr.com/ru/company/ruvds/blog/422893/ - Руководство по Node.js \n' \
    'https://learn.javascript.ru/basic-dom-node-properties - Классы DOM-узлов JS \n'


# -------------------- Запуск бота -----------------------
def start_bot(token):
    v = 5.95
    vk = vk_api.VkApi(token=token)
    vk._auth_token()
    longpooll = VkBotLongPoll(vk, 191808433)

    while True:
        try:
            for event in longpooll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:

                    # если пишем в беседу
                    if event.object.peer_id != event.object.from_id:
                        if event.object.text.lower() == 'пс':
                            vk.method('messages.send', {'peer_id': event.object.peer_id, 'message': links,
                                                        'random_id': random.randint(1, 2147483647)})

                    # если пишем боту в лс
                    elif event.object.peer_id == event.object.from_id:
                        if event.object.text.lower() == 'полезные ссылки:':
                            vk.method('messages.send', {'user_id': event.object.from_id, 'message': event.object.text,
                                                        'random_id': random.randint(1, 2147483647)})

        except Exception as E:
            time.sleep(1)


def main():
    # Токен для бота
    access_token_bot = 'token'
    start_bot(token=access_token_bot)

main()
