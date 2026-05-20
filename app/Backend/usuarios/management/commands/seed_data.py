from decimal import Decimal
import random

from django.core.management.base import BaseCommand

from inventario.models import MovimientoInventario
from pedidos.models import DetallePedido, EstadoPedido, Pedido
from productos.models import Categoria, Producto
from usuarios.models import Rol, Usuario


class Command(BaseCommand):
    help = "Crea datos deterministas para pruebas de carga y analisis."

    def add_arguments(self, parser):
        parser.add_argument("--productos", type=int, default=1000)
        parser.add_argument("--pedidos", type=int, default=3000)

    def handle(self, *args, **options):
        random.seed(42)
        roles = {
            nombre: Rol.objects.get_or_create(nombre=nombre)[0]
            for nombre in ["ADMIN", "EMPLEADO", "CLIENTE"]
        }
        admin, _ = Usuario.objects.get_or_create(
            email="admin@covagro.local",
            defaults={
                "nombre": "Admin Covagro",
                "telefono": "3000000000",
                "id_rol": roles["ADMIN"],
                "is_staff": True,
                "is_superuser": True,
            },
        )
        admin.set_password("Admin123*")
        admin.save()

        empleado, _ = Usuario.objects.get_or_create(
            email="empleado@covagro.local",
            defaults={"nombre": "Empleado Carga", "id_rol": roles["EMPLEADO"]},
        )
        empleado.set_password("Empleado123*")
        empleado.save()

        clientes = []
        for i in range(1, 101):
            cliente, _ = Usuario.objects.get_or_create(
                email=f"cliente{i}@covagro.local",
                defaults={"nombre": f"Cliente {i}", "id_rol": roles["CLIENTE"], "canal": "web"},
            )
            cliente.set_password("Cliente123*")
            cliente.save()
            clientes.append(cliente)

        categorias = [
            Categoria.objects.get_or_create(nombre=nombre)[0]
            for nombre in ["Fertilizantes", "Semillas", "Herramientas", "Riego", "Proteccion"]
        ]

        productos = []
        for i in range(1, options["productos"] + 1):
            producto, _ = Producto.objects.get_or_create(
                nombre=f"Producto agricola {i:04d}",
                defaults={
                    "id_categoria": random.choice(categorias),
                    "descripcion": f"Insumo agricola para pruebas de carga {i}",
                    "precio": Decimal(random.randint(5000, 250000)),
                    "stock_actual": random.randint(20, 500),
                    "stock_minimo": random.randint(5, 30),
                    "estado": True,
                },
            )
            productos.append(producto)

        estados = {
            nombre: EstadoPedido.objects.get_or_create(nombre=nombre, defaults={"descripcion": nombre})[0]
            for nombre in ["Pendiente", "En proceso", "Entregado", "Cancelado"]
        }

        pedidos_actuales = Pedido.objects.count()
        for _ in range(max(0, options["pedidos"] - pedidos_actuales)):
            pedido = Pedido.objects.create(
                id_cliente=random.choice(clientes),
                id_empleado=empleado,
                id_estado=random.choice(list(estados.values())),
                canal=random.choice(["web", "telefono", "mostrador"]),
                observaciones="Pedido generado para pruebas de rendimiento.",
            )
            total = Decimal("0")
            for producto in random.sample(productos, k=random.randint(1, 5)):
                cantidad = random.randint(1, 8)
                detalle = DetallePedido.objects.create(
                    id_pedido=pedido,
                    id_producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio,
                    subtotal=producto.precio * cantidad,
                )
                total += detalle.subtotal
            pedido.total = total
            pedido.save(update_fields=["total"])

        if not MovimientoInventario.objects.exists():
            for producto in random.sample(productos, k=min(500, len(productos))):
                MovimientoInventario.objects.create(
                    producto=producto,
                    tipo=random.choice(["entrada", "salida", "ajuste"]),
                    cantidad=random.randint(1, 50),
                    referencia="seed-carga",
                )

        self.stdout.write(self.style.SUCCESS("Datos de prueba creados."))
