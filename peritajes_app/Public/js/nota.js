function mostrarNota(containerId, select) {
    var notaContainer = document.getElementById(containerId);
    if (select.value) {
        notaContainer.style.display = "block";
    } else {
        notaContainer.style.display = "none";
    }
}