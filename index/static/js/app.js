const btn = document.getElementById("apply");
const modal = document.getElementById("modal");

btn.onclick = function(){
  modal.style.display = "block";
}

window.onclick = function(event){
  if(event.target == modal){
    modal.style.display = "none";
  }
}
