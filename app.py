from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/listings')
def listings():
    listings = [
        {'id': 1, 'title': "Dracula's Mansion", 'price': 2000},
        {'id': 2, 'title': "Rapunzel's Tower", 'price': 800},
        {'id': 3, 'title': "Sweeney Hall", 'price': 5000},
        {'id': 4, 'title': "Beach House", 'price': 250},
    ]
    return render_template('listings.html', listings=listings)

@app.route('/listing/<int:id>')
def listing_detail(id):
    return render_template('listing_detail.html', id=id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('dashboard', username=username))
    return render_template('login.html')

@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)

