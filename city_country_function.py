def city_country(city, country, population=''):
    if population == '':
        total = city + ' ' + country
    else:
        total = city + ' ' + country + "- population " + str(population)
        
    return total.title()
