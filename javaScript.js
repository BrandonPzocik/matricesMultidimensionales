const prompt = require("prompt-sync")(); // Importar la librería

let personas = []; // Array para almacenar los datos

while (true) {
    let nombre = prompt("Ingrese el nombre: ");
    let apellido = prompt("Ingrese el apellido: ");
    let dni = prompt("Ingrese el DNI: ");

    let telefonos = [];
    while (true) {
        let telefono = prompt("Ingrese un número de teléfono (o 'fin' para terminar): ");
        if (telefono.toLowerCase() === "fin") {
            break;
        }
        telefonos.push(telefono);
    }

    // Guardar la persona en el array
    personas.push([nombre, apellido, dni, telefonos]);

    // Preguntar si desea continuar
    let continuar = prompt("¿Desea cargar otra persona? (si/no): ");
    if (continuar.toLowerCase() !== "si") {
        break;
    }
}

// Mostrar los datos ingresados
console.log("\nDatos ingresados:");
personas.forEach(persona => {
    console.log(persona);
});
