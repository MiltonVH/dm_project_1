# Agrupación

Como en su mayoría las variables con las que cuenta el conjunto de datos son de tipo categórico, preguntas SI /NO o selección de la categoría más cercana,  el algoritmo K-Means no es el más adecuado para generar clústeres, este algoritmo espera tipos de datos numéricos como parámetros de ingreso y se base en calcular la distancia euclidiana entre puntos lo cual no tiene mucho sentido para datos categóricos. 

## K - Means

En figura [4](#gkmeans) se puede observar una gráfica con las únicas variables numéricas en los datos al aplicar K-Means junto con otras variables (convertidas a enteros) se puede ver que estas formaron clústeres muy cercanos al mismo punto. No es posible obtener mayores conclusiones de esta gráfica mas allá habilidad estimada para la mayoría de estudiante esta cerca del valor cero en ambas materias. 

```{figure} ../_static/img/kmeans.png
:name: gkmeans
:align: center
:width: 320px
Agrupación mediante K-Means
```

## K - Modes

Se utilizó el algoritmo K-Modes que esta diseñado para trabajar con datos categóricos ya que utiliza métricas de distancia adecuadas para datos categóricos, este calcula el centroide como el valor más frecuente para cada atributo en el cluster.

En las figuras [5](#gkmodes0) y [6](#gkmodes1) se puede ver los resultados de K-Modes en la primera se observa como los datos forma un grupo con que contiene a los estudiantes con mejor desempeño con los datos sin segmentar. 

```{figure} ../_static/img/kmodes_0.png
:name: gkmodes0
:align: center
:width: 550px
K-Modes con datos sin segmentar
```
En la segunda se aplico un filtro para utilizar solamente los datos de los estudiante que ganaron alguna de las evaluaciones (logro en mate o en lectura) se puede ver como los datos nuevamente logran separar a los estudiantes con los mejores resultados.

```{figure} ../_static/img/kmodes_1.png
:name: gkmodes1
:align: center
:width: 550px
K-Modes con estudiantes que obtuvieron al menos un logro
```

###  Observaciones

Al observar la tabla [1](#tabla-1) que muestra los cinco modos que fue capas de encontrar el algoritmo sobre la los datos, se puede hacer algunas observaciones como:

- Los estudiantes con obtiene resultados tienden a tener padres con educación (diversificada o universitaria).
- Los estudiantes que logran aprobar ambos evaluaciones tienden a indicar que cuenta con cinco periodos de clase en ambas materias a la semana.
- Por lo general los estudiantes que aprueban alguna evaluación están ubicando en la Ciudad Capital. \

:::{list-table} Agrupaciones de estudiantes que obtuvieron al menos un logro
:name: tabla-1
:header-rows: 1

* - Variable
  - g1
  - g2
  - g3
  - g4
  - g5
* - Logro_Mate
  - Logro
  - Logro
  - Logro
  - No Logro
  - No Logro
* - Logro_Lect
  - Logro
  - Logro
  - No Logro
  - Logro
  - Logro
* - Ed_Asistio_Preprimaria
  - Si
  - Si
  - Si
  - Si
  - Si
* - Sc_Electricidad
  - Si
  - Si
  - Si
  - Si
  - Si
* - Desempeño_Mate
  - Excelente
  - Excelente
  - Satisfactorio
  - Insatisfactorio
  - Debe Mejorar
* - Desempeño_Lect
  - Excelente
  - Excelente
  - Debe Mejorar
  - Excelente
  - Satisfactorio
* - Cod_Depa
  - Ciudad Capital
  - Ciudad Capital
  - Ciudad Capital
  - Guatemala
  - Ciudad Capital
* - Lect_Periodos_Lectura_Semana
  - 5 Períodos
  - Ninguno
  - 1 Período
  - Ninguno
  - Ninguno
* - Mate_Periodos_Matematicas_Semana
  - Cinco periodos
  - Cuatro periodos
  - Cinco periodos
  - Ninguno
  - Cinco periodos
* - Jornada
  - Matutina
  - Matutina
  - Matutina
  - Vespertina
  - Matutina
* - Ed_Trabaja_Actualmente
  - No
  - No
  - No
  - No
  - No
* - Cod_Sector
  - Privado
  - Privado
  - Privado
  - Privado
  - Privado
* - CC_Material_Predomina_En_Piso_Casa
  - Piso cerámico
  - Torta de cemento
  - Piso cerámico
  - Torta de cemento
  - Piso cerámico
* - Computadora
  - Si
  - Si
  - Si
  - Si
  - Si
* - CC_Familia_Automovil
  - Si
  - No
  - Si
  - Si
  - Si
* - Edad_RECO
  - 17 años
  - 18 años
  - 17 años
  - 18 años
  - 17 años
* - Sexo_RECO
  - Masculino
  - Femenino
  - Masculino
  - Femenino
  - Masculino
* - Cod_Area
  - Urbana
  - Urbana
  - Urbana
  - Urbana
  - Urbana
* - Sc_Servicio_Internet
  - Si
  - Si
  - Si
  - Si
  - Si
* - Fm_Grado_Alcanzo_Papa_RECO
  - Universidad o más
  - Diversificado
  - Primaria
  - Primaria
  - Universidad o más
* - Fm_Grado_Alcanzo_Mama_RECO
  - Diversificado
  - Primaria
  - Primaria
  - Primaria
  - Universidad o más
* - Grad_Trabajar
  - SI
  - SI
  - SI
  - SI
  - SI
* - Grad_Seguir_Estudiando
  - SI
  - SI
  - SI
  - SI
  - SI
* - Lectura_Gusto
  - Si
  - Si
  - Si
  - Si
  - Si
* - Identificacion_Etnica_RECO
  - Ladino
  - Ladino
  - Ladino
  - Ladino
  - Ladino
* - Lect_Libros_Completos_Ha_Leido
  - Dos libros
  - Dos libros
  - Un libro
  - Un libro
  - Dos libros
* - Tipo_Eval
  - Linea
  - Linea
  - Linea
  - Linea
  - Linea
* - Ed_Repitio_Algun_Grado
  - No
  - No
  - No
  - No
  - No
:::


