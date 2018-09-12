CREATE TABLE mensagem(
	id serial PRIMARY KEY,
	usuario_id INTEGER NOT NULL,
	texto varchar(140) NOT NULL
);