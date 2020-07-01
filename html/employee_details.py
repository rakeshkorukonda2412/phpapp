from flask import Flask
from flask import render_template # to render the html form
import psycopg2 # for database connection

app = Flask(__name__)
@app.route("/")

def MainCode():
  t_host = "cloud-app-db"
  t_port = "5432" #default postgres port
  t_dbname = "postgres"
  t_pw = "postgres123"
  t_user = "postgres"
  t_title = "Employee email id"
  db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
  db_cursor = db_conn.cursor()
  s = "SELECT firstname,lastname,email from useraccount;"
  db_cursor.execute(s)

  # Here we catch and display any errors that occur
  #   while TRYing to commit the execute our SQL script.
  try:
      array_softwares = db_cursor.fetchall()
  except psycopg2.Error as e:
      t_error_message = "Database error: " + e + "/n SQL: " + s
      # The "/n" we see above is a carriage return.
      # The "+ s" above tacks the SQL onto the error report, giving
      #   the developer potentially useful information on what
      #   may have caused the error.
      # NOTE: we did not supply the HTML to "error_report.html"
      #   You can build that page yourself using what you learned in studying results.html

      return render_template("error_report.html", t_error_message = t_error_message)

  return render_template("results.html", t_title = t_title, array_softwares = array_softwares)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
