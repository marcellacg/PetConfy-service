from helpers.database import db
from flask_restful import fields


endereco_fields = {
    'id': fields.Integer(attribute='id'),
    'logradouro': fields.String(attribute='logradouro'),
    'numero': fields.String(attribute='numero'),
    'cidade': fields.String(attribute='cidade'),
    'estado': fields.String(attribute='estado')
}


class EnderecoUsuario(db.Model):

    _tablename_ = "tb_enderecoUsuario"

    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String, nullable=False)
    numero = db.Column(db.String(9), nullable=False)
    cidade = db.Column(db.String(), nullable=False)
    estado = db.Column(db.String(), nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey("tb_usuario.id"))

    def _init_(self, logradouro, numero, cidade, estado):
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

    def _repr_(self):
        return '<Logradouro: {}\n Numero: {}\n Cidade: {}\n Estado: {}>'.format(self.logradouro, self.numero, self.cidade, self.estado)