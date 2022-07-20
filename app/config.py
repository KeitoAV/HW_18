# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.

import os


class Config:
    DEBUG = True
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'movies.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False