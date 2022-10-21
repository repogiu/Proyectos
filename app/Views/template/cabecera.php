<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Title</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
</head>
<body>
    <!-- b-navbar MENU: quitamos fixed-top para que el menu no sea flotante para que no desaparezca el boton crear-->
    <nav class="navbar navbar-expand-lg navbar-light bg-light ">
        <a class="navbar-brand">MENU</a>
        <button class="navbar-toggler" data-target="#my-nav" data-toggle="collapse" aria-controls="my-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div id="my-nav" class="collapse navbar-collapse">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="<?=base_url('listar')?>">Biblioteca <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="<?=base_url('crear')?>" tabindex="-1" aria-disabled="true">Añadir</a>
                </li>
            </ul>
        </div>
    </nav>
    
    <?php 
    // Para traer visualizar la informacion desde la base de datos hacemos un print_r le pasamos como argumento la variable libro de $datos['libros'] del controlador, ponerlo con $
    //print_r($libros)
    ?>
    <!-- b-container -->
    <div class="container">