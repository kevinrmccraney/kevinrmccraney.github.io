function tldr() {
  var x = document.querySelectorAll('details');
  var b = document.getElementById("tldr-btn");

  // Toggle the button text based on the current state
  if (b.textContent === "tell me more") {
    b.textContent = "tl;dr";
    Array.prototype.forEach.call(x, function (el) {
      // Toggle the 'open' attribute on <details> tags
      el.setAttribute("open", "");
    });
  } else {
    b.textContent = "tell me more";
    Array.prototype.forEach.call(x, function (el) {
      // Toggle the 'open' attribute on <details> tags
      el.removeAttribute("open");
    });
  }
  
}