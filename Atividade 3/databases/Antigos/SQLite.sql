DROP TABLE Pedidos;
DROP TABLE Itens;
DROP TABLE Usuario;
CREATE TABLE Pedidos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
      id_item TEXT NOT NULL,
      id_cliente INTEGER,
      quantidade INTEGER NOT NULL,
      numero_pedido TEXT NOT NULL,
  	  preco REAL NOT NULL,
      data_hora TEXT NOT NULL
);

CREATE TABLE Itens(
	id TEXT PRIMARY KEY,
	nome TEXT NOT NULL,
	preco REAL NOT NULL,
  	descricao TEXT,
  	imagem TEXT NULL
);

CREATE TABLE Usuario(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
  	email TEXT NOT NULL,
  	senha TEXT NOT NULL
);

INSERT INTO Itens VALUES
	("ABC", "WebCam Logtech 922S", 200, NULL, NULL),
	("CAF", "Café Curto Organico Brazil Essentials", 4.5, NULL, NULL),
	("SQL", "Aula do Murilo - ONLINE", 19.90, NULL, NULL),
	("COC", "Aula do Murilo - Presencial Particular", 45000, NULL, NULL),
	("FEL", "Overwatch 2 - Season Pass", 149, NULL, NULL);


SELECT * FROM Itens


