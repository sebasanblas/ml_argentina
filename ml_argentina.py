#!/usr/bin/env python3

'''
Aplicar diferentes modelos de Machine Learning a los casos de COVID-19, en Argentina.
(ampliar)
'''

#Importando modulos

from project.update_covid import update

from project.filter_covid import datos_filtrados, datos_filtrados_provincias, provincia_id

from project.tables_covid import tabla_regresion

from project.curvefit_covid import curvefit

###################################

update()

while True:

    print('''
-----------------------------------------------------------

Elija una opción:

    Estimación exponencial de casos - 1

    Regresión logística (Edad/Sexo)(Probabilidad de fallecimiento) - 2
''')

    __resp__ = input("[1/2/info/salir]:")

    if __resp__ == "1":

        __var_covid_filtrado__ = datos_filtrados()

        ___var_tabla_prov__, __var_provincia__ = datos_filtrados_provincias(__var_covid_filtrado__)

        __input_provincia__ = provincia_id(__var_provincia__)

        __tabla__, __name_provincia__ = tabla_regresion(___var_tabla_prov__, __input_provincia__)

        curvefit(__tabla__, __name_provincia__)

        continue

    if  __resp__ == "2":

        print("-------")
        print("Todavia no esta listo ;)")
        print("-------")

        continue

    if __resp__ in ("info", "i"):

        print("-------")
        print("Todavia no esta listo ;)")
        print("-------")

        continue

    if __resp__ in ("salir", "s"):

        print("Gracias")

        break

    print("Opción invalida")
