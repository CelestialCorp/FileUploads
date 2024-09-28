from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///files.db'  # Utilizza SQLite per semplicità
app.config['UPLOAD_FOLDER'] = 'uploads'  # Cartella per i file caricati
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limite di 16 MB
db = SQLAlchemy(app)

# Modello per il file
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)

# Crea la tabella se non esiste
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # Recupera solo i 5 file più recenti
    files = File.query.order_by(File.upload_date.desc()).limit(5).all()
    return render_template('index.html', files=files)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_file = File(filename=filename)
            db.session.add(new_file)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('upload.html')

@app.route('/download/<int:file_id>')
def download_file(file_id):
    file_record = File.query.get(file_id)
    if file_record is None:
        print(f'File con ID {file_id} non trovato')  # Debug
        return 'File non trovato', 404
    
    print(f'Scaricando il file: {file_record.filename}')  # Debug
    # Assicurati di fornire il percorso corretto per la directory di upload
    return send_from_directory(app.config['UPLOAD_FOLDER'], file_record.filename)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])  # Crea la cartella per i file se non esiste
    app.run(debug=True)
