products = [
    {'name': 'Pralka SAMSUNG WW90CGC04DAB AI Energy Mode EcoBubble 9kg 1400 obr', 'price': 2699.99},
    {'name': 'Lodówka SAMSUNG AI BRR29703EWW EF', 'price': 3999.00},
    {'name': 'Suszarka SAMSUNG AI DV90CGC2A0AB', 'price': 3699.99},
    {'name': 'Piekarnik SAMSUNG NV7B4345VAK U2 Dual Cook Flex Elektryczny parowy Czarny A+', 'price': 3299.99},
    {'name': 'Telewizor SAMSUNG QE65Q67C 65" QLED 4K Tizen TV', 'price': 3179.00},
    {'name': 'Zmywarka WHIRLPOOL WSIO 3T125 6 PE X', 'price': 1599.00},
    {'name': 'Płyta indukcyjna WHIRLPOOL WL B5860 AL', 'price': 1420.00},
    {'name': 'Kuchenka mikrofalowa SAMSUNG MC28A5135CK', 'price': 999.00}
]

promotion = {
    'products': ['Pralka SAMSUNG WW90CGC04DAB AI Energy Mode EcoBubble 9kg 1400 obr', 'Suszarka SAMSUNG AI DV90CGC2A0AB'],
    'bonus': 299.99
}

def pair_products_with_discount(products, promotion):
    # Sortuj produkty według ceny
    sorted_products = sorted(products, key=lambda x: x['price'])

    # Tworzenie par produktów
    paired_products = [(sorted_products[i], sorted_products[i+1]) for i in range(0, len(sorted_products)-1, 2)]

    # Dodaj 30% zniżki do tańszego produktu w parze
    discounted_pairs = []
    for pair in paired_products:
        bonus = 0
        if set(promotion['products']) == set([pair[0]['name'], pair[1]['name']]):
            bonus = promotion['bonus']
        if pair[0]['price'] > pair[1]['price']:
            discounted_pairs.append((pair[0], {'name': pair[1]['name'], 'price': round(pair[1]['price'] * 0.7, 2), 'original_price': pair[1]['price'], 'bonus': bonus}))
        else:
            discounted_pairs.append(({'name': pair[0]['name'], 'price': round(pair[0]['price'] * 0.7, 2), 'original_price': pair[0]['price'], 'bonus': bonus}, pair[1]))

    return discounted_pairs
    
    
discounted_pairs = pair_products_with_discount(products, promotion)

for pair in discounted_pairs:
    print(f"Zestaw: {pair[0]['name']} + {pair[1]['name']}")
    print(f"Produkt 1: {pair[0]['name']}, Cena: {round(pair[0]['price'], 2)}, Bazowa cena: {round(pair[0].get('original_price', pair[0]['price']), 2)}")
    print(f"Produkt 2: {pair[1]['name']}, Cena: {round(pair[1]['price'], 2)}, Bazowa cena: {round(pair[1].get('original_price', pair[1]['price']), 2)}")
    print(f"Rabat: {round(abs(pair[0]['price'] - pair[1]['price']), 2)}")
    print(f"Cena za zestaw: {round(pair[0]['price'] + pair[1]['price'], 2)}")
    print("-----")