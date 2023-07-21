import sqlite3
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, flash
import middleware.db_middleware as db


class TicketApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/", methods=["GET"])(self.home)
        self.app.route("/ticket/<int:numberTicket>", methods=["GET"])(self.ticket)
        self.app.route("/newTicket/", methods=["GET"])(self.new_ticket)
        self.app.route("/cadastrar/", methods=["POST"])(self.cadastrar)
        self.app.route("/excluir/<int:numberTicket>", methods=["GET","POST"])(self.excluir)
       # self.app.route("/open_tickets_by_category/", methods=["GET"])(self.open_tickets_by_category)
        self.app.route("/new_status/<int:numberTicket>", methods=["POST"])(self.new_status)

    def home(self):
        lista = list(db.get_itens())
        lista_dicionario = []
        for tupla in lista:
            dicionario = {"id": tupla[0],"title": tupla[1], "description": tupla[3], "status_id": tupla[5], "category_id": tupla[2]}
            lista_dicionario.append(dicionario)
        return render_template("home.html", lista=lista_dicionario)

    def ticket(self, numberTicket):
        ticket = list(db.get_itens())
        dicionario = {}
        for tupla in ticket:
            if numberTicket == tupla.id:
                dicionario = {"id": tupla[0],"title": tupla[1],"category_id": tupla[2] ,"description": tupla[3],"deadline": tupla[4] ,"status_id": tupla[5],"created_at": tupla[6],"solved_at": tupla[7],"created_by": tupla[8],"handled_by": tupla[9]}
        return render_template("ticket.html", ticket=dicionario)

    def new_ticket(self):
        return render_template("newTicket.html")

    def cadastrar(self):
        title = request.form['title']
        description = request.form['description']
        deadline = request.form['deadline']
        category_id = str(request.form.get('category_id'))
        created_at = datetime.now()
        created_by = request.form['created_by']
        db.insert_item(title, category_id, description, deadline, created_at, created_by)
        return redirect(url_for('home'))

    def excluir(self,numberTicket):
        ticket = list(db.get_itens())
        dicionario = {}
        for tupla in ticket:
            if numberTicket == tupla.id:
                dicionario = {"id": tupla[0],"title": tupla[1],"category_id": tupla[2] ,"description": tupla[3],"deadline": tupla[4] ,"status_id": tupla[5],"created_at": tupla[6],"solved_at": tupla[7],"created_by": tupla[8],"handled_by": tupla[9]}
        db.excluir(dicionario["id"])
        return redirect(url_for('home'))

    def new_status(self,numberTicket):
         ticket = list(db.get_itens())
         dicionario = {}
         for tupla in ticket:
            if numberTicket == tupla.id:
                dicionario = {"id": tupla[0],"title": tupla[1],"category_id": tupla[2] ,"description": tupla[3],"deadline": tupla[4] ,"status_id": tupla[5],"created_at": tupla[6],"solved_at": tupla[7],"created_by": tupla[8],"handled_by": tupla[9]}
         status_id = str(request.form.get('status_id'))
         solved_at = datetime.now()
         db.update_status(status_id,dicionario["id"],solved_at)
         print(solved_at)
       
         return redirect(url_for('home'))
        
       
   

ticket_app = TicketApp()
app = ticket_app.app

if __name__ == "__main__":
    app.run()