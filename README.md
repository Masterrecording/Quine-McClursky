# Quine-McClursky

**Funcionamiento:**
- Introducir todos los mintérminos
- Hacer tuplas de todos los mintérminos que se pueden combinar
- Eliminar los mintérminos repetidos y los que se combinan a sí mismos
- Comparar con los mintérminos originales y ver si hay algúno que no esté en la lista de tuplas. Si hay, almacenarlo como mintérmino primo
- A partir de estas tuplas hacer los términos con X (los llamaremos implicantes)
- Hacer las tuplas de todos los implicantes que se pueden combinar
- Eliminar los implicantes repetidos y los que se combinan a sí mismos
- Comparar con los implicantes originales y ver si hay alguno que no esté en la lista de tuplas. Si hay, almacenarlo como implicante primo
- Repetir este proceso hasta que la longitud de la lista de tuplas sea igual a 0
- Finalmente en la lista de términos primos usar la tabla para hallar a la función