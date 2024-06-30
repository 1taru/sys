# Tarea 3 Sistemas distribuidos

Este es un simulador de sistema de archivos simple que permite crear, eliminar, renombrar y navegar por directorios y archivos. También incluye funcionalidades para cambiar permisos, listar archivos, buscar archivos por nombre, visualizar la metadata y mantener un historial de comandos, donde es posible interactuar con este historial.

## Características

- Crear y eliminar archivos y directorios
- Renombrar archivos y directorios
- Navegar entre directorios
- Cambiar permisos de archivos y directorios
- Listar archivos en el directorio actual
- Mostrar metadata de archivos
- Buscar archivos y directorios por nombre
- Mantener un historial de comandos navegable con flechas del teclado y por índice

## Instalación

1. Descarga el repositorio
2. Entra al directorio del proyecto:
    ```bash
    cd tarea3_so
    ```
3. Instalar la biblioteca `readline`. En ubuntu y basados:
    ```bash
    sudo apt-get install libreadline-dev
    ```
    En red hat y basados:
    ```bash
    sudo dnf install readline-devel
    ```

## Compilación

Compila el programa con el siguiente comando:
```bash
gcc tarea3_so.c -o tarea3 -lreadline
```
Luego se ejecuta mediante:
```bash
    ./tarea3
```
# Lista de comandos escenciales
visualizacion de comandos:
```bash
    help
```
creacion de directorios:
```bash
    mkdir <nombre_archivo>
```
acceso a carpeta:
```bash
    cd <nombre_carpeta>
```
creacion de archivo:
```bash
    touch <nombre_archivo>
```
cambio de permisos archivo/directorio :
```bash
    chmod <nombre_archivo> <permisos>
```
Renombre de archivo/directorio :
```bash
    ren <nombre_antiguo> <nombre_nuevo>
```
Remocion de archivo:
```bash
    rm <nombre_archivo>
```
Remocion de directorio y contenido de este recursivamente:
```bash
    rm-f <nombre_directorio>
```
Listar archivos en ruta actual:
```bash
    ls
```
Listar archivos con identificador de i-nodo
```bash
    ls-i
```
Mostrar metadata de archivos:
```bash
    metadata
```
Busqueda de archivos/directorios por nombre:
```bash
    buscar <nombre_a_buscar>
```
Mostrar historial:
```bash
    historial
```
