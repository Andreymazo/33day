import operator
import json
import pprint

import sort


class Vacancy:  # Roditelskii class i zhelatelno abstractnii
    def __init__(self, link, name, description, price):
        self.name = link.json['employer'].get('name')
        self.description = link.json["snippet"].get("responsibility")
    #     __slots__ =
    # def __init__(self, data_json):
    #     self.counter += 1
    #     self.compare = data_json.get(self.counter)  # parametr dlya sravneniya


# class CountMixin:
#     @property
#     def get_count_of_vacancy(self):
#         #Vernut kolichestvo vacansii jn tekushego servisa. Poluchat neobhodimo dinamichesli iz fila
#         pass

class HHVacancy(Vacancy):  # Add counter mixin
    # HH vacancies
    countr = 0

    # vacancies=[]
    # @classmethod
    # def obrabotka_salary(cls, file):
    #     with open(file, 'r', encoding='utf-8') as f:  # Serializacia load i otpravili v sorting
    #         files = json.load(f)
    #
    #         for i in files:
    #             a =i['employer'].get('name')
    #             b = i['area'].get('name')
    #             try:
    #                 c = i['salary'].get('from')
    #             except AttributeError as e:
    #                 c = 0
    #
    #             cls.vacancies.append(HHVacancy(a, b, c))
    #             print(cls.vacancies)
    def __init__(self, data_json, start=0, stop=0, step=1):
        # (super().__init__(data_json))

        self.company_name = data_json['employer'].get('name')  # Ключи в вакансиях

        self.town = data_json['area'].get('name')
        try:
            self.salary = data_json["salary"].get("from")  # Ключи в вакансиях
        except AttributeError as e:
            self.salary = 0
            print(e)
        except TypeError as e:
            self.salary = 0
            print(e)

    def __lt__(self, other):
        try:
            return self.salary < other.salary
        except TypeError as e:
            return self.salary == 0

    def __str__(self):
        HHVacancy.countr += 1
        return f'{HHVacancy.countr}HH: {self.company_name} {self.town} {self.salary}'  #
    def __repr__(self):
        HHVacancy.countr += 1
        return f'{HHVacancy.countr}HH: {self.company_name} {self.town} {self.salary}'

    l = []

    @classmethod
    def filter_sorting(cls, vacancies):#Собирает данные в список кортежей, убирает ошибки, и None, сортирует по зарплате и выводит 5
        global i

        index = 0
        for i in vacancies:
            # print(i)
            if i is not None:
                company_name = i['employer'].get('name')
                try:
                    a = i["salary"].get('from')
                    # a =
                except AttributeError:
                    index += 1

                b = i['area'].get('name')
                try:
                    cls.l.append((company_name, b, a))
                    # a =
                except AttributeError:
                    index += 1

                # try:
                #     cls.l.append(
                #         HHVacancy(a, b))  # i.get("salary") vivodit salary: [{'from': 65000, 'to': 80000, 'currency': 'RUR
                # except AttributeError:
                #     index += 1
            else:
                # except i is None:
                index += 1
        def func(x):  # Убираем None
            if x[2] is not None:
                return x
        clean = [func(x) for x in HHVacancy.l if x[2] is not None]

        def func_1(x):  # Сортировка по 3му элементу кортежа
            return x[2]
        final = sorted(clean, key=func_1)
        # clean_dic={}#sozdadim slovar, контролируем пропажу дублей.Сортировку через словарь не доделал
        # index = 1
        # for i in clean:
        #
        #     clean_dic.update({index:i})
        #     index += 1
        # print(clean_dic)

        # ttt = int(input('Введите номер элемента в кортеже, по кокторому будем сортровать'))
        # final = sort.sortirovka(clean_dic, ttt)#Не успел доделать свою сортировку
        for i in final:
            print(i)  ###Выводим отсортрованное по зарплате
        index = 0  # Выведем 5 вакансий с максимальными зарплатами
        H = []

        print(max(final, key=func_1))
        for i in final:
            if index < 5:
                H.append(max(final, key=func_1))
                final.remove(max(final, key=func_1))  # избавляемся от дубликатов
                index += 1
            final.remove(max(final))
        print(f"Пять компаний с максимальными зарплатами вакансии Повар:  ")
        index = 1
        for i in H:  # Выводим 5 вакансий с максимальными заплатами
            print(f"{index} {i}")  ##################################
            index += 1

        # return cls.l ##Libo return libo print 106 strochka
            # pprint.pprint(cls.l, stream=None, indent=1, width=800)

        # clean = [x for x in cls.l if x is not None]
        # print(clean)

import pprint


# def sorting(vacancies):
#     pass

def get_top(vacancies, top_count):
    # Vozvrashaet top {top_count} zapisey po zarplate (iter, next magic methods)
    pass


class SJVacancy(Vacancy):  # Add counter mixin
    # SJ vacancies
    compare = []
    counter = 0

    def __init__(self, data_json, start=0, stop=0, step=1):  # , compare, start=0.0, stop=0.0, step=1.0
        # super().__init__(data_json)
        self.company_name = data_json['client'].get('title')  # Ключи в вакансиях
        self.salary = data_json.get('payment_from')
        self.salary: float

    def __lt__(self, other):
        # sc = other if isinstance(other, int) else other.seconds  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
        return self.salary < other.salary

    def __str__(self):
        SJVacancy.counter += 1
        return f'{SJVacancy.counter}SJ: {self.company_name} зарплата: {self.salary} руб.мес'

    def __repr__(self):
        return f'{SJVacancy.counter}SJ: {self.company_name} зарплата: {self.salary}'


def get_top(vacancies, top_count):
    # Vozvrashaet top {top_count} zapisey po zarplate (iter, next magic methods)
    pass

if __name__ == '__main__':
    with open('res.json', 'r', encoding='utf-8') as f:  # Serializacia load i otpravili v sorting
        files = json.load(f)




    # def sort_key(e):
    #     return e[2]
   # for i in sorted(HHVacancy.l, key=sort_key):
   #      print(i)