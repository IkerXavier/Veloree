from itertools import product

import cursor
import psycopg2


def get_db_connection():
    conn = psycopg2.connect(
        "postgresql://demo_flask_3ocp_user:nV0ECwl1GUGNMEwAt14QgcpnCHKLZThS@dpg-cumsn1ij1k6c73b3aq8g-a.oregon-postgres.render.com/demo_flask_3ocp"
    )
    return conn


def insert(cursor):
    conn = get_db_connection()

    insert_statement = """insert into kategorie (kategorie_id, kategorie_name, beschreibung)
    values (%s,%s,%s)"""
    insert_statement2 = """insert into groesse_preis (groesse_preis_id, size, price)
        values (%s,%s,%s)"""
    insert_statement3 = """insert into produkt (produkt_id, product_name,groesse_preis_id )
           values (%s,%s,%s)"""
    insert_statement4 = """insert into bestellung (bestellung_id, status, datum,gesamtpreis,kunde_id )
               values (%s,%s,%s,%s, %s)"""
    insert_statement5 = """insert into kunde (kunde_id, titel, vorname,nachname,geburtsdatum,email,passwort )
                   values (%s,%s,%s,%s, %s,%s, %s)"""
    insert_statement6 = """insert into produkt_bestellung (produkt_bestellung_id, produkt_id, bestellung_id)
                       values (%s,%s,%s)"""
    insert_statement7 = """insert into warenkorb (warenkorb_id, produkt_id, kunde_id)
                           values (%s,%s,%s)"""
    insert_statement8 = """insert into warenkorb_produkt (warenkorb_produkt_id, produkt_id, warenkorb_id)
                              values (%s,%s,%s)"""
    insert_statement9 = """insert into versand (versand_id, versandart, bestellung_id)
                                  values (%s,%s,%s)"""
    insert_statement10 = """insert into zahlung (zahlung_id, bestellung_id)
                                      values (%s,%s)"""






if __name__ == '__main__':
    conn = get_db_connection()

    cursor = conn.cursor()
    insert(cursor)

    postgreSQL_select_Query = "select * from warenkorb"
    cursor.execute(postgreSQL_select_Query)
    print('Warenkorb:')
    print("Selecting rows from publisher table using cursor.fetchfall")
    publisher_records = cursor.fetchall()
    print(publisher_records)

    print('-------------------------------------')

    postgreSQL_select_Query = "select * from bestellung"
    cursor.execute(postgreSQL_select_Query)
    print('Bestelldaten von Kunde:')
    print("Selecting rows from publisher table using cursor.fetchfall")
    publisher_records2 = cursor.fetchall()
    print(publisher_records2)

    print('-------------------------------------')

    postgreSQL_select_Query = "select * from produkt"
    cursor.execute(postgreSQL_select_Query)
    print('Produkt:')
    print("Selecting rows from publisher table using cursor.fetchfall")
    publisher_records3 = cursor.fetchall()
    print(publisher_records3)
    print('-------------------------------------')

    postgreSQL_select_Query = "select * from groesse_preis"
    cursor.execute(postgreSQL_select_Query)
    print('Grösse und Preis:')
    print("Selecting rows from publisher table using cursor.fetchfall")
    publisher_records4 = cursor.fetchall()
    print(publisher_records4)



    cursor.close()
    conn.close()
