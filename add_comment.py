import os


def add_comments_to_file():
    # Получаем комментарий от пользователя
    comment = input("Введите комментарий для добавления: ")

    # Формируем строку для добавления
    comment_text = f" comment={comment}"

    # Путь к файлу
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "domain-ip-resolve.txt")

    # Проверяем существование файла
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл {file_path} не найден")
        return

    # Читаем и изменяем файл
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                line = line.rstrip()
                if line:
                    file.write(line + comment_text + '\n')
                else:
                    file.write('\n')

        print("Комментарий успешно добавлен ко всем строкам файла")

    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")


if __name__ == "__main__":
    add_comments_to_file()
