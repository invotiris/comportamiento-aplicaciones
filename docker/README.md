# Despliegue con Docker Compose

Este escenario ejecuta Covagro en una sola maquina con tres servicios: PostgreSQL, backend Django y frontend Nginx/React.

```bash
docker compose up --build -d
```

Servicios expuestos:

- Frontend: http://localhost:3000
- API: http://localhost:8000/api/
- Usuario de prueba: `admin@covagro.local`
- Clave: `Admin123*`

Para limpiar el escenario:

```bash
docker compose down -v
```
