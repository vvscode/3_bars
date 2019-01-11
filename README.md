# Ближайшие бары

Проект обрабатывает базу данных с барами Москвы.
Отображает:

- самый большой бар (по числу мест)
- самый маленький бар
- ближайший бар к пользователю (на основе данных введенных пользователем)

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
$ python3 bars.py
Which url should we use to load data? (or just enter to use https://devman.org/fshare/1503831681/4/) -
Please enter your coordinates in format `lat, lng` (like `24.4667,54.3667`) or just press enter -
Biggest bar is `Спорт бар «Красная машина»` with 450 seats
Smallest bar is `БАР. СОКИ` with 0 seats
Closest bar is `Бар Виват` with  coordinates 37.511274999942046,55.448750279822924
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
