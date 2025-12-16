import sys

def get_company_info():
    COMPANIES = {
        'sber': 'sbr',
        'yandex': 'ynx',
        'tinkoff': 'tnf',
        'alfaa': 'alfaa',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'sbr': 287.73,
        'ynx': 173.79,
        'tnf': 416.90,
        'alfaa': 724.88,
        'NOK': 3.37
    }
    
    # Check number of arguments
    if len(sys.argv) != 2:
        return  # Do nothing if not exactly 1 argument
    
    ticker_symbol = sys.argv[1].strip().lower()  # Convert to uppercase for comparison
    
    # Search for the ticker symbol in STOCKS dictionary
    if ticker_symbol in STOCKS:
        # Find the company name for this ticker
        company_name = None
        for company, ticker in COMPANIES.items():
            if ticker == ticker_symbol:
                company_name = company
                break
        
        if company_name:
            print(f"{company_name} {STOCKS[ticker_symbol]}")
        else:
            print("Unknown ticker")
    else:
        print("Unknown ticker")

if __name__ == '__main__':
    get_company_info()