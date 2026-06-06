from alumno import Alumno
from profesor import Profesor

a1 = Alumno()
a1.set_nombre("Juan")
a1.set_correo("juan@example.com")
a1.set_telefono("123456789")
a1.set_id(1)
a1.set_carrera("Ingeniería en Sistemas")
a1.set_promedio(8.5)

p1 = Profesor()
p1.set_nombre("Pedro")
p1.set_horas(40)
p1.set_pago(20.0)
p1.set_id(2)
p1.set_correo("pedro@example.com")
p1.set_telefono("987654321")


print("El nombre del alumno es:", a1.get_nombre())
print("El correo del alumno es:", a1.get_correo())
print("El teléfono del alumno es:", a1.get_telefono())
print("El ID del alumno es:", a1.get_id())
print("La carrera del alumno es:", a1.get_carrera())
print("El promedio del alumno es:", a1.get_promedio())
print("")
print("El nombre del profesor es:", p1.get_nombre())
print("Las horas del profesor son:", p1.get_horas())
print("El pago del profesor es:", p1.get_pago())
print("El ID del profesor es:", p1.get_id())
print("El correo del profesor es:", p1.get_correo())
print("El teléfono del profesor es:", p1.get_telefono())