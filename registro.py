class Ticket:
    def __init__(self, ident, patente, tipo, pago, pais, km):
        self.identidad = ident
        self.patente = patente
        self.tipo = tipo
        self.pago = pago
        self.pais = pais
        self.kilometro = km

    def __str__(self):
        r = "Codigo de Identidad: {:<15}".format(self.identidad)
        paispatente = str(self.patente)
        r += " | Patente: {:<7}".format(self.patente)
        r += " | Pais de patente: {:<12}".format(det_patente(paispatente))
        vehiculo = ["Motocicleta", "Automovil", "Camion"][int(self.tipo)]
        r += " | Tipo de vehiculo: {:<12}".format(vehiculo)
        formapago = ["Manual", "Telepeaje"][int(self.pago) - 1]
        r += " | Forma de pago: {:<10}".format(formapago)
        paiscabina = ["Argentina", " Bolivia", "Brasil", "Paraguay", "Uruguay"][int(self.pais)]
        r += " | Pais de la cabina: {:<10}".format(paiscabina)
        r += " | Kilometros: {:<6}".format(self.kilometro)
        return r

    def moto(self):
        veh = self.tipo
        if veh == 0:
            return True

    def auto(self):
        veh = self.tipo
        if veh == 1:
            return True

    def camion(self):
        veh = self.tipo
        if veh == 2:
            return True

    def pagomanual(self):
        pag = self.pago
        if pag == 1:
            return True

    def pagotelepeaje(self):
        pag = self.pago
        if pag == 2:
            return True

    def paiscabinaarg(self):
        paiscab = self.pais
        if paiscab == 0:
            return True

    def paiscabinabolivia(self):
        paiscab = self.pais
        if paiscab == 1:
            return True

    def paiscabinabr(self):
        paiscab = self.pais
        if paiscab == 2:
            return True

    def paiscabinapar(self):
        paiscab = self.pais
        if paiscab == 3:
            return True

    def paiscabinauru(self):
        paiscab = self.pais
        if paiscab == 4:
            return True



def det_patente(patente):
    pais_patente = ""

    if len(patente) != 7:
        pais_patente = "Otro"

    else:
        if 'A' <= patente[0] <= 'Z' and 'A' <= patente[1] <= 'Z' and '0' <= patente[2] <= '9' and '0' <= patente[
            3] <= '9' and '0' <= patente[4] <= '9' \
                and '0' <= patente[3] <= '9' and '0' <= patente[4] <= '9' and 'A' <= patente[5] <= 'Z' and 'A' <= \
                patente[6] <= 'Z':
            pais_patente = "Argentina"

        elif "A" <= patente[0] <= "Z" and "A" <= patente[1] <= "Z" and "A" <= patente[2] <= "Z" and "0" <= patente[
            3] <= "9" and "0" \
                and "0" <= patente[3] <= "9" and "0" <= patente[4] <= "9" and "0" <= patente[5] <= "9" and "0" <= \
                patente[6] <= "9":
            pais_patente = "Uruguay"

        elif 'A' <= patente[0] <= 'Z' and 'A' <= patente[1] <= 'Z' and '0' <= patente[2] <= '9' and '0' <= patente[
            3] <= '9' \
                and '0' <= patente[4] <= '9' and '0' <= patente[5] <= '9' and '0' <= patente[6] <= '9':
            pais_patente = "Bolivia"

        elif patente[0] == " " and 'A' <= patente[1] <= 'Z' and 'A' <= patente[2] <= 'Z' and 'A' <= patente[3] <= 'Z' \
                and 'A' <= patente[4] <= 'Z' and "0" <= patente[5] <= "9" and "0" <= patente[6] <= "9":
            pais_patente = "Chile"

        elif 'A' <= patente[0] <= 'Z' and 'A' <= patente[1] <= 'Z' and 'A' <= patente[2] <= 'Z' and '0' <= patente[
            3] <= '9' and 'A' <= patente[4] <= 'Z' \
                and 'A' <= patente[4] <= 'Z' and '0' <= patente[5] <= '9' and '0' <= patente[6] <= '9':
            pais_patente = "Brasil"


        elif 'A' <= patente[0] <= 'Z' and 'A' <= patente[1] <= 'Z' and 'A' <= patente[2] <= 'Z' and 'A' <= patente[
            3] <= 'Z':
            if "0" <= patente[4] <= "9" and "0" <= patente[5] <= "9" and "0" <= patente[6] <= "9":
                pais_patente = "Paraguay"


        else:
            pais_patente = 'Otro'

    return pais_patente


def crear_alquiler(linea):
    tickets = linea.split(",")
    ident = int(tickets[0])
    patente = tickets[1]
    tipo = int(tickets[2])
    pago = int(tickets[3])
    pais = int(tickets[4])
    km = int(tickets[5])
    return Ticket(ident, patente, tipo, pago, pais, km)
