import os
from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'

    def ready(self):
        if os.environ.get('RENDER'):
            from django.contrib.auth import get_user_model
            Usuario = get_user_model()
            try:
                if not Usuario.objects.filter(username='admin').exists():
                    admin = Usuario.objects.create_superuser(
                        'admin', 'admin@sanchez-arteaga.edu.pe', 'admin123', rol='admin'
                    )
                profes = [
                    ('carlos.garcia', 'Carlos', 'García'),
                    ('maria.lopez', 'María', 'López'),
                    ('jose.ramirez', 'José', 'Ramírez'),
                    ('ana.martinez', 'Ana', 'Martínez'),
                    ('luis.hernandez', 'Luis', 'Hernández'),
                ]
                for username, first, last in profes:
                    if not Usuario.objects.filter(username=username).exists():
                        u = Usuario.objects.create_user(
                            username=username,
                            email=f'{username}@sanchez-arteaga.edu.pe',
                            password='profesor123',
                            first_name=first, last_name=last,
                            rol='profesor',
                        )
                alumnos = [
                    ('sofia.mendoza', 'Sofía', 'Mendoza'),
                    ('mateo.garcia', 'Mateo', 'García'),
                    ('valentina.ramirez', 'Valentina', 'Ramírez'),
                    ('santiago.lopez', 'Santiago', 'López'),
                    ('isabella.torres', 'Isabella', 'Torres'),
                ]
                for username, first, last in alumnos:
                    if not Usuario.objects.filter(username=username).exists():
                        u = Usuario.objects.create_user(
                            username=username,
                            email=f'{username}@sanchez-arteaga.edu.pe',
                            password='123456',
                            first_name=first, last_name=last,
                            rol='alumno',
                        )
            except Exception:
                pass
