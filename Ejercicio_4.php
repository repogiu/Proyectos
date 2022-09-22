<!--Hacer un programa que muestre un mensaje. Ilustre como incrustar codigo PHP en un doc HTML y como imprimir desde php -->

<!--
 en CSS se definen estilos para cualquier elemento de html (div, tablas, botones, parrafos) por medio de una clase o se
 asignan directamente al elemento por tipo de elemento, por id

ejemplos:
una asginacion de estilo por medio de la clase seria asi: (un punto al principio)
        .texto_grande {
            font-family: 'Lato', sans-serif;
            font-size: 18px;
        }

y se debe asignar a un elemento ej. <div class="texto_grande">

**********************
una asignacion de estilo por medio del elemento html natural
        div {
            font-family: 'Lato', sans-serif;
            font-size: 18px;
        }

        entonces todos los divs tendran el texto 18px y la letra Lato

**********************
una asignacion por medio de numeral #, le asignaria el estilo al elemento que tenga este nombre como id
        #btnPrincipal  {
            font-family: 'Lato', sans-serif;
            font-size: 18px;
        }


        en javascript, bootstrap, jquery, y otras librerias, utilizamos estos selectores como un estandar..

        el punto (.) es para referirnos a una clase
        el numeral es para referirnos a un id


-->


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Incrustar php en html</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    <style>
        .texto_grande {
            font-family: 'Lato', sans-serif;
            font-size: 18px;
        }

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





        <div class="mb-3">
            <label for="txtNombre" class="form-label">Nombre: </label>
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



        <?php
        $tablaInicial = 1;
        $tablaFinal = 9;
        for ($tabla = $tablaInicial; $tabla <= $tablaFinal; $tabla++) {
        ?>

            <div class="card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title"> <?php echo "Tabla del " . $tabla . "<br>" . "<br>";    ?> </h5>
                    <p class="card-text">

                        <?php
                        //programa que calcula una tabla de multiplicar. Ilustra como manejar variables y como usar bucles
                        for ($i = 1; $i <= 10; $i++) {
                            $resultado = $i * $tabla;
                            echo $tabla . " * " . $i . " = " . $resultado . "<br>";
                        }
                        ?>

                    </p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                    <a href="http://www.google.com" class="btn btn-success">ir a google</a>
                </div>
            </div>

        <?php
            echo "<br>";
        }

        ?>



    </div>




    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>


    <script>
        function muestraAlerta() {
            // definimos la variable en vacio
            var nombreTecleado = 0;

            // tambien podemos obtener elementos una vez, y usarlos varias veces
            // osea guardamos el eklemento completo en una variable
            var inputNombre = document.getElementById("txtNombre");

            // leemos lo que teclearon en txtNombre
            nombreTecleado = Number.parseInt(inputNombre.value) + 15;

            alert("Buena Clase " + nombreTecleado)
        }
    </script>


</body>

</html>