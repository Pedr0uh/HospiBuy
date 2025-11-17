import mysql.connector

conn = mysql.connector.connect(
    host="", # temos que aprender como esconder host e senha
    user="",
    password="",
    database="",
    port=,
    ssl_ca="/etc/ssl/certs/ca-certificates.crt"
)

cursor = conn.cursor(dictionary=True)