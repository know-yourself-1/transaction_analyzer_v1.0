import csv
from collections import defaultdict

"""
Скрипт для анализа Транзакций из CSV файла
"""

def analyze_transactions(csv_file):
	"""
    Анализирует транзакции из CSV файла.
    Возвращает словарь c общей суммой доходов, расходов и группировкой по категориям.
    
    Параметры:
        csv_file (str): Путь к CSV файлу c транзакциями
        
    Возвращает:
        dict: Словарь c результатами анализа или None при ошибке
    """

	total_income = 0.0
	total_expense = 0.0
	categories = defaultdict(float)

	try:
		with open(csv_file, mode ='r', encoding = 'utf-8') as file: # Открываем CSV файл в режиме чтения с UTF-8 кодировкой
			reader = csv.DictReader(file) # Создаем DictReader для чтения CSV как словарей

			# Проверка наличия обязательных колонок в CSV
			required_columns = {'amount', 'category', 'type'} # Множество обязательных колонок
			if not required_columns.issubset(reader.fieldnames): # Если каких то колонок нет - определяем каких именно
				missing = required_columns - set(reader.fieldnames)
				raise ValueError(f'В CSV отсутствуют необходимые колонки: {missing}')
			
			# Обрабатываем каждую строку CSV файла
			for row in reader:
				try:
					amount = float(row['amount']) # Преобразуем сумму в число с плавающей точкой
					category = row['category'] # Получаем категорию транзацкии
					transaction_type = row['type'].lower() # Получаем тип транзакции и переводим к нижнему регустру

					# Суммируем значения  в зависимости от типа транзакции
					if transaction_type == 'income':
						total_income += amount
					elif transaction_type == 'expense':
						total_expense += amount

					# Добавляем сумму к соответствующей категории
					categories[category] += amount

				# Обработка ошибок преобразования числа или отсутствия ключа
				except (ValueError, KeyError) as e: 
					print(f'Ошибка в обработке строки: {row}. Ошибка: {e}')
					continue

	# Обработка случая, когда файл не найден
	except FileNotFoundError: 
		print(f'Файл {csv_file} не найден.')
		return None
	# Обработка всех прочих ошибок.
	except Exception as e: 
		print(f'Произошла ошибка: {e}')
		return None
	
	# Возвращаем результаты в виде словаря
	return {
		'total_income': total_income,
		'total_expense': total_expense,
		'categories': dict(categories) # Преобразуем defaultdict в обычный dict
	}

def print_result(analysis):
	"""
	Выводит результаты анализа транзакций в удобочитаемом формате.

	Параметры:
		analysis (dict): Результаты работы analyze_transactions()
	"""
	# Если анализ не был выполнен (None), выходим из функции
	if not analysis:
		return
	
	# Выводим общие финансовые результаты
	print('\nРезультаты анализа транзакций:')
	print(f'Общий доход: {analysis['total_income']:.2f}') # :.2f - формат с 2 знаками после запятой
	print(f'Общий расход: {analysis['total_income']:.2f}')
	print(f'Баланс: {analysis['total_income'] - analysis['total_expense']:.2f}')

	# Выводим группировку по категориям
	print('\nГруппировка по категориям:')
	for category, amount in analysis['categories'].items():
		print(f'- {category}: {amount:.2f}')


if __name__ == '__main__':
	"""
	Основная точка входа пир запуске скрипта напрямую.
	"""
	csv_file = input('Введите путь к CSV файлу с транзакциями: ') # Запрашиваем у пользователя путь к CSV файлу
	analysis = analyze_transactions(csv_file) # Выполняем анализ
	print(f' Результат: {analysis}') # Выводим результаты
	