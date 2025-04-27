function validarCantidad() {
    var input = document.getElementById('imagenes');
    var archivos = input.files;
    var fileNameDisplay = document.getElementById('file-name');

    // Verificar la cantidad de archivos seleccionados
    if (archivos.length > 0) {
      var nombresArchivos = [];
      for (var i = 0; i < archivos.length; i++) {
        nombresArchivos.push(archivos[i].name);
      }
      fileNameDisplay.textContent = "Archivos seleccionados: " + nombresArchivos.join(', ');
    } else {
      fileNameDisplay.textContent = "No se han seleccionado archivos";
    }

    // Verificar la cantidad mínima y máxima de archivos seleccionados
    if (archivos.length < 2) {
      alert("Debes subir al menos 2 imágenes.");
      input.value = ""; // Limpiar el input
      fileNameDisplay.textContent = "No se han seleccionado archivos";
    } else if (archivos.length > 10) {
      alert("No puedes subir más de 10 imágenes.");
      input.value = ""; // Limpiar el input
      fileNameDisplay.textContent = "No se han seleccionado archivos";
    }
  }