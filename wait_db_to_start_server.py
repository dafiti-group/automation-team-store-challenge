import os
import subprocess
import time
import MySQLdb


def main():
    """ Main Function
    Responsible by verify msql connection
    """

    for count in range(0, 20):
        try:
            print("Attempt number %s", count)
            database_instance = MySQLdb.connect(host=os.getenv("DB_HOST"),
                                                user=os.getenv("DB_USER"),
                                                port=int(os.getenv("DB_PORT")),
                                                passwd=os.getenv("DB_PASS"),
                                                db=os.getenv("DB_NAME"))
        except MySQLdb.Error as err:
            print(err)
            print(os.getenv("DB_HOST"),
                  os.getenv("DB_USER"),
                  os.getenv("DB_USER"),
                  os.getenv("DB_PORT"),
                  os.getenv("DB_PASS"),
                  os.getenv("DB_NAME"))
            time.sleep(2)
            continue
        if database_instance:
            print("Connection successful")
            break
        print("Connection unsuccessful")


def run_application():
    """ start django application """
    subprocess.run("python manage.py makemigrations",
                   shell=True,
                   check=True)
    subprocess.run("python manage.py migrate",
                   shell=True,
                   check=True)
    subprocess.run("python manage.py runserver 0.0.0.0:8000",
                   shell=True,
                   check=True)


if __name__ == "__main__":
    main()
    run_application()
