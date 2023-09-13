# DataValidatorML
Данный код представляет класс FileWithData, который предоставляет функциональность для работы с файлами данных с использованием библиотеки Pandas. Код обрабатывает входной файл в формате csv, с разделителем запятая (",").

В файле присутствуют методы для:
- инициализации обработчика файла
- метод для удаления пустых столбцов
- метод для удаления дубликатов столбцов
- метод для сортировки по номеру/номерам столбцов
- метод для сохранения в файл


# Примеры использования

```python
    data = FileWithData('data.csv') # инициализация класса
    print(f'Количество столбцов до обработки: {data.column_count}')
    data.delete_empty_columns()  # удаление пустых столбцов
    print(f'Количество столбцов после удаения пустых столбцов: {data.column_count}')
    data.delete_duplicate_columns() # удаление дубликатов столбцов
    print(f'Количество столбцов после удаения повторяющихся столбцов: {data.column_count}')
    data.sort_by_columns([2, 1]) # сортировка по второму, а затем по первому столбцу
    data.save_to_file('data_result.csv') # сохранение в файл
```

