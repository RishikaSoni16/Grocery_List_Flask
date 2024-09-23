from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3 as sql

app = Flask(__name__)

def get_db_connection():
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    return con

@app.route("/")
@app.route("/index")
def index():
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM items")
    data = cur.fetchall()
    con.close()
    return render_template("index.html", datas=data)

@app.route("/add_item", methods=['POST', 'GET'])
def add_item():
    if request.method == 'POST':
        iname = request.form['iname']
        quantity = request.form['quantity']
        con = get_db_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO items (INAME, QUANTITY) VALUES (?, ?)", (iname, quantity))
        con.commit()
        con.close()
        flash('Item Added', 'success')
        return redirect(url_for("index"))
    return render_template("add_item.html")

@app.route("/edit_item/<string:id>", methods=['POST', 'GET'])
def edit_item(id):
    con = get_db_connection()
    if request.method == 'POST':
        iname = request.form['iname']
        quantity = request.form['quantity']
        cur = con.cursor()
        cur.execute("UPDATE items SET INAME=?, QUANTITY=? WHERE ID=?", (iname, quantity, id))
        con.commit()
        con.close()
        flash('Item Updated', 'success')
        return redirect(url_for("index"))
    
    cur = con.cursor()
    cur.execute("SELECT * FROM items WHERE ID=?", (id,))
    data = cur.fetchone()
    con.close()
    return render_template("edit_item.html", datas=data)

@app.route("/delete_item/<string:id>", methods=['GET'])
def delete_item(id):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM items WHERE ID=?", (id,))
    con.commit()
    con.close()
    flash('Item Deleted', 'warning')
    return redirect(url_for("index"))

# API endpoints
@app.route("/api/items", methods=['GET'])
def api_get_items():
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM items")
    items = cur.fetchall()
    con.close()
    return jsonify([dict(item) for item in items]), 200

@app.route("/api/items", methods=['POST'])
def api_add_item():
    data = request.get_json()
    iname = data.get('iname')
    quantity = data.get('quantity')

    if not iname or not quantity:
        return jsonify({'error': 'Invalid input'}), 400

    con = get_db_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO items (INAME, QUANTITY) VALUES (?, ?)", (iname, quantity))
    con.commit()
    con.close()
    return jsonify({'message': 'Item added successfully'}), 201

@app.route("/api/items/<string:id>", methods=['PUT'])
def api_edit_item(id):
    data = request.get_json()
    iname = data.get('iname')
    quantity = data.get('quantity')

    if not iname or not quantity:
        return jsonify({'error': 'Invalid input'}), 400

    con = get_db_connection()
    cur = con.cursor()
    cur.execute("UPDATE items SET INAME=?, QUANTITY=? WHERE ID=?", (iname, quantity, id))
    con.commit()
    con.close()
    return jsonify({'message': 'Item updated successfully'}), 200

@app.route("/api/items/<string:id>", methods=['DELETE'])
def api_delete_item(id):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM items WHERE ID=?", (id,))
    con.commit()
    con.close()
    return jsonify({'message': 'Item deleted successfully'}), 200

if __name__ == '__main__':
    app.secret_key = 'admin123'
    app.run(debug=True)
