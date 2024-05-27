# Se importa la librería para realizar los request con mysql
import mysql.connector

# Función para conectarse a la base de datos
def conectar_bd():
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Bruno1226*',
        database = 'db_examen2'
    )
    return conn

# Se importa Flask junto con los métodos necesarios
from flask import Flask, request, jsonify, render_template

# Se crea una instancia de flask
app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de alta de alumno
@app.route('/alta_alumno')
def alta_alumno():
    return render_template('alta_alumno.html')

# Ruta para la página de alta de sistema
@app.route('/alta_sistema')
def alta_sistema():
    return render_template('alta_sistema.html')

# Ruta para la página de alta de práctica
@app.route('/alta_practica')
def alta_practica():
    return render_template('alta_practica.html')

# Ruta para la página de modificar alumno
@app.route('/modificar_alumno')
def modificar_alumno():
    return render_template('modificar_alumno.html')

# Ruta para la página de modificar sistema
@app.route('/modificar_sistema')
def modificar_sistema():
    return render_template('modificar_sistema.html')

# Ruta para la página de listar
@app.route('/listar')
def listar():
    return render_template('listar.html')

# Ruta para manejar el alta de alumno
@app.route('/alumnos', methods=['POST'])
def alumnos():
    # Obtener los datos JSON de la solicitud POST
    data = request.json
    # Extraer los campos específicos de los datos recibidos
    grupo = data['grupo']
    matricula = data['matricula']
    nombre = data['nombre']
    # Conectar a la base de datos
    conn = conectar_bd()
    cursor = conn.cursor()
    # Verificar si ya existe un alumno con la matrícula proporcionada
    cursor.execute(f"SELECT * FROM alumno WHERE matricula = '{matricula}'")
    alumno = cursor.fetchall()
    if not len(alumno):
        # Si no existe un alumno con esa matrícula, insertar el nuevo alumno en la base de datos
        cursor.execute("INSERT INTO alumno (grupo, matricula, nombre) VALUES (%s, %s, %s)", (grupo, matricula, nombre))
        conn.commit()
        conn.close()
        return jsonify({'message': f'Alumno con matrícula {matricula} agregado correctamente'}), 200
    else:
        # Si ya existe un alumno con esa matrícula, devolver un mensaje indicando el conflicto
        conn.close()
        return jsonify({'message': f'El alumno con matrícula {matricula} ya existe'}), 404
    
# Ruta para dar de alta un sistema
@app.route('/sistemas', methods=['POST'])
def sistemas():
    # Obtener los datos JSON de la solicitud POST
    data = request.json
    # Extraer los campos específicos de los datos recibidos
    p1 = data['p1']
    p2 = data['p2']
    p3 = data['p3']
    # Conectar a la base de datos
    conn = conectar_bd()
    cursor = conn.cursor()
    # Verificar si ya existe un sistema con los valores p1, p2 y p3 proporcionados
    cursor.execute(f"SELECT * FROM sistema WHERE p1 = {p1} AND p2 = {p2} AND p3 = {p3}")
    sistema = cursor.fetchall()
    if not len(sistema):
        # Si no existe un sistema con esos valores, insertar el nuevo sistema en la base de datos
        cursor.execute("INSERT INTO sistema (p1, p2, p3) VALUES (%s, %s, %s)", (p1, p2, p3))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Sistema agregado correctamente'}), 200
    else:
        # Si ya existe un sistema con esos valores, devolver un mensaje indicando el conflicto
        conn.close()
        return jsonify({'message': 'El sistema indicado ya existe'}), 200

# Ruta para dar de alta un lab
@app.route('/labs', methods=['POST'])
def labs():
    # Obtiene los datos JSON enviados en la solicitud POST
    data = request.json
    # Extrae los valores de 'idalumno', 'idsistema' y 'numero_practica' del JSON recibido
    idalumno = data['idalumno']
    idsistema = data['idsistema']
    numero_practica = data['numero_practica']
    # Conecta a la base de datos
    conn = conectar_bd()
    cursor = conn.cursor()
    # Verifica si el 'idalumno' existe en la tabla 'alumno'
    cursor.execute(f"SELECT idalumno FROM alumno WHERE idalumno = {idalumno}")
    alumno = cursor.fetchall()
    # Verifica si el 'idsistema' existe en la tabla 'sistema'
    cursor.execute(f"SELECT idsistema FROM sistema WHERE idsistema = {idsistema}")
    sistema = cursor.fetchall()
    # Si el alumno y el sistema existen
    if len(alumno) > 0 and len(sistema) > 0:
        # Verifica si ya existe un registro en 'lab' con los mismos 'idalumno', 'idsistema' y 'numero_practica'
        cursor.execute(f"SELECT * FROM lab WHERE idalumno = {idalumno} AND idsistema = {idsistema} AND numero_practica = {numero_practica}")
        lab = cursor.fetchall()
        # Si no existe tal registro, inserta un nuevo registro en la tabla 'lab'
        if not len(lab):
            cursor.execute("INSERT INTO lab (idalumno, idsistema, numero_practica) VALUES (%s, %s, %s)", (idalumno, idsistema, numero_practica))
            conn.commit()  # Guarda los cambios en la base de datos
            conn.close()  # Cierra la conexión con la base de datos
            return jsonify({'message': 'Práctica agregada correctamente'}), 200
        else:
            return jsonify({'message': 'La práctica indicada ya existe'}), 200
    # Si el alumno existe pero el sistema no
    elif len(alumno) > 0:
        conn.close()  # Cierra la conexión con la base de datos
        return jsonify({'message': 'El sistema no existe'}), 404
    # Si el sistema existe pero el alumno no
    elif len(sistema) > 0:
        conn.close()  # Cierra la conexión con la base de datos
        return jsonify({'message': 'El alumno no existe'}), 404
    # Si ni el alumno ni el sistema existen
    else:
        conn.close()  # Cierra la conexión con la base de datos
        return jsonify({'message': 'Ni el alumno ni el sistema existen'}), 404

