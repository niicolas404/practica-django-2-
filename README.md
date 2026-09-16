# Peliplus - Django

Proyecto Django simple para mostrar una cartelera de películas usando una lista de diccionarios en `views.py`, sin base de datos ni modelos.

## Requisitos

- Python 3.10 o superior
- Git
- Entorno de desarrollo con acceso a la terminal

## Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/practica-django-2-.git
cd practica-django-2-
```

## Crear entorno virtual

En Windows:

```bash
py -m venv .venv
.venv\Scripts\activate
```

En macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Instalar dependencias

```bash
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

Si no existe el archivo `requirements.txt`, puedes instalar Django y demás dependencias manualmente:

```bash
py -m pip install Django==5.2.7
```

## Aplicar migraciones

Este proyecto no usa base de datos real ni modelos propios, por lo que no es necesario ejecutar migraciones. Si deseas validar la configuración base del proyecto:

```bash
py manage.py check
```

## Ejecutar el proyecto

```bash
py manage.py runserver
```

Luego abre en el navegador:

```text
http://127.0.0.1:8000/
```

## Rutas disponibles

- Inicio: `/`
- Detalle por película: `/<pelicula>/<int:id>/`

## Estructura principal

```text
practica-django-2-
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shop/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── shop/
├── static/
│   ├── css/
│   └── imagenes/
├── templates/
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

## Nota importante

- El proyecto usa archivos HTML en `templates/` y una lista de diccionarios en `shop/views.py`.
- No se usa base de datos ni `models.py`.
- La imagen del logo se encuentra en `static/imagenes/logo.png`.
- La imagen por defecto para cada película está en `static/imagenes/paquete.png`.

## Problemas comunes

### 1. El comando `python` no funciona en Windows
Usa:

```bash
py
```

en lugar de:

```bash
python
```

### 2. Error de paquetes no instalados
Ejecuta:

```bash
py -m pip install -r requirements.txt
```

### 3. El proyecto no abre en el navegador
Asegúrate de estar en la carpeta del proyecto y correr:

```bash
py manage.py runserver
```

## Autor

Proyecto para práctica de Django con plantillas y rutas.
