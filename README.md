
# Тестовое задание стажер Junior Backend Developer

Данный  скрипт позволяет определять осмысленный ли фидбэк предоставляемый пользователем или же нет.



## Описание кода
В эпоху стремительного развития искусственного интеллекта, было принято решение использовать уже имеющиеся технологии. Алгоритм работает на основе нейросети gpt3.5 от OpenAI, а вся логика построена вокруг правильного промпта. 

```
Based on the provided examples and your knowledge, identify is this feedback meaningful? Answer "Yes" or "No"
Examples: "ыдвшоаыолвтас" - No, "ля ля ля ля ля " - No, "good" - No, "123" - No, "👍" - Yes, "Все ок" - Yes, "было челенджево, но суперски. респект" - Yes, "1. Интересно 2. Креативно 3. всё понятно." - Yes
Feedback: {сам текст}
```
## Как запустить код?

Для работоспособности кода необходим API токен OpenAI. Его следует положить в переменную **openai_token** в файле **credentials.py**.

Далее следует установить python3 библиотеку *openai*

```bash
  pip install openai
```

Для запуска кода:
```bash
  python detector.py
```
___

Также в проекте приложен минимальный рабочий телеграм бот. Для его запуска нужно положить Telegram Bot токен в переменную **telegram_bot_token** в файле **credentials.py**.

Далее следует установить библиотеку python-telegram-bot v13.15:
```bash
  pip install python-telegram-bot==13.15
```


## Автор

- [@Aimurat1](https://github.com/Aimurat1)

