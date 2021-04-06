from app import db

class Pessoa(db.Model):
    __tablename__ = 'pessoas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    sexo = db.Column(db.String(1))
    salario = db.Column(db.Float)

    def __init__(self, nome, idade, sexo, salario):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.salario = salario
    
    def __repr__(self):
        return '<Pessoa %r>' % self.nome
