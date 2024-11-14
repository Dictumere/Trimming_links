import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, url):
    request_url = 'https://api.vk.ru/method/utils.getShortLink/'
    payload = {
        'access_token': token,
        'v': '5.199',
        'url': url,
        'private': '0'
    }
    response = requests.post(request_url, json=payload, params=payload)
    response.raise_for_status()
    answer = response.json()
    return answer['response']['short_url']


def count_clicks(token, url):
    parsed_url = urlparse(url)
    short_key = parsed_url.path.lstrip('/')
    request_url = 'https://api.vk.ru/method/utils.getLinkStats/'
    payload = {
        'access_token': token,
        'v': '5.199',
        'key': short_key,
        'interval': 'forever'
    }
    response = requests.post(request_url, json=payload, params=payload)
    response.raise_for_status()
    answer = response.json()
    return answer['response']['stats'][0]['views']


def is_shorten_link(token, url):
    parsed_url = urlparse(url)
    short_key = parsed_url.path.lstrip('/')
    request_url = 'https://api.vk.ru/method/utils.getLinkStats/'
    payload = {
        'access_token': token,
        'v': '5.199',
        'key': short_key,
        'interval': 'forever'
    }
    response = requests.post(request_url, json=payload, params=payload)
    response.raise_for_status()
    answer = response.json()
    return 'error' not in answer


def main():
    parser = argparse.ArgumentParser(description='Обработчик ссылок')
    parser.add_argument('url', type=str, help='Введите ссылку')
    url = parser.parse_args().url

    load_dotenv()
    vk_access_token = os.environ['VK_ACCESS_TOKEN']
    try:
        if is_shorten_link(vk_access_token, url):
            clicks = count_clicks(vk_access_token, url)
            print(f'Количество просмотров: {clicks}')
        else:
            short_url = shorten_link(vk_access_token, url)
            print(f'Короткая ссылка: {short_url}')
    except requests.exceptions.HTTPError as error:
        print(f'Проверьте вашу ссылку. Ошибка HTTP: {error}')
    except requests.exceptions.ConnectionError as error:
        print(f'Ошибка соединения: {error}')
    except KeyError:
        print('Ссылка приватная или введена неверно')
    except IndexError:
        print('Количество просмотров: 0')
    except Exception as error:
        print(f'Неизвестная ошибка: {error}')


if __name__ == '__main__':
    main()
