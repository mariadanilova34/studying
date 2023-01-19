import requests

res_monobank = requests.get('https://api.monobank.ua/bank/currency')
print(res_monobank.status_code)
resp = requests.get('https://api.monobank.ua/bank/currency') # Отримати

match resp.status_code:
    case 200:
        print('All okey, move on')
    case 429:
        print('Try later, more request')
    case _:
        print(resp.status_code)
# print(res_monobank.json()[:5:])

for obj in res_monobank.json():
    print(f'Object is {obj}, \nType is{type(obj)}', end = '\n\n')

my_currencies = {
    980: '🇺🇦',
    840: '🇺🇸',
    978: "🇪🇺",
    # 826: '🇬🇧',
}
print("-"*40)

my_rates = []
for obj in res_monobank.json():
    # print(obj.keys())
    if obj['currencyCodeA'] in my_currencies and obj not in my_rates:
        my_rates.append(obj)

# print(my_rates)

for obj in my_rates:
    # print(obj)
    print(f"Країна: {my_currencies[obj['currencyCodeA']]} Купівля {obj['rateBuy']} Продаж: {obj['rateSell']}")
