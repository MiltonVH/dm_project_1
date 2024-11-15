
# Reglas de asociación

Dado que la mayoría de los estudiantes fallaron las evaluaciones, se buscaron reglas de asociación primero con el los datos sin segmentar y luego enfocándose en los estudies que obtuviera buenos resultados para buscar asociaciones que explique su existo en la prueba.

## Apriori

Al buscar reglas de asociación con los datos sin segmentarlos, debido a la diversidad y cantidad de información, las reglas con mayor soporte que encuentra el algoritmo son simples y que se podrían buscar por otros medios. Aquellas reglas más complejas que asocian varias variables tiene poco soporte pero aún así aportan algo de información sobre los datos. 

Debido la mayoría de los estudiantes no lograron buenos resultados en ambas pruebas, el algoritmo sin filtrar, asocia distintas variables con un resultado negativo en matemáticas más que con resultado negativo en lectura dado que los estudiantes fallan mas frecuentemente la prueba de matemática que la de lectura.

-  **Regla 1**

    ```r
    # Año 2023
    {Sc_Electricidad=Si} => {Cod_Area=Urbana}
    0.8214097 0.8744000 0.9393981 1.0045790 113679

    {Ed_Asistio_Preprimaria=Si, Sc_Electricidad=Si} => {Logro_Mate=No Logro} 
    0.7404964 0.8933765 0.8288739 0.9922223 102481
    ```
    Reglas como las mostradas arriba son las que indican mayor soporte el conjunto de datos para el año 2023, sabiendo que la mayoría de los estudiantes evaluados están ubicados en la región metropolitana o en una área urbana es de esperarse que la mayoría cuente con servicios básicos como la electricidad. La siguiente una asociación un poco inesperada sobre haber cursado preprimaria y la falla en la prueba en matemáticas. Debido al alto porcentaje de fallo en la prueba (90%) no se puede afirma con certeza y habría que realizar mas análisis en esa dirección pero se podría hacer la observación de que haber la iniciado vida estudiantil a temprana edad no refleja un mejor resultado en la evaluación.

-  **Regla 2**

    ```r
    # Año 2023
    {Ed_Asistio_Preprimaria=Si,Sc_Electricidad=Si,Computadora=Si,
    Cod_Area=Urbana, Sc_Servicio_Internet=Si,Grad_Seguir_Estudiando=SI} 
    => {Logro_Mate=No Logro} 
    0.3256259 0.8412515 0.3870732 0.9343300 4506

    ```
    Entre las reglas que asocian una mayor cantidad de variables pero con menos soporte, se muestra esta regla con un conjunto de variables que se podría pensar estaría asociadas a un mejor resultado pero mas bien están asociadas a un resultado negativo. Nos muestra que una parte de los estudiantes a pesar de contar con algunos recursos tecnológicos (computadora, acceso a internet) y con la intención de continuar sus estudios obtuvieron un resultado negativo. 

-  **Regla 3**

    ```r
    {Ed_Asistio_Preprimaria=Si, Computadora=Si, Sc_Servicio_Internet=Si,
    Grad_Seguir_Estudiando=SI, Lectura_Gusto=Si} => {Cod_Area=Urbana}
    0.3474337 0.8832192 0.3933720 1.0648264 2579
    ```
    Al filtrar los datos para el sector *Oficial* (Estatal) y para buscar asociaciones dentro del grupo de alumnos que aprobó el examen de lectura resalta la asociaciones sobre el area del establecimiento, como la mostrada que no indica que sabiendo que el estudiante logró aprobar la evaluación de lectura, con acceso a algunos recursos tecnológicos y con la intención de seguir estudiante pertenece al área urbana.  

-  **Regla 4**

    ```r
    {Logro_Lect=Logro} => {Computadora=Si} 
    0.6850520 0.8561439 0.8001599 1.0418638 857

    {Computadora=Si,Cod_Area=Urbana,Sc_Servicio_Internet=Si,
    Grad_Seguir_Estudiando=SI} => {Logro_Lect=Logro}
    0.4700240 0.8724036 0.5387690 1.0902866 588
    ```
    Buscando relaciones con los estudiantes que ganaron la prueba de matemática y pertenecen al sector *Oficial* se puede ver como el acceso a la tecnología pueda favorecer obtener un buen resultado en la prueba, también que en general los estudiantes que obtuvieron un buen resultado en matemática también lo hicieron en lectura pero esta asociación no existe en la otra dirección.


## FP-Growth

Al igual que sucede con el algoritmo apriori las reglas obtenidas con FP-Growth que tienen un mayor confianza y soporte son evidente o aportan poca información adicional. 

-  **Regla 1**

    ```r
    {Logro_Lect=No Logro} => {Logro_Mate=No Logro}
    0.6672640 0.9757402 1.0836990 92346 1026
    ```
    Esta regla muestra como hay asociaciones entre fallar las pruebas, parece implicar que si un alumno no es capaz de aprobar la prueba de lectura seguramente falle en la de matemáticas. Los datos muestran como hay un porcentaje de probación mas alto en la prueba de lectura, podría indicar que aprobar esta prueba es más fácil que la de matemáticas.

-  **Regla 2**

    ```r
    {Ed_Asistio_Preprimaria=Si, Cod_Sector=Privado,
    CC_Material_Predomina_En_Piso_Casa=Piso cerámico} => {Cod_Area=Urbana}
    0.3630333 0.9225317 1.0598765 50242
    ```
    Con datos sin segmentar se encuentra esta asociación. Se sabe que la mayoría de los estudiantes que se someten a la evaluación pertenecen al sector privado y con uns cuantas condiciones adicionales en general su establecimiento se encuentra ubicando en un área urbana. Dentro de la gran cantidad de reglas que muestra FP-Growth muchas relación las condiciones de los estudiantes con el sector privado y el área urbana indicando que existe poca representación de los otro sectores y del area rural en el conjunto de dato. 

-  **Regla 3**

    ```r
    Ed_Trabaja_Actualmente=No,Sc_Servicio_Internet=Si,Identificacion_Etnica_RECO=Ladino} 
    => {Ed_Repitio_Algun_Grado=No}
    0.3600970 0.8129562 1.0822407 2673
    ```
    Filtrando  los datos, tomando solo estudiantes que aprobaron lectura y pertenecen al sector **oficial**, surge la asociación que nos indica con un soporte  bajo que si un estudian aprueba el examen de lectura y además cuenta con unos recursos mínimos (económicos y tecnológicos) seguramente nunca repitió un año escolar.  

- **Regla 4**

    ```r

    {Logro_Lect=Logro,Ed_Asistio_Preprimaria=Si,Ed_Trabaja_Actualmente=No,
    Computadora=Si} => {Ed_Repitio_Algun_Grado=No}
    0.3501199 0.8358779 1.0995617 438
    ```
    Nuevamente esta regl,  como una condición de aprobación  de matemática y pertenencia al sector **Oficial**, nos indica que si un estudiante aprobó ambas evaluaciones y además cuenta con unos recursos mínimos (económicos y tecnológicos) no repitió un año escolar. Estas dos últimas reglas muestra asociación entre  entre la variable de renitencia y la aprobación tanto en la prueba de lectura como en la matemática.  