document.addEventListener("DOMContentLoaded", function () {
    // Obtener la sección "FUGAS"
    const seccionFugas = document.getElementById("fugas-section");
    
    // Obtener solo los selects dentro de la sección de FUGAS, excepto el de "RECHAZADO"
    const selectsFugas = seccionFugas.querySelectorAll("select:not(#rechazado_datos)");
    const rechazadoSelect = seccionFugas.querySelector("#rechazado_datos");

    // Función para verificar las opciones seleccionadas
    function verificarRechazo() {
        let algunSi = Array.from(selectsFugas).some(select => select.value === "SI");
        let todosNo = Array.from(selectsFugas).every(select => select.value === "NO");

        // Si algún select tiene "SI", forzar el rechazo a "SI"
        if (algunSi) {
            rechazadoSelect.value = "SI";
        } 
        // Si todas las opciones son "NO", forzar el rechazo a "NO"
        else if (todosNo) {
            rechazadoSelect.value = "NO";
        }
    }

    // Agregar el evento "change" a cada select de la sección de FUGAS
    selectsFugas.forEach(select => {
        select.addEventListener("change", verificarRechazo);
    });
});
