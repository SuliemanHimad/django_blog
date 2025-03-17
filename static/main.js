const currentYear = new Date().getFullYear();
document.querySelector(".current").textContent = currentYear;

setTimeout(function () {
  document.querySelector(".messages").style.display = "none";
}, 1000);
