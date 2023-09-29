# Tarea1SD

## ahora se explicara los cambios hechos y los archivos creados 

### cambios:

## search.py : 
se agrega un tiempo_total para tomar el tiempo que toma toda la simulacion en la operacion 2

## server.py: 
en la linea 17 se crea una instancia de memcache.Client. Se usa el puerto 11211 porque es el predeterminado de memcache. Esta linea esta comentada pues solo se utiliza cuando se simulan busquedas con memcache.

### nuevos archivos:

## Ncache.py: 
codigo modificado de search.py que no utiliza el cache casero.

en su mayoria se mantiene igual, pero se cambia en la linea 70 agregando  find_car_by_id(int(key)), esto se hace para buscar en seguida en el JSON

## graficas.py: 
este archivo no influye en la entrega final, con este se pretendia graficar con la distribucion normal, sin embargo, nunca se pudo hacer que se vieran las graficas por lo que el codigo solo esta para evidenciar que se intento.
