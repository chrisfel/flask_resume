from flask import Flask, render_template

app = Flask(__name__)


#create Index Page
@app.route('/')
def index():
		first_name = "Chris"
		favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", "Supreme"]
		return render_template('index.html', f_name = first_name, favorite_pizza = favorite_pizza)

#Create About Page
@app.route('/about')
def about():
	return render_template('about.html')