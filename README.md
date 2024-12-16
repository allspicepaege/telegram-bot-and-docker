# Telegram bot and Docker

## Описание задачи
В данном задании реализован телеграм-бот, который принимает в качестве сообщений ФИО в кириллице и отдаёт ФИО на латинице
в соответствии с [Приказом МИД России от 12.02.2020 № 2113](https://www.consultant.ru/document/cons_doc_LAW_360580/9eb761ae644ec1e283b3a50ef232330b924577cb/)

## Порядок запуска программы
- убедитесь, что у вас установлен Docker. Если Docker не установлен, то сначала выполните его [установку.](https://docs.docker.com/engine/install/)

- находясь внутри папки с данным репозиторием, выполните следующую команду для создания docker-образа:

    `docker build .`

- проверить, что образ создан, можно при помощи следующей команды:

    `docker images`

- запустите полученный образ, указав IMAGE ID образа, который отобразился на предыдущем шаге:

    `docker run -d -p 80:80 <IMAGE ID>`

- посмотреть, что контейнер создан и запущен, можно выполнив команду:

    `docker ps`

Если вы видите строку, в которой указан ваш контейнер со значением в поле STATUS равным UP - ваш контейнер успешно создан и запущен, и вы можете использовать вашего бота по назначению! Теперь вы можете его запустить при помощи команды `/start` и затем вы можете отправлять ему значения ФИО, написанные на кириллице в любом регистре, разделенные между собой пробелами. Если вы отправили боту корректные данные, то в ответном сообщении вы получите текст, данные будут возвращены на латинице в соответствии с таблицей транслитерации в верхнем регистре. В случае, если в тексте присутствуют символы, отличные от символов кириллицы, вы получите сообщение об ошибке ввода данных.



В дальнейшем, чтобы освободить место на вашем диске, вы можете удалить созданный образ.

## Порядок действий для удаления Docker-образа

- сначала нужно остановить запущенный контейнер,выполнив команду:

    `docker stop <CONTAINER ID>`
    - узнать ваш CONTAINER ID вы можете выполнив команду: 

        `docker ps`

        P.S. Здесь же вы видите IMAGE ID в графе IMAGE, который нам понадобится в дальнейшем.

- теперь удаляем наш контейнер:

     `docker rm <CONTAINER ID>`

- последним шагом мы удаляем Docker-образ:

     `docker rmi <IMAGE ID>`

На этом все контейнеры и образы удалены, место на диске освобождено.

### **Благодарим Вас за использование нашего бота!!!**