from boa_constrictor import BoaConstrictor
from huron import Huron

boa1 = BoaConstrictor("Sneaky", 5, 3.6, "Colombia", 15.2)
huron1 = Huron("Bobby", 2, 9.1, "Canada", 2)

print("Boa1: \t", boa1.__dict__)
print("Huron1: \t", huron1.__dict__, "\n")

print(f"{boa1.nombre}: {boa1.hacer_sonido()}")
print(f"{huron1.nombre}: {huron1.hacer_sonido()}")

print(f"El costo de importar a la boa {boa1.nombre} ${boa1.calcular_flete()}")
print(f"El costo de importar a el hurón {
      huron1.nombre} ${huron1.calcular_flete()}\n")

boa1.comer_raton()

print(f"{boa1.nombre} se ha comido {boa1.ratones_comidos} ratones.")
boa1.comer_raton()

print(f"{boa1.nombre} se ha comido {boa1.ratones_comidos} ratones.")

huron1.comer(2)

print(f"El hurón {huron1.nombre} se ha comido {huron1.kilos_comidos} kilos")
