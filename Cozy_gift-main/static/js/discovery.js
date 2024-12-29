document.querySelector(".read-more").addEventListener("click", function () {
    const texts = document.querySelectorAll(".text-hidden-my"); // All hidden paragraphs
    const firstText = document.querySelector(".content-paragraph-my.visible"); // First visible paragraph
    const isAllVisible = Array.from(texts).every(text => text.classList.contains("visible")); // Check visibility
  
    if (isAllVisible) {
      // Hide all paragraphs except the first
      texts.forEach(text => text.classList.remove("visible"));
      firstText.classList.add("visible"); // Ensure first paragraph stays visible
      this.textContent = "READ MORE ↓";
    } else {
      // Show all paragraphs
      texts.forEach(text => text.classList.add("visible"));
      this.textContent = "READ LESS ↑";
    }
  });
  