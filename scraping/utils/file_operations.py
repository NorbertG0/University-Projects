
def save_data(data):
    with open('data.csv', 'a') as file:
        file.write(data)

def data_from_csv():
    with open('data.csv', 'r') as file:
        lines = file.readlines()

        data = []
        for line in lines:
            parts = line.strip().split(';')
            parts = [p for p in parts if p]

            if parts:
                population_amount = parts[5].replace(',', '')
                data.append({
                    'country': parts[0],
                    'year': parts[1],
                    'city': parts[2],
                    'type': parts[3],
                    'ref_year': parts[4],
                    'population': population_amount,
                })

    return data