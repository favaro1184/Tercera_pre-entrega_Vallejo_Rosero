# Tercera_pre-entrega_Vallejo_Rosero
Tercera preentrega de la certificación de PYTHON en Coder House

Para la tercera preentrega realice una pagina web de registro de citas medicas usando pyhon y django. 

el proyecto se compone de 4 clases, Paciente, Medico, Clinica y Cita

El orden de ejecucion del proyecto es el siguiente:

descargar el proyecto del link de Github a la ubicacion en el pc donde se va a correr el servidor
ubicarse en la ruta: Tercera_pre-entrega_Vallejo_Rosero

proceder a ejecutar el comando python manage.py migrate
despues ejecutar el comando python manage.py runserver

una vez arrancada la ejecucion del proyecto en el navegador web proceder primero a realizar el proceso de creacion de datos de la siguiente manera:
    *   primnero, poblar la tabla de paciente desde la url pacientes, en la cual encontrara el boton para crear y consultar pacientes. en la pagina
        principal tambien se visualizar los pacientes que ya esten registrados previamente.
    *   segundo, poblar la tabla de medico desde la url medicos, en la cual encontrara el boton para crear y consultar medicos. en la pagina
        principal tambien se visualizar los medicos que ya esten registrados previamente.
    *   tercero poblar la tabla de clinica desde la url clinicas, en la cual encontrara el boton para crear y consultar clinicas. en la pagina
        principal tambien se visualizar las clinicas que ya esten registrados previamente.
    *   por ultimo poblar la tabla de citas desde la url citas, en la cual encontrara el boton para crear y consultar citas. en la pagina
        principal tambien se visualizar los pacientes que ya esten registrados previamente. Esta tabla se deja de ultima ya que en sl momento de la 
        creacion de una cita solicita los id_paciente, id_medico, id_clinica, los cuales se crean en los pasos anteriores.
