CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    autor VARCHAR(255) NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    fecha_publicacion DATE NOT NULL,
    imagen_portada LONGBLOB NOT NULL
);