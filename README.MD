# kaelloskye-owl-bot
Бот, преобразующий стикеры в изображения. А еще его можно попросить что-нибудь подтвердить.

Пример: [@kaelloskye-owl-bot](https://t.me/kaelloskye_owl_bot)

## Установка

### Подготовка
Для начала создайте бота, используя [@BotFather](https://t.me/BotFather) ([Инструкция](https://core.telegram.org/bots#botfather)). Сохраните полученный API Token вашего бота, он понадобится в дальнейшем.

Создайте аккаунт на [Heroku](https://heroku.com/), установите [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

Авторизируйтесь с вашими данными Heroku
`$ heroku login`

### Установка и запуск бота

Клонируйте репозиторий

`$ git clone https://github.com/snowrill/kaelloskye-owl-bot.git`

`$ cd kaelloskye-owl-bot`

Создание и запуск на Heroku:

`$ heroku create <имя-приложения> --buildpack heroku/python`

`$ git push heroku master`

`$ heroku config:set TGBOT_TOKEN=<токен вашего бота>`

`$ heroku ps:scale bot=1`

## Конфигурация

Настройки в файле `config.json`
* `proxy` - адрес прокси, по умолчанию не указан
* `start_msg_file` - файл с сообщением-приветствием, которое бот посылает в начале беседы
* `help_msg` - справочное сообщение
* `bot_replies` - массив ответов, которые может прислать бот при подтверждении
* `download_link` - ссылка для скачивания стикеров
* `temp_dir` - папка для сохранения изображений