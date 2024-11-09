# Taller 3: Pruebas Unitarias en Python

Este proyecto implementa pruebas unitarias para un sistema de gestión de animales exóticos utilizando Python y el módulo unittest.

## Estructura del Proyecto

El proyecto contiene las siguientes clases y archivos de prueba:

- `animal.py` - Clase base Animal
- `animal_exotico.py` - Clase abstracta que hereda de Animal
- `boa_constrictor.py` - Clase que representa una Boa Constrictora
- `huron.py` - Clase que representa un Hurón
- `guarderia.py` - Clase que gestiona los animales

Tests:
- `tests/test_boa.py` - Pruebas para la clase BoaConstrictor
- `tests/test_huron.py` - Pruebas para la clase Huron  
- `tests/test_guarderia.py` - Pruebas para la clase Guarderia

## Pruebas Implementadas

### Test Boa Constrictor
- Prueba del método hacer_sonido()
- Prueba del método calcular_flete() 
- Prueba del método comer_raton()

### Test Hurón
- Prueba del método hacer_sonido()
- Prueba del método calcular_flete()

### Test Guardería
- Prueba del método alimentar_boa()

## Ejecución de las Pruebas

Para ejecutar todas las pruebas:
```
python -m unittest tests
```
También se puede ejecutar una prueba específica:
```
python -m tests/test_boa.py
python -m tests/test_huron.py
python -m tests/test_guarderia.py
```
	