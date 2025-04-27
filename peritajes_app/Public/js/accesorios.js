function agregarCampos(event) {
    // Prevenir que el botón haga scroll al inicio de la página
    event.preventDefault();

    // Crear un nuevo div con las clases form-group y accesorios
    var nuevoDiv = document.createElement("div");
    nuevoDiv.className = "form-group accesorios";

    // Crear input para marca
    var inputMarca = document.createElement("input");
    inputMarca.type = "text";
    inputMarca.name = "marca[]";
    inputMarca.placeholder = "Marca";
    inputMarca.required = true;

    // Crear input para descripción
    var inputDescripcion = document.createElement("input");
    inputDescripcion.type = "text";
    inputDescripcion.name = "descripcion[]";
    inputDescripcion.placeholder = "Descripción";
    inputDescripcion.required = true;

    // Añadir los inputs al nuevo div
    nuevoDiv.appendChild(inputMarca);
    nuevoDiv.appendChild(inputDescripcion);

    // Añadir el nuevo div al contenedor
    var accesorio = document.getElementById("accesorio");
    accesorio.insertBefore(nuevoDiv, accesorio.querySelector('.btn-agregar'));
}

function eliminarCampos() {
    // Obtener todos los divs de inputs
    var accesorio = document.getElementById("accesorio");
    var grupos = accesorio.getElementsByClassName("accesorios");
    
    // Eliminar el último div de inputs si existe
    if (grupos.length > 0) {
        accesorio.removeChild(grupos[grupos.length - 1]);
    }
}