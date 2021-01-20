const btn = document.getElementById("btn");
const nav = document.getElementById("nav");
const tali = "TALI ROZENMAN ISMAEL";


btn.addEventListener("click", () => {
    nav.classList.toggle("active");
    btn.classList.toggle("active");
});


let index = 0;

function writeText() {
    document.body.innerText = text.slice(0, index);

    index++;

    if (index > text.length) {
        index = 0;
    }
}

setInterval(writeText, 220);


