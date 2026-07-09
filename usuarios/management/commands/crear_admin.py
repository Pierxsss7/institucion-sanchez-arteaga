from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class Command(BaseCommand):
    help = 'Crea admin y usuarios de prueba si no existen'

    def handle(self, *args, **options):
        admin, created = Usuario.objects.get_or_create(
            username='admin',
            defaults={
                'first_name': 'Administrador',
                'last_name': 'General',
                'email': 'admin@sanchez-arteaga.edu.pe',
                'rol': 'admin',
                'is_staff': True,
                'is_superuser': True,
            },
        )
        if created:
            admin.set_password('admin123')
            admin.save()
            self.stdout.write(self.style.SUCCESS('OK Admin creado: admin / admin123'))
        else:
            if not admin.check_password('admin123'):
                admin.set_password('admin123')
                admin.save()
                self.stdout.write('OK Admin password reseteado')

        profes = [
            ('carlos.garcia', 'Carlos', 'García', 'profesor'),
            ('maria.lopez', 'María', 'López', 'profesor'),
            ('jose.ramirez', 'José', 'Ramírez', 'profesor'),
            ('ana.martinez', 'Ana', 'Martínez', 'profesor'),
            ('luis.hernandez', 'Luis', 'Hernández', 'profesor'),
        ]
        for username, first, last, rol in profes:
            u, c = Usuario.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': first,
                    'last_name': last,
                    'email': f'{username}@sanchez-arteaga.edu.pe',
                    'rol': rol,
                },
            )
            if c:
                u.set_password('profesor123')
                u.save()
                self.stdout.write(f'OK Profesor: {username} / profesor123')

        alumnos = [
            ('sofia.mendoza', 'Sofía', 'Mendoza'),
            ('mateo.garcia', 'Mateo', 'García'),
            ('valentina.ramirez', 'Valentina', 'Ramírez'),
            ('santiago.lopez', 'Santiago', 'López'),
            ('isabella.torres', 'Isabella', 'Torres'),
        ]
        for username, first, last in alumnos:
            u, c = Usuario.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': first,
                    'last_name': last,
                    'email': f'{username}@sanchez-arteaga.edu.pe',
                    'rol': 'alumno',
                },
            )
            if c:
                u.set_password('123456')
                u.save()
                self.stdout.write(f'OK Alumno: {username} / 123456')

        self.stdout.write(self.style.SUCCESS('\nTodos los usuarios listos.'))
