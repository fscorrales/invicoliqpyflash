# invicoliqpy

invicoliqpy es una flask webapp desarrollada para ser utilizada en el Dpto Contable de INVICO con la finalidad de facilitar la carga y control de honorarios.

# Instalación
 - **Clonar el repositorio:** La mejor alternativa es utilizar el comando *git clone* en la terminal del sistema operativo con el que se está trabajando. La dirección web a clonar es https://github.com/fscorrales/invicoliqpy.git
 - **Crear un entorno virual:** Nuevamente desde la terminal se puede utilizar el comando *python -m venv [nombre_virtual_enviroment]*
 - **Activar el entorno virtual**: Aplicativos como *Visual Studio Code* realizan este proceso en forma casi automática si la carpeta del entorno virtual generada en el paso anterior forma parte del proyecto. En caso que se desee activarlo de forma manual, en la terminal hay que ejecutar el siguiente comando *.\[venv]\Scripts\activate.ps1* (Windows)
 - **Instalar los modulos requeridos:** En la terminal, introducir el siguiente comando *pip install -r requirement.txt*

# Generar base de datos
Para esto recurriremos al módulo flask-migrate. Las etapas del proceso son las siguientes:
 -  **Inicializar la carpeta migrations:** En la terminal escribir el siguiente comando *flask db init*
 - **Realizar la migración inicial:** Seguidamente, introducir el comando *flask db migrate -m “Initial migration”*
 - **Ejecutar migración:** Por último, introducimos el comando *flask db upgrade*

Si al momento de inciar el proceso aparece el error “Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.” se debe probar alguno de los siguientes comandos: 
 - *$env:FLASK_APP = "run.py"*
 - *set FLASK_APP=run.py* (Windows) o *export FLASK_APP=run.py* (Linux y Mac)

 # Introducir registros
Para generar registros falsos en la base de datos se puede utilizar el módulo fake_db que forma parte de este paquete. Para ello deberá importar el paquete completo en una consola python y llamar a las funciones que forman parte del mencionado módulo identificando la cantidad de registros a agregar.

 # Eliminar Registros
Para eliminar todos los registros de una tabla deberá utilizar el método *query.delete()* del modelo que hace referencia a la tabla deseada. Por ejemplo, si desea eliminar todos los registros de la tabla honorarios_factureros, deberá:
 * import invicoliqpy
 * from invicoliqpy import db
 * invicoliqpy.models.HonorariosFactureros.query.delete()
 * db.session.commit()

 # Ejecutar flask en modo debug
 Simplemente hay que introducir el comando *python run.py* estando posicionados dentro de la raíz del paquete invicoliqpy
 