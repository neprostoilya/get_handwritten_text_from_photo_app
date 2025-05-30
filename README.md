# Get Handwritten Text From Photo

Приложение для обработки фотографий с рукописным текстом и преобразования их в четкий черно-белый вид.

## Возможности

- Выбор нескольких изображений (поддерживаются форматы PNG, JPG, JPEG, BMP)
- Автоматическая обработка изображений:
  - Увеличение контраста 
  - Размытие
  - Адаптивная бинаризация
  - Морфологические операции
- Сохранение результатов с высоким DPI (300 точек на дюйм)
- Выбор папки для сохранения обработанных файлов

## Установка

1. Убедитесь, что у вас установлен Python 3.8 или новее
2. Установите зависимости:
   ```bash:builder.spec
   pip install -r requirements.txt
   ```

## Сборка приложения

Для создания исполняемого файла:

1. Установите PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Выполните сборку:
   ```bash
   pyinstaller --onefile --windowed builder.spec
   ```
3. Готовый исполняемый файл будет находиться в папке `dist`

## Использование

1. Запустите приложение
2. Нажмите "Select Images" для выбора фотографий
3. Нажмите "Select Output Folder" для выбора папки сохранения
4. Нажмите зеленую кнопку "Convert" для обработки
5. Обработанные файлы будут сохранены с префиксом "processed_"

## Системные требования

- Windows 10/11
- 4 ГБ оперативной памяти
- 100 МБ свободного места на диске

## Скачать

[⬇️ Скачать .rar файл](https://github.com/neprostoilya/get_handwritten_text_from_photo_app/blob/main/app.rar)

## Лицензия

MIT License