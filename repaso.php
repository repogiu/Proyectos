<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">

    <style>
        
        #btnPrincipal {
            font-size: 25px;

        }
    </style>

</head>
<body>

<div class="container border border-danger p-3 m-3">
        <!--p es padding osea espacio. m es un margen -->

        <!-- Button trigger modal -->
        <button id="btnPrincipal" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalVentanaAviso">
            abrir ventana de aviso
        </button>         


        <!-- Button Javascript -->    
        <div class="mb-3">
            <label for="txtNombre" class="form-label p-3">Nombre: </label>
            <input type="text" class="form-control" id="txtNombre" placeholder="captura tu nombre">
        </div>


        <button id="" type="button" onclick="muestraAlerta()" onmouseover="" class="btn btn-danger">muestra una alerta de javascript</button>

        <hr>

          <!-- Modal -->
          <div class="modal fade" id="modalVentanaAviso" tabindex="-1" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Ventana de Aviso</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        Hola, ya casi es fin de semana.
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary">Save changes</button>
                    </div>
                </div>
            </div>
        </div>










<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>

<script>
        function muestraAlerta() {
            // definimos la variable en vacio
            var nombreTecleado = "";
            var nombreTecleado = document.getElementById("txtNombre").value;
            //nombreTecleado.innerHTML = "Usted" ;
            //nombreTecleado.style.color = "green" ;
            //nombreTecleado.style.fontSize = "20px" ;
            
            alert("El nombre que ingresaste es: " + nombreTecleado)
        }
    </script>

</body>
</html>