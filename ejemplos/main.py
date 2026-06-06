from motor import Motor
from auto import Auto
from moto import Moto

m1 = Motor()
m1.set_marca("Motor_Ford")
m1.set_serie("1234")
m1.set_caballos(150)

a1 = Auto()
a1.set_marca("Ford")
a1.set_modelo("Focus")
a1.set_color("Rojo")
a1.set_motor(m1)

mo = Moto()
mo.set_marca("Moto_Ford")
mo.set_modelo("Honda")
mo.set_color("Azul")
mo.set_motor(m1)

print("la marca del auto es:", a1.get_marca())
print("el modelo del auto es:", a1.get_modelo())
print("el color del auto es:", a1.get_color())
print("la marca del motor es:", a1.get_motor().get_marca())
print("la serie del motor es:", a1.get_motor().get_serie())
print("los caballos del motor son:", a1.get_motor().get_caballos())


print("la marca de la moto es:", mo.get_marca())
print("el modelo de la moto es:", mo.get_modelo())
print("el color de la moto es:", mo.get_color())
print("la marca del motor de la moto es:", mo.get_motor().get_marca())
print("la serie del motor de la moto es:", mo.get_motor().get_serie())
print("los caballos del motor de la moto son:", mo.get_motor().get_caballos())