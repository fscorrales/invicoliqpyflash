$(document).ready(function() {
    $('#table-factureros tfoot th').each( function () {
    var title = $(this).text();
    if (title != '') {
        $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
    }
} );

    var table = $('#table-factureros').DataTable( {
        ajax: '/api/factureros',
        scrollY:        450,
        deferRender:    true,
        bScrollCollapse: true,
        scroller:       true,
        columns: [
            {data: 'nombre_completo'},
            {data: 'actividad'},
            {data: 'partida'},
            {data: 'id', orderable: false,  className: 'dt-col-button', 
            render: function (data, type, full, meta) {
                        return '<form action=/factureros/editar/'+ parseInt(data) + '>' +
                            '<button class="btn-small edit-person">' +
                                '<i class="material-icons">edit</i>'+
                            '</button>' +
                        '</form>';
                        }
            },
            {data: 'id', orderable: false,  className: 'dt-col-button',
            render: function (data, type, full, meta) {
                        return '<form action=/factureros/borrar/'+ parseInt(data) + '>' +
                            '<button class="btn-small delete-person">' +
                                '<i class="material-icons">delete</i>'+
                            '</button>' +
                        '</form>';
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
            {text: '<form action="/factureros/agregar/">'+
                        '<span class="caption">Agregar</span>' +
                        '<span class="icon">' +
                            '<i class="material-icons add-person">person_add</i>' +
                        '</span>'+
                    '</form>',
            className: 'top add-person label-button',
            action: function ( e, dt, node, config ) {
                window.location.replace("/factureros/agregar");
            }}
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
} );