##Запуск на локальной машине осуществляется командой:

python project/main.py

Вычислим отношение(Scale) цен ETHUSDT/BTCUSDT. На данных во времени, можно посмотреть, что изменение
Scale во времени незначительно. Можно с определенной периодичностью проверять это значение и задать порог, 
при котором будет выдано уведомление "Изменение Scale превысило пороговое значение".

Далее делим временную шкалу на интервалы, например 1мин(Это удобно, так как API позволяет получить
уже готовую информацию для определенных интервалов). На каждом интервале исследуем цены открытия и закрытия
для двух активов. Вычисляем разницу между ценой открытия и закрытия для каждого: BTCUSDT_margin и ETHUSDT_margin
Разницу между последними двумя величинами с учетом Scale можно считать собственным движением ETHUSDT
(По крайней мере работаем с этой гипотезой)