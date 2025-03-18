# Pruebas automatizadas de UI para la aplicación web de UI Test Automation Playground

UI Test Automation Playground es una plataforma para practicar habilidades de pruebas automatizadas de interfaz de usuario.

### Descripción:

- El proyecto se desarrolló con Selenium WebDriver y POM, haciendo uso de Python como lenguaje de programación.
- Se crearon pruebas para interactuar con elementos dinámicos: alertas, elementos en movimiento, elementos con atributos cambiantes, elementos con valores variables y fuera del foco visible del usuario.
- Se crearon pruebas para elementos de tipo input y textarea, para cargar archivos, para realizar acciones con el mouse y teclado, así como interactuar con elementos en iframes y shadow DOM. 
- El archivo example_file.txt es utilizado para la prueba de carga de archivos.
- Este proyecto se enfoca más en el aprendizaje de interacciones con elementos de una página web que con el diseño de casos de pruebas exhaustivos. 

### Requisitos:
- Necesitas tener instalados el paquete pytest y pynput para ejecutar las pruebas, así como los drivers de Selenium Web Driver para Google Chrome.
- Para instalar los paquetes usa los comandos pip pytest y pip pynput.
- Debes contar con los archivos data.py, main.py y example_file.txt.
- Antes de ejecutar las pruebas asegurarse de tener las configuraciones de pytest adecuadas.

### Herramientas utilizadas:
- Pycharm
- Selenium WebDriver - Chrome
- Jira
- POM

### Instrucciones:

- Realizar una copia local del repositorio GitHub.
- Instalar el paquete pytest y pynput.
- Instalar Google Chrome, así como drivers de Selenium Web Driver para este navegador.
- Para realizar las pruebas de manera grupal: hacer click en el botón Run de la clase "TestUrbanRoutes" o hacer click en Run con la opción current file seleccionada.
- Para realizar pruebas individuales: desplegar la clase "TestUrbanRoutes" y hacer click en Run en la prueba de interés.

### Análisis de resultados y conclusiones

Realicé pruebas de usuario para interactuar con distintos elementos de la interfaz de usuario de UI Testing Playgound, donde pude experimentar distintas formas de generar una misma interacción, llegando a la conclusión que las funcionalidades se prueban según el diseño que tenga la página web. Aprendí a replicar acciones con el mouse y con el teclado, así como a interactuar con elementos en shadow DOM, elementos en iFrames y alertas emergentes, logrando implementar con éxito las esperas y completar el diseño de pruebas requerido para cada elemento. La página web tiene un comportamiento bastante robusto y bien diseñado, pero se encontró y se reportó un error al introducir un usuario inválido en "Sample App"; reporte que puede ser encontrado en la carpeta Bugs. 

[Reporte de bugs en JIRA de UI para Urban Routes](https://github.com/ibrarondon/Pruebas-automatizadas-para-UITestingPlayground/blob/e9a36951b95e2305976088c830284c6a43a06ba6/Bugs/UITEST%20bug%20report.pdf) 

*Desarrollado por: Ibrahim Rondón - c13 QA Engineer, TripleTen*
