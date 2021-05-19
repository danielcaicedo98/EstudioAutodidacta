print("programa de evaluación de notas de alunmos")

nota_alumno = input("Introduce nota:")

def evaluacion(nota):
	valoracion = "aprobado"
	if nota < 5:
		valoracion = "suspenso"
	return valoracion
	
print(evaluacion(int(nota_alumno)))		
