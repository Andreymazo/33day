import operator
import json


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


import pprint


def sorting(vacancies):
    pass


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
