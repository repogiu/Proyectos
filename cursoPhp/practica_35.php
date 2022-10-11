<?php 
// consumir una api y convertirla en una lista HTML

$url="https://api.dailymotion.com/videos?channel=sport&limit=10";
 // desactivamos la seguridad de https para leer la informacion com 2 opciones
$opciones= array("ssl"=>array("verify_peer"=>false,"verify_peer_name"=>false));
// leemos la informacion utilizando las opciones de desactivado de la lectura 
$desactivar=file_get_contents($url,false,stream_context_create($opciones));

$conversion=json_decode($desactivar);

//print_r($conversion);

foreach($conversion->list as $lista){
//print_r($lista);
//print_r($lista->title);
//print_r($lista->channel);

}

?>

<ul>
    <?php foreach($conversion->list as $lista){ ?>

    <li> <?php echo ($lista->title); ?> | <?php echo ($lista->channel);?></li>

    <?php } ?>
</ul>