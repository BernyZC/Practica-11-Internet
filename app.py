from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import base64
app = Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='libreria'
    )
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        autor = request.form['autor']
        titulo = request.form['titulo']
        fecha = request.form['fecha_publicacion']
        imagen = request.files['imagen']
        imagen_blob = imagen.read()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO libros (autor, titulo, fecha_publicacion, imagen_portada) VALUES (%s, %s, %s, %s)",
            (autor, titulo, fecha, imagen_blob)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('consulta'))
    return render_template('registro.html')
@app.route('/consulta')
def consulta():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM libros")
    libros_db = cursor.fetchall()
    cursor.close()
    conn.close()
    libros = []
    for libro in libros_db:
        imagen_b64 = base64.b64encode(libro['imagen_portada']).decode('utf-8')
        libro['imagen_b64'] = imagen_b64
        libros.append(libro)
    return render_template('consulta.html', libros=libros)
if __name__ == '__main__':
    app.run(debug=True)