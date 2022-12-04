### Auto Scraping Fisi

### Integrantes:
- Álvarez More, Diego [@diegoam11](https://github.com/diegoam11)
- Dávila Vásquez, Rodrigo Estéfano [@RodrigoDV03](https://github.com/RodrigoDV03)
- Falla Gallegos, Diego André [@diegoafg1009](https://github.com/diegoafg1009)
- Tupac Agüero, Kevin [@Jonathan101120](https://github.com/Jonathan101120)
- Villanueva Chirito, Mariano [@Marianoavc](https://github.com/Marianoavc)

### Pasos:
- Descargar el ChromeDriver, dependiendo de la versión de Chrome que tenga. [Link_Descarga_ChromeDriver](https://chromedriver.chromium.org/downloads)
- Poner el lugar donde esta descargado el ChromeDriver en la Clase Search dentro del metodo construtor. 
     Ejemplo: `self.__path = "C:\Program Files (x86)\chromedriver.exe"`
- El usuario podrá registrarse.
- El usuario podrá ingresar con su cuenta.
     - El usuario ingresará al menú de opciones, para escoger en que página se realizará la web scraping.
     - El usuario ingresará:
        - La marca
        - El modelo
        - El año
     - El programa emperazará su ejecución, culminando con la entrega de los datos en orden decendente, desde el que tenga menor precio hasta el mayor.
     - Esta información sera guardada en el historial del usuario, este podrá ser visto.
 - El usuario podrá salir del programa.

### Languages and Tools:
- Python
- BeautifulSoup
- Selenium
- Scrapy

"Proyecto del grupo 6 del curso de Algorítmica II de la Facultada de Ingeniería de Sistemas e Informática de la Universidad Nacional Mayor de San Marcos."
