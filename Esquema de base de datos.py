create DATABASE universidad;
use universidad;
drop TABLE asignaturas;
alter table estudiantes add edad int;
alter table estudiantes drop edad;
/* aqui renombramos la tabla */
alter table estudiantes RENAME estudiantes1;
/* la dejamos como estaba */
alter table estudiantes1 RENAME estudiantes;
/*cambia el nombre de el campo */
alter TABLE estudiantes rename COLUMN nombre to nombre1;
select * from asignaturas;
SELECT * from asignaturas where numero=1;
SELECT* from estudiantes where programa="ENFERMERIA";

create table asignaturas (
numero int(10) not NULL PRIMARY key,
matricula_estudiante VARCHAR (12) not null,
calificacion INT (2) not NULL,
programa VARCHAR (30),
requisitos VARCHAR(30) not null,
creditos INT (3) not null,
titulo VARCHAR (30)
);
create table profesores(
id_profesor INT (10) not null PRIMARY key,
nombre VARCHAR (30) not null,
departamento VARCHAR (30) not null,
titulo VARCHAR (30) not null
);
create table oferta(
numero_asignatura INT (10) not null PRIMARY key,
año INT (4) not null,
numero_seccion INT (4) not NULL,
horario DATETIME not null,
aulas INT (4) not null,
semestre INT (2) not null,
profesor VARCHAR (50) not null
);
create TABLE estudiantes (
id_estudiantes INT (12) not null PRIMARY key,
nombre VARCHAR (30) not null,
programa VARCHAR (30) not null
);
INSERT INTO asignaturas 
values
("1",000000000001,6,"Educacion fisica","materias anteriores",3,"matematicas"),
("2",000000000002,6,"Educacion fisica","materias anteriores",3,"Español"),
("3",000000000003,7,"Educacion fisica","materias anteriores",3,"Ciencias"),
("4",000000000004,8,"Educacion fisica","materias anteriores",3,"ciencias naturales"),
("5",000000000005,9,"Educacion fisica","materias anteriores",3,"civica"),
("6",000000000006,6,"Educacion fisica","materias anteriores",3,"historia"),
("7",000000000007,7,"Educacion fisica","materias anteriores",3,"biologia"),
("8",000000000008,8,"Educacion fisica","materias anteriores",3,"anatomia"),
("9",000000000009,9,"Educacion fisica","materias anteriores",3,"letras"),
("10",000000000010,10,"Educacion fisica","materias anteriores",3,"estadistica"),
("11",000000000011,7,"Educacion fisica","materias anteriores",3,"algoritmos"),
("12",000000000012,6,"Educacion fisica","materias anteriores",3,"psicologia"),
("13",000000000013,8,"Educacion fisica","materias anteriores",3,"matematicas2"),
("14",000000000014,9,"Educacion fisica","materias anteriores",3,"algoritmos2"),
("15",000000000015,7,"Educacion fisica","materias anteriores",3,"base de datos"),
("16",000000000016,8,"Educacion fisica","materias anteriores",3,"arquitectura de computadoras"),
("17",000000000017,9,"Educacion fisica","materias anteriores",3,"base de datos 2"),
("18",000000000018,10,"Educacion fisica","materias anteriores",3,"ingenieria de software"),
("19",000000000019,7,"Educacion fisica","materias anteriores",3,"administracion"),
("20",000000000020,7,"Educacion fisica","materias anteriores",3,"empresas");

