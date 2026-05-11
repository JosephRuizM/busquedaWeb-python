import webbrowser
#codigo estructura para mi agente que me envia a donde yo ocupe
#me ayuda a buscar los datos para los otros proyectos
plataforma = input("¿Dónde quieres buscar? (google, youtube, wikipedia, amazon): ").lower()
busqueda = input(f"¿Qué quieres buscar en {plataforma}?: ").replace(" ", "+")

# 1. Diccionario corregido con rutas y parámetros de búsqueda (?q=, ?search=, etc.)
buscadores = {
    "google": "https://www.google.com/search?q=",
    "youtube": "https://www.youtube.com/results?search_query=",
    "wikipedia": "https://es.wikipedia.org/wiki/Special:Search?search=",
    "amazon": "https://www.amazon.com/s?k=",
    "gemini": "https://gemini.google.com/app?q="
}

# 2. Verificación y apertura
if plataforma in buscadores:
    # Ahora 'url' será, por ejemplo: https://google.comspinosaurus
    url = buscadores[plataforma] + busqueda
    print(f"Abriendo {plataforma.capitalize()}...")
    webbrowser.open(url)
else:
    url = buscadores.get(plataforma, f"https://www.google.com/search?q={plataforma}+") + busqueda
    webbrowser.open(url)