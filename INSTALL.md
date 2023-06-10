# INSTALL

Near to step-by-step guide

1. создаем виртуальное окружение

    ```bash
    sudo apt-get install python3-venv
    python -m venv env
    source env/bin/activate
    ```
2. клонируем реп Катюши

    ```
    git clone https://github.com/j0k/Katusha
    ```
3. cd Katusha
4. устанавливаем зависимости

    ```bash
    pip install -r requirements.txt
    ```

5. пробуем запустить Катюшу

  ```bash
  python runva_vosk.py
  ```

6. заменяем в файле **options/core.json** с `"playWavEngineId":"audioplayer"` на `"sounddevice"`
7. доставляем завимости

  ```bash
  sudo apt-get install libsndfile1-dev
  sudo apt-get install libportaudio2
  pip install fastapi-utils
  sudo apt install espeak
  sudo apt install pkg-config libcairo2-dev gcc python3-dev libgirepository1.0-dev
  pip install PyGObject
  sudo apt-get install gstreamer-1.0
  ```

8. ставим supervisor для работы с Катюшей как с сервисом

  ```
  sudo apt-get install supervisor
  ```

9. создаем конфигурационный файл и директорию для логов сервиса

  ```bash
  nano /etc/supervisor/conf.d/katusha.conf
  [program:katusha]
  directory=/root/Katusha
  command=/root/env/bin/python /root/Katusha/runva_webapi.py
  autostart=true
  autorestart=true
  stderr_logfile=/var/log/katusha/katusha.err.log
  stdout_logfile=/var/log/katusha/katusha.out.log

  [group:katushagroup]
  programs:katusha
  ```

  ```bash
  mkdir /var/log/katusha
  ```

10. обновляем supervisor

  ```bash
  supervisorctl reread
  supervisorctl update

  #  проверяем наличие сервиса
  supervisorctl status

  # supervisorctl stop all - остановить сервис Катюша
  # supervisorctl start all - запустить сервис Катюша
  ```

11. для работы синтеза речи silero ставим Torch

  ```bash
  pip install torch
  ```

12. делаем пробный запуск c web_api

  ```bash
  python runva_webapi.py
  ```

  На этом этапе скрипт сгенерирует недостающие файлы в том числе файл `runva_webapi.json`, в нем необходимо заменить "host": "127.0.0.1" на "host": "0.0.0.0" тем самым делая доступ к API доступным извне.

  Пример итогового файла `runva_webapi.json`:

  ```json
  {
      "hash": "6abb2dcb0d9b2531b052e4c02c181184",
      "host": "0.0.0.0",
      "log_level": "info",
      "port": 5003,
      "use_ssl": false
  }
  ```


13. На этом этаже желательно проверить работу Катюши следующим кодом заменив IP 1.2.3.4 на актуальный.

  ```python
  import requests
  import json

  baseUrl = "http://1.2.3.4:5003/"
  ttsFormat = "saytxt"

  def ask(prompt):
    response = requests.get(baseUrl+"sendRawTxt",
                            params={"rawtxt": prompt,
                                    "returnFormat": ttsFormat})
    return json.loads(response.text)

  answer = ask("катюша привет")
  print(answer)
  ```

  результат работы
  ```
  $: python ask.py
  {'restxt': 'Рада тебя видеть!'}
  ```

  14. Для активации функционала ChatGPT заменить в файле **options/plugin_boltalka2_openai.json** "apiKey": на актуальный токен полученный через openai.

  Серверная часть Катюши готова.

Клиентская часть Катюши запускается на Rasberri Pi 4 путем прошивания образа SD Card 64Gb и изменения в **options.json** `"baseUrl"` с `"http://127.0.0.1:5003/"` на актуальный IP с запущенной серверной частью Катюши.

Бизнес-ассистент Катюша is online :)
