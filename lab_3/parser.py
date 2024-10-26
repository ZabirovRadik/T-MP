import re
import requests

from fake_headers import Headers

from auxiliary import write_csv


def quotes_parser(csv_file:str = "ria news",
                  folder:str = "data",
                  url: str = "https://ria.ru/world/",
                  headlines:str = ['Название статьи',
                                   'Время',
                                   'Просмотры',
                                   'Тэги']
                  ) -> None:
    """
    Парсит сайт ria.ru/world или другой сайт с похожим html кодом
    и записывает результат в csv файл

    Args:
        csv_file:str
            Название для файла с данными
        folder:str
            Папка для данных
        url: str
            URL сайта для парсинга
        headlines:str
            Названия столбцов данных в csv файле
    
    Return:
        None
    """

    response = requests.get(url, headers= Headers(
                                                browser = "Chrome",
                                                os = "win",
                                                headers = True
                                                ).generate())
    html_content = response.text
    data = []
    pattern = re.compile(
        r'class="list-item__title [\w-]+?">"{0,1}(.*?) (?:"|</a>|<span)' #Заголовок статьи
        r'.+?data-type="date">([\d:]{4,5})'            #Время публикации
        r'.+?(\d+)</span>',                            #Число просмотров
        re.DOTALL
        )
    matches = pattern.findall(html_content)

    pattern_blocks_with_tags = re.compile(
        r'<div class="list-item__tags-list">(.*?)</div>', #Для получения блоков с тегами новостей 
        re.DOTALL
        )
    blocks_with_tags = pattern_blocks_with_tags.findall(html_content)

    pattern_tags = re.compile(
        r'list-tag__text">([ \w]+?)<',  #Для получения тэгов новостей
        re.DOTALL
        )
    for match in matches:
        block = blocks_with_tags.pop(0)
        tags = re.findall(pattern_tags, block)
        data.append([match[0], match[1], match[2], tags])
    write_csv(folder, csv_file, headlines, data)


if __name__ == "__main__":
    quotes_parser()
