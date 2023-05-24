from flask import Flask, render_template, request, make_response
import sqlite3
 
# FLASK SETTINGS + INIT
HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "./data/community_center_data.db"
app = Flask(__name__)

# GET ALL ITEMS FROM DATABASE 
def getitems():
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM `community_center`")
  results = cursor.fetchall()
  conn.close()
  return results

# DEFAULT ROUTE
@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    items = getitems()
    return render_template("table.html", item = items)
  else: #POST JS Script das on klick event abfängt und dann den Post request an das Python Backend weitergibt mit Element welches sich geändert hat un den Zustand. Also "Apfel" und "checked". 
    data = request.form.getlist('checkbox')
    conn = sqlite3.connect(DBFILE)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE `community_center` SET checked = 'false' WHERE checked = 'true'")
    conn.commit()
    for item in data:
      cursor.execute(f"UPDATE `community_center` SET checked = 'true' WHERE name = '{item}'")
      conn.commit()
    conn.close()
    items = getitems()
    return render_template("table.html", item = items)
 
# START
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)
