class empleado:
    def calcular_ingreso_total(self):
        ingreso_total = self.salario + self.calcular_comision()
        return ingreso_total
    def mostrar_datos(self):
        texto = f"Nombre y apellido: {self.nombre} {self.apellido}\n"
        texto += f"DNI: {self.dni} - Salario: {self.salario}\n"
        return texto