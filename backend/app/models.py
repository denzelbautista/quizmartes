from flask_sqlalchemy import SQLAlchemy
from config.local import config
import uuid

db = SQLAlchemy()

def setup_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = config['DATABASE_URI'] if database_path is None else database_path
    db.app = app
    db.init_app(app)
    db.create_all()

class Convocatoria(db.Model):
    __tablename__ = 'convocatorias'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    jugador = db.Column(db.String(80), nullable=False)
    equipo = db.Column(db.String(120), unique=False, nullable=False)
    torneo = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, jugador, equipo, torneo):
        self.jugador = jugador
        self.equipo = equipo
        self.torneo = torneo
    
    def __repr__(self):
        return '<Convocatoria %r %r>' % (self.jugador, self.equipo)
    
    def __serialize__(self):
        return {
            'id': self.id,
            'jugador': self.jugador,
            'equipo': self.equipo,
            'torneo': self.torneo,
        }
