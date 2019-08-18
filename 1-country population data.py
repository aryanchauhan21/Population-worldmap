import json

with open('population_data.json') as fin:
    data = json.load(fin)
    for dic_item in data:
        if dic_item['Year'] == '2010':
            name = dic_item['Country Name']
            population = int(float(dic_item['Value']))
            print('Country name : ' + name + '\nPopulation : ', population,'\n')
