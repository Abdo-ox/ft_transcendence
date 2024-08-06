/****** register form ** */
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirm_password");

confirmPassword.addEventListener("input", () => {
  if (password.value !== confirmPassword.value) {
    confirmPassword.setCustomValidity("Passwords does not  match.");
  } else {
    confirmPassword.setCustomValidity("");
  }
})