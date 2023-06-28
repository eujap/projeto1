function add_carro(){

    container = document.getElementById("form-carro")

    html = "<br><div class='row'> <div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro'></div> <div class='col-md'> <input type='text' placeholder='Placa' class='form-control' name='Placa'></div> <div class='col-md'> <input type='numero' placeholder='ano' class='form-control' name='ano' ></div></div>"

    container.innerHTML += html


}