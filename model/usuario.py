from sqlalchemy import ForeignKey
from helpers.database import db
from sqlalchemy.types import String
from flask_restful import fields
from model.enderecoUsuario import endereco_fields

usuario_fields = {
    'id': fields.Integer(attribute='id'),
    'email': fields.String(attribute='email'),
    'senha': fields.String(attribute='senha'),
    'endereco': fields.Nested(endereco_fields),
    'telefone': fields.String(attribute='telefone'),
    'observacoes': fields.String(attribute='observacoes')
}

class Usuario(db.Model):

    _tablename_ = "tb_usuario"

    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True)
    senha = db.Column(db.String(30), unique=True, nullable=False)
    telefone = db.Column(db.String(11))
    observacoes = db.Column(db.String(700))

    EnderecoUsuario = db.relationship("EnderecoUsuario", uselist=False)

    # Herança: Superclasse
    tipo_usuario = db.Column('tipo_usuario', String(50))
    _mapper_args_ = {'polymorphic_on': tipo_usuario}

    def _init_(self, nome, email, senha, telefone, endereco: EnderecoUsuario, observacoes):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco
        self.observacoes = observacoes

    def _repr_(self):
        return '<Nome: {}\n Email: {}\n Telefone: {}\n Observacoes: {}>'.format(self.nome, self.email, self.telefone, self.observacoes)