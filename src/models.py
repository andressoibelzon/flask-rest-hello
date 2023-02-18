from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }



# traigo mis tablas
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    fecha_de_suscripcion = db.Column(db.String(250), nullable=False)
    nombre = db.Column(db.String(250), nullable=False)
    apellido = db.Column(db.String(250), nullable=False)
    # favoritos = relationship('Favoritos', backref='usuario', lazy='true')

    def __repr__(self):
        return '<Usuario %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "fecha_de_suscripcion": self.fecha_de_suscripcion,
            "nombre": self.nombre,
            "apellido": self.apellido
            # do not serialize the password, its a security breach
        }


class Personajes(db.Model):
    __tablename__ = 'personajes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    altura = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(250), nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    # favoritos = relationship('Favoritos', backref='personajes', lazy='true')

    def __repr__(self):
        return '<Personajes %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "altura": self.altura,
            "genero": self.genero,
            "peso": self.peso
            # do not serialize the password, its a security breach
        }


class Planetas(db.Model):
    __tablename__ = 'planetas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    habitantes = db.Column(db.Integer, nullable=False)
    periodo_orbital = db.Column(db.Integer, nullable=False)
    diametro = db.Column(db.Integer, nullable=False)
    # favoritos = relationship('Favoritos', backref='planetas', lazy='true')

    def __repr__(self):
        return '<Planetas %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "habitantes": self.habitantes,
            "periodo_orbital": self.periodo_orbital,
            "diametro": self.diametro
            # do not serialize the password, its a security breach
        }


class Vehiculos(db.Model):
    __tablename__ = 'vehiculos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    cantidad_ruedas = db.Column(db.Integer, nullable=False)
    consumo_combustible = db.Column(db.Integer, nullable=False)
    # favoritos = relationship('Favoritos', backref='planetas', lazy='true')

    def __repr__(self):
        return '<Vehiculos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad_ruedas": self.cantidad_ruedas,
            "consumo_combustible": self.consumo_combustible,
            # do not serialize the password, its a security breach
        }



class Favoritos(db.Model):
    __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    # usuario_id = db.Column(db.Integer, ForeignKey('usuario.id'))
    # personajes_id = db.Column(db.Integer, ForeignKey('personajes.id'))
    # planetas_id = db.Column(db.Integer, ForeignKey('planetas.id'))

    def __repr__(self):
        return '<Favoritos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            # "usuario_id": self.usuario_id,
            # "personajes_id": self.personajes_id,
            # "planetas_id": self.planetas_id
            # do not serialize the password, its a security breach
        }