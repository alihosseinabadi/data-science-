def transform_to_dictionary():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Iran', '12')
    ]
    
    result_dict = {}
    
    for country, number in list_of_tuples:
        if number in result_dict:
            result_dict[number].append(country)
        else:
            result_dict[number] = [country]
    
    for number, countries in result_dict.items():
        for country in countries:
            print(f"'{number}' : '{country}'")

if __name__ == '__main__':
    transform_to_dictionary()