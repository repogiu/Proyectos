<?php 
namespace App\Models;

use CodeIgniter\Model;

class Libro extends Model{
    protected $table='libros';
    // Uncomment below if you want add primary key
    protected $primaryKey='id';
     // activamos el acceso a las columnas
    protected $allowedFields=['nombre','imagen'];
}