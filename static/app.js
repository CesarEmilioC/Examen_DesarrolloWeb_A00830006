// Espera a que todo el contenido del documento haya sido cargado y esté listo.
document.addEventListener('DOMContentLoaded', function() {

    // Obtiene el formulario de alta de alumno por su ID
    const altaAlumnoForm = document.getElementById('alta-alumno-form');
    // Verifica si el formulario existe en la página
    if (altaAlumnoForm) {
        // Agrega un evento de escucha para el evento 'submit' del formulario
        altaAlumnoForm.addEventListener('submit', function(e) {
            // Previene el comportamiento predeterminado del formulario (recargar la página)
            e.preventDefault();
            // Obtiene los valores de los campos del formulario
            const grupo = document.getElementById('grupo-alumno').value;
            const matricula = document.getElementById('matricula-alumno').value;
            const nombre = document.getElementById('nombre-alumno').value;
            // Envía una solicitud POST al servidor con los datos del formulario
            fetch('/alumnos', {
                method: 'POST', // Especifica que el método de la solicitud es POST
                headers: { 'Content-Type': 'application/json' }, // Especifica que el contenido es JSON
                body: JSON.stringify({ grupo, matricula, nombre }) // Convierte los datos del formulario a una cadena JSON y los incluye en el cuerpo de la solicitud
            })
            // Maneja la respuesta del servidor
            .then(response => response.json()) // Convierte la respuesta a JSON
            .then(data => {
                // Muestra una alerta indicando que el alumno ha sido agregado
                alert(data['message']);
                // Resetea el formulario para limpiar los campos
                altaAlumnoForm.reset();
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Hubo un error al obtener los datos');
            });
        });
    }

    // Obtiene el formulario de alta de sistema por su ID
    const altaSistemaForm = document.getElementById('alta-sistema-form');
    // Verifica si el formulario existe en la página
    if (altaSistemaForm) {
        // Agrega un evento de escucha para el evento 'submit' del formulario
        altaSistemaForm.addEventListener('submit', function(e) {
            // Previene el comportamiento predeterminado del formulario (recargar la página)
            e.preventDefault();
            // Obtiene los valores de los campos del formulario
            const p1 = document.getElementById('p1-sistema').value;
            const p2 = document.getElementById('p2-sistema').value;
            const p3 = document.getElementById('p3-sistema').value;
            // Envía una solicitud POST al servidor con los datos del formulario
            fetch('/sistemas', {
                method: 'POST', // Especifica que el método de la solicitud es POST
                headers: { 'Content-Type': 'application/json' }, // Especifica que el contenido es JSON
                body: JSON.stringify({ p1, p2, p3 }) // Convierte los datos del formulario a una cadena JSON y los incluye en el cuerpo de la solicitud
            })
            // Maneja la respuesta del servidor
            .then(response => response.json()) // Convierte la respuesta a JSON
            .then(data => {
                // Muestra una alerta indicando que el sistema ha sido agregado
                alert(data['message']);
                // Resetea el formulario para limpiar los campos
                altaSistemaForm.reset();
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Hubo un error al obtener los datos');
            });
        });
    }

    // Obtiene el formulario para modificar un alumno por su ID
    const modificarAlumnoForm = document.getElementById('modificar-alumno-form');
    // Verifica si el formulario existe en la página
    if (modificarAlumnoForm) {
        // Agrega un evento de escucha para el evento 'submit' del formulario
        modificarAlumnoForm.addEventListener('submit', function(e) {
            // Previene el comportamiento predeterminado del formulario (recargar la página)
            e.preventDefault();
            // Obtiene los valores de los campos del formulario
            const idalumno = document.getElementById('idalumno-modificar').value;
            const nombre = document.getElementById('nombre-alumno-modificar').value;
            const matricula = document.getElementById('matricula-alumno-modificar').value;
            const grupo = document.getElementById('grupo-alumno-modificar').value;
            // Envía una solicitud POST al servidor con los datos del formulario
            fetch(`/alumnosModificacion`, {
                method: 'POST', // Especifica que el método de la solicitud es POST
                headers: { 'Content-Type': 'application/json' }, // Especifica que el contenido es JSON
                body: JSON.stringify({ idalumno, nombre, matricula, grupo }) // Convierte los datos del formulario a una cadena JSON y los incluye en el cuerpo de la solicitud
            })
            // Maneja la respuesta del servidor
            .then(response => response.json()) // Convierte la respuesta a JSON
            .then(data => {
                // Muestra una alerta con el mensaje recibido en la respuesta del servidor
                alert(data.message);
                // Resetea el formulario para limpiar los campos
                modificarAlumnoForm.reset();
            })
            // Maneja cualquier error que ocurra durante la solicitud
            .catch(error => {
                console.error('Error:', error);
                alert('Hubo un error al obtener los datos');
            });
        });
    }

    // Obtiene el formulario para modificar un sistema por su ID
    const modificarSistemaForm = document.getElementById('modificar-sistema-form');
    // Verifica si el formulario existe en la página
    if (modificarSistemaForm) {
        // Agrega un evento de escucha para el evento 'submit' del formulario
        modificarSistemaForm.addEventListener('submit', function(e) {
            // Previene el comportamiento predeterminado del formulario (recargar la página)
            e.preventDefault();
            // Obtiene los valores de los campos del formulario
            const idsistema = document.getElementById('idsistema-modificar').value;
            const p1 = document.getElementById('p1-sistema-modificar').value;
            const p2 = document.getElementById('p2-sistema-modificar').value;
            const p3 = document.getElementById('p3-sistema-modificar').value;
            // Envía una solicitud POST al servidor con los datos del formulario
            fetch(`/sistemasModificacion`, {
                method: 'POST', // Especifica que el método de la solicitud es POST
                headers: { 'Content-Type': 'application/json' }, // Especifica que el contenido es JSON
                body: JSON.stringify({ idsistema, p1, p2, p3 }) // Convierte los datos del formulario a una cadena JSON y los incluye en el cuerpo de la solicitud
            })
            // Maneja la respuesta del servidor
            .then(response => response.json()) // Convierte la respuesta a JSON
            .then(data => {
                // Muestra una alerta con el mensaje recibido en la respuesta del servidor
                alert(data.message);
                // Resetea el formulario para limpiar los campos
                modificarSistemaForm.reset();
            })
            // Maneja cualquier error que ocurra durante la solicitud
            .catch(error => {
                console.error('Error:', error);
                alert('Hubo un error al obtener los datos');
            });
        });
    }

    // Obtiene el formulario con el ID 'alta-lab-form'
    const altaLabForm = document.getElementById('alta-lab-form');
    // Verifica si el formulario existe en el documento
    if (altaLabForm) {
        // Agrega un evento de escucha para el evento 'submit' del formulario
        altaLabForm.addEventListener('submit', function(e) {
            // Previene el comportamiento predeterminado del formulario (recargar la página)
            e.preventDefault();
            // Obtiene los valores de los campos del formulario
            const idalumno = document.getElementById('idalumno-lab').value;
            const idsistema = document.getElementById('idsistema-lab').value;
            const numero_practica = document.getElementById('numero-practica-lab').value;
            // Envía una solicitud POST al servidor con los datos del formulario
            fetch('/labs', {
                method: 'POST', // Método HTTP a usar para la solicitud
                headers: { 'Content-Type': 'application/json' }, // Especifica que el contenido es JSON
                body: JSON.stringify({ idalumno, idsistema, numero_practica }) // Convierte los datos a una cadena JSON
            })
            .then(response => response.json()) // Convierte la respuesta del servidor a JSON
            .then(data => {
                // Muestra un mensaje de alerta con la respuesta del servidor
                alert(data.message);
                altaLabForm.reset();
            })
            .catch(error => {
                alert(`Hubo un error al realizar la consulta: ${error}`);
            });
        });
    }

    // Obtiene el formulario para listar una práctica por su ID
    const listarForm = document.getElementById('listar-form');
    // Verifica si el formulario existe en la página
    if (listarForm) {
        // Agrega un evento de escucha para el evento 'submit' del formulario
        listarForm.addEventListener('submit', function(e) {
            // Previene el comportamiento predeterminado del formulario (recargar la página)
            e.preventDefault();
            // Obtiene el valor del campo de entrada del formulario por su ID
            const numero_practica = document.getElementById('numero-practica-listar').value;
            // Envía una solicitud GET al servidor con el número de práctica
            fetch(`/labsListar?numero_practica=${numero_practica}`, {
                method: 'GET', // Método HTTP a usar para la solicitud
            })
            // Maneja la respuesta del servidor
            .then(response => response.json()) // Convierte la respuesta a JSON
            .then(data => {
                // Verifica si la lista de alumnos no está vacía
                if (data.alumnos.length != 0) {
                    // Obtiene el elemento de resultado por su ID
                    const result = document.getElementById('result');
                    // Inicializa una variable HTML para construir la lista de alumnos
                    let html = '<h2>Alumnos</h2><ul>';
                    // Itera sobre cada alumno en los datos recibidos
                    data.alumnos.forEach(alumno => {
                        // Agrega cada alumno a la lista HTML junto con la información del sistema
                        html += `<li>Matrícula: ${alumno.matricula}, Nombre: ${alumno.nombre}, P1: ${alumno.p1}, P2: ${alumno.p2}, P3: ${alumno.p3}</li>`;
                    });
                    // Cierra la lista HTML
                    html += '</ul>';
                    // Inserta la lista HTML en el elemento de resultado
                    result.innerHTML = html;
                    // Muestra un mensaje de alerta con el mensaje recibido del servidor
                    alert(data.message);
                } else {
                    // Si no hay alumnos, limpia el contenido del elemento de resultado
                    let html = '';
                    result.innerHTML = html;
                    // Muestra un mensaje de alerta con el mensaje recibido del servidor
                    alert(data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Hubo un error a la hora de realizar la consulta');
            });
        });
    }
});
