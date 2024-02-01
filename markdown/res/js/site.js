function tldr() {
  var x = document.querySelectorAll('.blockquote.blockquote.p');
  var b = document.getElementById("tldr-btn");

  Array.prototype.forEach.call(x, function(el) {
    // Do stuff here
    if (el.style.display === "none") {
      el.style.display = "block";
      b.textContent="tl;dr";
    } else {
      el.style.display = "none";
      b.textContent="tell me more";
    }
})};
