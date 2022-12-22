import sqlite3
import matplotlib.pyplot as plt

def grafica():
    agraf = input('Ingrese el Ticker a Graficar:')
    con = sqlite3.connect("dbacciones")
    cursor = con.cursor()
    cursor.execute(f'SELECT Fecha, Volumen, PrecioCierre FROM {agraf};')
    fechasacc = cursor.fetchall()
    Fecha = []
    Volumen = []
    ValorCierre = []
    for j in fechasacc:
        Fecha.append(j[0])
        Volumen.append(j[1])
        ValorCierre.append(j[2])
    #print(Fecha)
    #print(Volumen)
    con.close()

    plt.subplot(2, 1, 1)
    plt.bar(Fecha, Volumen)
    #plt.ylim(0, 5)
    plt.xlabel("Fecha")
    plt.ylabel("Volumen")
    plt.title("VOLUMEN")
    plt.subplot(2, 1, 2)
    plt.plot(Fecha, ValorCierre)
    #plt.ylim(0, 5)
    plt.xlabel("Fecha")
    plt.ylabel("Valor de Cierre")
    plt.title("PRECIO DE CIERRE")
    plt.suptitle(f"TICKER DE {agraf}")
    plt.show()
    
    return None