# Ruta para modificar alumno
@app.route('/alumnosModificacion', methods=['POST'])
def alumnosModificacion():
    # Obtener los datos JSON de la solicitud POST
    data = request.json
    # Extraer los campos específicos de los datos recibidos
    idalumno = data['idalumno']
    nombre = data['nombre']
    matricula = data['matricula']
    grupo = data['grupo']
    # Conectar a la base de datos
    conn = conectar_bd()
    cursor = conn.cursor()
    # Verificar si existe un alumno con el idalumno proporcionado
    cursor.execute(f"SELECT idalumno FROM alumno WHERE idalumno = {idalumno}")
    alumno = cursor.fetchall()
    if len(alumno) > 0:
        # Verificar si ya existe un alumno con la misma matrícula
        cursor.execute(f"SELECT * FROM alumno WHERE matricula = '{matricula}' AND idalumno != {idalumno}")
        alumno = cursor.fetchall()
        if not len(alumno):
            # Si no existe un alumno con esa matrícula, actualizar los datos del alumno con el idalumno proporcionado
            cursor.execute("UPDATE alumno SET nombre = %s, matricula = %s, grupo = %s WHERE idalumno = %s", 
                           (nombre, matricula, grupo, idalumno))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Alumno actualizado correctamente'}), 200
        else:
            # Si ya existe un alumno con esa matrícula, devolver un mensaje indicando el conflicto
            conn.close()
            return jsonify({'message': f'El alumno con matrícula {matricula} ya existe'}), 404
    else:
        # Si no existe un alumno con el idalumno proporcionado, devolver un mensaje de error
        conn.close()
        return jsonify({'message': 'No existe el alumno con ese id'}), 404

# Ruta para modificar sistema
@app.route('/sistemasModificacion', methods=['POST'])
def sistemasModificacion():
    # Obtener los datos JSON de la solicitud POST
    data = request.json
    # Extraer los campos específicos de los datos recibidos
    idsistema = data['idsistema']
    p1 = data['p1']
    p2 = data['p2']
    p3 = data['p3']
    # Conectar a la base de datos
    conn = conectar_bd()
    cursor = conn.cursor()
    # Verificar si existe un sistema con el idsistema proporcionado
    cursor.execute(f"SELECT idsistema FROM sistema WHERE idsistema = {idsistema}")
    sistema = cursor.fetchall()
    if len(sistema) > 0:
        # Verificar si ya existe un sistema con los valores p1, p2 y p3 proporcionados
        cursor.execute(f"SELECT * FROM sistema WHERE p1 = {p1} AND p2 = {p2} AND p3 = {p3}")
        sistema = cursor.fetchall()
        if not len(sistema):
            # Si no existe un sistema con esos valores, actualizar el sistema con el idsistema proporcionado
            cursor.execute("UPDATE sistema SET p1 = %s, p2 = %s, p3 = %s WHERE idsistema = %s", (p1, p2, p3, idsistema))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Sistema actualizado correctamente'}), 200
        else:
            # Si ya existe un sistema con esos valores, devolver un mensaje indicando el conflicto
            conn.close()
            return jsonify({'message': 'El sistema indicado ya existe'}), 404
    else:
        # Si no existe un sistema con el idsistema proporcionado, devolver un mensaje de error
        conn.close()
        return jsonify({'message': 'No existe un sistema con ese id'}), 404
    
# Ruta para listar alumnos y sistemas de una práctica
@app.route('/labsListar', methods=['GET'])
def labsListar():
    # Obtener el parámetro 'numero_practica' de la solicitud GET
    numero_practica = request.args.get('numero_practica')
    # Conectar a la base de datos
    conn = conectar_bd()
    cursor = conn.cursor()
    # Ejecutar una consulta para seleccionar registros de la tabla 'lab' donde 'numero_practica' coincide
    cursor.execute(f"SELECT * FROM lab WHERE numero_practica = {numero_practica}")
    lab = cursor.fetchall()
    # Verificar si se encontraron registros
    if len(lab) > 0:
        # Si se encontraron registros, ejecutar una consulta para obtener datos de 'alumno' y 'sistema'
        cursor.execute(f"""SELECT alumno.matricula, alumno.nombre, sistema.p1, sistema.p2, sistema.p3 
                           FROM alumno 
                           INNER JOIN sistema 
                           INNER JOIN lab 
                           ON alumno.idalumno = lab.idalumno 
                           AND sistema.idsistema = lab.idsistema 
                           WHERE lab.numero_practica = {numero_practica}""")
        resultados = cursor.fetchall()
        # Crear una lista para almacenar los datos de los alumnos
        alumnos = []
        # Recorrer los resultados y agregar cada alumno a la lista
        for alumno in resultados:
            alumnos.append({'matricula': alumno[0], 'nombre': alumno[1], 'p1': alumno[2], 'p2': alumno[3], 'p3': alumno[4]})
        # Cerrar la conexión a la base de datos
        conn.close()
        # Devolver una respuesta JSON con la lista de alumnos y un mensaje de éxito
        return jsonify({'alumnos': alumnos, 'message': 'Práctica listada correctamente'}), 200
    else:
        # Si no se encontraron registros, cerrar la conexión a la base de datos
        conn.close()
        # Devolver una respuesta JSON indicando que no existe el número de práctica seleccionado
        return jsonify({'alumnos': [], 'message': 'No existe el número de práctica seleccionado'}), 404

# Condicional para correr la instancia de Flask si se está ejecutando el archivo actual
if __name__ == '__main__':
    app.run(debug=True)