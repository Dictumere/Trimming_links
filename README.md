# Обрезка ссылок с помощью Битли

Этот скрипт представляет собой утилиту для работы с длинными и короткими ссылками через API ВКонтакте. Программа позволяет сокращать длинные ссылки и получать статистику по кликам для уже сокращенных ссылок.

### Основные функции:

1. **Сокращение ссылок** — Программа принимает длинный URL и сокращает его с помощью API ВКонтакте, возвращая ссылку в формате ```https://vk.cc/{short_key}```.
2. **Отслеживание кликов по сокращенной ссылке** — Если пользователь вводит сокращенный URL, программа получает статистику по кликам на эту ссылку, позволяя увидеть количество переходов.   

### Как установить
1. Создайте виртуальное окружение:
```bash
python3 -m venv .venv
```
2. Активируйте виртуальное окружение:
```bash
source .venv/bin/activate
```
3. Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```bash
pip install -r requirements.txt
```

### Запуск

Для запуска потребуется [токен доступа](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/tokens/service-token) к API ВКонтакте.   

1. Создайте файл ```.env``` в корне проекта и добавьте токен:   
```python
VK_ACCESS_TOKEN=ваш_токен_доступа
```
2. Для запуска программы выполните команду:
```wsl
python3 main.py [Ваша ссылка]
```
### Взаимодействие с программой   
При запуске программа предложит ввести ссылку. В зависимости от формата ссылки, она либо:   
- Cокращает длинный URL, если ссылка не была сокращенной ранее, и выводит сокращенную ссылку;
- Выводит количество кликов, если ссылка сокращенная.

### Пример использования
1. Ввод длинной ссылки:
```bash
python3 main.py https://example.com
```
Результат:
```bash
Короткая ссылка: https://vk.cc/dfcF3j
```
2. Ввод сокращенной ссылки:
```bash
python3 main.py vk.cc/dfcF3j
```
Результат:
```bash
Количество просмотров: 1
```

### Цель проекта:
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.

