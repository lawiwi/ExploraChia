// Obtener los botones y las categorías
const todosBtn = document.getElementById("todosBtn");
const comidaBtn = document.getElementById("comidaBtn");
const ocioBtn = document.getElementById("ocioBtn");
const deportesBtn = document.getElementById("deportesBtn");

const comidaCategory = document.getElementById("comida");
const ocioCategory = document.getElementById("ocio");
const deportesCategory = document.getElementById("deportes");

// Función para mostrar las categorías
function showCategory(category) {
    comidaCategory.style.display = 'none';
    ocioCategory.style.display = 'none';
    deportesCategory.style.display = 'none';
    category.style.display = 'block';
}

// Mostrar todas las categorías al presionar "Todos"
todosBtn.addEventListener("click", function() {
    comidaCategory.style.display = 'block';
    ocioCategory.style.display = 'block';
    deportesCategory.style.display = 'block';
});

// Mostrar categoría de comida
comidaBtn.addEventListener("click", function() {
    showCategory(comidaCategory);
});

// Mostrar categoría de ocio
ocioBtn.addEventListener("click", function() {
    showCategory(ocioCategory);
});

// Mostrar categoría de deportes
deportesBtn.addEventListener("click", function() {
    showCategory(deportesCategory);
});