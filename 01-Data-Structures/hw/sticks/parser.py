import os


def parser(string: str) -> list:
    """ function parse data string to list of dates """
    data = []
    string = string.replace('[{"', '')
    string = string.replace('"}]', '')
    for raw_line in string.split('}, {"'):
        data.append(dict(part.split('": ') for part in raw_line.split(', "')))
        for elem in data[-1]:
            data[-1][elem] = data[-1][elem].replace('"', '')
            if (elem == 'price' and data[-1][elem] == 'null'):
                data[-1][elem] = '0'
    return data


def dumper(data_list: list, i=1) -> str:
    """ create new json string for file """
    curr_strings = []
    for obj in data_list:
        curr_strings.append(',\n'.join(['\t ' *i + '"' + str(key) + '": "'
                                        + str(obj[key]) + '"' for key in obj]))
    return '{\n' + '\n },\n {\n'.join(curr_strings) + '\n' +'\t' * i + ' }\n'


data = []
file_names = 'winedata_1.json', 'winedata_2.json'
for name in file_names:
    with open(os.path.join('.','files', name)) as file:
        data.extend(parser(file.read()))

# delete dublicate and sorting
data = [dict(part) for part in set(tuple(dc.items()) for dc in data)]
data = sorted(sorted(data, key=lambda i: i['variety']),
              key=lambda i: int(i['price']), reverse=True)

# create new file
with open(os.path.join('.','files', 'winedata_full.json'), 'w') as file:
    file.write(dumper(data))

# find info for wine
varieties = ['Gew\\u00fcrztraminer', 'Riesling', 'Merlot',
             'Madera', 'Tempranillo', 'Red Blend']
info = ['average_price', 'min_price', 'max_price',
        'most_common_region', 'most_common_country', 'average_score']
result = {wine: {elem: '0' for elem in info} for wine in varieties}

for var_wine in varieties:
    wines_by_var = [wine for wine in data if wine['variety'] == var_wine]
    if len(wines_by_var):
        # 1 average price
        wine_prices = [int(wine['price']) for wine in wines_by_var
                       if int(wine['price']) > 0]
        result[var_wine]['average_price'] = sum(wine_prices) / len(wines_by_var)

        # 2 min price
        result[var_wine]['min_price'] = min([i for i in wine_prices if i > 0])

        # 3 max price
        result[var_wine]['max_price'] = max(wine_prices)

        # 4 most common_region
        regions = {}
        country = {}
        for wine in wines_by_var:
            region_1 = wine['region_1']
            region_2 = wine['region_2']
            if region_1 in regions:
                regions[region_1] += 1
            elif region_1 != 'null':
                regions[region_1] = 1
            if region_2 in regions:
                regions[region_2] += 1
            elif region_2 != 'null':
                regions[region_2] = 1
                # 5 most common_country
            if wine['country'] in country:
                country[wine['country']] += 1
            else:
                country[wine['country']] = 1
        result[var_wine]['most_common_region'] = max(regions.items(),
                                                     key=lambda i: i[1])[0]
        result[var_wine]['most_common_country'] = max(country.items(),
                                                      key=lambda i: i[1])[0]
        # 6 average score
        wine_score = [int(wine['points']) for wine in wines_by_var]
        result[var_wine]['average_score'] = sum(wine_score) / len(wine_score)

# find result
total_stats = {'most_expensive_wine': '', 'cheapest_wine': '',
               'highest_score': '', 'lowest_score': '',
               'most_expensive_country': '', 'cheapest_country': '',
               'most_rated_country': '', 'underrated_country': '',
               'most_active_commentator': ''}

# cheapest wine
min_price, i = 0, -1
while not min_price:
    if int(data[i]['price']):
        min_price = data[i]['price']
        break
    else:
        i -= 1

max_score, min_score = 0, 100
country_stat = {}
commentators = {}
for wine in data:
    # highest and lowest score
    if int(wine['points']) > max_score:
        max_score = int(wine['points'])
    if int(wine['points']) < min_score:
        min_score = int(wine['points'])
    # expensive and cheapest country, most and underrated_country
    country = wine['country']
    if country in country_stat:
        if wine['price']:
            country_stat[country][0] += int(wine['price'])
            country_stat[country][1] += 1
        country_stat[country][2] += int(wine['points'])
        country_stat[country][3] += 1
    else:
        country_stat[country] = [0, 1, 0, 1]
    # most active commentator
    if wine['taster_name'] in commentators:
        commentators[wine['taster_name']] += 1
    elif wine['taster_name'] != 'null':
        commentators[wine['taster_name']] = 1

# statistic calculations
total_stats['most_expensive_wine'] = [wine['title'] for wine in data
                                      if wine['price'] == data[0]['price']]
total_stats['cheapest_wine'] = [wine['title'] for wine in data
                                if wine['price'] == min_price][:10]
total_stats['highest_score'] = [wine['title'] for wine in data
                                if wine['points'] == str(max_score)]
total_stats['lowest_score'] = [wine['title'] for wine in data
                               if wine['points'] == str(min_score)][:10]
total_stats['most_expensive_country'] = max(country_stat.items(),
                                            key=lambda i: i[1][0] / i[1][1])[0]
total_stats['cheapest_country'] = min(country_stat.items(),
                                      key=lambda i: i[1][0] / i[1][1])[0]
total_stats['most_rated_country'] = max(country_stat.items(),
                                        key=lambda i: i[1][2] / i[1][3])[0]
total_stats['underrated_country'] = min(country_stat.items(),
                                        key=lambda i: i[1][2] / i[1][3])[0]
total_stats['most_active_commentator'] = max(commentators.items(),
                                             key=lambda i: i[1])[0]

# record new statistic
with open('.\\files\\stats.json', 'w') as file:
    file.write('{"statistic": {\n\t"wine": {\n')
    for wine in result:
        file.write('\t\t"' + wine + '": ')
        file.write(dumper([result[wine]], i=3))
    file.write('\n\t},\n')
    string = []
    for stats in total_stats:
        if type(total_stats[stats]) is list:
            string.append('\t"' + stats + '": ["' +
                          '", "'.join(total_stats[stats]) + '"]')
        else:
            string.append('\t"' + stats + '": "' +
                          total_stats[stats] + '"')
    file.write(',\n'.join(string))
    file.write('\n\t}\n}')

# record new markdown
with open('.\\files\\markdown_file.txt', 'w') as file:
    file.write('Statistics on selected varieties\n\n')
    for wine in result:
        file.write(wine + '\n')
        for stat in info:
            file.write('{0:25} ==> {1:1} \n'.format(stat, result[wine][stat]))
        file.write('-' * 30 + '\n')

    file.write('Statistics by wines\n\n')
    for stat in total_stats:
        file.write('{0:25} ==> {1:1} \n'.format(stat, str(total_stats[stat])))
    file.write('-' * 30 + '\n')
