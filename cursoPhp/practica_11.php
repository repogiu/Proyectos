<!-- Operadores artimeticos -->
<?php 
if($_POST){
    $valorA=$_POST['valorA'];
    $valorB=$_POST['valorB'];
    
    
    $suma= $valorA+$valorB;
    $resta= $valorA-$valorB;
    $multiplicacion= $valorA*$valorB;
    $division= $valorA/$valorB;
    
    echo "<br/>"."El resultado de la suma es: ".$suma;
    echo "<br/>"."El resultado de la resta es: ".$resta;
    echo "<br/>"."El resultado de la multiplicacion es: ".$multiplicacion;
    echo "<br/>"."El resultado de la division es: ".$division;

    if($valorA==$valorB) {
        echo "<br/>"."El valor de A es igual al valor de B es <br/>";

        if($valorA==4) {
            echo "El valor es 4";
        }
        if($valorA==5) {  
            echo "El valor es 5";
        }
        }



}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="practica_11.php" method="post">
        <br/>
        Valor A:
        <input type="text" name="valorA" id="">
        <br/>
        <br/>
        Valor B:
        <input type="text" name="valorB" id="">
        <br/>
        <br/>
        <input type="submit" value="Calcular">

    </form>

</body>

</html>