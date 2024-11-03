# створення файлу із заробітною платою
def create_salary_file(path):
    salary_data = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000"""

    with open(path, 'w', encoding='utf-8') as file:
        file.write(salary_data)  # записуємо дані у файл
    print(f"File '{path}' created successfully.")  # повідомляємо про успіх

# обчислення загальної та середньої зарплати
def total_salary(path):
    try:
        total_salary = 0  # ініціалізуємо загальну зарплату
        count = 0  # лічильник кількості записів

        # відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')  # розділяємо ім'я та зарплату
                total_salary += int(salary)  # додаємо зарплату до загальної
                count += 1  # збільшуємо лічильник

        # обчислюємо середню зарплату
        average_salary = total_salary / count if count > 0 else 0
        return total_salary, average_salary
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")  # обробляємо відсутність файлу
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")  # обробляємо інші помилки
        return None, None

# основна функція
def main():
    file_path = "salaries.txt"  # шлях до файлу
    create_salary_file(file_path)  # створюємо файл
    total, average = total_salary(file_path)  # обчислюємо загальну та середню зарплату

    if total is not None and average is not None:
        # виводимо результати
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()
