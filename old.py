from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/') # путь/ручка
def main(): # вьюха/view
	return render_template('index.html')


@app.route('/about') # путь/ручка
def about(): # вьюха/view
	return '<h1> О нас </h1>'


@app.route('/posts')
def all_posts():
	return '''
	<p> Как я изучил Flask </p
	<p> Новая версия Python 3.14 </p>
	<p> Встреча в Белом доме </p>
	'''

@app.route('/posts/<int:id>')
def detail_post(id):
	print(type(id))
	# Идет запрос в БД чтоб достать новость под ID=3
	return f'Новость под ID: {id}'


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		login = request.form.get('login')
		password = request.form.get('password')
		print(login)
		print(password)
		# Добавлять их в БД

	return '''
	<form method="POST">
		<input type="text" name="login">
		<input type="password" name="password">
		<button> Войти </button>
	</form>
	'''


@app.route('/search')
def search():
	category = request.args.get('category')
	price = request.args.get('price')
	# if category:
	# 	# Запрос в БД на получение товаров именно из этой категории
	# if price:
	# 	# Запрос в БД на получение товаров именно из такой ценовой категории
	# # Запрос на получение всех товаров
	return f'Товары из категории: {category} c ценой: {price}'




if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=3000)




# Практическое задание:
# Создать словарь (типа БД) с ключами int (id) и значениями dict (информация о задаче)
# Реализовать путь /tasks (Для отображения всех задач)
# Реализовать динамический путь /tasks/<int:id> (Отображение конкретной одной задачи из БД)

# Пример БД:
tasks = {
	1: {'title': 'Купить хлеб', 'content': 'Успеть до закрытия магазина'},
	2: {'title': 'Поменять масло', 'content': 'Заехать в СТО'},
	3: {'title': 'Закончить проект', 'content': 'Дедлайн до завтра'}
}
