import operator


class Vacancy:  # Roditelskii class i zhelatelno abstractnii
    pass
    # def __init__(self, data_json):
    #     self.company_name = data_json['employer'].get('name')  # Ключи в вакансиях
    #     self.salary = data_json.get('salary')
    # def __str__(self):
    #     SJVacancy.counter += 1
    #     return f'{SJVacancy.counter}SJ: {self.company_name} зарплата: {self.salary} руб.мес'
    # def __repr__(self):
    #
    #     return f'{SJVacancy.counter}SJ: {self.company_name} зарплата: {self.salary}'
    #     __slots__ =
    #
    #     # def __init__(self, name, link, description, price):
    #
    #
    #     def __str__(self):
    #         return f'HH: {self.company_name}, зарплата: {self.salary} руб.мес'
    #
    #     @property#jtgelno ustanavlivaemii atribut classa
    #     def name
    #
    #     def __str__(self):
    #
    # def __init__(self, data_json):
    #     self.counter += 1
    #     self.compare = data_json.get(self.counter)  # parametr dlya sravneniya
    #
    # @classmethod
    # def verify_val(cls, other):
    #     if not isinstance(other, int or str):
    #         raise TypeError('Vvod dolzhen bit celim chislom ili strokoi')
    #     other = int(other)
    #     return other
    #
    # @classmethod
    # def __verify_data(cls, other):
    #     if not isinstance(other, (str, Vacancy)):
    #         raise TypeError("Operand d bit tipa str ili Myint")
    #     return int(other) if isinstance(other, str) else other.compare

    # def __eq__(self, other):  # cls ili self stavit ne znau
    #     sc = self.__verify_data(other)
    #     return self.compare == sc  # Zdes piton sravnivaet i vidaet True ili False
    #
    # def __ne__(self, other):
    #     sc = self.__verify_data(other)
    #     return self.compare != sc
    #
    # def __lt__(self, other):
    #     sc = other if isinstance(other,int) else other.seconds  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
    #     return self.compare < sc
    #
    # def __gt__(self, other):
    #     sc = self.__verify_data(other)  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
    #     return self.compare > sc
    #
    # def __le__(self, other):
    #     sc = self.__verify_data(other)  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
    #     return self.compare <= sc
    #
    # def __ge__(self, other):
    #     sc = self.__verify_data(other)  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
    #     return self.compare >= sc


#
# class CountMixin:
#     @property
#     def get_count_of_vacancy(self):
#         #Vernut kolichestvo vacansii jn tekushego servisa. Poluchat neobhodimo dinamichesli iz fila
#         pass

class HHVacancy(Vacancy):  # Add counter mixin
    # HH vacancies
    counter = 0

    def __init__(self, data_json, start=0, stop=0, step=1):
        # (super().__init__(data_json))
        self.company_name = data_json['employer'].get('name')  # Ключи в вакансиях
        # try:
        #     self.salary = data_json["salary"].get("from")
        # except Exception as e:
        #     print(e)

        self.town = data_json['area'].get('name')
        # if data_json["salary"].get("from") is not None:
        #     self.salary = data_json["salary"].get("from")
        # else:
        #     print('salary is None')

        self.salary = data_json.get('salary')
        self.salary: float
        # self.compare = list(compare)#Sozdali spisok v classe
        # SJVacancy.counter += 1

        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step
        HHVacancy.counter += 1

    # def __str__(self):
    #     return f'HH: {self.company_name}, зарплата: {self.salary} руб.мес'
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __eq__(self, other):  # cls ili self stavit ne znau
        return self.salary == other  # Zdes piton sravnivaet i vidaet True ili False

    def __ne__(self, other):
        return self.salary != other

    def __lt__(self, other):
        # if isinstance(other, float or int):
        #     return self.salary < other.salary
        # print('Операнд справа должен bit chislom')
        # return other.salary == 0
        return self.salary < other.salary

        # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock

    def __gt__(self, other):
        # sc = self.__verify_data(other)  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
        return self.salary > other.salary

    def __le__(self, other):
        # sc = self.__verify_data(other)  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
        return self.salary <= other.salary

    def __ge__(self, other):
        # sc = self.__verify_data(other)  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
        return self.salary >= other.salary

    # def __getitem__(self, item):
    #     return self.compare[item]
    #
    # def __setitem__(self, key, value):
    #     self.compare[key] = value

    def __str__(self):
        HHVacancy.counter += 1
        return f'HH{HHVacancy.counter}: {self.company_name}, {self.town}, {self.salary}'

    def __repr__(self):
        HHVacancy.counter += 1
        return f'HH{HHVacancy.counter}: {self.company_name}, {self.town}, {self.salary}'
        # try:
        #     return f'HH{HHVacancy.counter}: {self.company_name}, {self.town}, {self.salary}'
        # except AttributeError as e:
        #     print(e)






def sorting(vacancies):
    # vacancies_itog = []
    # if Vacancy.compare
    #     for i in vacancies:
    #         for k, v in query.items():
    #             if i[k] == v:
    #                 data_from_file.append(d)
    #     return data_from_file
    # Sortiruem spisok vakansii
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
        # self.compare = list(compare)#Sozdali spisok v classe
        # SJVacancy.counter += 1

        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __eq__(self, other):  # cls ili self stavit ne znau
        return self.salary == other.salary  # Zdes piton sravnivaet i vidaet True ili False

    def __ne__(self, other):
        return self.salary != other.salary

    def __lt__(self, other):
        # sc = other if isinstance(other, int) else other.seconds  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
        return self.salary < other.salary

    def __gt__(self, other):
        # sc = self.__verify_data(other)  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
        return self.salary > other.salary

    def __le__(self, other):
        # sc = self.__verify_data(other)  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
        return self.salary <= other.salary

    def __ge__(self, other):
        # sc = self.__verify_data(other)  # sc vozmet secundu libo iz other esli other int libo iz self.seconds, esli other Clock
        return self.salary >= other.salary

    def __getitem__(self, item):
        return self.compare[item]

    def __setitem__(self, key, value):
        self.compare[key] = value

    def __str__(self):
        SJVacancy.counter += 1
        return f'{SJVacancy.counter}SJ: {self.company_name} зарплата: {self.salary} руб.мес'

    def __repr__(self):

        return f'{SJVacancy.counter}SJ: {self.company_name} зарплата: {self.salary}'


# class Edge:
#     def __init__(self, source, dest, weight=float('inf')):
#         self.source = source
#         self.dest = dest
#         self.weight = weight
#
#     def __repr__(self):
#         return f"Edge: ({self.source}, {self.dest}, {self.weight})"
#
#     def __lt__(self, other):
#         return self.weight < other.weight

def sorting(vacancies):
    SJVacancy.compare.append(vacancies)
    # key = 'payment_from'
    # # for i in vacancies:
    # if vacancies(key):
    #     vacancies_key_ls.append(vacancies.get(key))

    # return vacancies_itog_l
    # print(vacancies_itog_l)
    # <vacancies[index+1].get('payment_from'):

    # if i.get('payment_from') < Vacancy.compare[SJVacancy.counter]
    #     vacancies_itog.append(i)
    #
    #     for k, v in query.items():
    #         if i[k] == v:
    #             data_from_file.append(d)
    # return data_from_file


def get_top(vacancies, top_count):
    # Vozvrashaet top {top_count} zapisey po zarplate (iter, next magic methods)
    pass
