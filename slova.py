import random
def rand_ch():
    dicc = [{
        "word": "питон",
         "subwords":  [
             "пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт"
         ]},
        {
        "word": "набор",
        "subwords":  [
              "бар", "бон", "бор", "раб", "бра", "боа", "нора", "роба", "барон"
         ]},
        {
        "word": "строка",
        "subwords": [
             "акр", "акт", "кот", "рак", "орк", "оса", "сок", "ток", "тор", "кора",
             "коса", "сота", "торс", "роса", "скат"
         ]},
        {
        "word": "маркер",
        "subwords": [
            "акр", "мак", "рак",
            "каре", "крем", "мрак", "река",
            "мерка"

        ]},
        {"word": "паравоз",
        "subwords": [
        "ара", "ров", "вар", "пар", "воз",
        "ваза", "взор", "пара", "поза", "пора", "роза",
        "вапор", "запор", "повар", "право", "проза",
        "оправа"
        ]
    }]
    key_lst = []
    value_lst = []
    for i in range(len(dicc)):
        key_lst.append(dicc[i].get('word'))
    # print((key_lst))
    word = random.choice(key_lst)
    for i in range(len(dicc)):
        if dicc[i].get('word') == word:
            value_lst = dicc[i].get('subwords')
    return word, value_lst

word, value_lst = w1 = rand_ch()


if __name__ == "__main__":

    vvod = str(input(f'Введите слова от слова {word} или стоп, чтобы прервать'))
    val = value_lst
    print(len(val))
    while len(val) > 1 or vvod == "стоп":
        if vvod not in val:
            print(f'Такого слова нет подсказка: {value_lst}')
        val.remove(vvod)

        vvod = str(input(f'Введите слова от слова {word} или стоп, чтобы прервать'))
        print(value_lst, len(value_lst))
        if len(val) == 1:
            print('Finish')
