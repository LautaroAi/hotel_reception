fetch("/huespedes")
    .then(res => res.json())
    .then(data => {
    const cont = document.getElementById("huespedes");
    data.forEach(h => {
        const p = document.createElement("p");
        p.textContent = `Nombre: ${h.nombre}, Documento: ${h.documento}`;
        cont.appendChild(p);
    });
});
