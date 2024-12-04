async def filter_products(products, filters):
    filtered_products = []
    for product in products:
        satisfies_all_conditions = True

        if 'priceRange' in filters:
            min_price = filters['priceRange'].get('min')
            max_price = filters['priceRange'].get('max')
            if min_price is not None and max_price is not None:
                if not (min_price <= product['Стоимость'] <= max_price):
                    satisfies_all_conditions = False

        if 'reviewsRange' in filters:
            min_reviews = filters['reviewsRange'].get('min')
            max_reviews = filters['reviewsRange'].get('max')
            if product.get('Количество отзывов') == "Нету":
                continue
            else:
                if min_reviews is not None and max_reviews is not None:
                        if not (min_reviews <= product['Количество отзывов'] <= max_reviews):
                                satisfies_all_conditions = False

        if 'ratingRange' in filters:
            min_rating = filters['ratingRange'].get('min')
            max_rating = filters['ratingRange'].get('max')
            if product.get('Средняя оценка') == "Нету":
                continue
            else:
                if min_rating is not None and max_rating is not None:
                        if not (min_rating <= product['Средняя оценка'] <= max_rating):
                                satisfies_all_conditions = False

        if 'textInput' in filters:
            search_tovar = filters['textInput'].split()
            if not all(word.lower() in product["Описание"].lower() for word in search_tovar):
                satisfies_all_conditions = False

        if satisfies_all_conditions:
            filtered_products.append(product)

    return filtered_products