import sys
from pathlib import Path
from colorama import init, Fore

# ініціалізуємо colorama для автоскидання кольору після кожного використання
init(autoreset=True)

# функція для друку структури директорії
def print_directory_structure(path, level=0):
    try:
        dir_path = Path(path)  # створюємо об'єкт Path з шляху
        if not dir_path.exists() or not dir_path.is_dir():
            # перевіряємо, чи існує шлях і чи це директорія
            print(Fore.RED + f"Error: '{path}' is not a valid directory.")  # виводимо помилку червоним кольором
            return

        # ітеруємося по елементах у директорії
        for item in dir_path.iterdir():
            indent = '    ' * level  # додаємо відступи для вкладеності
            if item.is_dir():
                # виводимо папки синім кольором
                print(f"{indent}{Fore.BLUE}📂 {item.name}")
                # рекурсивно обходимо піддиректорії
                print_directory_structure(item, level + 1)  
            else:
                # виводимо файли зеленим кольором
                print(f"{indent}{Fore.GREEN}📜 {item.name}")

    except Exception as e:
        # обробляємо інші помилки
        print(Fore.RED + f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        # виводимо інструкцію, якщо скрипт викликано неправильно
        print(Fore.YELLOW + "Usage: python t3.py /path/to/directory")
        return
    
    directory_path = sys.argv[1]  
    print_directory_structure(directory_path)  

if __name__ == "__main__":
    main()
