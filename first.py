from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
# socketio = SocketIO(app)
socketio = SocketIO(app, async_mode='threading') 

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@app.route('/')
def home():
    return "Bonjour"

# Définir la route pour servir la page HTML de saisie des valeurs de position
@app.route('/input')
def input_page():
    return render_template('index.html')

# Définir la route pour servir la page HTML de la scène de réalité virtuelle
@app.route('/vr_scene')
def vr_scene():
    return render_template('vr_scene.html')

# Écouter les mises à jour de position du client
@socketio.on('position_update', namespace='/')
def handle_position_update(data):
    # Diffuser les données à tous les clients connectés
    socketio.emit('position_update', data)

if __name__ == '__main__':
    socketio.run(app)