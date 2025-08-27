import os
import re

file = 'daty.csv'

months = {
    '01': ('Styczen', 31),
    '02': ('Luty', 28),
    '03': ('Marzec', 31),
    '04': ('Kwiecien', 30),
    '05': ('Maj', 31),
    '06': ('Czerwiec', 30),
    '07': ('Lipiec', 31),
    '08': ('Sierpien', 31),
    '09': ('Wrzesien', 30),
    '10': ('Pazdziernik', 31),
    '11': ('Listopad', 30),
    '12': ('Grudzien', 31)
}


def date(x):
    yy, dd, mm = x.group(1), x.group(2), x.group(3)
    day = int(dd)
    yyyy = int('20' + yy) if int(yy) <= 50 else int('19' + yy)

    if mm in months:
        month_name, max_days = months[mm]
        yyyy = int(yyyy)

        if mm == '02':
            if (yyyy % 4 == 0):
                max_days = 29
            else:
                max_days = 28

        if 1 <= day <= max_days:
            return f'{day} {month_name} {yyyy}'
        else:
            print(f"Błąd: Niepoprawna data {x.group(0)} (za dużo dni w miesiącu {month_name} w roku {yyyy})")
            return x.group(0)
    else:
        print(f"Błąd: Nieznany miesiąc w dacie {x.group(0)}")
        return x.group(0)

if os.path.isfile(file):
    with open(file, 'r') as f:
        for line in f:
            fields = line.strip().split(',')
            for i in range(len(fields)):
                if i != 2:
                    fields[i] = re.sub(r'\b(\d{2})/(\d{2})/(\d{2})\b', date, fields[i])
            print(','.join(fields))
else:
    print('Wybrany plik nie istnieje')
