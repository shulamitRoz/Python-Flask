import pyodbc

# פונקציה להתחברות למסד הנתונים המקומי
def get_connection():
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'
        'DATABASE=car_database;'
        'Trusted_Connection=yes;'
    )
    return conn

# פונקציה לקבלת כל המכוניות
def get_all_cars():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM car"
    cursor.execute(query)
    cars = cursor.fetchall()
    conn.close()
    return cars

# פונקציה לקבלת מכונית לפי מזהה
def get_car_by_id(car_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM car WHERE car_id = ?"
    cursor.execute(query, (car_id,))
    car = cursor.fetchone()
    conn.close()
    return car

# פונקציה להוספת מכונית חדשה (POST)
def create_car(new_car):
    conn = get_connection()
    cursor = conn.cursor()
    query = """INSERT INTO car (model,year, company, price, suppliers, color, style, car_image) 
               VALUES (?, ?, ?, ?, ?, ?, ?,? )"""
    
    values = (
        new_car['model'],
        new_car['year'],
        new_car['company'],
        new_car['price'],
        new_car['suppliers'],
        new_car['color'],
        new_car['style'],
        new_car['car_image']  
    )
    
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    
    return {'status': 200, 'message': 'Car added successfully', 'new_car': new_car}


# פונקציה למחיקת מכונית לפי מזהה (DELETE)
def delete_car(car_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM car WHERE car_id = ?"
    cursor.execute(query, (car_id,))
    conn.commit() 
    conn.close()
    return {'status': 'success', 'message': 'Car deleted successfully'}



def get_supplier_id(supplier_name):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT supplier_id FROM suppliers WHERE name = ?"
    cursor.execute(query, (supplier_name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


    conn = get_connection()
    cursor = conn.cursor()

    supplier = parameters.get('suppliers', 'Supplier')
    model = parameters.get('model', '')
    price = parameters.get('price', '')

    conditions = []
    values = []

    if supplier != 'Supplier':
        supplier_id = get_supplier_id(supplier)
        if supplier_id:
            conditions.append("suppliers = ?")
            values.append(supplier_id)
        else:
            print("Supplier not found")
            conn.close() 
            return []

    if model:
        conditions.append("model = ?")
        values.append(model)
    if price:
        conditions.append("price <= ?")
        values.append(price)

    query = "SELECT * FROM cars"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    print(query)  # For debugging purposes
    cursor.execute(query, values)
    results = cursor.fetchall()

    conn.close()
    return results
def search_car(parameters):
    conn = get_connection()
    cursor = conn.cursor()

    # Get the parameters and handle cases when no values are provided
    supplier = parameters.get('suppliers', None)
    model = parameters.get('model', '')
    price = parameters.get('price', '')

    conditions = []
    values = []

    # Only add conditions if values are provided
    if supplier:
        supplier_id = get_supplier_id(supplier)
        if supplier_id:
            conditions.append("suppliers = ?")
            values.append(supplier_id)
        else:
            print("Supplier not found")
            conn.close() 
            return []

    if model:
        conditions.append("model = ?")
        values.append(model)
        
    if price:
        conditions.append("price <= ?")
        values.append(price)

    # Use the correct table name and construct the query
    query = "SELECT * FROM car"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    print(query)  # For debugging
    cursor.execute(query, values)
    results = cursor.fetchall()

    conn.close()
    return results
    
    
new_car = {
    'model': 'Superfast',
    'year':2024,
    'price': 300000,
    'color': 'blue',
    'style': 'modern',
    'company': 'Ferrari',
    'suppliers': 1,
    'car_image': b'\x80PNG...'  # Add binary data for the image
}
           

# create_car(new_car)
# print(get_all_cars())
    

