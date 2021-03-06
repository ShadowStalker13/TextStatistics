# TEXT STATISTICS

## Оглавление

1. [Описание](#Описание)
2. [Установка](#Установка)
3. [Функции](#Функции)
4. [Особенности](#Особенности)
## Описание

Библиотека предназначена для подсчета количества слов текста, выводит их количество, количество уникальных слов и сами эти слова.

### Версия Python

Поддерживается версия Python 3.9

## Установка

### Windows

```
py -m pip install TextStatistic
```
## Функции


### count_words()

Данная функция принимает на входе путь к файлу. На выходе получается
значение, которое показывает сколько слов в тексте.

```python
from TextStatistic import count_words


filename = r"C:\Users\Home_PC\Downloads\TestText.txt"
cw = count_words(filename)
print(cw)
```
```
181
```
### count_unique_words()

Данная функция принимает на входе путь к файлу. На выходе получается
значение, которое показывает сколько уникальных(неповторяющихся) слов в тексте.

```python
from TextStatistic import count_unique_words


filename = r"C:\Users\Home_PC\Downloads\TestText.txt"
cuw = count_unique_words(filename)
print(cuw)
```
```
127
```

### all_words()

Данная функция принимает на входе путь к файлу. На выходе получается
словарь, в котором находятся слова и сколько раз они встречались в тексте.

```python
from TextStatistic import all_words


filename = r"C:\Users\Home_PC\Downloads\TestText.txt"
aw = all_words(filename)
print(aw)
```
```
{'а': 2, 'автор': 2, 'боли': 1, 'боялся': 1, 'будут': 1, 'бы': 2, 'в': 5, 'ведь': 1, 'верить': 1, 'вернуться': 1, 'викторович': 1, 'вкладывать': 1, 'впасть': 1, 'вперед': 1, 'всего': 2, 'всех': 1, 'встретить': 1, 'две': 1, 'депрессию': 1, 'детстве': 1, 'для': 1, 'домой': 1, 'дочки': 1, 'его': 3, 'если': 4, 'есть': 1, 'ждал': 1, 'жена': 1, 'жизнью': 1, 'задуматься': 1, 'и': 13, 'им': 1, 'их': 1, 'каждый': 1, 'колька': 3, 'кольке': 1, 'которых': 1, 'летное': 1, 'летчиком': 2, 'ли': 3, 'любит': 1, 'мечта': 1, 'мечте': 1, 'мечту': 3, 'мечты': 1, 'мизеров': 1, 'мизеровым': 1, 'много': 1, 'могу': 1, 'может': 1, 'можешь': 1, 'на': 1, 'навряд': 1, 'над': 1, 'найти': 1, 'нам': 1, 'наслаждаться': 1, 'не': 6, 'него': 1, 'неизвестности': 1, 'новую': 1, 'нужно': 2, 'о': 1, 'однако': 1, 'окончания': 1, 'он': 5, 'осуществил': 1, 'осуществить': 2, 'от': 1, 'откажешься': 1, 'отчаиваться': 1, 'охватил': 1, 'очень': 1, 'передумал': 1, 'повествует': 1, 'позже': 1, 'полностью': 1, 'после': 1, 'поступил': 1, 'поступить': 2, 'предлагает': 1, 'приехав': 1, 'прикладывать': 1, 'проблемой': 1, 'резко': 1, 'решил': 3, 'с': 1, 'сбываться': 1, 'сбылась': 1, 'сбыться': 1, 'св': 1, 'своего': 1, 'себя': 1, 'сергей': 1, 'сердце': 1, 'скорее': 1, 'смог': 1, 'сможет': 1, 'сможешь': 1, 'согласиться': 1, 'станет': 1, 'станцию': 1, 'стараться': 1, 'стать': 1, 'стонет': 1, 'страх': 1, 'стремиться': 1, 'суждено': 1, 'считает': 1, 'так': 1, 'то': 4, 'того': 1, 'трудиться': 1, 'у': 2, 'усилий': 1, 'училище': 3, 'учиться': 1, 'хотелось': 1, 'хочешь': 1, 'цель': 1, 'часа': 1, 'человек': 1, 'что': 3, 'чтобы': 1, 'школы': 1, 'щемящей': 1, 'этой': 1}
```

#### get_words()

Данная функция принимает на входе путь к файлу. На выходе получается 
список отсортированных по алфавиту слов файла без знаков препинания.

```python
from TextStatistic import get_words


filename = r"C:\Users\Home_PC\Downloads\TestText.txt"
gw = get_words(filename)
print(gw)
```
```
['а', 'а', 'автор', 'автор', 'боли', 'боялся', 'будут', 'бы', 'бы', 'в', 'в', 'в', 'в', 'в', 'ведь', 'верить', 'вернуться', 'викторович', 'вкладывать', 'впасть', 'вперед', 'всего', 'всего', 'всех', 'встретить', 'две', 'депрессию', 'детстве', 'для', 'домой', 'дочки', 'его', 'его', 'его', 'если', 'если', 'если', 'если', 'есть', 'ждал', 'жена', 'жизнью', 'задуматься', 'и', 'и', 'и', 'и', 'и', 'и', 'и', 'и', 'и', 'и', 'и', 'и', 'и', 'им', 'их', 'каждый', 'колька', 'колька', 'колька', 'кольке', 'которых', 'летное', 'летчиком', 'летчиком', 'ли', 'ли', 'ли', 'любит', 'мечта', 'мечте', 'мечту', 'мечту', 'мечту', 'мечты', 'мизеров', 'мизеровым', 'много', 'могу', 'может', 'можешь', 'на', 'навряд', 'над', 'найти', 'нам', 'наслаждаться', 'не', 'не', 'не', 'не', 'не', 'не', 'него', 'неизвестности', 'новую', 'нужно', 'нужно', 'о', 'однако', 'окончания', 'он', 'он', 'он', 'он', 'он', 'осуществил', 'осуществить', 'осуществить', 'от', 'откажешься', 'отчаиваться', 'охватил', 'очень', 'передумал', 'повествует', 'позже', 'полностью', 'после', 'поступил', 'поступить', 'поступить', 'предлагает', 'приехав', 'прикладывать', 'проблемой', 'резко', 'решил', 'решил', 'решил', 'с', 'сбываться', 'сбылась', 'сбыться', 'св', 'своего', 'себя', 'сергей', 'сердце', 'скорее', 'смог', 'сможет', 'сможешь', 'согласиться', 'станет', 'станцию', 'стараться', 'стать', 'стонет', 'страх', 'стремиться', 'суждено', 'считает', 'так', 'то', 'то', 'то', 'то', 'того', 'трудиться', 'у', 'у', 'усилий', 'училище', 'училище', 'училище', 'учиться', 'хотелось', 'хочешь', 'цель', 'часа', 'человек', 'что', 'что', 'что', 'чтобы', 'школы', 'щемящей', 'этой']
```

#### words_into_dict()

Данная функция принимает на входе список слов, на выходе получается словарь
слов без повторений. Ключ словаря это слово, а его значение это
число, показывающее сколько раз это слово встречается в тексте

```python
from TextStatistic import words_into_dict
from TextStatistic import get_words


filename = r"C:\Users\Home_PC\Downloads\TestText.txt"
words = get_words(filename)
wid = words_into_dict(words)
print(wid)
```
```
{'а': 2, 'автор': 2, 'боли': 1, 'боялся': 1, 'будут': 1, 'бы': 2, 'в': 5, 'ведь': 1, 'верить': 1, 'вернуться': 1, 'викторович': 1, 'вкладывать': 1, 'впасть': 1, 'вперед': 1, 'всего': 2, 'всех': 1, 'встретить': 1, 'две': 1, 'депрессию': 1, 'детстве': 1, 'для': 1, 'домой': 1, 'дочки': 1, 'его': 3, 'если': 4, 'есть': 1, 'ждал': 1, 'жена': 1, 'жизнью': 1, 'задуматься': 1, 'и': 13, 'им': 1, 'их': 1, 'каждый': 1, 'колька': 3, 'кольке': 1, 'которых': 1, 'летное': 1, 'летчиком': 2, 'ли': 3, 'любит': 1, 'мечта': 1, 'мечте': 1, 'мечту': 3, 'мечты': 1, 'мизеров': 1, 'мизеровым': 1, 'много': 1, 'могу': 1, 'может': 1, 'можешь': 1, 'на': 1, 'навряд': 1, 'над': 1, 'найти': 1, 'нам': 1, 'наслаждаться': 1, 'не': 6, 'него': 1, 'неизвестности': 1, 'новую': 1, 'нужно': 2, 'о': 1, 'однако': 1, 'окончания': 1, 'он': 5, 'осуществил': 1, 'осуществить': 2, 'от': 1, 'откажешься': 1, 'отчаиваться': 1, 'охватил': 1, 'очень': 1, 'передумал': 1, 'повествует': 1, 'позже': 1, 'полностью': 1, 'после': 1, 'поступил': 1, 'поступить': 2, 'предлагает': 1, 'приехав': 1, 'прикладывать': 1, 'проблемой': 1, 'резко': 1, 'решил': 3, 'с': 1, 'сбываться': 1, 'сбылась': 1, 'сбыться': 1, 'св': 1, 'своего': 1, 'себя': 1, 'сергей': 1, 'сердце': 1, 'скорее': 1, 'смог': 1, 'сможет': 1, 'сможешь': 1, 'согласиться': 1, 'станет': 1, 'станцию': 1, 'стараться': 1, 'стать': 1, 'стонет': 1, 'страх': 1, 'стремиться': 1, 'суждено': 1, 'считает': 1, 'так': 1, 'то': 4, 'того': 1, 'трудиться': 1, 'у': 2, 'усилий': 1, 'училище': 3, 'учиться': 1, 'хотелось': 1, 'хочешь': 1, 'цель': 1, 'часа': 1, 'человек': 1, 'что': 3, 'чтобы': 1, 'школы': 1, 'щемящей': 1, 'этой': 1}
```

#### *Приложение*

Используемый для примера текст

```text
Каждый ли человек может осуществить мечту? Над этой проблемой предлагает задуматься Сергей Викторович Мизеров.
Автор повествует нам о Кольке и его мечте стать летчиком. Колька в детстве решил, что станет летчиком и ждал своего часа. 
После окончания школы, он решил поступить в летное училище. Приехав на станцию, его охватил страх. Скорее всего он боялся 
неизвестности, сможет ли он поступить и учиться в училище. И Колька резко передумал и решил вернуться домой. Позже он так 
и не осуществил мечту и “Сердце его стонет от щемящей боли”. Однако у него есть жена и две дочки, которых он любит, и 
если бы Колька поступил в училище, то навряд ли смог встретить их.
Автор считает, что если хочешь осуществить мечту, то нужно очень стараться, а если откажешься, то можешь впасть в 
депрессию и не сможешь полностью наслаждаться жизнью.
Не могу не согласиться с С.В. Мизеровым, ведь для того чтобы сбылась мечта, нужно прикладывать много усилий, трудиться и
вкладывать всего себя.
Хотелось бы верить, что у всех будут сбываться мечты, а если им не суждено сбыться, то не отчаиваться и стремиться вперед 
и найти новую цель. 
```

## Особенности

Вследствие особенности Python, а именно символа ` \ `, вставляя путь таким каким он есть,
Python выдает ошибку. Это связано с экранированием последовательностей. Для того чтобы
путь передавался корректно необходимо перед строкой с путем ставить модификатор 
`r`, как показано в примерах.
