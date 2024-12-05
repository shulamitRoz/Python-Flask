import datetime
import smtplib
from  models import cars_model, suppliers_model, user_model
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

@app.route('/')
def root():
    return render_template('login.html')

@app.route('/login.html', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        res = user_model.login(username, password)
        if res['status'] == 200:
            # global user
            user = res['user']
            return redirect(url_for('home'))
        elif res['status'] == 400:
            error = "Invalid credentials, please try again."
        else:
            return redirect(url_for('register'))

    return render_template('login.html', error=error)

@app.route('/register.html', methods=['POST', 'GET'])
def register():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        phone=request.form['phone']
        age = request.form['age']
        country=request.form['country']
        res = user_model.create_user({'name':name, 'password':password, 'email':email,'phone':phone, 'age':age,'country':country})
    
        if res['status'] == 200:
            # global user
            user = res['new user']
            return redirect(url_for('home'))
        else:
            error = "A problem occurred, please try again."

    return render_template('register.html', error=error)


# @app.route('/index.html', methods = ['GET'])
# def home():
    cars= cars_model.get_all_cars()
    sup=suppliers_model.get_all_suppliers()
    print(cars)
    search_parameters = {
        'suppliers': request.args.get('suppliers'),
        'model': request.args.get('model'),
        'price': request.args.get('price')
    }
    if any(search_parameters.values()):
        filteredCars = cars_model.search_car(search_parameters)
        print(filteredCars)
    else:
        filteredCars = cars
    
    return render_template('index.html', cars=filteredCars, sup=sup, full_cars=cars)

@app.route('/index.html', methods=['GET'])
def home():
    cars = cars_model.get_all_cars()
    sup = suppliers_model.get_all_suppliers()
    
    # Collect the search parameters from the request
    search_parameters = {
        'suppliers': request.args.get('suppliers'),
        'model': request.args.get('model'),
        'price': request.args.get('price')
    }
    
    print("Search parameters received:", search_parameters)  # For debugging
    
    # Check if any search parameter is provided
    if any(search_parameters.values()):
        filteredCars = cars_model.search_car(search_parameters)
        print("Filtered Cars:", filteredCars)  # Debugging
    else:
        filteredCars = cars
    
    # Render the template with the full and filtered car lists
    return render_template('index.html', cars=filteredCars, sup=sup, full_cars=cars)

@app.route('/carDetails', methods=['GET'])
def carDetails():
    car_id = request.args.get('car_id')
    if car_id:
        car = cars_model.get_car_by_id(car_id)
        if car:
            manu = suppliers_model.get_supplier_by_id(car[7])
            car_data = {
                'model': car[3],
                'color': car[6],
                'suppliers': manu[1],
                'price': car[5],
                'style': car[4],
                'company':[2],

            }
            return render_template('carDetails.html', car=car_data, car_id=car_id)
        else:
            return "Car not found", 404
    else:
        return "Car ID not provided", 400

if __name__ == '__main__':
    app.run(port=3000)