from datetime import datetime
from operator import itemgetter
from src.constants import DATA
import json


def _read_json(data):
    with open(data, encoding="utf-8") as f:
        return json.load(f)


def _sorted_by_date():
    data = _read_json(DATA)
    data_new = []
    for item in data:
        if 'date' in item:
            item['date'] = datetime.strptime(item['date'][:10], '%Y-%m-%d').date()
            data_new.append(item)
    sorted_data = sorted(data_new, key=itemgetter('date'), reverse=True)
    executed_transactions = [operation for operation in sorted_data if operation["state"] == "EXECUTED"]
    return executed_transactions


def _hide_digits(requisites):
    requisites_digits = requisites.split(' ')[-1]
    if len(requisites_digits) == 20:
        return f'Счет **{requisites_digits[16:]}'
    else:
        if len(requisites.split(' ')) == 3:
            card_name = ' '.join(requisites.split(' ')[:2])
        else:
            card_name = requisites.split(' ')[0]
        return f'{card_name} {requisites_digits[:4]} {requisites_digits[4:6]}** **** {requisites_digits[12:]}'


def format_last_operations(count_operations):
    data = _sorted_by_date()
    last_operations = []
    data_new = []
    for i in range(count_operations):
        last_operations.append(data[i])
    for item in last_operations:
        if 'from' in item:
            item['from'] = _hide_digits(item['from'])
        item['to'] = _hide_digits(item['to'])
        data_new.append(item)
    return data_new
