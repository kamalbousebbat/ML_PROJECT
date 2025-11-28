// Smooth neon glow on inputs
document.querySelectorAll(".form-control, .form-select").forEach(input => {
    input.addEventListener("focus", () => {
        input.classList.add("focus-glow");
    });
    input.addEventListener("blur", () => {
        input.classList.remove("focus-glow");
    });
});