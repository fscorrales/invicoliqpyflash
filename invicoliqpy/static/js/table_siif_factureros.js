// DataTable init
$(document).ready(function() {
    $('#table-siif-factureros tfoot th').each( function () {
    var title = $(this).text();
    if (title != '') {
        $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
    }
} );

    var table = $('#table-siif-factureros').DataTable( {
        ajax: '/api/siif-factureros',
        scrollY:        450,
        scrollX: false,
        deferRender:    true,
        bScrollCollapse: true,
        scroller:       true,
        columns: [
            {data: 'nro_comprobante'},
            {data: 'fecha'},
            {data: 'importe_bruto'},
            {data: 'cantidad'},
            // {data: 'iibb'},
            // {data: 'libramiento_pago'},
            // {data: 'sellos'},
            // {data: 'seguro'},
            // {data: 'otras_retenciones'},
            // {data: 'anticipo'},
            // {data: 'descuento'}
            {data: 'nro_comprobante', orderable: false,  className: 'dt-col-button', 
            render: function (data, type, full, meta) {
                        return '<form action='+ $URL_FACTUREROS_EDITAR.replace(0, parseInt(data)) + '>' +
                            '<button class="btn-small edit siif">' +
                                '<i class="material-icons">edit</i>'+
                            '</button>' +
                        '</form>';
                        }
            },
            {data: 'nro_comprobante', orderable: false,  className: 'dt-col-button',
            render: function (data, type, full, meta) {
                        return'<button class="btn-small delete siif" id='+ (data) +'>' +
                                '<i class="material-icons">delete</i>'+
                            '</button>'
                        }
            },
        ],
        // columnDef: [
        //     {
        //         targets: [1],
        //         className: 'dt-body-center'
        //     }
        // 
        dom: "<'row'<'col-sm-12 col-md-6'l><'col-sm-12 col-md-6'B>>" +
            "<'row'<'col-sm-12'tr>>" +
            "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>",
        button: {
            className: 'btn'
        },
        buttons: [
            {extend: 'collection',
            text: '<i class="material-icons">content_copy</i>',
            className: 'top copy',
            buttons:[
                'copyHtml5',
                'excelHtml5',
                'csvHtml5',
                'pdfHtml5'
            ]},
            {text:'<i class="material-icons">file_download</i>',
            className: 'top download'
            },
            // {text: '<form action="/factureros/agregar/">'+
            //             '<span class="caption">Agregar</span>' +
            //             '<span class="icon">' +
            //                 '<i class="material-icons add-person">person_add</i>' +
            //             '</span>'+
            //         '</form>',
            // className: 'top add-person label-button',
            // action: function ( e, dt, node, config ) {
            //     // $('#modal-agregar-facturero').modal('show');
            //     window.location.replace($URL_FACTUREROS_AGREGAR);
            // }}
        ],
        // language: {
        //     lengthMenu: "Display _MENU_ records per page",
        //     zeroRecords: "Nothing found - sorry",
        //     info: "Showing page _PAGE_ of _PAGES_",
        //     infoEmpty: "No records available",
        //     infoFiltered: "(filtered from _MAX_ total records)"
        // },
        initComplete: function () {
        // Apply the search
        this.api().columns().every( function () {
            var that = this;

            $( 'input', this.footer() ).on( 'keyup change clear', function () {
                if ( that.search() !== this.value ) {
                    that
                        .search( this.value )
                        .draw();
                }
            } );
        } );
    }
    } );
// } );
// END DataTable init

var fila; //captura la fila, para editar o eliminar
var nro_comprobante;

//Borrar
$(document).on("click", ".delete.siif", function(){
    nro_comprobante = this.id;
    // fila = $(this);           
    // var nombre = ($(this).closest('tr').find('td:eq(0)').text()) ;	
    // $("#formUsuarios").trigger("reset");
    // $(".modal-header").css( "background-color", "#17a2b8");
    // $(".modal-header").css( "color", "white" );
    $(".modal-title").text("Borrar Comprobante SIIF");
    $(".modal-message").text("¿Desea borrar el Nro Comprobante SIIF: " + nro_comprobante + "?");
    $('#modal-borrar-siif-factureros').modal('show');		     
    // var respuesta = confirm("¿Está seguro de borrar el registro "+id+"?");                
    // if (respuesta) {      
    // '<form action=/factureros/borrar/'+ parseInt(data) + '>' +      
    //     $.ajax({
    //         url: "bd/crud.php",
    //         type: "POST",
    //         datatype:"json",    
    //         data:  {opcion:opcion, user_id:user_id},    
    //         success: function() {
    //             tablaUsuarios.row(fila.parents('tr')).remove().draw();                  
    //         }
    //     });	
    // }
});
//submit para el Alta y Actualización
$(document).on("click", "#submit-delete-siif", function(){       
    $('#borrar-siif-factureros').modal('hide');
    nro_comprobante = nro_comprobante.replace('/','-')
    window.location.replace($URL_SIIF_FACTUREROS_BORRAR.replace('0', nro_comprobante));
});



// var fila; //captura la fila, para editar o eliminar
// //submit para el Alta y Actualización
// $('#formUsuarios').submit(function(e){                         
//     e.preventDefault(); //evita el comportambiento normal del submit, es decir, recarga total de la página
//     username = $.trim($('#username').val());    
//     first_name = $.trim($('#first_name').val());
//     last_name = $.trim($('#last_name').val());    
//     gender = $.trim($('#gender').val());    
//     password = $.trim($('#password').val());
//     status = $.trim($('#status').val());                            
//         $.ajax({
//           url: "bd/crud.php",
//           type: "POST",
//           datatype:"json",    
//           data:  {user_id:user_id, username:username, first_name:first_name, last_name:last_name, gender:gender, password:password ,status:status ,opcion:opcion},    
//           success: function(data) {
//             tablaUsuarios.ajax.reload(null, false);
//            }
//         });			        
//     $('#modalCRUD').modal('hide');											     			
// });

});    