// copy button
const copyButtons = document.querySelectorAll(".copy-btn");
copyButtons.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    const text = e.target.dataset.clipboardText;
    navigator.clipboard.writeText(text).then(() => {
      e.target.textContent = "Copied!";
      setTimeout(() => {
        e.target.textContent = "Copy";
      }, 2000);
    });
  });
});
