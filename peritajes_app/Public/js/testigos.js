document.addEventListener("DOMContentLoaded", function () {
    // Obtener la sección "TESTIGOS"
    const seccionTestigos = document.getElementById("testigos-section");

    // Obtener todos los selects de testigos excepto el de "RECHAZADO"
    const selectsTestigos = seccionTestigos.querySelectorAll("select:not(#rechazado_testigos)");
    const rechazadoSelectTestigos = seccionTestigos.querySelector("#rechazado_testigos");

    // Función para verificar las opciones seleccionadas
    function verificarRechazoTestigos() {
        let algunEncendido = Array.from(selectsTestigos).some(select => select.value === "ENCENDIDO");
        let todosApagado = Array.from(selectsTestigos).every(select => select.value === "APAGADO");

        // Si algún select tiene "ENCENDIDO", forzar el rechazo a "SI"
        if (algunEncendido) {
            rechazadoSelectTestigos.value = "SI";
        } 
        // Si todas las opciones son "APAGADO", forzar el rechazo a "NO"
        else if (todosApagado) {
            rechazadoSelectTestigos.value = "NO";
        }
    }

    // Agregar evento "change" a cada select de la sección de TESTIGOS
    selectsTestigos.forEach(select => {
        select.addEventListener("change", verificarRechazoTestigos);
    });
});
