// =============================================
// script.js — Interactions & Animations
// OpenCode will help you add scroll effects,
// hover interactions, and microanimations here.
// =============================================

// Your JavaScript goes below this line

// =============================================
// FAQ accordion — open one answer at a time
// =============================================

const faqButtons = document.querySelectorAll(".faq__question");

faqButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const panel = document.getElementById(
      button.getAttribute("aria-controls")
    );
    const wasOpen = button.getAttribute("aria-expanded") === "true";

    // Close every answer first (exclusive accordion).
    faqButtons.forEach((btn) => {
      const otherPanel = document.getElementById(
        btn.getAttribute("aria-controls")
      );
      otherPanel.classList.remove("faq__panel--open");
      otherPanel.hidden = true;
      btn.setAttribute("aria-expanded", "false");
    });

    // Open the clicked answer, unless it was already open.
    if (!wasOpen) {
      panel.hidden = false;        // show the panel in its closed state
      void panel.offsetHeight;     // let the browser see "closed" first
      panel.classList.add("faq__panel--open");  // then animate open
      button.setAttribute("aria-expanded", "true");
    }
  });
});
