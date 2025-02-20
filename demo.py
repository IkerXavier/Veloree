import psycopg2

conn = psycopg2.connect(
    "postgresql://demo_flask_3ocp_user:nV0ECwl1GUGNMEwAt14QgcpnCHKLZThS@dpg-cumsn1ij1k6c73b3aq8g-a.oregon-postgres.render.com/demo_flask_3ocp"
)


def insert(cursor):
    insert_statement = """insert into person (person_id, first_name, last_name, birth_date)
    values (%s,%s,%s,%s)"""
    insert_statement2 = """insert into pet (pet_id, first_name, color, legs, age, habitat) 
    values (%s,%s,%s,%s,%s,%s)"""
    insert_statement3 = """insert into club (club_id, club_name, league, country, founding_date, stadium, manager)
    values (%s,%s,%s,%s,%s,%s,%s)"""



    record_to_insert = [(5, 'Paul', 'Schwers', '2008-05-05'), (6, 'Florian', 'Ramadani', '2007-04-01'), (7, 'Pauli','Oily','2023-08-01')]
    for record in record_to_insert:
        cursor.execute(insert_statement, record)
        count = cursor.rowcount
        print(count, "Record inserted succesfully into publisher table")

    record_to_insert2 = [(8, 'Toni', 'braun', 2, 2, 'Tupperware von Lena'), (9, 'Bruce', 'orange', 4, 5, 'Nachbaren von Pöli')]
    for record in record_to_insert2:
        cursor.execute(insert_statement2, record)
        count = cursor.rowcount
        print(count, "Record inserted succesfully into publisher table")

    record_to_insert3 = [(4, 'FC Barcelona','La Liga', 'Spanien', '1899-11-29', 'Camp Nou','Xavi')]
    for record in record_to_insert3:
        cursor.execute(insert_statement3, record)
        count = cursor.rowcount
        print(count, "Record inserted succesfully into publisher table")

if __name__ == '__main__':
    cursor = conn.cursor()
    insert(cursor)

    postgreSQL_select_Query = "select * from person"
    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from publisher table using cursor.fetchfall")
    publisher_records = cursor.fetchall()
    print(publisher_records)

    print('-------------------------------------')

    postgreSQL_select_Query = "select * from pet"
    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from publisher table using cursor.fetchfall")
    publisher_records2 = cursor.fetchall()
    print(publisher_records2)

    print('-------------------------------------')

    postgreSQL_select_Query = "select * from club"
    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from publisher table using cursor.fetchfall")
    publisher_records3 = cursor.fetchall()
    print(publisher_records3)

    print('-------------------------------------')

    cursor.close()
    conn.close()

