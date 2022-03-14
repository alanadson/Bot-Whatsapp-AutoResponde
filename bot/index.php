<?php
 
$servidor = "localhost";
$usuario = "root";
$senha = "";
$banco = "bot";
$conn = mysqli_connect($servidor,$usuario,$senha,$banco);
 
if(!$conn){
    echo "Error connect<br/";
} else {
    echo "Server to connect<br/>";
}

?>

<?php
$msg = $_GET['msg'];

$menu = "Hi";

if($msg){
    echo $menu;
    if($msg == 'Hi'){
        echo "Testando";
    }
}

?>
