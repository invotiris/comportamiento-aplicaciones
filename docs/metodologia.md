# Metodologia experimental

## Aplicacion evaluada

Covagro SII es una aplicacion con backend Django REST, frontend React/Vite y persistencia en PostgreSQL para los escenarios de despliegue. La API expone recursos de usuarios, productos, inventario, pedidos, detalles y notificaciones.

## Escenarios

1. Docker Compose en una maquina: PostgreSQL, backend y frontend.
2. Kubernetes con un nodo: backend con 1, 2 y 3 replicas.
3. Kubernetes con dos nodos: backend con 1, 2 y 3 replicas.
4. Kubernetes con tres nodos: backend con 1, 2 y 3 replicas.

## Cargas

Ejecutar al menos tres niveles de concurrencia para cada escenario:

- 25 usuarios concurrentes.
- 50 usuarios concurrentes.
- 100 usuarios concurrentes.

Mantener el mismo `RAMP_UP` y `DURATION` para comparar de forma justa.

## Metricas

Registrar desde el dashboard de JMeter:

- Tiempo medio de respuesta en milisegundos.
- Throughput en solicitudes por segundo.
- Porcentaje de errores.
- Percentil 95 de tiempo de respuesta.

## Control de variables

- Usar el mismo seed de datos en todos los escenarios.
- Reiniciar o limpiar el cluster antes de cambiar el numero de nodos.
- Cambiar solamente una variable por corrida: numero de nodos, replicas o usuarios.
- Guardar los dashboards generados en `results/`.
