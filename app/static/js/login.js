
const togglePassword = document.getElementById("togglePassword");
const password = document.getElementById("password");

togglePassword.addEventListener("click", function () {

    const isPassword = password.type === "password";

    password.type = isPassword ? "text" : "password";

    const icon = this.querySelector("i");

    icon.classList.toggle("fa-eye");
    icon.classList.toggle("fa-eye-slash");

});
