
DROP TABLE Itens;
DROP TABLE Usuario;


CREATE TABLE Itens(
	id TEXT PRIMARY KEY,
	nome TEXT NOT NULL,
	preco REAL NOT NULL,
  	descricao TEXT,
  	imagem TEXT NULL
);

CREATE TABLE Usuario(
  	email TEXT PRIMARY KEY,
	nome TEXT NOT NULL,
  	senha TEXT NOT NULL
);

INSERT INTO Itens VALUES
	("ABC", "WebCam Logtech 922S", 200, NULL, NULL),
	("CAF", "Café Curto Organico Brazil Essentials", 4.5, NULL, NULL),
	("SQL", "Aula do Murilo - ONLINE", 19.90, NULL, NULL),
	("COC", "Aula do Murilo - Presencial Particular", 45000, NULL, NULL),
	("1", "Produto 1", 450, NULL, "assets/lechonk.jpg"),
	("2", "Produto 2", 4503, NULL, "essa/imagem/nao/existe"),
	("3", "Produto 3", 4502, NULL, NULL),
	("4", "Produto 4", 4501, NULL, NULL),
	("5", "Produto 4", 4501, NULL, NULL),
	("6", "Produto 4", 4501, NULL, NULL),
	("7", "Produto 4", 4501, NULL, NULL),
	("FEL", "Overwatch 2 - Season Pass", 149, NULL, NULL);

INSERT INTO Usuario VALUES
	("a@gmail.com", "A", "a"),
	("b@gmail.com", "B", "b"),
	("c@gmail.com", "C", "c"),
	("d@gmail.com", "D", "d"),
	("e@gmail.com", "E", "f");

SELECT * FROM Usuario


