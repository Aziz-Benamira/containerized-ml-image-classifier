from flask import Flask, request, render_template, send_from_directory
import requests
import os
import psycopg2
import json

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ML_SERVICE_URL = 'http://ml-service:5001/classify'

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database=os.getenv('DB_NAME', 'classifier'),
        user=os.getenv('DB_USER', 'user'),
        password=os.getenv('DB_PASSWORD', 'password'),
        port=os.getenv('DB_PORT', '5432')
    )
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS classifications (
            id SERIAL PRIMARY KEY,
            image_filename TEXT NOT NULL,
            predictions JSONB NOT NULL
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No image uploaded", 400
        file = request.files['image']
        if file.filename == '':
            return "No file selected", 400
        
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)

        with open(image_path, 'rb') as f:
            response = requests.post(ML_SERVICE_URL, files={'image': f})
        
        if response.status_code != 200:
            return "Error contacting ML service", 500
        
        predictions = response.json()['predictions']
        pred_list = [(p['label'], p['probability']) for p in predictions]

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO classifications (image_filename, predictions) VALUES (%s, %s)",
            (file.filename, json.dumps(predictions))
        )
        conn.commit()
        cur.close()
        conn.close()

        return render_template('result.html', predictions=pred_list, image_path=file.filename)
    
    return render_template('index.html')

@app.route('/history')
def history():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT image_filename, predictions FROM classifications ORDER BY id DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    history_data = [
        {
            'image_filename': row[0],
            'predictions': [(p['label'], p['probability']) for p in row[1]]
        }
        for row in rows
    ]
    return render_template('history.html', history=history_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)