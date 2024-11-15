# Exploración inicial

## Contexto 

El Ministerio de Educación de Guatemala (MINEDUC)  a través de la Dirección General de Evaluación e Investigación Educativa (DIGEDUCA) realiza anualmente una evaluación a los graduandos de nivel diversificado para medir su rendimiento sus en matemáticas así como en lenguaje y compresión lectora. 

Es una evaluación diagnostica que  deben realizar todos los estudiantes que están por graduarse, tiene objetivo de establecer en que medida los estudiantes lograron alcanzar los objetivos de aprendizaje, recolectar información sobre el estado del sistema educativo de Guatemala e identificar líneas de acción para mejorarlo. 

Durante la pandemia de COVID-19 no fue posible realizar esta evaluación, en su lugar se utilizaron otras herramientas por lo que no hay disponibles datos para los años 2020 y 2021.

## Conjunto de datos

Los datos pueden ser obtenidos en la sección de [resultados de las evaluaciones](https://edu.mineduc.gob.gt/digeduca/?p=resultadosevaluacionesMain.asp) de la página web del MINEDUC, cada conjunto de datos esta disponible por año, en formato `.xlsx`, `.xls.` o `.sav`, junto su diccionario de variables; para esta exploración básica se tomaron los datos de los años 2023, 2022 y 2019.

Utilizando el lenguaje de programación R se cargaron, limpiaron y serializaron los datos, esto último para recuperarlos de forma más rápida en diferentes scripts. Abajo se muestra la cantidad de registros de cada uno de los *datasets* que representan la cantidad de estudiantes evaluados ese año. 

Los datos del 2022 difieren en varios aspectos comparado con los otros dos años debido a ser este conjunto al que corresponde a la primera evaluación luego de la pandemia, mas adelante se hablara de esto, pero se pudo ver que este año se cuenta con registros con una sola evaluación matemática o lectura, posiblemente por esto pueda atribuirse a que un grupo de estudiantes se evaluó unicamente en una sola area matemáticas o lectura.. 

```r
# Datos 2023
[1] "Total estudiantes: 144899"

# DAtos 2022
[1] "Total estudiantes: 136144"
[1] "Evaluaciones mate: 135285"
[1] "Evaluaciones lect: 131358"

# Datos 2019
[1] "Total estudiantes: 163825"
```

## Variables de interés  

Los datos para cada año cuentan con una gran cantidad de variables la gran mayoría categóricas, también difiere el número de variables disponibles el 2023 cuenta con 74, el 2022 con 276 y e 2019 con 185. En el 2022 al realizarse la primera evaluación después la pandemia se agregaron variables asociadas a las condiciones de la educación en ese momento, como por ejemplo la forma de acceder a internet o el uso de plataformas virtuales (Zoom, Google Meet, etc.) es debido a ello la mayor diferencia de variables. 

Debido a la cantidad de datos disponible, que requiere una cantidad de tiempo y recursos considerable si se desean analizar en profundidad, se seleccionaron algunas variables para limitar la cantidad de información.

Al revisar las descripciones de los datos para cada año se podría clasificar las variables dentro de alguna de las siguientes categorías.

- Identificación (por código de estudiante, establecimientos, etc)
- Ubicación
- Aspectos socioeconómicos
- Aspectos educativos
- Resultados

A continuación se muestran ejemplos de las variables que conforman los, sobre las que podría encontrarse relaciones para comprender mejor los resultados obtenidos en las evaluaciones. Las variables para aplicar los algoritmos solicitados en el trabajo serán escogidas  por representar de alguna manera las categorías antes mencionadas. 

```{list-table}
:header-rows: 1
* - Variable
  - Descripción
* - Logro_Lect
  - Logro en Lectura
* - Logro_Mate
  - Logro en Matemáticas
* - Desempeño_Mate
  - Desempeño en Matemáticas
* - Desempeño_Lect
  - Desempeño en Lectura
* - Cod_Region
  - Código de Región donde se encuentra ubicado el Establecimiento
* - Jornada
  - Jornada del Establecimiento
* - Cod_Sector
  - Sector del Establecimiento(privado, oficial, ...)
* - CC_Familia_Automovil
  - ¿Su familia tiene vehículo propio?
* - Edad_RECO
  - Edad del Estudiante (Recodificada en Intervalos)
* - Sexo_RECO
  - Código Género del Estudiante
* - Cod_Area
  - Código del Área del Establecimiento (urbano, rural)
* - Fm_Grado_Alcanzo_Papa_RECO
  - Marque el grado más alto que completó su papá.
* - Fm_Grado_Alcanzo_Mama_RECO
  - Marque el grado más alto que completó su mamá.
* - Ed_Repitio_Algun_Grado
  - ¿Repitió algún grado?
* - Sc_Servicio_Internet
  - Servicios que tiene en su casa: Internet 
* - Tipo_Eval
  - Tipo de Evaluación (en línea, presencial)
```

## Descripción

Mediante la aplicación de la función `summary()` de R, para describir rápidamente los datos, en este caso se obtienen por consola las tablas de frecuencias para las variables, como se muestra a continuación de forma recordada. 

```console
Cod_Region                       Edad_Reco                CC_Servicio_Internet
Región 1 o Metropolitana:59512   16 años o Menos :18486   No  :92627
Región 6 o Suroccidental:35846   17 años         :44933   Si  :70069
Región 5 o Central      :18572   18 años         :44144   NA's: 1129
Región 4 o Suroriental  :12812   19 años         :21464
Región 3 o Nororiental  :11985   20 años         :10735
Región 7 o Noroccidental:10766   Mayor de 20 años:24040
(Other)                 :14332   NA's            :   23
```
### Observaciones

Con las tablas de frecuencia se puede hacer algunas observaciones rápidas sobre la información en distintos años. 

- Para los tres años la mayoría de los estudiantes evaluados corresponde a la región Metropolitana. 
- La mayoría de los estudiantes tienen una edad entre 17 y 18 años al momento de graduarse.
- Para el año 2019 la mayoría de los estudiante indicaron no tener servicio de internet en su casa, esta variable se invierte para los años 2022 y 2023. 
- Para los años 2023 y 2022 la mayoría de los estudiantes evaluados pertenecen al sector privado, también la mayoría para ambos años fuero evaluados en línea. Las variables que indican sector y tipo de evaluación no están presentes en los datos del año 2019. 
- Durante los tres años la mayoría de los estudiante evaluados estudiaron en el sector privado.

## Desempeño

Debido a que el objetivo de este trabajo es aplicar los los algoritmos mencionados previamente para buscar relaciones en los datos, se hace evidente que la mejor forma de abordarlo es buscando relaciones que expliquen los resultados de desempeño de los estudiantes en la prueba o si se logró aprobar la misma. 

Por ello a continuación en las figuras [1.1](#g2023), [1.2](#g2022) y [1.3](#g2019) se presentan gráficos de los resultados obtenidos en los tres años para ayudar a orientar la búsqueda de relaciones en la información.

```{figure} ../_static/img/g2023.png
:name: g2023
:align: center
:width: 650px

Resultados de evaluaciones 2023
```
En los tres años se puede observar como la mayoría de estudiantes obtienen resultados insatisfactorios en ambas evaluaciones siendo el porcentaje de aprobación más alto los para lectura que para matemáticas. Se puede observar como el porcentaje de aprobación en lectura decayó del año 2019 al 2022 con la pandemia de por medio y de 2022 al 2023 bajo el porcentaje de aprobación para matemática. 

```{figure} ../_static/img/g2022.png
:name: g2022
:align: center
:width: 650px
Resultados de evaluaciones 2022
```
```{figure} ../_static/img/g2019.png
:name: g2019
:align: center
:width: 650px
Resultados de evaluaciones 2019
```
