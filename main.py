import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from parse_wine_list import get_wine_list
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime


def working_years():
    today = datetime.date.today()

    def make_year_agree_with_number(number: int) -> str:
        if 11 <= number % 100 <= 19:
            return f"{number} лет"
        elif number % 10 in [2, 3, 4]:
            return f"{number} года"
        elif number % 10 == 1:
            return f"{number} год"
        else:
            return f"{number} лет"

    return make_year_agree_with_number(today.year - 1920)


def prepare_page(wine_list_file_name: str):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        years=working_years(),
        wine_list=get_wine_list(wine_list_file_name)
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--wine_list",
        default='wine_list.xlsx',
        help='Имя файла, в котором хранятся данные винной карты. По умолчанию - wine_list.xlsx'
    )
    args = parser.parse_args()
    prepare_page(wine_list_file_name=args.wine_list)
    server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
