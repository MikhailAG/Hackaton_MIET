window.addEventListener('DOMContentLoaded', () => {

    document.querySelector(".jsFilter").addEventListener("click", function () {
      document.querySelector(".filter-menu").classList.toggle("active");
    });
    document.querySelector(".mode-switch").addEventListener("click", function () {
      document.documentElement.classList.toggle("dark");
      document.documentElement.classList.toggle("light");
      document.querySelector(".mode-switch").classList.toggle("active");
    });

});