from flask import Flask, render_template, redirect, request, url_for, flash
import middleware.db_middleware as db




app = Flask(__name__)


 
@app.route("/", methods=["GET"])
def home():

    lista=list(db.get_itens())

    lista_dicionario = []

    for tupla in lista:
        dicionario = {"id": tupla[0],"title": tupla[1], "description": tupla[3], "status_id": tupla[5], "category_id": tupla[2]}
        lista_dicionario.append(dicionario)
        
    return render_template("home.html",lista=lista_dicionario)

@app.route("/ticket/<int:numberTicket>",methods=["GET"])
def ticket(numberTicket):
    
     ticket=list(db.get_itens())

     
     dicionario = {}

     for tupla in ticket:
            if numberTicket == tupla.id:
    
             dicionario = {"id": tupla[0],"title": tupla[1],"category_id": tupla[2] ,"description": tupla[3],"deadline": tupla[4] ,"status_id": tupla[5],"created_at": tupla[6],"solved_at": tupla[7],"created_by": tupla[8],"handled_by": tupla[9]}
             print(dicionario)
        
     return render_template("ticket.html",ticket=dicionario)


# Redireciona para a pagina
@app.route("/newTicket/",methods=["GET"])
def newticket():   
    return render_template("newTicket.html")



@app.route("/cadastrar/",methods=["POST"])
def cadastrar():

    title = request.form['title']
    description = request.form['description']
    deadline = request.form['deadline']
    category_id = str(request.form.get('category_id'))
    created_at = request.form['created_at']
    created_by = request.form['created_by']
 
    db.insert_item(title, category_id, description, deadline, created_at, created_by)
    return redirect (url_for('home'))


@app.route("/excluir/", methods=["GET","POST"])
def excluir():
    
    data = request.get_json()
    id=data['id']
    
    return render_template(url_for('home')
    )

if __name__ == "__main__":
    app.run()



