nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]
nombres = nombres.replace("'","").split(",")


def crearEstructura(nombres,notas_1,notas_2):
    dicc = {}
    for alumno,nota1,nota2 in zip(nombres,notas_1,notas_2):
        dicc[alumno.strip(" ").strip("\n")] = [nota1,nota2]   
    return dicc

def crearPromedio (dicc):
    diccProm = dict(map(lambda x: (x[0], sum(x[1]) / 2), dicc.items()))
    return diccProm 
    #diccProm = {}
    #for elem in dicc:
     #   diccProm[elem] = sum(dicc[elem]) / 2
    #return diccProm

def promedioCurso (diccProm):
    promedio = sum(diccProm.values())
    return promedio / len(diccProm)

def notaMasAlta (diccProm):
    alumno = max(diccProm.items(), key = lambda x: x[1])[0]
    nota = max(diccProm.values())
    return (alumno,nota)        

def notaMasBaja (diccProm):
    alumno = min(diccProm.items(), key = lambda x: x[1])[0]
    nota = min(diccProm.values())
    return  (alumno,nota)     


dicc = crearEstructura(nombres,notas_1,notas_2)
dicc_prom = crearPromedio(dicc)
promedio = round(promedioCurso(dicc_prom),2)
alumno_mayor_promedio = notaMasAlta(dicc_prom)
alumno_menor_promedio = notaMasBaja(dicc_prom)
print(f" El Alumno con mayor promedio es {alumno_mayor_promedio}, y el Alumno con menor promedio es {alumno_menor_promedio}")





