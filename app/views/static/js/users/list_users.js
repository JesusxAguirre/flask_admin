

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


//CREANDO CONSTANTES PARA VALIDAR FORMULARIO DE EDITAR
const selects = document.querySelectorAll('#formulario_editar select');
const campos = {
    roles: false
}

const ValidarFormulario = (e) => {
	switch (e.target.name) {

		case "roles":
			ValidarSelect(e.target, 'roles');
			break;
	
	}
}


const ValidarSelect = ( input, campo) => {
    
	if (input.value === "admin" || input.value === "gerente" || input.value === "almacenista" || input.value === "vendedora") {
        document.querySelector(`#grupo__${campo} p`).classList.remove('d-block');
        document.querySelector(`#grupo__${campo} select`).classList.remove('is-invalid')

        document.querySelector(`#grupo__${campo} p`).classList.add('d-none');
		campos[campo] = true;
	} else {
        
		document.querySelector(`#grupo__${campo} p`).classList.remove('d-none');

        document.querySelector(`#grupo__${campo} p`).classList.add('d-block');
        document.querySelector(`#grupo__${campo} select`).classList.add('is-invalid')
        
		campos[campo] = false;
	}
}

//AGREGANDO EVENTOS A LOS SELECTS
selects.forEach((select) => {
    select.addEventListener('change', ValidarFormulario);
    select.addEventListener('blur', ValidarFormulario);
});

//PULSACION DE BOTON EDITAR PETICICION PUT
$('#tabla_usuarios tbody').on('click', '.btn-edit', function () {
    var row = $(this).closest('tr');
    var id = row.find('td:eq(0)').text();


    let url = "/users/" + id
    $.ajax({
        type: 'GET',
        url: url,
        success: function (response) {

            // Actualizar contenido de cada span con los datos del objeto
            $("#rol option[value=" + response.rol + "]").attr("selected", true);
            $('#name').text(response.name);
            $('#apellido').text(response.apellido);
            $('#email').text(response.email);

            // Mostrar el modal
            $('#modalEditar').modal('show');



            //envio de formulario 



            $('#formulario_editar').submit(function (event) {
                event.preventDefault(); // Evita que el formulario se envíe automáticamente
                if (!(campos.rol)) {
                    Swal.fire({
                        icon: 'error',
                        title: 'Lo siento ',
                        text: 'Registra el formulario correctamente ',
                        position: 'center'
                    })
                } else {
                    let url = document.getElementById("url_register").value
                    $.ajax({
                        type: 'PUT',
                        url: url,
                        data: $(this).serialize(),// Obtiene los datos del formulario
                        success: function (response) {
                            document.getElementById("formulario").reset()
                            for (let key in campos) {
                                campos[key] = false;
                            }
                            Swal.fire({
                                icon: 'success',
                                title: 'Te has registrado correctamente en el sistema'
                            })
                        },
                        error: function (xhr, status, error) {
                            // Código a ejecutar si se produjo un error al realizar la solicitud

                            if (xhr.responseJSON.ErrorType == "UserAlreadyExist") {
                                document.querySelector(`#grupo__email p`).classList.remove('d-none');

                                document.querySelector(`#grupo__email p`).classList.add('d-block');
                                document.querySelector(`#grupo__email input`).classList.add('is-invalid')
                                campos.email = false;

                                document.getElementById('mensaje_email').textContent = xhr.responseJSON.Message
                            }
                            Swal.fire({
                                icon: 'error',
                                title: xhr.responseJSON.ErrorType,
                                text: xhr.responseJSON.Message
                            })



                        }
                    });
                }
            });

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









































