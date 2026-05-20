# Analisis del comportamiento de aplicaciones

Proyecto final para comparar el rendimiento de Covagro SII bajo Docker Compose y Kubernetes con variacion de replicas y nodos.

## Estructura

- `app/Backend`: API Django REST de Covagro.
- `app/Frontend`: frontend React/Vite servido con Nginx.
- `docker-compose.yml`: escenario de una maquina.
- `kubernetes/`: manifiestos y configuraciones kind para 1, 2 y 3 nodos.
- `jmeter/`: plan de carga y plantilla de resultados.
- `notebooks/`: notebook de analisis comparativo.
- `docs/`: metodologia e instrucciones complementarias.

## Ejecucion rapida con Docker Compose

```bash
docker compose up --build -d
```

Abrir:

- Frontend: http://localhost:3000
- API: http://localhost:8000/api/

Credenciales de prueba:

- Usuario: `admin@covagro.local`
- Clave: `Admin123*`

## Kubernetes

Ver [kubernetes/README.md](kubernetes/README.md) para crear clusters kind, cargar imagenes, desplegar y variar replicas.

## JMeter

Ver [jmeter/README.md](jmeter/README.md). Ejemplo:

```powershell
.\scripts\run_jmeter.ps1 -BaseUrl http://localhost:8000 -Scenario docker-compose -Nodes 1 -Replicas 1 -Users 25
```

## Analisis

Completa `jmeter/results_template.csv` o crea un CSV equivalente con las metricas observadas. Luego abre `notebooks/analisis_comportamiento.ipynb` y ejecuta las celdas para generar tablas, graficos y conclusiones.

## Entrega sugerida

1. Ejecutar Compose y guardar resultados JMeter.
2. Ejecutar Kubernetes de 1 nodo con replicas 1, 2 y 3.
3. Ejecutar Kubernetes de 2 nodos con replicas 1, 2 y 3.
4. Ejecutar Kubernetes de 3 nodos si el curso lo solicita o si la VM tiene recursos suficientes.
5. Completar el CSV de resultados y actualizar el notebook con observaciones y conclusiones.
