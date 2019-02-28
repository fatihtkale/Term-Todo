import sqlite3

conn = sqlite3.connect('db.db')
query = conn.cursor()

def run_program():

    def get_info():
        query = conn.cursor()
        query.execute("SELECT * FROM Information")

        rows = query.fetchall()

        for row in rows:
            print(row)

        run_program()

    def save_info(value):
        query.execute("INSERT INTO information (info) values ('"+value+"')")
        conn.commit()
        run_program()

    def delete_info(value):
        query.execute("DELETE FROM information WHERE info=?", (value,))
        conn.commit()
        run_program()

    print("Choose one of the options listed below")
    print("[S]ave for saving a information | [D]elete | [L]ist all the information | [Q]uit the program")

    choice = input()

    if choice.lower() == "s":
        print("Type a piece of information you want to save.")
        val = input()
        save_info(val)
    elif choice.lower() == "d":
        print("Type the data you want to remove")
        val = input()
        delete_info(val)
    elif choice.lower() == "l":
        get_info()
    elif choice.lower() == "q":
        conn.close()
        return 0

run_program()