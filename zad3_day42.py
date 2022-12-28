import json


class Bank:
    j = []
    counter = 0

    def __init__(self, file):
        self.date = file.get("date", 0)
        self.description = file.get("description")
        # i['salary'].get('from', 0)
        self.card = file.get('from')
        try:
            self.date_new = self.date[:10].replace('[0-9]', '') if self.date else 0#None type error bez etoi pripiski
        except TypeError as e:
            print(e)

    def __lt__(self, other):
        try:
            return self.date < other.date
        except TypeError as e:
            print(e)

    def __str__(self):
        try:
            Bank.counter += 1
            return "{0} Дата {1} {2} {3}".format(Bank.counter, self.date_new if self.date_new is int or float or str else 0, self.card, self.description)
        except AttributeError as e:
            print(e)
    def __repr__(self):
        Bank.counter += 1
        try:
            Bank.counter += 1
            return "{0} {1} {2} {3}".format(Bank.counter, self.date_new, self.card, self.description)
        except AttributeError as e:
            print(e)

if __name__ == "__main__":
    try:
        with open('operations.json', 'r', encoding='utf-8') as infile:
            result = json.load(infile)
        with open('res_bank', 'w', encoding='utf-8') as outfile:
            result = json.dump(result, outfile, ensure_ascii=False)
        # for i in result:
        #     data_f_clss = Bank(i)
        #     print(i)
        with open('res_bank', 'r', encoding='utf-8') as infile:
            result = json.load(infile)
            # print(result)
            g = 'from'
            for i in result:
                data_f_clss = Bank(i) #Пробрасываем через класс Bank
                Bank.j.append(data_f_clss)
                # print(Bank.j)
                #print(data_f_clss)#Printuet norm
                # for i in Bank.j:
                #     print(i)#5150 Дата 2019-01-05 Счет 46363668439560358409 Перевод со счета на счет
                            #5151 Дата 2019-07-13 Maestro 1308795367077170 Перевод с карты на счет
                            # Dalshe sortiruem po 2 chlenu
                g = sorted(Bank.j)
                for i in g:
                    print(i)#Otsortirovali i printanuli
                print('Here len', len(Bank.j))
                index = 0
                H = []
                for i in g:
                    if index < 5:
                        H.append(max(g))

                        g.remove(max(g))
                        index += 1
                    # l.remove(max(l))
                for i in H:  # Выводим 5 вакансий с максимальными заплатами
                    print(f"Пять последних транзакций:  {i}")##################################

    except FileNotFoundError as e:
        print('Smthing here', e)
