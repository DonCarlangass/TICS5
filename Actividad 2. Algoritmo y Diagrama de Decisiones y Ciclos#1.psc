Algoritmo Salario
	Definir salarioActual, nuevoSalario Como Real
	Escribir 'Ingrese el salario actual del empleado: '
	Leer salarioActual
	Si salarioActual<4000 Entonces
		nuevoSalario <- salarioActual*1.10
	SiNo
		nuevoSalario <- salarioActual
	FinSi
	Escribir 'El nuevo salario es: ', nuevoSalario
FinAlgoritmo