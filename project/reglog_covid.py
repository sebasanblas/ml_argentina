#!/usr/bin/env python3

'''
Función para calcular la probabilidad de fallecimiento, basandose en la edad del
paciente y en su sexo. Se aplica primero el modelo de regresión logistica, sin
penalizaciones.
Ya que la distribución de datos, al día 30/06 esta de forma desbalanceada, comparando
las personas fallecidas vs personas con el virus activo, se procede a balancear los datos
por diferentes metologías, priorizando el valor que me aporte un "recall"(clase que expresa
cuan bien puede el modelo detectar a esa clase) más alto de casos de fallecimiento.
Posteriormente, se grafica dicha probabilidad.
'''

try:

    import pandas as pd
    import numpy as np

    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import classification_report
    from sklearn.metrics import precision_recall_fscore_support as score
    from imblearn.under_sampling import NearMiss

except ImportError:

    raise ImportError('No se pudieron importar los modulos necesarios!')

def reg_log(tabla):

    '''Función para calcular regresión logistica, sobre casos confirmados'''

    tabla_2 = tabla.loc[tabla['clasificacion_resumen'] == 'Confirmado']

    tabla_3 = tabla_2[tabla_2['sexo'].isin(['M', 'F'])]

    tabla_3["sexo"] = tabla_3["sexo"].map(GEN_)

    tabla_3["fallecido"] = tabla_3["fallecido"].map(FALL_)

    x_tabla = tabla_3.iloc[:, :2]

    x_tabla = x_tabla.values.reshape(-1, 2)

    x_orig = np.nan_to_num(x_tabla)

    y_orig = tabla_3['fallecido']

    return tabla_3, x_orig, y_orig

def clf_corregido(x_orig, y_orig):

    '''Función que se utiliza para corregir el desbalance sufrido por los datos'''

    nearmiss = NearMiss(sampling_strategy=0.20, n_neighbors=3, version=2)
    x_us, y_us = nearmiss.fit_resample(x_orig, y_orig)
    clf_us = LogisticRegression(random_state=0, class_weight='balanced').fit(x_us, y_us)
    y_clf_us = clf_us.predict(x_orig)

    print('''
--------------------------------------------------------------------------------

''')
    print(classification_report(y_orig, y_clf_us))

    _, recall_corregido, _, _ = score(y_orig, y_clf_us)

    recall_corregido_prom = (recall_corregido[0]+recall_corregido[1])/2

    DICC_['clf_corregido'] = recall_corregido_prom

    return clf_us

def prediction(clf):

    '''Funcion que se encarga de la predicción de probabilidad de fallecimiento'''

    sexo = int(input("Sexo[0:Femenino/1:Masculino]: "))
    print('')
    edad = int(input("Edad: "))

    pred = clf.predict_proba([[sexo, edad]])[0][1]
    print('')
    print("Probabilidad de fallecimiento para persona de sexo {}, de {} años de edad: {:.2%}"
          .format(sexo, edad, pred))
    print('')
##Constantes
pd.set_option('mode.chained_assignment', None)
GEN_ = {'M': 1, 'F': 0}
FALL_ = {'SI': 1, 'NO': 0}
DICC_ = {}
