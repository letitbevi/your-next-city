#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Create README.md for each city on GitHub

import os
import glob
import json

class GenREADME(object):
    """Generate README.md for each city"""
    def __init__(self, username, continent, city):
        self.root = 'https://github.com/{}/your-next-city/blob/master'.format(username)      
        self.continent = continent
        self.city = city
        self.u_city = city.replace(' ', '_')

    def create_template(self, file):  
        self.template = file
        ### Start writing README.md
        self.template.write('# {}\n\n'.format(self.city))
        self.template.write('#![{}]({}/{}/{}/{}.png)\n\n'.format(self.u_city, self.root, self.continent, self.u_city, self.u_city))
        self.template.write('Visualize top 20 related news categories from 2007 to 2016\n\n')
        self.template.write('# Data\n\n')
        self.template.write('The [data]({}/{}/{}/data) folder contains 10 JSON files that I scraped from [The Guardian](https://www.theguardian.com/):\n\n'.format(self.root, self.continent, self.city))
        self.template.write('| File Name        | Num of Documents  |  Num of sentences that mentioned `{}` |\n'.format(self.city))
        self.template.write('| ------------- |:-------------:|:-----:|\n')
        self.template.write('{}\n\n'.format(self._count_docs_sents()))
        self.template.write('Trends related to {} from 2007 to 2016\n\n'.format(self.city))
        self.template.write('![2007-2016_{}_Top_20_News_Categories]'.format(self.city))
        self.template.write('({}/{}/{}/fig/2007-2016_{}_Top_20_News_Categories.png)\n\n'.format(self.root, self.continent, self.city, self.city))
        for year in range(2007, 2017):
            self.template.write('![{}_{}_Top_20_News_Categories]'.format(year, self.city))
            self.template.write('({}/{}/{}/fig/{}_{}_Top_20_News_Categories.png)\n\n'.format(self.root, self.continent, self.city, year, self.city))

    def _count_docs_sents(self):
        lines = ''
        total_docs = 0
        total_sents = 0
        paths = glob.glob("{}/{}/data/*.json".format(self.continent, self.city))
        for path in paths:
            with open(path, encoding='utf-8') as f:
                news_one_year = json.load(f)
                total_docs += news_one_year['docs']
                total_sents += news_one_year['sentences']
                lines += '| `{}`  | {} | {} |\n'.format(os.path.basename(path), news_one_year['docs'], news_one_year['sentences'])
        lines += '| `ALL`  | {} | {} |'.format(total_docs, total_sents)
        return lines

if __name__ == '__main__':
    username = 'letitbevi'
    continent = 'Asia'   
    with open('{}/cities.txt'.format(continent)) as f:
        cities = f.read().splitlines()
    for city in cities:
        u_city = city.replace(' ', '_')
        fopen = open('{}/{}/README.md'.format(continent, u_city), 'w')
        readme = GenREADME(username, continent, city)
        readme.create_template(fopen)






