"""
main.py

Este script ejecuta una serie de scripts de Python en un orden específico:
1. dijkstra.py
2. dijkstra_reverso.py
3. calculo_pac.py

Funciones:
- ejecutar_script(nombre_script): Ejecuta un script de Python utilizando subprocess.
- main(): Función principal que ejecuta los scripts en el orden especificado.

Uso:
Este script se utiliza para automatizar la ejecución de múltiples scripts de Python
en un orden predefinido.
"""

import subprocess

def ejecutar_script(nombre_script):
    """
    Ejecuta un script de Python utilizando subprocess.

    Parámetros:
    - nombre_script (str): Nombre del script a ejecutar.
    """
    try:
        resultado = subprocess.run(
            ['python3', nombre_script],
            check=True,
            text=True,
            capture_output=True
        )
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar {nombre_script}: {e}")
        print(e.stderr)

def main():
    """
    Función principal que ejecuta los scripts en el orden especificado.
    """
    # Ejecutar los scripts en el orden especificado
    ejecutar_script('dijkstra.py')
    ejecutar_script('dijkstra_reverso.py')
    ejecutar_script('calculo_pac.py')

if __name__ == "__main__":
    main()
