import sqlite3

bd = sqlite3.connect("DB.db")

def connect_base():
    cursor = bd.cursor()
    return cursor

def create_base():
    
    cursor = connect_base()
    cursor.execute('''CREATE TABLE IF NOT EXISTS personal(
    id integer primary key AUTOINCREMENT,
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INT,
    bonus INT
    )''')
    baza=[(1,"Иван","Иванов","главный инженер",50000,10000),
          (2,"Игорь","Семенов"," инженер",20000,8000),
          (3,"Олег","Петров","завхоз",12000,3000)]
    try:
      cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)',baza)
      bd.commit()
    except:
         print('Данные присутствуют!')


def del_record():
    preview()
    nam = input('Укажите номер удаляемой записи: ')
    cursor = connect_base()
    cursor.execute(f'DELETE from personal WHERE id={nam};')
    bd.commit()
    
def edit_record():
    preview()
    try:
        cursor=connect_base()
        id = input("Выберите id записи:")
        zp = input("Ввведите желаемый размер зарплаты:")
        premia = input("Ввведите желаемый размер премии: ") 
        cursor.execute(f'UPDATE personal SET salary={zp} WHERE id={id};')
        cursor.execute(f'UPDATE personal SET bonus ={premia} WHERE id={id};')
        bd.commit()
        print("Изменения внесены")
    except:
        print("Вы ввели не коректные значения")
    
def add_record():

    try:
        cursor = connect_base()
        id = input('Введите номер записи: ')
        nam = input('Введите имя сотрудника: ').capitalize()
        last_na = input('Введите фамилию сотрудника: ').capitalize()
        position = input('Введите должность сотрудника: ')
        sal = input('Введите размер заработной платы сотрудника: ')
        bon = input('Введите размер премии сотрудника: ')
        cursor.execute('INSERT INTO personal VALUES(?,?,?,?,?,?)',(id, nam, last_na, position, sal,bon))
        bd.commit()
    except:
        print('Что то пошло не так!')

def find_record():

    cursor = connect_base()
    nam = input('Введите фамилию сотрудника :').capitalize()
    cursor.execute(f'select * from personal WHERE last_name LIKE "{nam}";')
    result = cursor.fetchall()
    if result == []:
        print(f"Сотрудник c фамилией {nam} в базе отсутствует ")
    else:
        for i in result:
            print(*i)

def preview():
    cursor = connect_base()
    for i in cursor.execute('SELECT * FROM personal'):
        print(*i)
     