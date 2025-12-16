import sys

def get_stock_price():
    COMPANIES = {
        'sber': 'sbr',
        'yandex': 'ynx',
        'retube': 'rt',
        'Tinkoff': 'tnf',
        'alfa': 'alf'
    }

    STOCKS = {
        'sbr': 287.73,
        'ynx': 173.79,
        'rt': 416.90,
        'tnf': 724.88,
        'alf': 3.37
    }
    
    if len(sys.argv) != 2:
        return  
    
    company_name = sys.argv[1].strip()
    
    found = False
    for company, ticker in COMPANIES.items():
        if company.lower() == company_name.lower():
            print(STOCKS[ticker])
            found = True
            break
    
    if not found:
        print("Unknown company")

if __name__ == '__main__':
    get_stock_price()