
//declarando constante que guarda en un array todos los inputs dentro del id formulario
const inputs = document.querySelectorAll("#formulario input")


const campos = {
    name: false,
    apellido: false,
    email: false,
    password: false,
    retype_password: false,
}

const expresiones = { //objeto con varias expresiones regulares

    caracteres: /^[A-ZÑa-zñáéíóúÁÉÍÓÚ'°]{3,12}$/, // Letras y espacios, pueden llevar acentos.
    password: /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/, // 6 a 16 digitos.
    email: /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i,

}



const validar_formulario = (e) => {

    switch (e.target.name) {
        case "name":
            validar_campo(expresiones.caracteres, e.target, 'name');
            break;

        case "apellido":
            validar_campo(expresiones.caracteres, e.target, 'apellido');
            break;

        case "email":
            validar_campo(expresiones.email, e.target, 'email');
            break;

        case "password":
            validar_campo(expresiones.password, e.target, 'password');
            break;

        case "password2":
            validar_equals_password(expresiones.password, e.target, 'password2');
            break

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

const validar_equals_password = (expresion,input,campo)=> {
    if (expresion.test(input.value) && input.value == document.getElementById('password').value ) {
       
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
    if (!(campos.name && campos.apellido && campos.email && campos.password && campos.retype_password)) {
        Swal.fire({
            icon: 'error',
            title: 'Lo siento ',
            text: 'Registra el formulario correctamente ',
            position: 'center'
        })
    } else {
        $.ajax({
            type: 'POST',
            url: '/register',
            data: $(this).serialize(),// Obtiene los datos del formulario
            success: function (response) {
                console.log("entro en el success")
                // Código a ejecutar si la solicitud se realizó correctamente
            },
            error: function (xhr, status, error) {
                // Código a ejecutar si se produjo un error al realizar la solicitud
                Swal.fire({
                    icon: 'error',
                    title: 'Lo siento ',
                    text: 'Registra el formulario correctamente '
                })


                console.log(xhr.responseJSON)
            }
        });
    }
});


//recorriendo foreach de inputs por ada inputs se le agrega un evento y se llama la funcion validar formulario
inputs.forEach((input) => {
    input.addEventListener('keyup', validar_formulario);
    input.addEventListener('blur', validar_formulario);

});

