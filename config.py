import os



class Config:


    DEBUG = "True"
    FLASK_DEBUG= "development"
    
    #VARIABLES DE BASE DE DATOS
    SECRET_KEY = "e23895acc525f92e886e9fe425046e0743855fbc038a70067540742c9fd34179"

    SQLALCHEMY_DATABASE_URI='mysql://root:@localhost:3306/psicoanalitica-caracas'

    SQLALCHEMY_TRACK_MODIFICATION= False

    #SOBREESCRIBIENDO RUTAS DE FLASK

    TEMPLATE_FOLDER= "views/templates"
    STATIC_FOLDER = "views/static"