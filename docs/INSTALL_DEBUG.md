# Общие принципы отладки при установке

Хотя мы делаем всё, чтобы все работало с самого начала, что-то может не заработать.

Давайте рассмотрим, как это побыстрее отладить.

Движок использует следующую схему работы:

**Speech-To-Text (распознавание голоса) -> vacore -> plugin -> Text-To-Speech (генерация голосового ответа)**

Если у вас что-то не работает сразу после старта, то рекомендуется запустить
**runva_cmdline.py**. Это клиент, который сразу отправляет команду "привет" движку, т.е.
использует только следующую цепочку

**vacore -> plugin -> Text-To-Speech**

Если при запуске **runva_cmdline.py**:
1. у вас всё заработало, значит проблема в STT движке. Возможно, не установился vosk или что-то в этом духе.
2. у вас даже не запустилось, значит, что-то не установлено, скорее всего пакеты
3. у вас не отработал TTS/какие-то странные вещи при озвучке - значит, надо наладить TTS движок. 
Последнее - частая история на Linux/MAC, читайте инструкцию по наладке.

**Если у вас 2 или 3 пункт, но непонятно, что именно не работает..**

Установите в options/core.json

`"ttsEngineId": "console",`

и запустите еще раз. Вы должны увидеть результат команды в консоли вместо звука.

Если 
1. всё заработало, значит проблема была в TTS движке, надо его наладить.
2. не заработало, значит проблема в ядре/плагинах (основном коде Катюшы), что маловероятно, 
или вы что-то недоустановили (скорее всего) 