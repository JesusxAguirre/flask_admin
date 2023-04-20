$(document).ready(function () {
    $.ajax({
        url: document.getElementById('url_data').value,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            $('#tabla_usuarios').DataTable({
                data: data,
                columns: [
                    { data: 'id', title: 'ID' },
                    { data: 'name', className: "text-capitalize", title: 'Nombre' },
                    { data: 'apellido', className: "text-capitalize", title: 'Apellido' },
                    { data: 'email', title: 'Email' },
                    {
                        data: null,
                        title: "Acciones",
                        className: "project-actions text-center",
                        defaultContent: '<a class="btn btn-primary btn-sm btn-view" href="#"><i class="fas fa-folder"/>Ver </i></a> <a class="btn btn-info btn-sm btn-edit" href="#"><i class="fas fa-pencil-alt"></i> Editar</a> <a class="btn btn-danger btn-sm btn-delete" href="#"><i class="fas fa-trash"></i>Eliminar </a>',
                        orderable: false
                    },

                ],
                "responsive": true, "lengthChange": false, "autoWidth": false,
                buttons: [
                    'csv', 'excel', 'pdf', 'print'
                ],

            }).buttons().container().appendTo('#tabla_usuarios_wrapper .col-md-6:eq(0)');

        },
        error: function (xhr, status, error) {
            console.log(xhr)
        }
    });



    //PULSACION DE BOTON DE EDIT SOLICITUD GET POR URL ASINCRONICA
    $('#tabla_usuarios tbody').on('click', '.btn-view', function () {
        var row = $(this).closest('tr');
        var id = row.find('td:eq(0)').text();
        // Aquí puedes realizar las acciones correspondientes con el id recuperado
        console.log("Id de la fila seleccionada: " + id);

        let url = "/users/" + id
        $.ajax({
            type: 'GET',
            url: url,
            success: function (response) {
                
                // Actualizar contenido de cada span con los datos del objeto
                $('#rolUsuario').text(response.rol);
                $('#nombreUsuario').text(response.name);
                $('#apellidoUsuario').text(response.apellido);
                $('#emailUsuario').text(response.email);
                $('#telefonoUsuario').text(response.telefono ? response.telefono : 'Sin identificar');
                $('#direccionUsuario').text(response.direccion ? response.direccion : 'Sin identificar');
                $('#fechaUsuario').text(response.fecha_registro);
               
               

                // Mostrar el modal
                $('#modalVer').modal('show');

            },
            error: function (xhr, status, error) {
                // Código a ejecutar si se produjo un error al realizar la solicitud

                Swal.fire({
                    icon: 'error',
                    title: xhr.responseJSON.ErrorType,
                    text: xhr.responseJSON.Message
                })
            }
        });
    });




    //PULSACION DE BOTON EDITAR PETICICION PUT
    $('#tabla_usuarios tbody').on('click', '.btn-edit', function () {
        var row = $(this).closest('tr');
        var id = row.find('td:eq(0)').text();

        
        let url = "/users/" + id
        $.ajax({
            type: 'PUT',
            url: url,
            success: function (response) {
                
                // Actualizar contenido de cada span con los datos del objeto
                $("#rol option[value="+ response.rol +"]").attr("selected",true);
                $('#name').text(response.name);
                $('#apellido').text(response.apellido);
                $('#email').text(response.email);
             
                // Mostrar el modal
                $('#modalEditar').modal('show');

            },
            error: function (xhr, status, error) {
                // Código a ejecutar si se produjo un error al realizar la solicitud

                Swal.fire({
                    icon: 'error',
                    title: xhr.responseJSON.ErrorType,
                    text: xhr.responseJSON.Message
                })
            }
        }); 



    });


    //PULSACION DE BOTON DELETE PETICION DELETE
    $('#tabla_usuarios tbody').on('click', '.btn-delete', function () {
        var row = $(this).closest('tr');
        var id = row.find('td:eq(0)').text();
        // Aquí puedes realizar las acciones correspondientes con el id recuperado
        console.log("Id de la fila seleccionada: " + id);
    });











































});
