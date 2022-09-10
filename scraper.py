# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import pandas as pd
import sqlite3
import json

lang = str

# temp
lang = 'sk'

url = fr'https://www.shmu.sk/{lang}/?page=1&id=ran_sprav'

shmu_waterways_page = pd.read_html(url)

waterways_table = shmu_waterways_page[0]

print(waterways_table)

"""with open('./data.json', 'r+', encoding='utf-8') as f:
    waterways_dict = waterways_table.to_json(
        f, 'index', force_ascii=False, indent=4)"""

data = waterways_table.to_sql('data', sqlite3.Connection)
