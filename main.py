import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from parse_wine_table import get_wines
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime


def make_year_agree_with_number(number: int) -> str:
    if 11 <= number % 100 <= 19:
        return f'{number} лет'
    elif number % 10 in [2, 3, 4]:
        return f'{number} года'
    elif number % 10 == 1:
        return f'{number} год'
    else:
        return f'{number} лет'


def count_working_years() -> str:
    today = datetime.date.today()
    start_year = 1920
    return make_year_agree_with_number(today.year - start_year)


def prepare_page(wine_table_file_name: str):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        years=count_working_years(),
        wine_table=get_wines(wine_table_file_name)
    )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--wine_table',
        default='wine_table.xlsx',
        help='Имя файла, в котором хранятся данные винной карты. По умолчанию - wine_table.xlsx'
    )
    args = parser.parse_args()
    prepare_page(wine_table_file_name=args.wine_table)
    server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
