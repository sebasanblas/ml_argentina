#!/usr/bin/env python3

'''
--------------------------------------------------------------------------------
Machine Learning Argentina
Versión: 0.2

Sebastian San Blas
sebastiansanblas@gmail.com

2020
--------------------------------------------------------------------------------
ACLARACIÓN: este script es totalmente estadístico y carece de carácter médico.
Los valores ofrecen una estimación de cómo podrían evolucionar los acontecimientos
de mantenerse la tendencia actual.
--------------------------------------------------------------------------------
Por favor, seguir las recomendaciones básicas para evitar contagios:
    1. QUÉDATE en casa lo máximo posible.
    2. MANTÉN el distanciamiento social.
    3. LÁVATE las manos con frecuencia.
    4. TOSE o ESTORNUDA en el pliegue del codo.
    5. LLAMA a los servicios de emergencias si tienes síntomas.

Más información:
https://www.who.int/es/emergencies/diseases/novel-coronavirus-2019/advice-for-public
--------------------------------------------------------------------------------
Descripción: script para graficar y calcular diferentes modelos de machine learning
vinculados a los casos del nuevo coronavirus en Argentina.

Opciones:
    1) Graficar el total de casos confirmados de COVID-19 en Argentina o en alguna
    provincia en particular. Posteriormente, esquematizar la estimación exponencial
    de los positivos ya confirmados.
    2) Estimar la cantidad de contagios de COVID-19 que habrá en Argentina o en alguna
    provincia en un día determinado. Se incluye el error aproximado.
    3) Realizar una regresión logística para calcular la probabilidad de fallecimiento
    por edad y sexo. Este procedimiento puede llevarse a cabo considerando los datos de
    todo el país o de alguna provincia en particular.Es importante saber que la estimación
    será más precisa mientras se considere una mayor cantidad de información.
--------------------------------------------------------------------------------
'''

#Importando modulos

from datetime import datetime

from project.update_covid import update, update_datos, check_update

from project.filter_covid import datos_filtrados, datos_filtrados_provincias, provincia_id

from project.tables_covid import tabla_regresion, fecha_inicial

from project.curvefit_covid import curvefit, func_exp

from project.plots_covid import plot_curve_fit_low, plot_curve_fit_high, histograma, plot_proba

from project.reglog_covid import reg_log, clf_corregido, prediction

print(__doc__)

update()

try:
    check_update()
except OSError:
    print('Base de datos no encontrada. Se descargará de forma automática')
    update_datos()

