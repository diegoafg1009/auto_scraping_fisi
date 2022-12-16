# Auto Scraping Fisi

## Integrantes:
- Álvarez More, Diego [@diegoam11](https://github.com/diegoam11)
- Dávila Vásquez, Rodrigo Estéfano [@RodrigoDV03](https://github.com/RodrigoDV03)
- Falla Gallegos, Diego André [@diegoafg1009](https://github.com/diegoafg1009)
- Tupac Agüero, Kevin [@Jonathan101120](https://github.com/Jonathan101120)
- Villanueva Chirito, Mariano [@Marianoavc](https://github.com/Marianoavc)

## Nuevas Funcionalidades:
1. Agregar a favoritos:
      - Con esta funcionalidad el usuario podrá guardar los datos de un auto que le haya llamado la atención al momento de realizar su búsqueda, estos autos favoritos a su vez podrán ser visualizados en el menú que aparece luego de iniciar sesión.
2. Modificar datos del usuario:
     - Contamos con una opción donde el usuario podrá ingresar y modificar solo sus datos que el desee, como: Nombre, Apellidos, nombre de usuario, correo electrónico y contraseña. De ingresar un correo o nombre de usuario que ya se encuentre en uso el programa no permitirá la modificación.
3. Buscar en Autopia (En optimizacion):
     - El usuario podra buscar el auto de su preferencia en la pagina "Autopia".
          
## Instrucciones:
1. Descargar y extraer el ChromeDriver, dependiendo de la versión de Chrome que tenga. [Link_Descarga_ChromeDriver](https://chromedriver.chromium.org/downloads). Para mas informacion: [Tutorial](https://youtu.be/MCocyBNgPU0)
2. Poner la ruta sin comillas del ChromeDriver en el archivo **driver_path.txt**. 
     * Ejemplo: `C:\Program Files (x86)\chromedriver.exe`
3. Antes de correr el programa, se deberan de instalar las librerias usadas, estas estan en el archivo `requirements.txt`. Para esto recomendamos el uso de *pycharm* ya que detecta automaticamente este archivo; en caso se utilice otro IDE, se debera de correr el siguiente comando en consola: `$ pip install -r requirements.txt`
4.
     * El usuario podrá registrarse mediante el ingreso de su información.
     * El usuario podrá iniciar sesión con su cuenta.
          * El usuario ingresará al menú de opciones, para escoger en que página se realizará la búsqueda o tambien podra buscar en todas las páginas.
          * El usuario ingresará:
             * La marca [Ingresara la marca del auto]
             * El modelo [Ingresara el modelo del auto]
             * El año [Ingresara el intervalo del año del auto]
             * La cantidad [Ingresara la cantidad de autos a mostrar]
          * El programa empezará su ejecución, culminando con la entrega de los datos de los autos ordenados por precio de manera ascendente y solo mostrara la cantidad de autos que se pidió.
          * Esta información sera guardada en el historial de busqueda del usuario, para que en una próxima oportunidad pueda visualizarlas.
     * El usuario podrá salir del programa.


"Proyecto del grupo 6 del curso de Algorítmica II de la Facultad de Ingeniería de Sistemas e Informática de la Universidad Nacional Mayor de San Marcos."
