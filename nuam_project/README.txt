	Guía de instalación y ejecución

Este archivo contiene las instrucciones completas para instalar y ejecutar el
proyecto NUAM en tu computador, tanto en Linux como en Windows.

El proyecto utiliza Django y Django REST Framework y permite trabajar con
diferentes tipos de moneda (CLP, COP, PEN y USD).



	REQUISITOS GENERALES


Antes de comenzar, asegúrate de tener instalado lo siguiente:

1. Python 3.10 o superior (recomendado 3.12)
2. pip (gestor de paquetes de Python)
3. Git (para clonar el repositorio)
4. Conexión a internet (para instalar dependencias y actualizar tasas)



	INSTALACIÓN EN LINUX


1. Actualiza el sistema
sudo apt update && sudo apt upgrade -y

2. Instala Python y herramientas necesarias
sudo apt install -y python3 python3-pip python3-venv git

3. Clona el proyecto desde GitHub
git clone https://github.com/RenBriones03/Ev3BackEnd
cd nuam_project

4. Crea el entorno virtual
python3 -m venv venv
source venv/bin/activate

5. Instala las dependencias del proyecto
pip install -r requirements.txt

6. Aplica las migraciones y crea el superusuario
python manage.py migrate
python manage.py createsuperuser

7. Carga tasas iniciales y actualiza las reales
python manage.py seed_rates
python manage.py update_rates

8. Inicia el servidor
python manage.py runserver

El proyecto estará disponible en:
http://127.0.0.1:8000/



	INSTALACIÓN EN WINDOWS (PowerShell)


1. Clona el proyecto
git clone https://github.com/tuusuario/nuam_project.git
cd nuam_project

2. Crea y activa el entorno virtual
python -m venv venv
venv\Scripts\Activate

3. Instala las dependencias
pip install -r requirements.txt

4. Aplica migraciones y crea el superusuario
python manage.py migrate
python manage.py createsuperuser

5. Carga tasas iniciales y actualiza las reales
python manage.py seed_rates
python manage.py update_rates

6. Inicia el servidor
python manage.py runserver

Accede desde tu navegador a:
http://127.0.0.1:8000/



	EJECUCIÓN AUTOMÁTICA (SCRIPTS)


El proyecto incluye scripts automáticos para simplificar la instalación.

En Linux:
bash setup.sh

En Windows (PowerShell):
powershell -ExecutionPolicy Bypass -File setup.ps1

Estos scripts crean el entorno virtual, instalan dependencias,
aplican migraciones y ejecutan el servidor automáticamente.



	ACTUALIZAR TASAS DE CAMBIO MANUALMENTE


Si deseas actualizar las tasas en cualquier momento, ejecuta:
python manage.py update_rates

Esto consultará una API pública y actualizará los valores de CLP, COP y PEN
en la base de datos.



	PROBLEMAS COMUNES Y SOLUCIONES


❌ Error: "Invalid block tag: 'static'"
✅ Solución: Agrega la línea {% load static %} al inicio de tu archivo base.html

❌ Error: "missing_access_key" o no se actualizan tasas
✅ Solución: Asegúrate de tener conexión a internet. El proyecto usa la API https://open.er-api.com que no requiere clave.

❌ Error: "ModuleNotFoundError"
✅ Solución: Activa el entorno virtual y reinstala dependencias:
source venv/bin/activate  (Linux)
venv\Scripts\Activate    (Windows)
pip install -r requirements.txt

❌ Error: "no such table" o "OperationalError"
✅ Solución: Ejecuta las migraciones: python manage.py migrate



	COMANDOS ÚTILES


-Crear superusuario: python manage.py createsuperuser
-Cargar tasas de ejemplo: python manage.py seed_rates
-Actualizar tasas reales: python manage.py update_rates
-Ejecutar servidor: python manage.py runserver
-Salir del entorno virtual: deactivate



	LISTO


Si seguiste estos pasos, tu proyecto NUAM ya debería estar funcionando
correctamente en tu computador.

Puedes acceder al panel de administración en:
http://127.0.0.1:8000/admin/



	FIN DEL DOCUMENTO

