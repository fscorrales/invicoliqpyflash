from flask import render_template, request, url_for
from werkzeug.utils import redirect
from invicoliqpy import app, db
from invicoliqpy.models import Factureros
from invicoliqpy.forms import FacturerosForm

#http://localhost:5000/
@app.route('/')
def inicio():
    factureros = Factureros.query
    return render_template('table_factureros.html', factureros = factureros)

""" @app.route('/agregar', methods=['GET','POST'])
def agregar():
    facturero = Factureros()
    factureroForm = FacturerosForm(obj=facturero)
    if request.method == 'POST':
        if factureroForm.validate_on_submit():
           factureroForm.populate_obj(facturero)
           app.logger.debug(f'Persona a insertar: {facturero}')
           #Insertamos el nuevo registro
           db.session.add(facturero)
           db.session.commit()
           return redirect(url_for('inicio'))
    return render_template('agregar.html', forma = factureroForm) """

@app.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    #Recuperamos el objeto persona a editar
    facturero = Factureros.query.get_or_404(id)
    factureroForm = FacturerosForm(obj=facturero)
    if request.method == 'POST':
        if factureroForm.validate_on_submit():
            factureroForm.populate_obj(facturero)
            app.logger.debug(f'Facturero a actualizar: {facturero}')
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('form_factureros.html', 
    titulo = 'Editar',
    form = factureroForm)

@app.route('/delete/<int:id>')
def delete(id):
    facturero = Factureros.query.get_or_404(id)
    try:
        db.session.delete(facturero)
        db.session.commit()
        #Return messagge:
        #flash("delete facturero")
    except:
        #flash("problema al borrar un facturero")
        app.logger.debug(f'Facturero: {facturero} no se pudo borrar')
    finally:
        factureros = Factureros.query
        return render_template('table_factureros.html', factureros = factureros)