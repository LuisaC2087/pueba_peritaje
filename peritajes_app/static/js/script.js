const categoriaSelect = document.getElementById('categoria');
const carroceriaSelect = document.getElementById('carroceria');

// Objeto que define las opciones válidas por cada categoría
const opcionesPorCategoria = {
    LIVIANO: ['SEDAN', 'HATCHBACK', 'COUPE', 'PICKUP DC', 'PICKUP S', 'VAN', 'CAMIONETA 5P', 'CAMIONETA 3P'],
    PESADO: ['TRACTOCAMION', 'CAMION', 'VOLCO', 'CHASIS', 'BUS', 'TRAILER']
};

// Función para actualizar las opciones de "CARROCERÍA" según la categoría seleccionada
function actualizarCarroceria() {
    // Obtener la categoría seleccionada
    const categoriaSeleccionada = categoriaSelect.value;
    const opcionesValidas = opcionesPorCategoria[categoriaSeleccionada];

    // Mostrar solo las opciones válidas
    for (let i = 0; i < carroceriaSelect.options.length; i++) {
        const option = carroceriaSelect.options[i];
        if (opcionesValidas.includes(option.value)) {
            option.style.display = 'block';  // Mostrar la opción
        } else {
            option.style.display = 'none';   // Ocultar la opción
        }
    }
    
    // Reiniciar la selección de "CARROCERÍA" si no es válida
    carroceriaSelect.value = '';
}

// Asignar el evento al cambio de categoría
categoriaSelect.addEventListener('change', actualizarCarroceria);

// Ejecutar la función al cargar la página para establecer las opciones correctas
actualizarCarroceria();


