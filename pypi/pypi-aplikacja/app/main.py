import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from library.api.data_parser import get_dishes

# Pobieramy dane
dishes_names = get_dishes()[0]
dishes_images = get_dishes()[1]

dishes = list(zip(dishes_names, dishes_images))
current_index = 0

def show_dish(index):
    global photo

    name = dishes[index][0]
    image_url = dishes[index][1]

    try:
        response = requests.get(image_url)
        image_data = BytesIO(response.content)
        image = Image.open(image_data).resize((300, 200))
        photo = ImageTk.PhotoImage(image)

        label_image.config(image=photo)
        label_name.config(text=name)
    except Exception as e:
        label_name.config(text=f"Błąd ładowania: {e}")
        label_image.config(image='')

def next_dish():
    global current_index
    current_index = (current_index + 1) % len(dishes)
    show_dish(current_index)

root = tk.Tk()
root.title("Przeglądarka potraw")

label_image = tk.Label(root)
label_image.pack(pady=10)

label_name = tk.Label(root, font=("Arial", 16))
label_name.pack()

next_button = tk.Button(root, text="Następne", command=next_dish)
next_button.pack(pady=10)

show_dish(current_index)

root.mainloop()
