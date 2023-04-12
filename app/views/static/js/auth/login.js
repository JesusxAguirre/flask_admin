//declarando constante que guarda en un array todos los inputs dentro del id formulario
const inputs = document.querySelectorAll("#formulario input")


const campos = {
   
    email: false,

}


const expresiones = { //objeto con varias expresiones regulares

    
  
    email: /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i,

}

const validar_formulario = (e) => {

    switch (e.target.name) {
      
        case "email":
            validar_campo(expresiones.email, e.target, 'email');
            break;


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
    event.preventDefault(); // Evita que el formulario se envíe automáticamente
    if (!(campos.email)) {
        Swal.fire({
            icon: 'error',
            title: 'Lo siento ',
            text: 'Registra el formulario correctamente ',
            position: 'center'
        })
    } else {
        let url = document.getElementById('url_login').value
        $.ajax({
            type: 'POST',
            url: url,
            data: $(this).serialize(),// Obtiene los datos del formulario
            success: function (response) {
                document.getElementById("formulario").reset()
                for (let key in campos) {
                    campos[key] = false;
                }
                Swal.fire({
                    icon: 'success',
                    title: 'Has iniciado seccion correctamente'
                })

                setTimeout(location.href = document.getElementById('url_dashboard').value, 3000)
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