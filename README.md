# Ближайшие бары

Проект обрабатывает базу данных с барами Москвы.
Отображает:

- самый большой бар (по числу мест)
- самый маленький бар
- ближайший бар к пользователю (на основе данных введенных пользователем)

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Для загрузки данных можно использовать url `https://devman.org/fshare/1503831681/4/`

Скачать и сохранить файл с данными можно командой

`wget 'https://devman.org/fshare/1503831681/4/' -O bars.json`

Запуск на Linux:

`python3 bars.py DB_FILE.json`

```bash
$ python3 bars.py
Your coordinates in format `lat, lng` or just press enter
We detected your  coordinates as `25.2582,55.3047` -
Biggest bar is ``Спорт бар «Красная машина»` (seat(s) - 450, coordinates - 37.638228501070095,55.70111462948684)`
Smallest bar is ``БАР. СОКИ` (seat(s) - 0, coordinates - 37.35805920566864,55.84614475898795)`
Closest bar is ``Бар Виват` (seat(s) - 35, coordinates - 37.511274999942046,55.448750279822924)`
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