while True:

    print('''
--------------------------------------------------------------------------------

Elija una opción:

    1)  Graficar casos confirmados de COVID-19 en Argentina, o en provincias.

    2)  Estimar la cantidad de contagios de COVID-19 que habrá en Argentina o en
    alguna provincia en un día determinado.

    3)  Regresión logística.

    info)  Obtener información sobre las opciones anteriores.
''')

    __resp__ = input("[1/2/3/info/salir]:")

    if __resp__ == "1":

        __var_covid_filtrado__ = datos_filtrados()

        ___var_tabla_prov__, __var_provincia__ = datos_filtrados_provincias(__var_covid_filtrado__)

        __input_provincia__ = provincia_id(__var_provincia__)

        __tabla__, __name_provincia__ = tabla_regresion(___var_tabla_prov__, __input_provincia__)

        __x_curve__, __y__, __y_pred__, __r2__, __a__, __b__ = curvefit(__tabla__)

        if __r2__ < 0.95:

            print('''
--------------------------------------------------------------------------------

Calidad del modelo por debajo del 95 %

Se recomienda no continuar la estimación ya que el modelo no será representativo.

¿Desea continuar?
''')

            __resp__ = input("[\"y\" para continuar]:")

            if __resp__ == "y":

                print('''
--------------------------------------------------------------------------------
''')

                plot_curve_fit_low(__x_curve__, __y__, __y_pred__, __n_p__=__name_provincia__)

                print("R cuadrado: {:.2f}".format(__r2__))
                print("")
                input("Presionar Enter para continuar...")

        if __r2__ >= 0.95:

            print('''
--------------------------------------------------------------------------------
''')
            plot_curve_fit_high(__x_curve__, __y__, __y_pred__, __r2__, __n_p__=__name_provincia__)

            print("R cuadrado: {:.2f}".format(__r2__))
            print("")
            input("Presionar Enter para continuar...")

        continue

    if  __resp__ == "2":

        __var_covid_filtrado__ = datos_filtrados()

        ___var_tabla_prov__, __var_provincia__ = datos_filtrados_provincias(__var_covid_filtrado__)

        __input_provincia__ = provincia_id(__var_provincia__)

        __tabla__, __name_provincia__ = tabla_regresion(___var_tabla_prov__, __input_provincia__)

        __fecha_init__ = fecha_inicial(___var_tabla_prov__)

        __x_curve__, __y__, __y_pred__, __r2__, __a__, __b__ = curvefit(__tabla__)

        if __r2__ < 0.95:

            print('''
--------------------------------------------------------------------------------

Calidad del modelo por debajo del 95 %.

Se recomienda no continuar la estimación ya que el modelo no será representativo.

¿Desea continuar?
''')

            __resp__ = input("[\"y\" para continuar]:")

            if __resp__ == "y":

                print('''
--------------------------------------------------------------------------------
''')

                print("R cuadrado: {:.2f}".format(__r2__))
                print("")
                YYYY = input('Inserte año (Ej 2020): ')
                MM = input('Inserte mes (Ej 08): ')
                DAY = input('Inserte día (Ej 09): ')
                __fecha_final__ = YYYY +'-'+ MM +'-'+ DAY
                __fecha_final_datetime__ = datetime.strptime(__fecha_final__, '%Y-%m-%d')
                X_INPUT = __fecha_final_datetime__ - datetime.strptime(__fecha_init__, '%Y-%m-%d')
                __x__ = X_INPUT.days
                Y_INPUT = func_exp(__x__=__x__, __fea__=__a__, __feb__=__b__)
                print("")
                print("Estimación de casos acumulados para el día {}: {} personas"
                      .format(__fecha_final_datetime__, int(Y_INPUT)))
                print("")
                input("Presionar Enter para continuar...")

        if __r2__ >= 0.95:

            print('''
--------------------------------------------------------------------------------
''')

            print("R cuadrado: {:.2f}".format(__r2__))
            print("")
            YYYY = input('Inserte año (Ej 2020): ')
            MM = input('Inserte mes (Ej 08): ')
            DAY = input('Inserte día (Ej 03): ')
            __fecha_final__ = YYYY +'-'+ MM +'-'+ DAY
            __fecha_final_datetime__ = datetime.strptime(__fecha_final__, '%Y-%m-%d')
            X_INPUT = __fecha_final_datetime__ - datetime.strptime(__fecha_init__, '%Y-%m-%d')
            __x__ = X_INPUT.days
            Y_INPUT = func_exp(__x__=__x__, __fea__=__a__, __feb__=__b__)
            print("")
            print("Estimación de casos acumulados para el día {}: {} personas"
                  .format(__fecha_final_datetime__, int(Y_INPUT)))
            print("")
            input("Presionar Enter para continuar...")

        continue

    if __resp__ == "3":

        __var_covid_filtrado__ = datos_filtrados()

        ___var_tabla_prov__, __var_provincia__ = datos_filtrados_provincias(__var_covid_filtrado__)

        __tabla__, __x__, __y__ = reg_log(___var_tabla_prov__)

        __input_provincia__ = provincia_id(__var_provincia__)

        histograma(__tabla__, __input_provincia__)
        print('')
        print("Se calculará el modelo predictivo, requiere tiempo")
        input("Presionar Enter para continuar...")

        __clf__ = clf_corregido(__x__, __y__)

        plot_proba(__clf__, __input_provincia__)

        print("¿Desea predecir probabilidad de fallecimiento?")
        print('')
        __resp_3__ = input("[S] ó Enter para salir:")
        print('')
        if __resp_3__ in ("S", "s"):

            prediction(__clf__)

        input("Presionar Enter para continuar...")

    if __resp__ in ("info", "i"):

        print('''
1) Graficar el total de casos confirmados de COVID-19 en Argentina o en alguna
provincia en particular. Posteriormente, esquematizar la estimación exponencial
de los positivos ya confirmados.

2) Estimar la cantidad de contagios de COVID-19 que habrá en Argentina o en alguna
provincia en un día determinado. Se incluye el error aproximado.

3) Realizar una regresión logística para calcular la probabilidad de fallecimiento
por edad y sexo. Este procedimiento puede llevarse a cabo considerando los datos de
todo el país o de alguna provincia en particular.Es importante saber que la estimación
será más precisa mientras se considere una mayor cantidad de información.
    ''')
        input("Presionar Enter para continuar...")
        continue

    if __resp__ in ("salir", "s"):

        print('''
--------------------------------------------------------------------------------

Gracias.

--------------------------------------------------------------------------------
''')

        break

    print('''
--------------------------------------------------------------------------------

Opción invalida.
''')
