import mysql.connector

conn = mysql.connector.connect(
    host="shinkansen.proxy.rlwy.net", # temos que aprender como esconder host e senha
    user="root",
    password="eSGzRtPwShQdjLoqAqsjUCpAIzHqPLRX",
    database="HospiBuy",
    port="18428"
)

cursor = conn.cursor(dictionary=True)

