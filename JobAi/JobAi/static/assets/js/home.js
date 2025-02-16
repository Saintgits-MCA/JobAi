document.addEventListener("DOMContentLoaded", function () {
  let savedTab = localStorage.getItem("activeTab");
  if (savedTab) {
      document.querySelector(`.box[href='${savedTab}']`)?.classList.add("active");
  }

  document.querySelectorAll(".box").forEach(link => {
    link.addEventListener("click", function () {
      document.querySelectorAll(".box").forEach(el => el.classList.remove("active"));
      this.classList.add("active");
      localStorage.setItem("activeTab", this.getAttribute("href"));
    });
  });
});

