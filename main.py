import json

import requests
from abc import ABC, abstractmethod
from Class import HHVacancy
from Class import SJVacancy
from Class import sorting

class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):#Vozvrashaet ekzempliar classsa
        pass


class HH(Engine):
    __url = 'http://api.hh.ru'
    __per_page = 20

    def get_vacancies(self, search_word, page):#area_id Sain-Petersburg = 2
        print(f'Try to get page {page}')
        response = requests.get(f'{self.__url}/vacancies?text={search_word}&area=2&page={page}')
        if response.status_code ==200:
            return response.json()
        return None

    def get_request(self, search_word, vacancies_count):#
        page = 0
        result = []
        while self.__per_page * page <= vacancies_count:
            tmp_result = self.get_vacancies(search_word, page)
            if tmp_result:#Eto proverka na 'found' Esli budet ne 200 videm iz funkcii s result
                result += tmp_result.get('items')
                page += 1
            else:
                break
        return result


class SuperJob(Engine):
    __url = 'https://api.superjob.ru/2.0'
    __secret ='v3.r.137222938.adcc1bf5602cc5a2c697d63eb9c580dd5029f96f.049aae965267ebe71bbc7c587187da62cdbc560e'
    __per_page = 20

    def _send_request(self, search_word, page):
        #url = f'{self.__url}/vacancies/?page={page}&keyword={search_word}'
        headers = {
            'X-Api-App-Id': self.__secret,
            'Content-Type': 'application / x - www - form - urlencoded'
        }
        # tt = 'Санкт-Петербург'    &town={tt} mozhno piter vstavit
        response = requests.get(url=f'{self.__url}/vacancies?keyword={search_word}&page={page}', headers=headers)
        if response.status_code == 200:
            print(f'Try to get page {page}')
            return response.json()#, print(response.status_code)#, print(response.status_code)Esli printim, to obvalivaetsya str81 result += tmp_result.get('objects')
#AttributeError: 'tuple' object has no attribute 'get' Hotya net vivel 200)
        return None


    def get_request(self, search_word, vacancies_count):#,
        page = 0
        result = []
        while self.__per_page * page <= vacancies_count:
            tmp_result = self._send_request(search_word, page)
            if tmp_result:  # Eto proverka na 'found' Esli budet ne 200 videm iz funkcii s result
                result += tmp_result.get('objects')
                page += 1
            else:
                break
        return result


#         response = requests.get(url=url, headers=headers)
#         print(response)
#         return self.get_vacancies('items'), result.get('found'), result('per_page'), result.get('page')

if __name__ == '__main__':
    vvod = int(input('Выбирите SuperJob 1 или HH 2'))
    l=[]
    if vvod == 1:
        sj_engine = SuperJob()
        search_word = 'повар'
        vacancies_count = 100
        result = sj_engine.get_request(search_word, vacancies_count)
        with open('ressj.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False)#Dannie decodirovat nado
        # vacancies_itog_l=[]
        # vacancies_itog_d={}

        for i in result:
            # print(result)
             # print(f"{i['client'].get('title'), i['catalogues'][0]['title']}, {i['town'].get('title')}")#,{i.get('positions')}
        #
            vac_tec = SJVacancy(i)#Podaem i vacacii v class SJVacancy, poluchaem otfilrtrovanii spisok c counterom
            # sorting(vac_tec)   # Vizivaemfunc sortirovki, podaem tuda nashi dannie vac_tec
            # vacancies_itog_l.append(vac_tec)
            #print(vacancies_itog_l)
            # print(vac_tec)
            l.append(vac_tec)
        print('Vivodim otsortirovannii spisok po zarplate')
        l = sorted(l)#120SJ:    Партнеры Красноярск, 120000
                     #120SJ: Партнеры Красноярск, 120000
        for i in l:
            print(i) #Обратно список в строку если надо print("\n".join(l))
            #### Naiti 10 s maksimalnoi zarplatoi
        # print(max(l))#120SJ: Азбука вкуса, 130000
        index = 0
        H = []
        for i in l:
            if index < 5 and max(l) not in H:
                H.append(max(l))

                l.remove(max(l))
                index+=1
            l.remove(max(l))
        for i in H:#Выводим 5 вакансий с максимальными заплатами
            print(f"Пять компаний с максимальными зарплатами вакансии Повар:  {i}")

    if vvod == 2:
        # item_to_add = 'items'
        hh_engine = HH()
        search_word = 'повар'
        vacancies_count = 100
        result = hh_engine.get_request(search_word, vacancies_count)  # 'found': 5673, 'pages': 100, 'per_page': 20, 'page': 0, 'clusters': None, 'arguments': None, 'alternate_url': 'https://hh.ru/search/vacancy?enable_snippets=true&text=java'}
        with open('res.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False)  # Dannie decodirovat nado
            index = 0
            for i in result:
                vac_tec = HHVacancy(i)
                print(f"{index} {i['employer'].get('name')}, {i['area'].get('name')}, {i['salary'].get('from')}")
                index +=1
                # l.append(vac_tec)
                # print(l)
                # try:#Oshibkaa bila Attribute error
                #
                #
                #     #print(f"{i.get('name')},{i['salary'].get('from')}, {i['area'].get('name')}")
                #     l.append(vac_tec)
                #     print(l)
                # except Exception as e:
                #     pass
                #     continue# print(e)

        # print('Vivodim otsortirovannii spisok po zarplate')
        # print(l)
        # from operator import itemgetter
        # l = sorted(l, key=itemgetter('from'))

                # for i in l:
                #     print(i)

            # for i in result:

        # index = 0  # Выводим 5 вакансий с максимальными заплатами
        # H = []
        # for i in l:
        #     if index < 5 and max(l) not in H:
        #         H.append(max(l))
        #
        #         l.remove(max(l))
        #         index += 1
        #     l.remove(max(l))
        # print(len(H))

            # for i in H:  # Выводим 5 вакансий с максимальными заплатами
            #     print(f"Пять компаний с максимальными зарплатами вакансии Повар:  {i}")




            # for i in result:
            #     vac_tec = HHVacancy(i)
            #     print(vac_tec)
    # else:
    #     print('Nabrali nepravilno')

############################################
    # hh_engine = HH()
    # search_word = 'kotlin'
    # vacancies_count = 100
    # result = hh_engine.get_request(search_word, vacancies_count)#'found': 5673, 'pages': 100, 'per_page': 20, 'page': 0, 'clusters': None, 'arguments': None, 'alternate_url': 'https://hh.ru/search/vacancy?enable_snippets=true&text=java'}
    # with open('res.json', 'w', encoding='utf-8') as f:
    #     json.dump(result, f)#Dannie decodirovat nado
    #         #print(result)
    # with open('res.json', 'r', encoding='utf-8') as f:
    #     res = json.load(f)
    #     for i in res:
    #         print(f"{i.get('name')},{i.get('salary')}, {i['area'].get('name')}")



# par = {'per_page': '10', 'page':i}
# requests.get(self.url, params=par)
# import requests
# # url = "https://api.hh.ru/vacancies?text=python&page=0&per_page=1"
# url = 'https://api.hh.ru/areas/countries'
# response = requests.request("GET", url, headers={})
# print(response.text)

#
# url = ""
#
# payload={}
# headers = {
#   'X-Api-App-Id': 'YOU_TOKEN'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)