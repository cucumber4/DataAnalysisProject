base_URL = 'https://market.forte.kz/categories/shiny-1113?page='

fortebank_market_links = []

for link in range(1, 108):
    fortebank_market_links.append(base_URL+str(link))
    print(base_URL+str(link))

