# Wir importieren zuerst das Flask-Objekt aus dem Package
import sqlite3

from flask import Flask, request, render_template, url_for, redirect, session
from select import select

from db import get_db_connection

# mock data
languages = [
    {"name": "Python", "creator": "Guido van Rossum", "year": 1991},
    {"name": "JavaScript", "creator": "Brendan Eich", "year": 1995},
    {"name": "Java", "creator": "James Gosling", "year": 1995},
    {"name": "C#", "creator": "Microsoft", "year": 2000},
    {"name": "Ruby", "creator": "Yukihiro Matsumoto", "year": 1995},
    {"name": "TypeScript", "creator": "Microsoft", "year": 2012},
]

# Definieren einer Variable, die die aktuelle Datei zum Zentrum
# der Anwendung macht.
app = Flask(__name__)

"""
Festlegen einer Route für die Homepage. Der String in den Klammern
bildet das URL-Muster ab, unter dem der folgende Code ausgeführt
werden soll.
z.B.
* @app.route('/')    -> http://127.0.0.1:5000/
* @app.route('/abc') -> http://127.0.0.1:5000/abc
"""


# @app.route("/")
# def home() -> str:
#  print(math_service.add(1.0, 2.0))
#   app.logger.info("Rendering home page")
#    return render_template("home.html")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contact")
def contact() -> str:
    return render_template("contact.html")


@app.route("/about_flask")
def about_flask() -> str:
    app.logger.info("Rendering About Flask page")
    return render_template("about_flask.html")


# Route to handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    app.logger.info("Form submitted")
    # Access form data (request body parameters)
    name = request.form.get("name")
    # Redirect to a new URL, passing a parameter in the URL
    return redirect(url_for("result", name=name))


# Route with a parameter in the URL
@app.route("/result/<name>")
def result(name) -> str:
    app.logger.info(f"Showing result for {name}")
    return render_template("result.html", name=name)


@app.route("/get_languages")
def get_languages() -> str:
    return render_template("languages.html", languages=languages)


###########################
# BEISPIELE
###########################
@app.route('/helloWorld')
def hello_world() -> str:
    # Die Anzeigefunktion 'hello_world' gibt den String "Hello, World" als Antwort zurück
    return 'Hello, World!'


#########################
# PARFÜM
#########################
@app.route("/menu")
def menu() -> str:
    return render_template("menu.html")


@app.route("/konto")
def konto() -> str:
    return render_template("konto.html")


@app.route('/warenkorb')
def warenkorb():
    cart_items = session.get('cart', [])
    return render_template('warenkorb.html', cart=cart_items)


@app.route("/ueberuns")
def ueberuns() -> str:
    return render_template("ueberuns.html")


@app.route("/frauen")
def frauen() -> str:
    return render_template("frauen.html")


@app.route("/maenner")
def maenner() -> str:
    return render_template("maenner.html")


@app.route("/parfumepage")
def parfumepage() -> str:
    return render_template("parfumepage.html")


@app.route("/unisex")
def unisex() -> str:
    return render_template("unisex.html")


@app.route("/kontakt")
def kontakt() -> str:
    return render_template("kontakt.html")


@app.route("/homepage")
def homepage() -> str:
    return render_template("homepage.html")


@app.route("/bundlepage")
def bundlepage() -> str:
    return render_template("bundlepage.html")


@app.route("/message")
def message() -> str:
    return render_template("message.html")


@app.route("/createaccount")
def createaccount() -> str:
    return render_template("createaccount.html")


@app.route("/zahlen")
def zahlen() -> str:
    return render_template("zahlungsformular.html")


def save_to_pay(name, email, address, city, zip_code, creditcard, delivery_method, kunde_id):
    print(
        f"Speichere Bestellung: Name={name}, Email={email}, Address={address}, City={city}, Zip={zip_code}, Creditcard={creditcard}, Delivery={delivery_method}")

    conn = get_db_connection()
    cursor = conn.cursor()
    # cursor.execute("drop  table if exists warenkorb cascade")

    cursor.execute("select kunde_id from kunde")
    kunde_id = cursor.fetchall()
    cursor.execute(
        "insert into bestellung (name, email,address, city, zip_code, creditcard, delivery_method,kunde_id) values (%s, %s,%s, %s,%s, %s,%s,%s)",
        (name, email, address, city, zip_code, creditcard, delivery_method, kunde_id))

    conn.commit()
    conn.close()
    cursor.close()


