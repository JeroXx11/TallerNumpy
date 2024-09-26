import numpy as np
import matplotlib.pyplot as plt
x = np.random.randint(0,100, size = 720)
j,k = 120,6

Matriz = x.reshape(j,k)
Matriz_f = x.reshape(j,k, order= "F")

Matriz_transpuesta= Matriz.T
Matriz_transpuestaF = Matriz_f.T

ej1=plt.axes([0,0, 0.3,0.3])
ej2=plt.axes([0.4,0, 0.3,0.3])
ej3=plt.axes([0,0.4, 0.3,0.3])
ej4=plt.axes([0.4,0.4, 0.3,0.3])
ej5=plt.axes([0.8,0, 0.3,0.3])
ej6=plt.axes([0.8,0.4,0.3,0.3])

Matriz1 = Matriz_transpuesta[0,]
Matriz2 = Matriz_transpuesta[1,]
Matriz3 = Matriz_transpuesta[2,]
Matriz4 = Matriz_transpuesta[3,]
Matriz5 = Matriz_transpuesta[4,]
Matriz6 = Matriz_transpuesta[5,]

ej1.plot(Matriz1, label = "Fila 1")

ej2.scatter(np.arange(len(Matriz2)), Matriz2, color = "b", label = "Fila 2")

error = np.random.rand(len(Matriz3))*5
ej3.errorbar(np.arange(len(Matriz3)),Matriz3,yerr = error,fmt='o', color='green', label = "Fila 3")

ej4.hist(Matriz4, label = "Fila 4")

labels = [f'Sección {i+1}' for i in range(len(Matriz5))]
ej5.pie(Matriz5, labels = labels, autopct = '%1.1f%%')

ej6.plot(Matriz6, color = "m", label = "Fila 6")

ej1.legend(loc='upper right')
ej2.legend(loc='upper right')
ej3.legend(loc='upper right')
ej4.legend(loc='upper right')
ej6.legend(loc='upper right')

plt.show()
