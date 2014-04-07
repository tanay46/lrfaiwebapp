from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route("/dashboard")
def view_dashboard():
	return render_template('dashboard.html')

@app.route("/artists/<artist>")
def get_artist_page(artist):
	return artist

if __name__ == '__main__':
    app.run()