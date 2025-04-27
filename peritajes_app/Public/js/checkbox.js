document.getElementById('peritaje_formulario').addEventListener('submit', function(event) {
    // Evita el envío del formulario si no pasa la validación
    if (!validarCheckboxes()) {
        event.preventDefault(); // Evita el envío
        alert('Debes seleccionar al menos una opcion en cada sección.');
    }
});

function validarCheckboxes() {
    // Obtener todas las secciones de checkboxes (clase form-group)
    const checkboxGroups = document.querySelectorAll('.form-group');
    let isValid = true; // Variable para comprobar si la validación es correcta
    let firstInvalidGroup = null; // Variable para el primer grupo no válido

    checkboxGroups.forEach(group => {
        const checkboxes = group.querySelectorAll('input[type="checkbox"]'); // Solo checkboxes
        const isChecked = Array.from(checkboxes).some(checkbox => checkbox.checked); // Comprobar si hay al menos uno seleccionado

        // Eliminar la clase 'highlight' si ya existe
        group.classList.remove('highlight');

        if (checkboxes.length > 0 && !isChecked) { // Validar solo si hay checkboxes
            isValid = false; // La validación falla

            // Marcar la primera sección no válida
            if (!firstInvalidGroup) {
                firstInvalidGroup = group;
            }

            // Resaltar el grupo no válido
            group.classList.add('highlight');
        }
    });

    // Si hay una sección no válida, hacer scroll hasta ella
    if (firstInvalidGroup) {
        firstInvalidGroup.scrollIntoView({ behavior: 'smooth' });
    }

    return isValid; // Devuelve true si todas las secciones de checkboxes son válidas
}