# Entorno de trabajo

## Librerías R

### 1. dplyr
Es una librería de R para la manipulación de datos. Ofrece funciones para filtrar, seleccionar, modificar y resumir datos de manera eficiente y legible.

```r
install.packages("dplyr")
library(dplyr)

# Filtrar y seleccionar columnas
data(mtcars)
mtcars %>%
  filter(mpg > 20) %>%
  select(mpg, hp)

```

### 2. here

La librería ayuda a gestionar rutas de archivos en proyectos R, facilitando la creación de rutas relativas desde el directorio principal del proyecto.

```r
install.packages("here")
library(here)

# Obtener la ruta del archivo 'data.csv' en el directorio 'data'
file_path <- here("data", "data.csv")
```

### 3. foreign

Es una librería que permite leer y escribir archivos de datos en formatos de otros programas estadísticos como SPSS, SAS y Stata.

```r
install.packages("foreign")
library(foreign)

# Leer un archivo .sav 
data <- read.dta("path/to/file.sav")
```

### 4. patchwork

Es una librería que facilita la combinación de varios gráficos de `ggplot2` en una sola visualización.

```r
install.packages("patchwork")
library(ggplot2)
library(patchwork)

# Crear dos gráficos y combinarlos
p1 <- ggplot(mtcars, aes(x = mpg, y = hp)) + geom_point()
p2 <- ggplot(mtcars, aes(x = mpg, y = wt)) + geom_point()

p1 + p2
```

### 5. klaR

Es una librería que proporciona herramientas para el análisis de datos, incluyendo clasificación, análisis discriminante y visualización.

```r
install.packages("klaR")
library(klaR)

# Ejemplo: 
modes <- kmodes(categorias, 4)
View(modes)

```

## Docs

### Sphinx 

Es una herramienta de documentación para proyectos en Python, que permite generar documentación estática. Utiliza reStructuredText como su formato principal, permitiendo generar documentación en varios formatos (HTML, Latex, etc.) y soporta características avanzadas agregando extensiones. 

### MyST
Es una extensión de Sphinx que permite escribir documentación utilizando Markdown. MyST facilita la creación de documentación sencilla y accesible, mientras mantiene las características de Sphinx para generar documentación estructurada y dinámica