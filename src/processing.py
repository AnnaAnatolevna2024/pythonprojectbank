from typing import Dict, List


def filter_by_state(start_list: List[Dict], state_id: str = "EXECUTED") -> List[Dict]:
    """Функция, которая принимает список словарей и опционально значение для ключа state"""
    list_new = []
    for i in start_list:
        if i["state"] == state_id:
            list_new.append(i)
            return list_new


def sort_by_date(start_list: List[Dict], revers: bool = True) -> List[Dict]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки"""
    sorted_list = sorted(start_list, key=lambda x: x["date"], reverse=revers)
    return sorted_list
