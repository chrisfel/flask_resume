from flask import Flask, render_template

app = Flask(__name__)


#create Index Page
@app.route('/')
def index():
		
		return render_template('index.html')

@app.route('/degrees')
def degrees():
		
		return render_template('index2.html')