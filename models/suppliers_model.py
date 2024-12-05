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

# GET: קבלת כל הספקים
def get_all_suppliers():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM suppliers"
    cursor.execute(query)
    suppliers = cursor.fetchall()
    conn.close()
    return suppliers

# GET BY ID: קבלת ספק לפי מזהה
def get_supplier_by_id(supplier_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM suppliers WHERE supplier_id = ?"
    cursor.execute(query, (supplier_id,))
    supplier = cursor.fetchone()
    conn.close()
    return supplier

# POST: יצירת ספק חדש
def create_supplier(new_supplier):
    conn = get_connection()
    cursor = conn.cursor()
    query = """INSERT INTO suppliers (name, country, phone, email) 
               VALUES (?, ?, ?, ?)"""
    values = (
        new_supplier['name'],
        new_supplier['country'],
        new_supplier['phone'],
        new_supplier['email'])
    cursor.execute(query, values)
    conn.commit()  
    conn.close()
 
    return {'status': 200, 'message': 'Supplier added successfully', 'new_supplier': new_supplier}

# PUT: עדכון ספק קיים
def update_supplier(supplier_id, updated_supplier):
    conn = get_connection()
    cursor = conn.cursor()
    query = """UPDATE suppliers SET name = ?, country = ?, phone = ?, email = ?
               WHERE supplier_id = ?"""
    values = (
        updated_supplier['name'],
        updated_supplier['country'],
        updated_supplier['phone'],
        updated_supplier['email'],
        supplier_id)
    cursor.execute(query, values)
    conn.commit()  
    conn.close()
    return {'status': 'success', 'message': 'Supplier updated successfully', 'updated_supplier': updated_supplier}

new_suppliers = {
    'name':"ssss",
    'country':"bb",
    'phone':123,
    'email':'sss@gmail.com'

}
create_supplier(new_suppliers)