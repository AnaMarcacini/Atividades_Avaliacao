from email.mime import image
import sqlite3
from src.models.product import Product
class ProdutoDAO:
    _instance = None
    def __init__(self) -> None:
        self._connect()
    @classmethod
    def get_instance(cls):#ok
        if cls._instance == None:
            cls._instance = ProdutoDAO()
        return cls._instance
    def _connect(self):#ok
        self.conn = sqlite3.connect('./databases/sqlite.db',check_same_thread=False)
    def get_all(self):#ok
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Itens;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Product(id=resultado[0], name=resultado[1], price=resultado[2], descricao = resultado[3], url= resultado[4]))
        self.cursor.close()
        return resultados
    def inserir_item(self, item):#ok    falta retornar falso ou true
        self.cursor = self.conn.cursor()
        print("oi")
        print("*"*1000)
        self.cursor.execute("""
            INSERT INTO Itens (id, nome, preco, descricao,imagem)
            VALUES(?,?,?,?,?);
        """, (item.id, item._name, item._price,item._url,item.descricao))
        self.conn.commit()
        self.cursor.close()
    
    def pegar_item(self, id):#ok
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE id = '{id}';
        """)
        item = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            item = Product(id=resultado[0], name=resultado[1], price=resultado[2], descricao = resultado[3], url= resultado[4])
        self.cursor.close()
        return item
    
    def atualizar_item(self, item):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Itens SET
                nome = '{item.name}',
                preco = {item.price},
                descricao = '{item.descricao}'
                imagem = '{item.imagem}'
                WHERE id = '{item.id}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def deletar_item(self, id):#ok
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Itens 
                WHERE id = '{id}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def search_all_for_name(self,nome): #ok
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE nome LIKE '{nome}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Product(id=resultado[0], name=resultado[1], price=resultado[2],descricao= resultado[3],image = resultado[4]))
        self.cursor.close()
        return resultados
