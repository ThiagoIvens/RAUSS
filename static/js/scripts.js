// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");

function imgzoom(name, image){
  modal.style.display = "block";
  modalImg.src = image;
  captionText.innerHTML = name;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

$(document).ready(function() {
  $('#carouselPortifolioIndicators').carousel({
    interval: 3000
  })
});

$(document).ready(function() {
  $('#carouselProjetosIndicators').carousel({
    interval: 3000
  })
});