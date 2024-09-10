from typing import List, Dict


def filter_by_state(start_list: List[Dict], state_id: str = "EXECUTED") -> List[Dict]:
    """Функция, которая принимает список словарей и опционально значение для ключа state"""
    list = []
    for i in start_list:
        if i["state"] == state_id:
            list.append(i)
            return list


def sort_by_date(start_list: List[Dict], revers: bool = True) -> List[Dict]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки"""
    sorted_list = sorted(start_list, key=lambda x: x["date"], reverse=revers)
    return sorted_list


if __name__ == "__main__":
    start_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    print(filter_by_state(start_list))

    reverse = bool(input())
    print(sort_by_date(start_list, reverse))
