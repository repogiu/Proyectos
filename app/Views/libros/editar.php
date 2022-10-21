<?= $cabecera; ?>
Formulario de editar
<!-- para saber si me esta llegando la informacion  -->
<?php // print_r($libro);?>

<!-- si hay valores en session, mostrar mensaje -->
<?php if(session('mensaje')){?>

<!-- b-alert Mensaje de alerta en caso de fallar la validacion-->
<div class="alert alert-danger" role="alert">
    <?php echo session('mensaje');?> 

</div>

<?php } ?>


<!-- b-card -->
<div class="card">
    <div class="card-body">
        <h5 class="card-title">Ingresar datos del Libro</h5>
        <p class="card-text">
            <!-- b-form-enctype    formulario para enviar archivo con metodo post -->
        <form method="post" action="<?= site_url('/actualizar') ?>" enctype="multipart/form-data">
        <!-- input:hidden para ocultar el id del libro -->    
        <input type="hidden" name="id" value="<?=$libro['id']?>">
            <!-- b-form-group para crear campo de nombre de libro -->
            <div class="form-group">
                <label for="nombre">Nombre: </label>
                <!-- agregamos el valor para que nos muestre el nombre del libro -->
                <input id="nombre" value="<?=$libro['nombre']?>" class="form-control" type="text" name="nombre">
            </div>
            <!-- b-form-file para crear capturar imagen de libro -->
            <div class="form-group">
                <label for="imagen">Archivo: </label>
                <br/>
                <!-- b-img-thumbnail para que me muestre la imagen -->
                <img class="img-thumbnail" src="<?=base_url()?>/uploads/<?=$libro['imagen'];?>" width="100" alt="">
                <br/>
                <br/>
                <input id="imagen" class="form-control-file" type="file" name="imagen">

            </div>
            <br />
            <!-- b-btn -->
            <button class="btn btn-success" type="submit">Actualizar</button>
            <!-- a:link para que regrese a listar-->
            <a href="<?=base_url('listar');?>" class="btn btn-primary">Cancelar</a>
            <br />

        </form>

        </p>
    </div>
</div>

<?= $pie; ?>