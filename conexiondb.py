import pymysql

def conexiondb():
    PORT=3306
    HOST= "localhost"
    USER= "root"
    PASS= ""
    db = "rockola10"
    conexion = pymysql.connect(host=HOST,port=PORT,user=USER,passwd=PASS,db=db)
    return conexion