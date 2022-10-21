<?= $cabecera; ?>
Formulario de crear
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
            <!-- b-form-enctype Formulario para enviar archivo con metodo post -->
        <form method="post" action="<?=site_url('/guardar')?>" enctype="multipart/form-data">
            <!-- b-form-group para crear campo de nombre de libro -->
            <div class="form-group">
                <label for="nombre">Nombre: </label>
                <!-- old(): imprime el valor perdidos o antiguos si no lo cumple -->
                <input id="nombre" value="<?=old('nombre')?>" class="form-control" type="text" name="nombre"> 
            </div>
            <!-- b-form-file para crear capturar imagen de libro -->
            <div class="form-group">
                <label for="imagen">Archivo: </label>
                <input id="imagen" class="form-control-file" type="file" name="imagen">

            </div>
            <br />
            <!-- b-btn -->
            <button class="btn btn-success" type="submit">Guardar</button>
            <!-- a:link para que regrese a listar-->
            <a href="<?=base_url('listar');?>" class="btn btn-primary">Cancelar</a>
            <br />

        </form>

        </p>
    </div>
</div>

<?= $pie; ?>