INSERT INTO profesores 
values
(1,"carlos aguilar dominguez","Administrativo","Doctorado"),
(2,"maria olga villa","Administrativo","Doctorado"),
(3,"modesta soriano ","Administrativo","Doctorado"),
(4,"enriqueta guirado ","Administrativo","Doctorado"),
(5,"ana captevila Perez","Administrativo","Doctorado"),
(6,"belen villa Perez","Administrativo","Doctorado"),
(7,"efren aguilar ramirez","Administrativo","Doctorado"),
(8,"pedro ramirez santos","Administrativo","Doctorado"),
(9,"rosa sanchez arcos","Administrativo","Doctorado"),
(10,"jaquelite duran felicidad","Administrativo","Doctorado"),
(11,"adriana falfan americo","Administrativo","Doctorado"),
(12,"julio galvan yunes","Administrativo","Doctorado"),
(13,"rocio yunes obrador","Administrativo","Doctorado"),
(14,"jorge captevila galves","Administrativo","Doctorado"),
(15,"andrea soriano perez","Administrativo","Doctorado"),
(16,"shelton guirado ramirez","Administrativo","Doctorado"),
(17,"miguel martinez sanchez","Administrativo","Doctorado"),
(18,"daniel martinez delgadillo","Administrativo","Doctorado"),
(19,"lizeth martinez sangabriel","Administrativo","Doctorado"),
(20,"karla martinez Perez","Administrativo","Doctorado");

insert INTO oferta 
values (1,2024,1,"2024-05-31 8:00:00",1,6,"karla martinez Perez"),
(2,2024,1,"2024-05-31 8:00:00",1,6,"lizeth martinez sangabriel"),
(3,2024,1,"2024-05-31 8:00:00",1,6,"daniel martinez delgadillo"),
(4,2024,1,"2024-05-31 8:00:00",1,6,"miguel martinez sanchez"),
(5,2024,1,"2024-05-31 8:00:00",1,6,"shelton guirado ramirez"),
(6,2024,1,"2024-05-31 8:00:00",1,6,"andrea soriano perez"),
(7,2024,1,"2024-05-31 8:00:00",1,6,"jorge captevila galves"),
(8,2024,1,"2024-05-31 8:00:00",1,6,"rocio yunes obrador"),
(9,2024,1,"2024-05-31 8:00:00",1,6,"julio galvan yunes"),
(10,2024,1,"2024-05-31 8:00:00",1,6,"adriana falfan americo"),
(11,2024,1,"2024-05-31 8:00:00",1,6,"jaquelite duran felicidad"),
(12,2024,1,"2024-05-31 8:00:00",1,6,"rosa sanchez arcos"),
(13,2024,1,"2024-05-31 8:00:00",1,6,"pedro ramirez santos"),
(14,2024,1,"2024-05-31 8:00:00",1,6,"efren aguilar ramirez"),
(15,2024,1,"2024-05-31 8:00:00",1,6,"belen villa Perez");

