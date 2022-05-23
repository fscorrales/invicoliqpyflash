from flask import render_template, request, url_for, flash
from werkzeug.utils import redirect
from invicoliqpy import app, db
from invicoliqpy.models import Factureros, HonorariosFactureros
from invicoliqpy.forms import FacturerosForm

def get_list_of_dict(keys, list_of_tuples):
    """
    This function will accept keys and list_of_tuples as args and return list of dicts
    """
    list_of_dict = [dict(zip(keys, values)) for values in list_of_tuples]
    return list_of_dict

#http://localhost:5000/
@app.route('/')
def inicio():
    return render_template('home.html')

@app.route('/factureros')
def factureros():
    return render_template('table_factureros.html')

# @app.route('/agentes')
# def factureros():
#     factureros = Factureros.query
#     return render_template('table_factureros_basic.html', factureros = factureros)

@app.route('/api/factureros')
def api_factureros():
    return {'data': [facturero.to_dict() for facturero in Factureros.query]}

@app.route('/factureros/agregar', methods=['GET','POST'])
def facturero_agregar():
    facturero = Factureros()
    factureroForm = FacturerosForm(obj=facturero)
    if request.method == 'POST':
        if factureroForm.validate_on_submit():
            factureroForm.populate_obj(facturero)
            app.logger.debug(f'Persona a insertar: {facturero}')
            #Insertamos el nuevo registro
            db.session.add(facturero)
            db.session.commit()
            return redirect(url_for('factureros'))
    return render_template('form_factureros.html',
    titulo = 'Agregar',
    form = factureroForm)

@app.route('/factureros/editar/<int:id>', methods=['GET','POST'])
def facturero_editar(id):
    #Recuperamos el objeto persona a editar
    facturero = Factureros.query.get_or_404(id)
    factureroForm = FacturerosForm(obj=facturero)
    if request.method == 'POST':
        if factureroForm.validate_on_submit():
            factureroForm.populate_obj(facturero)
            app.logger.debug(f'Facturero a actualizar: {facturero}')
            db.session.commit()
            return redirect(url_for('factureros'))
    return render_template('form_factureros.html', 
    titulo = 'Editar',
    form = factureroForm)

@app.route('/factureros/borrar/<int:id>')
def facturero_borrar(id):
    facturero = Factureros.query.get_or_404(id)
    try:
        db.session.delete(facturero)
        db.session.commit()
        #Return messagge:
        #flash("delete facturero")
        return redirect(url_for('factureros'))
    except:
        flash("problema al borrar un facturero")
        app.logger.debug(f'Facturero: {facturero} no se pudo borrar')
        return redirect(url_for('factureros'))

@app.route('/siif-factureros')
def siif_factureros():
    return render_template('table_siif_factureros.html')

@app.route('/api/honorarios-factureros')
def api_honorarios_factureros():
    return {'data': [honorario.to_dict() for honorario in HonorariosFactureros.query]}

@app.route('/api/siif-factureros')
def api_siif_factureros():
    comprobantes_siif = db.session.query(HonorariosFactureros.nro_comprobante, 
    HonorariosFactureros.fecha, db.func.sum(HonorariosFactureros.importe_bruto), 
    db.func.count(HonorariosFactureros.nro_comprobante)).group_by(HonorariosFactureros.nro_comprobante).all()
    keys = ('nro_comprobante', 'fecha', 'importe_bruto', 'cantidad')
    return {'data':get_list_of_dict(keys, comprobantes_siif)}

@app.route('/siif-factureros/agregar')
def siif_facturero_agregar():
    # facturero = Factureros()
    # factureroForm = FacturerosForm(obj=facturero)
    # if request.method == 'POST':
    #     if factureroForm.validate_on_submit():
    #         factureroForm.populate_obj(facturero)
    #         app.logger.debug(f'Persona a insertar: {facturero}')
    #         #Insertamos el nuevo registro
    #         db.session.add(facturero)
    #         db.session.commit()
    #         return redirect(url_for('factureros'))
    return render_template('wizard_download_honorarios.html')

@app.route('/siif-factureros/borrar/<nro_comprobante>')
def siif_factureros_borrar(nro_comprobante):
    nro_comprobante = nro_comprobante.replace('-','/')
    siif = HonorariosFactureros.query.filter_by(nro_comprobante=nro_comprobante)
    try:
        siif.delete()
        db.session.commit()
        #Return messagge:
        #flash("delete facturero")
        return redirect(url_for('siif_factureros'))
    except:
        flash("problema al borrar un facturero")
        app.logger.debug(f'Nro comprobante: {nro_comprobante} SIIF no se pudo borrar')
        return redirect(url_for('siif_factureros'))