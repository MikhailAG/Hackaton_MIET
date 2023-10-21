window.addEventListener('DOMContentLoaded', () => {

    document.querySelector(".btn.choice-soft-skills").addEventListener("click", function () {
      document.querySelector(".btn.choice-soft-skills").classList.toggle("active");
    });
    document.querySelector(".btn.choice-hard-skills").addEventListener("click", function () {
      document.querySelector(".btn.choice-hard-skills").classList.toggle("active");
    });

    document.querySelector(".jsFilter").addEventListener("click", function () {
      document.querySelector(".filter-menu").classList.toggle("active");
    });
    document.querySelector(".mode-switch").addEventListener("click", function () {
      document.documentElement.classList.toggle("dark");
      document.documentElement.classList.toggle("light");
      document.querySelector(".mode-switch").classList.toggle("active");
    });
});