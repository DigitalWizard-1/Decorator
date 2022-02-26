import requests
import datetime

def decor(log_path):
    def _decor(old_func):
        def new_func(*args, **kwargs):
            date = datetime.datetime.today()
            time = datetime.datetime.now().time()
            log_file = log_path + 'decor.log'
            with open(log_file, 'wt', encoding='utf-8') as file:
                file.write(f'Текущая дата: {date.strftime("%d-%B-%Y")}\n')
                file.write(f'Текущее время: {time.strftime("%H:%M:%S")}\n')
                file.write(f'Вызвана функция: {old_func.__name__}\n')
                file.write(f'С аргументами: {args}, {kwargs}\n')
                # print('путь: ', log_path)
                # print('Сегодня:', date.strftime('%d-%B-%Y'))
                # print('Текущее время: ', time.strftime('%H:%M:%S'))
                # print(f'Вызвана функция: {old_func.__name__}')
                # print('С аргументами: ', *args, **kwargs)
                result = old_func(*args, **kwargs)
                file.write(f'Результат: {result}\n')
                # print('Результат :', result)
                # print()
            return result
        return new_func
    return _decor

@decor(log_path='C:\\temp\\')
def stack_request(name):
    url = 'https://api.stackexchange.com/'+name
    response = requests.get(url)
    temp = response.json()
    return temp

if __name__ == '__main__':
    test = stack_request(
        '/2.3/questions?fromdate=1635724800&todate=1635811200&order=desc&sort=activity&tagged=Python&site=stackoverflow')[
        'items']
    n = 0
    for id in test:
        n += 1
        print(n, id['title'])

