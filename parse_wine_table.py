import pandas


def get_wines(wine_table_file_name: str) -> dict[str:list]:
    wine_table = pandas.read_excel(wine_table_file_name, na_values=None, keep_default_na=False)
    wine_records = wine_table.to_dict(orient='index')
    categories = wine_table['Категория'].unique()
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


if __name__ == '__main__':
    get_wines("wine_table.xlsx")
