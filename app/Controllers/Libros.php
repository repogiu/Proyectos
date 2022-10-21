<?php

namespace App\Controllers;

use CodeIgniter\Controller;
use App\Models\Libro;

class Libros extends Controller
{
    // definimos el metodo index que direcciona a la pagina listar.php
    public function index()
    {

        $libro = new Libro(); // nombre del modelo
        // ordenamos la informacion por id del libro y de manera ascendente 
        // findAll para que busque todos los registros libros
        $datos['libros'] = $libro->orderBy('id', 'ASC')->findAll();

        // incluimos cabecera y pie de pagina en listar.php
        $datos['cabecera'] = view('template/cabecera');
        $datos['pie'] = view('template/pie');

        //return view('libros/listar');
        return view('libros/listar', $datos);
    }
    // definimos el metodo crear
    public function crear()
    {
        $libro = new Libro();

        // incluimos cabecera y pie de pagina en crear.php
        $datos['cabecera'] = view('template/cabecera');
        $datos['pie'] = view('template/pie');
        return view('libros/crear', $datos);
    }

    // definimos el metodo guardar para recepcionar los datos ingresados en crear.php
    // request nos permite capturar variables enviadas desde formularios con los métodos GET o POST
    // getVar para que agarre el valor que tenga el campo nombre
    public function guardar()
    {
        //$nombre=$this->request->getVar('nombre');
        // Primero referenciamos al modelo Libro para capturar toda la informacion y ingresarla a la bd
        $libro = new Libro();

        // validamos el campo nombre y imagen
        $validacion = $this->validate([
            'nombre' => 'required|min_length[3]', // campo requerido con una long minima de 3
            'imagen' => [
                'uploaded[imagen]', // validamos que tenga una imagen
                'mime_in[imagen,image/jpg,image/jpeg,image/png,image/png]',
                'max_size[imagen,1024]' // tamaño maximo 
            ]

        ]);
        if (!$validacion) {
            $session = session();
            $session->setFlashdata('mensaje', 'Revise la informacion'); // envia el mensaje en un determinado lugar (mensaje es la variable y el valor de ese mensaje)
            // Retornamos hacia atras (back) enviando valores (withInput) que son recepcionados en crear.php
            return redirect()->back()->withInput();

            //return $this->response->redirect(site_url('/listar'));
        }



        // validamos si hay imagen
        if ($imagen = $this->request->getFile('imagen')) {
            //guardamos la imagen con un nombre diferente para que no choque con otras imagenes que tengan el mismo nombre
            $nuevoNombre = $imagen->getRandomName();
            // se guarda la imagen en la carpeta imagenes que se crea auto...
            $imagen->move('../public/uploads/', $nuevoNombre);
            // lo insertamos en la bd en forma de arreglo
            $datos = [
                // para la columna 'nombre' vamos a utilizar $nombre
                'nombre' => $this->request->getVar('nombre'),
                'imagen' => $nuevoNombre
            ];
            // insertamos a la bd con la fx insert
            $libro->insert($datos);
            // verificamos si llega la informacion con print_r
            //print_r($nombre);


        }
        echo "Ingresado a la base de datos";
        return $this->response->redirect(site_url('/listar'));
    } //cierra funcion guardar

    public function borrar($id = null)
    {
        $libro = new Libro();
        // busca informacion en un id que coincida con el id que esta solicitando y que muestre el primer elemento
        $datosLibro = $libro->where('id', $id)->first();
        // busca la ruta
        $ruta = ('../public/uploads/' . $datosLibro['imagen']);
        //se borra el archivo de uploads
        unlink($ruta);
        // borrado del libro
        $libro->where('id', $id)->delete($id);
        // se borra el archivo de la bd respetando el id que se envio y luego redireccionamos a la ruta listar
        return $this->response->redirect(site_url('/listar'));
        //echo "Borrar registro"." ".$id;

    } // cierra funcion borrar

    public function editar($id = null)
    {
        print_r($id);
        $libro = new Libro(); // creamos un nuevo modelo
        // consultamos todos los libros que coincida con el id 
        $datos['libro'] = $libro->where('id', $id)->first();
        // incluimos cabecera y pie de pagina en editar.php de
        $datos['cabecera'] = view('template/cabecera');
        $datos['pie'] = view('template/pie');

        return view('libros/editar', $datos);
    } // cierra funcion editar

    public function actualizar()
    {
        $libro = new Libro(); // incluimos el modelo
        // lo insertamos en la bd en forma de arreglo
        $datos = [
            // actualizamos nombre
            "nombre" => $this->request->getVar("nombre")
        ];
        // recuperamos el id oculto de la interfaz editar para recepcionar el nombre
        $id = $this->request->getVar("id");
        // validamos antes del update el campo nombre y imagen
        $validacion = $this->validate([
            'nombre' => 'required|min_length[3]', // campo requerido con una long minima de 3
        ]);

        if (!$validacion) {
            $session = session();
            $session->setFlashdata('mensaje', 'Revise la informacion'); // envia el mensaje en un determinado lugar, mensaje es la variables y el valor de ese mensaje
            // Retornamos hacia atras (back) enviando valores (withInput) que son recepcionados en crear.php
            return redirect()->back()->withInput();
        }

        // actualizamos el libro utilizando el id del libro y los datos 
        $libro->update($id, $datos);
        // validamos el campo imagen
        $validacion = $this->validate([
            'imagen' => [
                'uploaded[imagen]', // validamos que tenga una imagen
                'mime_in[imagen,image/jpg,image/jpeg,image/png,image/png]',
                'max_size[imagen,1024]' // tamaño maximo 
            ]

        ]);

        if ($validacion) {
            if ($imagen = $this->request->getFile('imagen')) {
                // para actualizar tenemos que borrar la imagen anterior.
                $datosLibro = $libro->where('id', $id)->first();
                $ruta = ('../public/uploads/' . $datosLibro['imagen']);
                //se borra el archivo de uploads
                unlink($ruta);
                // utilizamos el mismo fragmento de codigo de la fx guardar   
                // si encuentra la imagen le cambiamos el nombre y lo copiamos a la ruta
                $nuevoNombre = $imagen->getRandomName();
                $imagen->move('../public/uploads/', $nuevoNombre);
                // luego escribimos ese nombre en la bd por medio del update
                $datos = ['imagen' => $nuevoNombre];
                // actualizamos a la bd con la fx update
                $libro->update($id, $datos);
            }
        } // cierra if validacion
        return $this->response->redirect(site_url('/listar'));
    }  // cierra funcion actualizar


} // cierra class libro