insert into estudiantes values
(1,"ANA LIZBETH RODRIGUEZ CEJA","PSICOLOGIA"),
(2,"JOAN EMANUEL LANDA RODRIGUEZ","DERECHO"),
(3,"ANA MARIA CEJA HURTADO","ENFERMERIA"),
(4,"ABEL RODRIGUEZ SALAZAR","AGRONOMIA"),
(5,"EDNA RODRIGUEZ SALAZAR","CONTABILIDAD"),
(6,"MARIANA ABURTO ROBLES","DERECHO"),
(7,"CLARA MENDEZ MAVIL","CONTABILIDAD"),
(8,"CARLOS PEREZ GARCIA","DERECHO"),
(9,"ANAHI ROSSEL VIVEROS","PSICOLOGIA"),
(10,"JOSE SANCHEZ MARTINEZ","DERECHO"),
(11,"GUSTAVO LEAL PEREZ","SISTEMAS"),
(12,"RAFAEL LANDA SOTO","INFORMATICA"),
(13,"DANIEL DURAN SANCHEZ","ADMINISTRACION"),
(14,"DIANA LAURA SOTO BAEZ","DERECHO"),
(15,"RAMON LANDA HERNANDEZ","INFORMATICA"),
(16,"MARIA LARA DURAN","LEYES"),
(17,"CLARA RODRIGUEZ LANDA","MEDICINA"),
(18,"JOSE GARCIA LANDA","DERECHO"),
(19,"DANIEL DURAN LANDA","LEYES"),
(20,"KARLA PINOS LINO","SISTEMAS"),
(21,"RAMON HUESCA LARA","ADMINISTRACION"),
(22,"VICTOR LANDA PEREZ","LEYES"),
(23,"CARLOS SOYO HOYOS","TURISMO"),
(24,"JUAN LANDA HUESCA","ARQUITECTURA"),
(25,"MARLEN RODRIGEUZ PEREZ","DERECHO"),
(26,"URIEL RENTERIA GARCIA","LEYES"),
(27,"ARMANDO AVILA SOTO","NEGOCIOS"),
(28,"KEILA LANDA MENDEZ","QUIMICA"),
(29,"OLGA RODRIGUEZ SALZAR","PEDAGOGIA"),
(30,"DIANA MARTINEZ RODRIGUEZ","PEDAGOGIA"),
(31,"VANESA GARCIA PEREZ","CONTABILIDAD"),
(32,"KAREN PEREZ AVILA","INFORMATICA"),
(33,"VICTOR ALARCON DIAZ","TURISMO"),
(34,"JORGE PEREZ LEON","LEYES"),
(35,"LAURA DIAZ ACOSTA","DERECHO"),
(36,"CARMEN LOPEZ DIAZ","LEYES"),
(37,"JOSE ROBERTO DIAZ PEREZ","QUIMICA"),
(38,"ROCIO AGUILAR MONTERO","TURISMO"),
(39,"JOEL CARMONA REYES","NEGOCIOS"),
(40,"CARLOS SANTIGO ALONSO","ENFERMERIA"),
(41,"ROBERTO PEREZ ALARCON","LEYES"),
(42,"PEDRO MENDEZ ROAN","TURISMO"),
(43,"ARIEL AVILA CAMACHO","DERECHO"),
(44,"RUBEN HERNANDEZ DIAZ","LEYES"),
(45,"CARLOS DIAZ PERES","TURISMO"),
(46,"ABURTO AREVALO DILAN MARTÍN","LEYES"),
(47,"ALARCÓN VELASCO YARITZA XIMENA","TURISMO"),
(48,"ARGUELLES JUAN IGNACIO GAEL","PEDAGOGIA"),
(49,"BRIONES ALARCÓN LIAM YAREK","ENFERMERIA"),
(50,"DÍAS JUAN BRENDA JAZMIN","MEDICINA"),
(51,"DURÁN HERNANDEZ LÍA ROMINA","QUIMICA"),
(52,"DURÁN MENDEZ MARIA MAGDALENA","ADMINISTRACION"),
(53,"HERNÁNDEZ MENDOZA CARLOS","LEYES"),
(54,"HERNÁNDEZ ORTIZ ARIEL","QUIMICA"),
(55,"LANDA MENDOZA ADHARA JOSHELYN","ENFERMERIA"),
(56,"LANDA RODRÍGUEZ JOAN EMANUEL","ENFERMERIA"),
(57,"MARTÍNEZ LUNA LEYDI DIANA","QUIMICA"),
(58,"MARTÍNEZ FRAMÍREZ ANGEL DAVID","MEDICINA"),
(59,"MENDIVIL MARTÍNEZ ARA","PEDAGOGIA"),
(60,"MENDOZA CRUZ ÁNGEL DE JESÚS","DERECHO"),
(61,"MENDOZA DURÁN REYES","TURISMO"),
(62,"MENDOZA SALAZAR MELISA","ADMINISTRACION"),
(63,"RÍOS MARTÍNEZ LYAN MATEO","ADMINISTRACION"),
(64,"SAUCEDO DURÁN JUAN PABLO","LEYES"),
(65,"PEREZ JUAN CARLOS","DERECHO"),
(66,"SALAZAR MATA ROBERTA","LEYES"),
(67,"BECERRA GARCIA LILIA","ADMINISTRACION"),
(68,"LANDA LOPEZ MAYRA","LEYES"),
(69,"SANCHEZ MATA LUIS","TURISMO"),
(70,"DIAZ PEREZ EMILIANO","SISTEMA");