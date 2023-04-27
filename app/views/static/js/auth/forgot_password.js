//declarando constante que guarda en un array todos los inputs dentro del id formulario
const formulario = document.getElementById("formulario")
const inputs = document.querySelectorAll("#formulario input")
const boton_submit = document.getElementById("boton_submit")

const campos = {

    email: false,
    tokenCorreo: false,

}




const expresiones = { //objeto con varias expresiones regulares



    email: /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i,
    tokenCorreo: /^[0-9]{6}$/ 
}

const validar_formulario = (e) => {

    switch (e.target.name) {

        case "email":
            validar_campo(expresiones.email, e.target, 'email');
            break;

        case "tokenCorreo":
            console.log("entra al case")



            validar_campo(expresiones.tokenCorreo, e.target, 'tokenCorreo')
    }

}

const validar_campo = (expresion, input, campo) => {
    if (expresion.test(input.value)) {

        document.querySelector(`#grupo__${campo} p`).classList.remove('d-block');
        document.querySelector(`#grupo__${campo} input`).classList.remove('is-invalid')

        document.querySelector(`#grupo__${campo} p`).classList.add('d-none');
        campos[campo] = true;

    } else {


        document.querySelector(`#grupo__${campo} p`).classList.remove('d-none');

        document.querySelector(`#grupo__${campo} p`).classList.add('d-block');
        document.querySelector(`#grupo__${campo} input`).classList.add('is-invalid')
        campos[campo] = false;
    }
}

$('#formulario').submit(function (event) {
    console.log("Entra en el primer formulario")
    event.preventDefault(); // Evita que el formulario se envíe automáticamente
    if (!(campos.email)) {
        Swal.fire({
            icon: 'error',
            title: 'Lo siento ',
            text: 'Registra el formulario correctamente ',
            position: 'center'
        })
    } else {
        let url = document.getElementById('url_forgot').value
        $.ajax({
            type: 'POST',
            url: url,
            data: $(this).serialize(),// Obtiene los datos del formulario
            success: function (response) {
                // Crear un elemento div
                var div = document.createElement('div');
                div.id = 'grupo__tokenCorreo'
                div.innerHTML = `
                    <div class="input-group mb-3">
                        <input id="tokenCorreo" name="tokenCorreo" type="text" class="form-control" placeholder="Codigo">
                        <div class="input-group-append">
                            <div class="input-group-text">
                                <span class="fas fa-key"></span>
                            </div>
                        </div>
                    </div>
                    <p class="text-danger d-none">Escriba un token valido</p>`;

                // Obtener el nodo padre del botón_submit
                var nodo = formulario.lastElementChild;

                // Insertar el elemento div antes del nodo padre del botón_submit
                formulario.insertBefore(div, nodo);

                // Deshabilitar el elemento con el id "email"
                document.getElementById("email").setAttribute('readonly', true);

                formulario.id = "formulario2"

                boton_submit.setAttribute('form', 'formulario2') 

                $('#boton_submit').attr('form', 'formulario2');

                boton_submit.textContent = "Enviar codigo"
                
                const inputs = document.querySelectorAll("#formulario2 input")

                inputs.forEach((input) => {
                    input.addEventListener('keyup', validar_formulario);
                    input.addEventListener('blur', validar_formulario);
                
                });

                Swal.fire({
                    toast: true,
                    title: 'Se ha enviado un codigo a tu correo por favor colocalo en el campo del formulario para resetear tu password',
                    position: 'top-end',
                    html: 'El tiempo se acabara en <b></b> .',
                    showConfirmButton: false,
                    timerProgressBar: true,
                    timer: 300000, // Tiempo en milisegundos (5 minutos = 300000 milisegundos)
                    didOpen: () => {
                        Swal.showLoading();
                        const b = Swal.getHtmlContainer().querySelector('b');
                        let contador = 300;
                        const intervalo = setInterval(() => {
                            contador--;
                            // Formatear el tiempo restante en minutos y segundos
                            const minutos = Math.floor(contador / 60);
                            const segundos = contador % 60;
                            b.textContent = `${minutos}:${segundos.toString().padStart(2, '0')}`;
                            if (contador === 0) {
                                clearInterval(intervalo);
                                Swal.close();
                            }
                        }, 1000);
                    },
                    willClose: () => {
                        window.location.replace(url);
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
    }
});


$('#formulario2').submit(function (event) {
    console.log("entra en el segundo formulario")
    event.preventDefault(); // Evita que el formulario se envíe automáticamente
    if (!(campos.email && campos.tokenCorreo)) {
        Swal.fire({
            icon: 'error',
            title: 'Lo siento ',
            text: 'Registra el formulario correctamente ',
            position: 'center'
        })
    } else {
        let url = document.getElementById('url_forgot').value
        $.ajax({
            type: 'POST',
            url: url,
            data: $(this).serialize(),// Obtiene los datos del formulario
            success: function (response) {

                console.log(response)

                Swal.fire({
                    icon: 'success',
                    title: 'Se ha restaurado tu contraseña correctamente, revisa tu correo'
                }).then((result) => {
                    /* Read more about isConfirmed, isDenied below */
                    if (result.isConfirmed) {
                     window.location.replace(url);
                    } 
                  })

    
                
                setTimeout(function() {
                    window.location.replace(url);
                  },4000);



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
    }
});





//recorriendo foreach de inputs por ada inputs se le agrega un evento y se llama la funcion validar formulario
inputs.forEach((input) => {
    input.addEventListener('keyup', validar_formulario);
    input.addEventListener('blur', validar_formulario);

});

