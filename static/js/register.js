document.getElementById("id_adress").style.display = "none";

box = document.getElementById("id_is_market")
box.addEventListener('change', (event) => {
    if (event.currentTarget.checked) {
        document.getElementById("id_adress").style.display = "block";
        document.getElementById("id_adress").required = true;
    } else {
        document.getElementById("id_adress").style.display = "none";
    }
  })