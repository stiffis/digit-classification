# Proyecto 2 de Introducción a las Ciencias de la Computación
Otra vez amanecidas 😴</p>
Pongan emojis tambien, para que IAN nos apruebe 👍</p>
## Instrucciones de instalación
1. Clonar el proyecto
2. Crear un entorno virtual en el directorio raiz con:
    >python -m venv env
3. Activar el entorno virtual:
    >env\Scripts\activate</p>
    
    En caso no funcione:</p>
    - Abre PowerShell como administrador</p>
    - Y copiar la siguiente línea (darle "Y" a todo):</p>
        >Set-ExecutionPolicy RemoteSigned -Scope CurrentUser</p>
    - Vuelve a intentar activar el entorno virtual
4. Instalar las dependencias con:
    >pip install -r requirements.txt
## Comandos principales para navegar por Git Bash:
- Inicia el repositorio local.
    > git init
- Cambia la direccion de carpeta/directorio en la que te encuentres.
    > cd <"nombre del directorio/carpeta a moverse">
    
- Cambia a la direccion de carpeta/directorio anterior.
    >cd ..
- Verificar el estado del repositorio local.
    >git status
- Empezar a hacer seguimiento  los archivos.
    >git add <"nombre del archivo">
- Hacer un "screenshot" o una salvaguardo de lo hecho hasta ese momento.
    >git commit -m "mensaje descriptivo de lo hecho"    
- Empujar los cambios al GitHub(cuidado)‼️‼️.
    >git push origin <"nombre de su rama">
- Obtener cambios del GitHub.
    >git pull origin <"nombre la de rama">
- Crear nueva rama.
    >git branch <"nombre de la rama">
- Moverse entre ramas.
    >git checkout <"nombre de la rama">
- Lista de las ramas existentes.
    >git branch
- Fusionar ramas con la actual.
    >git merge <"nombre de la rama a fusionar">
- Obtener todas las ramas del repositorio remoto.
    >git fetch
- Eliminar rama local.
    >git branch -d <"nombre de la rama a eliminar">
- Eliminar una rama del GitHub(cuidado)‼️‼️.
    >git push origin --delete <"nombre de la rama">
- Mostrar el historial de commits:
    >git log
- Mostrar las diferencias entre commits:
    >git diff

## Flujo de trabajo 
- Una vez lista la instalación del proyecto y sus dependencias, comenzaran a modificar/crear los archivos que consideren necesarios para realizar la parte que se les designo.
    - Cuando tengan lo necesario, subirlo al GitHub para que los demás podamos visualizarlo, hacer sugerencias, o continuar con el proyecto. Pero subiran solo la rama con su nombre osea (>git push origin <"nombre de la rama">) para que no interfiera ni malogre el producto final.
    - Cuando quieran obtener los cambios o aportes de las demás ramas ya sea por que lo necesitan para continuar el proyecto o mirar el progreso usar (git pull origin <"nombre la de rama">).
    - Mantener comunicación frecuente ya que este proyecto es colectivo, por lo que tendremos que ayudarnos unos a otros. No olviden pedir ayuda o avisar antes de hacer algun pull o push.
    - Cuando tengan que añadir librerias por algun motivo avisar a los demás para editar (requirements.txt).
    - Buena suerte! 😁