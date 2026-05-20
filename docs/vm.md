# Ejecucion en la maquina virtual

Conectarse:

```bash
ssh student1@IP_DE_LA_VM
```

Instalar herramientas si no existen:

```bash
docker --version
docker compose version
kubectl version --client
kind version
jmeter --version
```

Clonar el entregable:

```bash
git clone https://github.com/invotiris/comportamiento-aplicaciones.git
cd comportamiento-aplicaciones
```

Ejecutar Docker Compose:

```bash
docker compose up --build -d
```

Ejecutar JMeter para Compose:

```bash
jmeter -n -t jmeter/covagro-load-test.jmx -l results/docker-compose.jtl -e -o results/docker-compose-dashboard -JBASE_URL=http://localhost:8000 -JUSERS=25 -JRAMP_UP=30 -JDURATION=120
```

Para Kubernetes, seguir `kubernetes/README.md`. En una VM remota, si se necesita acceder desde tu navegador local, usa tuneles SSH:

```bash
ssh -L 3000:localhost:3000 -L 8000:localhost:8000 -L 30080:localhost:30080 -L 30081:localhost:30081 student1@IP_DE_LA_VM
```
