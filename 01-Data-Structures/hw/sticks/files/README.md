Подготовка:
* [Посмотреть синтаксис json формата](https://www.quackit.com/json/tutorial/json_syntax.cfm)
* Прочитать [PEP8](https://www.python.org/dev/peps/pep-0008/)

Задание: 
1. DONE Реализовать простейший parser/dumper json
2. DONE Смерджить два файла в один `winedata_full.json`, убрав, если они есть, дупликаты и отсортировать объекты в низходящем порядке по цене, в случае коллизий сортировать по сорту в лексикографическом порядке
   * табуляция на ваше усмотрение
3. DONE Найти для сортов `Gew[üu]rztraminer, Riesling, Merlot, Madera, Tempranillo, Red Blend` следующую информацию:
   * `avarege_price`
   * `min_price`
   * `max_price`
   * `most_common_region` где больше всего вин этого сорта производят ?
   * `most_common_country`
   * `avarage_score`
    
   DONE Найти:
   * `most_expensive_wine` в случае коллизий тут и далее делаем список.
   * `cheapest_wine`
   * `highest_score`
   * `lowest_score`
   * `most_expensive_coutry` в среднем самое дорогое вино среди стран
   * `cheapest_coutry` в среднем самое дешевое вино среди стран
   * `most_rated_country`
   * `underrated_country`
   * `most_active_commentator`
   
	Эти данные, именно с этими ключами сохранить в виде json - объекта в файл `stats.json`
	Объект вида:
	```
	{"statistics": {
			"wine": {
				"Riesling": { ... },
				...
			},
			"most_expensive_wine": ...,
			...
		}
	}

4. DONE Оформить результаты из пункта `3` в виде красивого `markdown` файла


Проверка:   
* оба файла - валидные json
* статистика собрана верно
* код написан согласно PEP8 (буду проверять чем-то вроде [этого](https://pypi.org/project/pep8/))

Дополнительно:
* использованы наиболее подходящие функции, структуры данных и методы, но без фанатизма
* самое быстрое решение - дополнительный балл
  * мерять буду так `bash time python3 script.py`

Обратить внимание:
* запрещается использовать какие-либо библиотеки/функции, типа `eval` для парсинга/дампа json. Все делаем руками. Исключение, встроенные функции для работы со строками, которые мы прошли на лекции.
