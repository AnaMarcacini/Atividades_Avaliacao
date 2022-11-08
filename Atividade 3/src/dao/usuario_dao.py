from operator import truediv
import sqlite3
from src.models.user import User
class UsuarioDao:
    #ItemDAO || Item id
    _instance = None
#User(email=resultado[0], name=resultado[1], password=resultado[2])
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):#usar sempre a mesma instancia -- ok
        if cls._instance == None:
            cls._instance = UsuarioDao()
        return cls._instance

    def _connect(self):#ok
        try:
            self.conn = sqlite3.connect('./databases/sqlite.db')
        except:
            print("Erro, possivel endereço incorreto da base de dados")

    def get_all(self):#get_all_users ok 
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Usuario;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(email=resultado[0], name=resultado[1], password=resultado[2]))
        self.cursor.close()
        return resultados
    
    def inserir_usuario(self, usuario):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO Usuario (email, nome, senha)
                VALUES(?,?,?);
            """, (usuario.email, usuario.name, usuario.password))########Talvez erro#########
            self.conn.commit()
            self.cursor.close()
            return True
        except:
            return False
    
    def pegar_usuario(self, email):#ok
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Usuario
            WHERE email = '{email}';
        """)
        usuario = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            usuario = User( email=resultado[0], name=resultado[1], password=resultado[2])
        self.cursor.close()
        return usuario
    
    def atualizar_Usuario(self, usuario):#ok
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Usuario SET
                nome = '{usuario.name}',
                senha = {usuario.password}
                WHERE email = '{usuario.email}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def deletar_usuario(self, email):#ok
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Usuario 
                WHERE email = '{email}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

#    def search_all_for_name(self,nome):
#        self.cursor = self.conn.cursor()
#        self.cursor.execute(f"""
#            SELECT * FROM Itens
#            WHERE nome LIKE '{nome}%';
#        """)
#        resultados = []
#        for resultado in self.cursor.fetchall():
#            resultados.append(Item(id=resultado[0], nome=resultado[1], preco=resultado[2]))
#        self.cursor.close()
#        return resultados
