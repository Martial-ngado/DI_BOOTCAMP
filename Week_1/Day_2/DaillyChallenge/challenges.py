#Daily Challenge - 1


word = input('Enter a word: ')
positions = {}
for index, char in enumerate(word):
    if char in positions:
        positions[char].append(index)
    else:
        positions[char] = [index]
print(positions)

#Daily Challenge - 2

def clean_price(price_str):
    return int(price_str.replace('$', '').replace(',', ''))


def get_affordable_items(items_purchase, wallet):
    wallet_amount = clean_price(wallet)
    basket = []

    for item, price_str in items_purchase.items():
        price = clean_price(price_str)
        if price <= wallet_amount:
            basket.append(item)
            wallet_amount -= price

    return "Nothing" if not basket else sorted(basket)


if __name__ == "__main__":
    items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
    wallet = "$300"
    print(get_affordable_items(items_purchase, wallet))




