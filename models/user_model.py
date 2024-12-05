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

def login(username, user_password):
    conn = get_connection()  
    cursor = conn.cursor()
    user_query = "SELECT user_id, password FROM users WHERE name = ?"
    cursor.execute(user_query, (username,))
    user = cursor.fetchone()
    conn.close()  
    if user:
        user_id, password = user
        if password == user_password:
            return {'status': 200, 'user': user}
        else:
            return {'status': 400, 'message': 'Password does not match'}
    else:
        return {'status': 404, 'message': 'User does not exist'}


# GET: קבלת כל המשתמשים
def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    conn.close()
    return users

# GET BY ID: קבלת משתמש לפי מזהה
def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE user_id = ?"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

# POST: יצירת משתמש חדש
# def create_user(new_user):
#     conn = get_connection()
#     cursor = conn.cursor()
#     query = """INSERT INTO users (name,password,email,phone, age,country) 
#                VALUES (?, ?, ?, ?, ?,?)"""
#     values = (
#         new_user['name'],
#         new_user['password'],
#         new_user['email'],
#         new_user['phone'],
#         new_user['age'],
#         new_user['country'])
    
#     cursor.execute(query, values)
#     conn.commit() 
#     conn.close()
#     return {'status': 200, 'message': 'User added successfully', 'new user': new_user}
def create_user(new_user):
    conn = get_connection()
    cursor = conn.cursor()
    query = """INSERT INTO users (name, password, email, phone, age, country) 
               VALUES (?, ?, ?, ?, ?, ?)"""
    values = (
        new_user['name'],
        new_user['password'],
        new_user['email'],
        new_user['phone'],
        new_user['age'],
        new_user['country'])
    
    cursor.execute(query, values)
    conn.commit() 
    conn.close()
    return {'status': 200, 'message': 'User added successfully', 'new user': new_user}

# PUT: עדכון משתמש קיים
def update_user(user_id, updated_user):
    conn = get_connection()
    cursor = conn.cursor()
    query = """UPDATE users SET name = ?, age = ?, country = ?, email = ?, phone = ?, 
               WHERE user_id = ?"""
    values = (
        updated_user['name'],
        updated_user['age'],
        updated_user['country'],
        updated_user['email'],
        updated_user['phone'],
        user_id)
    cursor.execute(query, values)
    conn.commit()  
    conn.close()
    return {'status': 'success', 'message': 'User updated successfully', 'updated_user': updated_user}

# DELETE: מחיקת משתמש לפי מזהה
def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM users WHERE user_id = ?"
    cursor.execute(query, (user_id,))
    conn.commit() 
    conn.close()
    return {'status': 'success', 'message': 'User deleted successfully'}


new_user = {
    'name': 'gdzgfggggg bbb',
    'email': 'ohn.o@example.com',
    'age': 30,
    'password': '68dfaa3g',
    'country':'aaa',
    # 'car_id':'12345',
    'phone':'123456'

}

#create_user(new_user)