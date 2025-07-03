from library.api.api_connection import get_data

def get_dishes():
    response = get_data()
    results = response.json()
    dishes_names = []
    dishes_images = []
    for dish in results['results']:
        dishes_names.append(dish['title'])
        dishes_images.append(dish['image'])

    return dishes_names, dishes_images