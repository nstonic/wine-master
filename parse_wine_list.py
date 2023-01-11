import pandas


def _get_records(file_name: str) -> dict:
    wine_data = pandas.read_excel(file_name, na_values=None, keep_default_na=False)
    return wine_data.to_dict(orient='index')


def get_wines(wine_table_file_name: str) -> dict[str:list]:
    wine_records = _get_records(wine_table_file_name)
    categories = set(record['Категория'] for record in wine_records.values())
    wines = {category: [] for category in categories}
    for _, wine_record in wine_records.items():
        wine = {
            'title': wine_record['Название'],
            'grape': wine_record['Сорт'],
            'price': wine_record['Цена'],
            'image': wine_record['Картинка'],
            'promo': wine_record['Акция']
        }
        wines[wine_record['Категория']].append(wine)

    return wines
