import sys

def process_stock_queries():
    COMPANIES = {
        'sber': 'SBR',
        'tinkoff': 'TNF',
        'yandex': 'YNX',
        'vtb': 'VTB',
        'avtar': 'AVT'
    }
    
    STOCKS = {
        'SBR': 287.73,
        'TNF': 173.79,
        'YNX': 416.90,
        'VTB': 724.88,
        'AVT': 3.37
    }
    
    if len(sys.argv) != 2:
        return
    
    input_string = sys.argv[1].strip()
    
    if ',,' in input_string or input_string.endswith(',') or input_string.startswith(','):
        return
    
    TICKER_TO_COMPANY = {}
    for company, ticker in COMPANIES.items():
        TICKER_TO_COMPANY[ticker] = company
    
    COMPANIES_LOWER = {}
    for company in COMPANIES.keys():
        COMPANIES_LOWER[company.lower()] = company
    
    expressions = input_string.split(',')
    for expr in expressions:
        expr = expr.strip()
        if not expr:
            continue
            
        expr_upper = expr.upper()
        expr_lower = expr.lower()
        found = False
        
        if expr_upper in TICKER_TO_COMPANY:
            company_name = TICKER_TO_COMPANY[expr_upper] or TICKER_TO_COMPANY[expr_lower]
            print(f"{expr_upper} is a ticker symbol for {company_name}")
            found = True
        
        elif expr_lower in COMPANIES_LOWER:
            proper_name = COMPANIES_LOWER[expr_lower]
            ticker = COMPANIES[proper_name]
            price = STOCKS[ticker]
            print(f"{proper_name} stock price is {price}")
            found = True
        
        if not found:
            print(f"{expr} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    process_stock_queries()