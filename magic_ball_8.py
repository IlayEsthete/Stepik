import random
import sys


GREETINGS = '- Привет, я магический шар, и я знаю ответ на любой Ваш вопрос.'
YOUR_NAME = '- Как к Вам обращаться? - '
YOUR_QUESTION = '- На какой вопрос Вы хотите получить ответ?'
TRY_AGAIN = '\n- Хотите ещё что-то узнать? (Да/Нет) - '
GOODBYE = '- Возвращайся если возникнут вопросы!'


def greatings():
    print(GREETINGS)
    name = input(YOUR_NAME)
    print('- Привет,', name.title())


def your_question():
    print(YOUR_QUESTION)
    question = input()


def try_again():
    s = input(TRY_AGAIN)
    if s.lower() == 'да':
        print()
    else:
        print(GOODBYE)
        sys.exit(0)


answers = [
    "Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да",
    "Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего",
    "Хорошие перспективы", "Знаки говорят - да", "Да",
    "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать",
    "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять",
    "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
    "Перспективы не очень хорошие", "Весьма сомнительно"
]

if __name__ == '__main__':
    greatings()
    while True:
        your_question()
        print(random.choice(answers))
        try_again()
