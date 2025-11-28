# Biblioteca Virtual - CRUD con Python y MySQL

Este proyecto es un sistema CRUD para la gestión de libros,
desarrollado en Python con conexión a MySQL utilizando DJANGO COMO FREAMEWORK.

## Funcionalidades
- Registrar libros
- Listar libros
- Actualizar libros
- Eliminar libros
- Registrar ventas
- Evitar ventas con stock insuficiente
- Actualizar stock automáticamente
- Restaurar stock al eliminar ventas

## Requisitos
- Python 3.10+
- mysql-connector-python
- MySQL/XAMPP

## Ejecución
python -m venv venv

venv\Scripts\activate      # Windows

# INSTALAR DEPENDENCIAS
pip install -r requirements.txt

# REALIZAR MIGRACIONES

python manage.py migrate

# EJECUTAR EL SERVIDOR

python manage.py runserver

