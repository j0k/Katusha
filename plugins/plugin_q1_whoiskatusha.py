# Приветствие (и демо-плагин)
# author: Vladislav Janvarev (inspired by EnjiRouz)

import random
from vacore import VACore

# функция на старте
def start(core:VACore):
    manifest = { # возвращаем настройки плагина - словарь
        "name": "Катюша", # имя
        "version": "1.0", # версия
        "require_online": False, # требует ли онлайн?

        "description": "Кто такая Катюша\n"
                       "Голосовая команда: расскажи про себя|кто ты такая",

        "commands": { # набор скиллов. Фразы скилла разделены | . Если найдены - вызывается функция
            "расскажи про себя|кто ты такая": play_greetings,
        }
    }
    return manifest

def play_greetings(core:VACore, phrase: str): # в phrase находится остаток фразы после названия скилла,
                                              # если юзер сказал больше
                                              # в этом плагине не используется
    # Проигрывание случайной приветственной речи
    greetings = [
        "Я бизнес ассистент созданный для решения задач предпринимателей, чем я могу сейчас помочь?",
    ]
    greet_str = greetings[random.randint(0, len(greetings) - 1)]
    print(f"- Сейчас я скажу фразу {greet_str}...\nЕсли вы её не услышите, значит, у вас проблемы с TTS или выводом звука и их надо настроить через менеджер настроек.")
    core.play_voice_assistant_speech(greet_str)
    print(f"- Я сказала фразу {greet_str}")