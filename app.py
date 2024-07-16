
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

class Cuenta:
  def __init__(self, numero, nombre, saldo, contactos):
    self.numero = numero
    self.nombre = nombre
    self.saldo = saldo
    self.contactos = contactos
    self.historial = []

  def historialOperaciones(self):
    return self.historial

  def transferir(self, destino, valor):
    if self.saldo >= valor and destino.numero in self.contactos:
        operacion = Operacion(self.numero, destino.numero, valor, datetime.now().strftime('%d/%m/%Y'))
        self.saldo -= valor
        destino.saldo += valor
        self.historial.append(f"Transferencia realizada a {destino.nombre} por un valor de {valor}")
        destino.historial.append(f"Transferencia recibida de {self.nombre} por un valor de {valor}")
        return True, operacion
    else:
        return False, None

class Operacion:
    def __init__(self, origen, destino, valor, fecha):
        self.origen = origen
        self.destino = destino
        self.valor = valor
        self.fecha = fecha


# Base de datos en memoria
BD = [
    Cuenta("21345", "Arnaldo", 200, ["123", "456"]),
    Cuenta("123", "Luisa", 400, ["456"]),
    Cuenta("456", "Andrea", 300, ["21345"])
]

def buscar_cuenta(numero):
    for cuenta in BD:
        if cuenta.numero == str(numero):
            return cuenta
    return None

@app.route('/billetera/contactos')
def contactos():
    minumero = request.args.get('minumero')
    cuenta = buscar_cuenta(minumero)
    if cuenta:
        resultado = {contacto: buscar_cuenta(contacto).nombre for contacto in cuenta.contactos}
        return jsonify(resultado)
    return "Cuenta no encontrada", 404

@app.route('/billetera/pagar')
def pagar():
    minumero = request.args.get('minumero')
    numerodestino = request.args.get('numerodestino')
    valor = float(request.args.get('valor'))

    #print(minumero, numerodestino, valor)
    cuenta_origen = buscar_cuenta(minumero)
    cuenta_destino = buscar_cuenta(numerodestino)

    #print(cuenta_origen, cuenta_destino)

    if cuenta_origen and cuenta_destino:
        if cuenta_origen.saldo >= valor:
            cuenta_origen.saldo -= valor
            cuenta_destino.saldo += valor

            fecha = datetime.now().strftime('%d/%m/%Y')
            cuenta_origen.historial.append(f"Pago realizado de {valor} a {cuenta_destino.nombre} el {fecha}")
            cuenta_destino.historial.append(f"Pago recibido de {valor} de {cuenta_origen.nombre} el {fecha}")

            return f"Pago realizado el {fecha}", 200
        return "Saldo insuficiente", 400
    return "Cuenta no encontrada", 404

@app.route('/billetera/historial')
def historial():
    minumero = request.args.get('minumero')
    cuenta = buscar_cuenta(minumero)
    if cuenta:
        resultado = {
            "Saldo": cuenta.saldo,
            "Operaciones": cuenta.historial
        }
        return jsonify(resultado)
    return "Cuenta no encontrada", 404

if __name__ == '__main__':
    app.run()

# curl "http://localhost:5000/billetera/contactos?minumero=21345"
# curl "http://localhost:5000/billetera/pagar?minumero=21345&numerodestino=123&valor=100"
# curl "http://localhost:5000/billetera/historial?minumero=123"