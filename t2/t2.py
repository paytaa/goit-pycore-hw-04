# функція для отримання інформації про котів з файлу
def get_cats_info(path):
    cats_info = []  # створюємо порожній список для збереження інформації про котів

    try:
        # відкриваємо файл для читання
        with open(path, 'r') as file:
            for line in file:
                # розбиваємо рядок на id, ім'я та вік
                cat_id, name, age = line.strip().split(',')
                # створюємо словник для кожного кота
                cat_dict = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat_dict)  # додаємо словник у список

        return cats_info  # повертаємо список з інформацією про котів
    except FileNotFoundError:
        # обробляємо випадок, коли файл не знайдено
        print(f"Error: File '{path}' not found.")
        return []  # повертаємо порожній список
    except Exception as e:
        # обробляємо інші помилки
        print(f"An error occurred: {e}")
        return []  # повертаємо порожній список

# основна функція
def main():
    file_path = "B:/Projects/goit-pycore-hw-04/goit-pycore-hw-04/t2/cats.txt"  
    cats_info = get_cats_info(file_path)  # отримуємо інформацію про котів
    
    print(cats_info)  # виводимо інформацію про котів

if __name__ == "__main__":
    main()
