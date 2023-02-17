## Запуск на локальной машине осуществляется командой:
python project/main.py

## Запуск через докер, из директории содержащей файл docker-compose.yaml:
docker-compose up

## 1
 - Вычислим отношение(**Scale**) цен **ETHUSDT/BTCUSDT**.
 - На данных во времени видно, что изменение **Scale** во времени незначительно.
 - Можно с определенной периодичностью проверять это значение и задать порог, 
при котором будет выдано уведомление "Изменение **Scale** превысило пороговое значение".
- В скрипте значение **Scale** вычисляется один раз в начале работы.

## 2
- Далее, делим временную шкалу на интервалы, например 1мин(Это удобно, так как API позволяет получить
уже готовую информацию для определенных интервалов).
- Вычисляем разницу между ценой открытия и закрытия для каждого интервала: **BTCUSDT_margin** и **ETHUSDT_margin**
- Разницу между последними двумя величинами, с учетом **Scale**, можно считать собственным движением **ETHUSDT**

## 3
- Скрипт выводит в консоль текущее собственное изменение цены в процентах. 
- Чтобы вывод осуществлялся только при достижении значения в 1% , нужно добавить в скрипт условие (не стал добавлять для наглядности)

## Contacts
- email: semen.gorbunov@gmail.com
- telegram: @SemenSergeevich