
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
	correo: /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i,

}


const validar_formulario  = (e) => {

    switch(e.target.name){
        case "name":
			validar_campo(expresiones.caracteres, e.target, 'name');
			break;
    }

}



$('#formulario').submit(function(event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente
  
    $.ajax({
      type: 'POST',
      url: '/register',
      data:  $(this).serialize(),// Obtiene los datos del formulario
      success: function(response) {
        console.log("entro en el success")
        // Código a ejecutar si la solicitud se realizó correctamente
      },
      error: function(xhr, status, error) {
        // Código a ejecutar si se produjo un error al realizar la solicitud
       


        console.log(xhr.responseJSON)
      }
    });
  });


//recorriendo foreach de inputs por ada inputs se le agrega un evento y se llama la funcion validar formulario
inputs.forEach((input) => {
	input.addEventListener('keyup', validar_formulario);
	input.addEventListener('blur', validar_formulario);

});

