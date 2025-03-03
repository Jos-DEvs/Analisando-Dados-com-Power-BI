CREATE TABLE Data( 
	idData int primary key,
	data datetime);

CREATE TABLE Curso( 
	idCurso int primary key,
	data datetime,
	Nome_do_curso varchar(50),
	Descrição varchar(50));

CREATE TABLE Disciplina( 
	idDisciplina int primary key,
	data datetime,
	nome_da_disciplina varchar(50),
	Descrição varchar(50));

CREATE TABLE Departamento( 
	idDepartamento int primary key,
	nome_do_departamento varchar(50),
	campus varchar(50));

CREATE TABLE Professor( 
	idProfessor int primary key,
	idData int REFERENCES DATA(idData),
	idCurso int REFERENCES CURSO(idCurso),
	idDisciplina int REFERENCES DISCIPLINA(idDisciplina),
	idDepartamento int REFERENCES DEPARTAMENTO(idDepartamento) ,
	Nome_completo varchar(50));
