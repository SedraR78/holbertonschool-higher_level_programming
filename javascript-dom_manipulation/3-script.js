document.querySelector("toggle_header").onclick = function() {
    const header = document.querySelector("header");
    if (header.classList.contains("red")) {
        header.classList.replace("red", "geen");
    } else {
        header.classList.replace("green", "red");
    }
};