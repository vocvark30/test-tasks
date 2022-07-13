import functools
import locale
import requests


def print_letters_count():
    api = "https://ru.wikipedia.org/w/api.php"

    params = {
        'action': 'query',
        'list': 'categorymembers',
        'cmtitle': 'Категория:Животные_по_алфавиту',
        'format': 'json',
        'cmlimit': 'max'
    }

    letters = {}
    query = True

    response_count = 0
    while query:
        response = requests.get(api, params=params)
        query = response.status_code == 200

        if query:
            response_json = response.json()
            response_count += 1
            print(f'{response_count} : получен ответ на очередной запрос...')
            for item in response_json['query']['categorymembers']:
                str_item = item['title']

                # Увеличиваем счётчик букв в словаре letters
                if ord('А') <= ord(str_item[0]) <= ord('Я') or str_item[0] == 'Ё':
                    letters[str_item[0]] = letters[str_item[0]] + 1 if str_item[0] in letters else 1

            if 'continue' in response_json:  # Если получено ещё не все
                params['cmcontinue'] = response_json['continue']['cmcontinue']
            else:
                query = False

    count = 0
    # Сортировка букв
    for i in sorted(letters.keys(), key=functools.cmp_to_key(locale.strcoll)):
        count += letters[i]
        print(f'{i} : {letters[i]}')
    print(f'Всего: {count}')


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
    print_letters_count()
