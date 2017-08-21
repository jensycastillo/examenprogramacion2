import Animales

class Perro(Animales.Animal):
    def Beber(self,cantidadagua):
        self.cantidadagua+=cantidadagua
        print('El perro tiene{0}litros de agua'.format(self.cantidadagua))

    def Alimentar(self,tipoalimento,cantidadalimento):
        if(tipoalimento.lower=="Dogui"):
            self(cantidadalimento= cantidadalimento)
        else:
            print("Solo me alimento de Dogui")
