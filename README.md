# Machine Learning Argentina

Repositorio creado por Sebastian San Blas.

Script para calcular diferentes modelos de machine learning sobre los casos de Covid-19 en Argentina.

## ¿Qué se puede realizar con este script?

1. Visualización de los casos positivos, por día, en el país o por provincias.
2. Estimar ecuación que se ajuste a los casos ya confirmados.
3. Estimación exponencial de casos de forma acumulativa.
4. Regresión logística (Edad/Sexo)(Probabilidad de fallecimiento) **Próximamente**

## ¿Cómo ejecutar?

Dar permisos de ejecución `chmod +x ml_argentina.py`

Ejecutar `./ml_argentina.py`

## Data

Los datos históricos provienen de la página oficial del Ministerio de Salud.

### Descarga y uso de datos

Es posible [__Descargar el CSV de datos históricos Oficiales__](https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Determinaciones.csv).

Para poder entender las columnas del archivo .csv, [__ver "campos de este recurso"__](http://datos.salud.gob.ar/dataset/covid-19-casos-registrados-en-la-republica-argentina/archivo/fd657d02-a33a-498b-a91b-2ef1a68b8d16).

## Todo

    * Agregar función independiente para estimar paciente confirmados en determinado
    día (opción 2).
    * Agregar función para regresión logística (opción 3).
    * Corrección de docstrings en funciones.
    * Completar documentación.
    * Completar test de funciones.
----------------------------------------------------------------------------
## Licencia

El trabajo se publica bajo licencia  Atribución-NoComercial 4.0 Internacional (CC BY-NC 4.0).
Ver [Licencia CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode) para mayor detalles.

## Sugerencias

Son más que bienvenidas!

Para correcciones de errores, sugerencias o alguna función adicional, por favor contáctame a sebastiansanblas@gmail.com o [@sebasanblas1](https://twitter.com/SebaSanBlas1).

Gracias.
