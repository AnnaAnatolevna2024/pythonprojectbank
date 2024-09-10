# Виджет банковских операций клиента

## Цель проекта

Этот проект разработан для упрощения управления финансами: фильтрации и сортировки транзакций на основе их состояния и
даты выполнения. Он предоставляет функции для работы с списком транзакций, представленным в виде словарей.

## Установить

Чтобы использовать проект, просто скопируйте его репозиторий на свой локальный компьютер или загрузите необходимые файлы
в вашу среду разработки.




## Использование

Для использования функций, находящихся в модуле `processing.py`, просто импортируйте их в своем коде:

from processing import filter_by_state, sort_by_date

### Описание функций

1. **filter_by_state(start_list: List[Dict], state_id: str = "EXECUTED") -> List[Dict]:**
    - Эта функция фильтрует список транзакций по значению ключа `state`.
    - Параметры:
        - `start_list`: Список словарей с транзакциями.
        - `state_id`: Строка, по которой нужно фильтровать транзакции. По умолчанию `'EXECUTED'`.
    - Возвращает новый список словарей, у которых ключ `state` соответствует указанному значению.

2. **sort_by_date(start_list: List[Dict], revers: bool = True) -> List[Dict]:**
    - Эта функция сортирует список транзакций по дате.
    - Параметры:
        - `start_list`: Список словарей с транзакциями.
        - `revers`: Булевое значение, указывающее, по убыванию (по умолчанию `True`) или по возрастанию (если
          `False`).
    - Возвращает новый отсортированный список.

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE). 