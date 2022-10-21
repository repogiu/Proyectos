        <?=$cabecera?>
        <!-- a:link  creamos un enlace que se diriga a la vista crear-->
        <a class="btn btn-success" href="<?=base_url('crear')?>">Crear un libro</a>
        <br/>
        <br/>
        <!-- b-table-header -->
        <table class="table table-light">
            <thead class="thead-light">
                <tr>
                     <!-- nombres de la columnas -->
                    <th>#</th>
                    <th>Imagen</th>
                    <th>Nombre</th>
                    <th>Acciones </th>
                </tr>
            </thead>
            <tbody>
                <!-- mostrar libro por separado -->
                <?php foreach($libros as $libro):?>
                <tr>
                    <!--tnm se puede poner asi: echo $libro['id'];-->
                    <td><?= $libro['id'];?></td>
                    <td>
                        <!-- b-img-thumbnail para mostrar la imagen  -->
                        <img class="img-thumbnail" src="<?=base_url()?>/uploads/<?=$libro['imagen'];?>" width="100" alt="">
                        <?= $libro['imagen'];?>
                    </td>
                    <td><?= $libro['nombre'];?></td>
                    <td>
                    <!-- boton editar -->
                    <a href= "<?=base_url('editar/'.$libro['id']);?>" class="btn btn-info" type="button">Editar</a>
                    <!-- boton borrar: href me va a llevar a una ubicacion de borrado concatenado con el id del libro -->
                    <a href= "<?=base_url('borrar/'.$libro['id']);?>" class="btn btn-danger" type="button">Borrar</a>
                </td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
        <?=$pie?>
