from django.http import Http404
from django.shortcuts import render

PELICULAS = [
    {
        'id': 1,
        'título': 'Django: Unchained',
        'genero': 'Western',
        'duracion': 165,
        'director': 'Quentin Tarantino',
        'año': 2012,
        'sala': 3,
        'horario': '18:30',
        'sinopsis': 'Un esclavo busca venganza mientras se embarca en una peligrosa misión junto a un cazador de recompensas.',
        'imagen': 'imagenes/paquete.png',
    },
    {
        'id': 2,
        'título': 'Inception',
        'genero': 'Ciencia ficción',
        'duracion': 148,
        'director': 'Christopher Nolan',
        'año': 2010,
        'sala': 1,
        'horario': '20:00',
        'sinopsis': 'Un ladrón de sueños debe plantar una idea en la mente de un empresario mediante una compleja operación mental.',
        'imagen': 'imagenes/paquete.png',
    },
    {
        'id': 3,
        'título': 'La La Land',
        'genero': 'Musical',
        'duracion': 128,
        'director': 'Damien Chazelle',
        'año': 2016,
        'sala': 2,
        'horario': '16:45',
        'sinopsis': 'Una aspirante a actriz y un pianista de jazz se enamoran mientras persiguen sus sueños en Los Ángeles.',
        'imagen': 'imagenes/paquete.png',
    },
    {
        'id': 4,
        'título': 'Memento',
        'genero': 'Thriller',
        'duracion': 113,
        'director': 'Christopher Nolan',
        'año': 2000,
        'sala': 4,
        'horario': '22:15',
        'sinopsis': 'Un hombre con amnesia intenta resolver el misterio del asesinato de su esposa recordando fragmentos de su pasado.',
        'imagen': 'imagenes/paquete.png',
    },
]


def inicio(request):
    return render(request, 'inicio.html', {'peliculas': PELICULAS})


def detalle(request, pelicula, id):
    elemento = next((p for p in PELICULAS if p['id'] == id), None)
    if elemento is None:
        raise Http404('La película no existe')
    return render(request, 'detalle.html', {'pelicula': elemento})