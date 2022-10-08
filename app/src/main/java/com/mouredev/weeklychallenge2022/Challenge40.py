??? desde aquí hasta ???FIN las líneas pueden haber sido insertadas/borradas
/*
 * Reto #40
 * TRIÁNGULO DE PASCAL
 * Fecha publicación enunciado: 03/10/22
 * Fecha publicación resolución: 10/10/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole
 * únicamente el tamaño del lado.
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */

def resto_filas(ladoCounter,fila):
    longFila= len(fila)
    #print("long fila...",longFila)
    counter=0
    filaNew=[1]
    while longFila > counter + 1:
       # print("fila counter ",fila[counter]," fila counter+ ",fila[counter+1]," suma ",fila[counter]+fila[counter+1])
       suma = fila[counter]+fila[counter+1]
       filaNew+= [suma]
       counter+=1
    filaNew+=[1]
    #print(filaNew)
    return (filaNew)
    
    
def pascal_triangle(lado):
    ladoCounter=lado
    fila=[]
    while 0!=ladoCounter:
         if 0==lado-ladoCounter:
             fila=[1]
             print (fila)
         elif 1==lado-ladoCounter:
             fila=[1,1]
             print(fila)
         else:
             #print("resto")
             #print (len(fila))
             fila=resto_filas(ladoCounter,fila)
             #resto_filas(ladoCounter,fila)
             print(fila)
         ladoCounter-=1

print("\nTriangulo lado 5:\n")           
pascal_triangle(5)
print("\nTriangulo lado 11:\n")
pascal_triangle(11)
