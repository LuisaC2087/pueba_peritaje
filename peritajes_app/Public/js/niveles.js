document.addEventListener("DOMContentLoaded", function () {
    // Obtener la sección "NIVELES"
    const seccionNiveles = document.getElementById("niveles-section");

    // Obtener solo los selects dentro de la sección de NIVELES, excepto el de "RECHAZADO"
    const selectsNiveles = seccionNiveles.querySelectorAll("select:not(#rechazado_datos_niveles)");
    const rechazadoSelectNiveles = seccionNiveles.querySelector("#rechazado_datos_niveles");

    // Función para verificar las opciones seleccionadas
    function verificarRechazoNiveles() {
        let algunBajoNivel = Array.from(selectsNiveles).some(select => select.value === "BAJO NIVEL");
        let todosNivelNormal = Array.from(selectsNiveles).every(select => select.value === "ACEPTABLE");

        // Si algún select tiene "BAJO NIVEL", forzar el rechazo a "SI"
        if (algunBajoNivel) {
            rechazadoSelectNiveles.value = "SI";
        } 
        // Si todas las opciones son "ACEPTABLE", forzar el rechazo a "NO"
        else if (todosNivelNormal) {
            rechazadoSelectNiveles.value = "NO";
        }
    }

    // Agregar el evento "change" a cada select de la sección de NIVELES
    selectsNiveles.forEach(select => {
        select.addEventListener("change", verificarRechazoNiveles);
    });
});
