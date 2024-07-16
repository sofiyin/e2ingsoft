
### 3. Se requiere realizar un cambio en el software para que soporte un valor máximo de 200 soles a transferir por día.

**¿Qué cambiaría en el código (Clases / Métodos) - No realizar la implementación, sólo
descripción.**

Como son 200 soles por día en total, esto quiere decir que el usuario puede transferir a ”n “ personas “x”  cantidad de dinero siempre y cuando la suma total de sus transferencias de ese día no supere los 200 soles por día, entonces:

Cambios en clases:
En la clase Cuenta: Cada usuario tendría que tener un nuevo atributo: TransferenciaDiaria.

Cambios en Métodos:
Se tendría que modificar la función Transferir para cuando se realice una transferencia (a cualquier persona) el monto transferido se vaya sumando al atributo TransferenciaDiaria si y solo si TransferenciaDiara no supera 200 soles.
Finalmente esta vuelve a ser 0 al final del día para vuelva a funcionar el día siguiente.


**¿Qué casos de prueba nuevos serían necesarios?**
Caso de prueba exitoso: El valor de transferenciaDiaria se actualiza a 0 al finalizar el día.
2do Caso de prueba nuevo: Verificar que el valor de una operación y de TransferenciaDiaria no supera los 200 soles.


**Los casos de prueba existentes garantizan que no se introduzcan errores en la funcionalidad existente:**

Tenemos un caso de prueba que asegura que un usuario transfiera con éxito, este también asegura que el usuario posea el valor transferido en su billetera. Por ende, podríamos modificarlo para añadir una condicionalidad extra que asegure que el atributo de TransferenciaDiara de un usuario sea menor a 200.

Otros adicionales son respecto a los contactos donde asegura que se transfiera a un usuario existente en los contactos.