@app.route("/bestellbestaetigung", methods=["POST"])
def bestellbestaetigung():
    name = request.form.get("name")
    email = request.form.get("email")
    address = request.form.get("address")
    city = request.form.get("city")
    zip_code = request.form.get("zip")
    creditcard = request.form.get("creditcard")
    delivery_method = request.form.get("delivery_method")  # Holt den Wert

    app.logger.info(f"Liefermethode erhalten: {delivery_method}")

    cart_items = session.get('cart', [])
    total_price = round(sum(float(item['price']) for item in cart_items), 2)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select kunde_id from kunde")
    kunde_id = cursor.fetchall()

    cursor.close()
    conn.close()

    save_to_pay(name, email, address, city, zip_code, creditcard, delivery_method, kunde_id)

    return render_template("bestellbestaetigung.html",
                           name=name,
                           email=email,
                           address=address,
                           city=city,
                           zip=zip_code,
                           creditcard=creditcard,
                           cart=cart_items,
                           total_price=total_price,
                           delivery_method=delivery_method)


app.secret_key = "geheimschlüssel"


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']

        return redirect(url_for('login'))

    return render_template('passwortvergessen.html')


@app.route("/zblank")
def zblank() -> str:
    return render_template("zblank.html")


def save_to_db(produkt_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("insert into warenkorb (produkt_id) values (%s)",
                   (produkt_id,))

    conn.commit()
    conn.close()
    cursor.close()


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():

    product_name = request.form.get('product_name')
    size = request.form.get('size')
    price = request.form.get('price')
    image = request.form.get('image')



    print(f"Product: {product_name}, Size: {size}, Price: {price}, Image: {image}")  # Debugging

    if not all([product_name, size, price, image]):
        print("Fehlende Daten!")
        return "Fehlende Daten", 400

    try:
        price = float(price.replace(" CHF", ""))
    except ValueError:
        print("Fehler bei der Preisumwandlung!")
        return "Ungültiger Preis", 400

    product_name = product_name.strip()
    size = size.strip()
    print(f"Gesuchter Produktname: {product_name}")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select groesse_preis_id from groesse_preis where size = %s", (size,))
    groesse_preis_id = cursor.fetchall()

    if not groesse_preis_id:
        print(f"Größe '{size}' nicht gefunden in der Tabelle 'groesse_preis'")
        return "Größe nicht gefunden", 400

    groesse_preis_id = groesse_preis_id[0]

    cursor.execute("select produkt_id from produkt where product_name = %s and groesse_preis_id = %s ",
                   (product_name, groesse_preis_id))
    produkt_id = cursor.fetchone()

    if not produkt_id:
        print(f"Kein Produkt gefunden mit dem Namen: {product_name}")
        return "Produkt nicht gefunden", 400

    produkt_id = produkt_id[0]

    save_to_db(produkt_id)




    cursor.close()
    conn.close()

    if 'cart' not in session:
        session['cart'] = []


    session['cart'].append({
        'name': product_name,
        'size': size,
        'price': price,
        'image': image,
        'warenkorb_id': produkt_id
    })


    session.modified = True
    return redirect(url_for('warenkorb'))


@app.route('/add_to_cash', methods=['POST'])
def add_to_cash():
    product_name = request.form.get('product_name')
    size = request.form.get('size')
    price = request.form.get('price')
    image = request.form.get('image')

    if not all([product_name, size, price, image]):
        return "Fehlende Daten", 400

    if 'cart' not in session:
        session['cart'] = []

    existing_item = next((item for item in session['cart'] if item['name'] == product_name and item['size'] == size),
                         None)

    if existing_item:
        return redirect(url_for('warenkorb'))

    session['cart'].append({
        'name': product_name,
        'size': size,
        'price': float(price),
        'image': image
    })

    session.modified = True
    return redirect(url_for('warenkorb'))


@app.route("/clear_cart")
def clear_cart():
    session["cart"] = []
    return redirect(url_for("warenkorb"))


@app.route("/zahlungversand")
def zahlungversand():
    cart_items = session.get('cart', [])
    total_price = sum(float(item['price']) for item in cart_items)

    return render_template("zahlungversand.html", cart=cart_items, total_price=total_price)


@app.route("/datenschutzerklaerung")
def datenschutzerklaerung() -> str:
    return render_template("datenschutzerklaerung.html")


@app.route("/agb")
def agb() -> str:
    return render_template("AGB.html")


@app.route("/remove_from_cart/<int:index>")
def remove_from_cart(index):
    cart = session.get("cart", [])



    if 0 <= index < len(cart):
        produkt_id = cart[index].get("warenkorb_id")
        print(f"Produkt-ID erhalten: {produkt_id}")

        if produkt_id is not None:

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("select warenkorb_id from warenkorb where produkt_id = %s", (produkt_id,))
            warenkorb_id = cursor.fetchone()
            if warenkorb_id:
                warenkorb_id = warenkorb_id[0]
                print(f"Warenkorb-ID zum Löschen: {warenkorb_id}")


                cursor.execute("delete from warenkorb where warenkorb_id = %s", (warenkorb_id,))
                conn.commit()


            cursor.close()
            conn.close()

        del cart[index]
        session["cart"] = cart
        session.modified = True

    return redirect(url_for("warenkorb"))




