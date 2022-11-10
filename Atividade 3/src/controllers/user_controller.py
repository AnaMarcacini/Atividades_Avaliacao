from models.user import User
from dao.usuario_dao import UsuarioDao
"""
Ana Helena A. C. R. Marcacini
        RA: 20.01305-0
"""
class UserController():
    def __init__(self) -> None:
        #Carrega os dados dos usuários
        self.users = [
            User(name="joao", password="arroz", email="joao@mail.com"),
            User(name="joao2", password="arroz2", email="joao@amaarroz.com"),
            User(name="tais", password="petacular", email="tais_@condida.com"),
            User(name="Ana", password="Ana", email="Ana"),
            User(name="a@gmail.com", password="a", email="a@gmail.com"),
            User(name="a", password="a", email="a"),
            
        ]

    def getALL():#usar nas funções check user e login
        return UsuarioDao.get_instance().get_all()
    
    def checkUser(self,user):
        return user in UsuarioDao.get_instance().get_all()

    def checkLogin(self, name, password):
        print("estou aqui")
        user_teste = User(name=name, password=password, email=None)
        for user in UsuarioDao.get_instance().get_all():
            if user.name == user_teste.name and user.password == user_teste.password:
                return True
        return False

    def inserirUsuario(usuario):
        print("ERRO NESSA FUNÇAÕ")
        return UsuarioDao.get_instance().inserir_usuario(usuario)
    def pegarUsuario(self, email):
        return UsuarioDao.get_instance().pegar_usuario(email)
    def atualizarUsuario(self, usuario):
        return UsuarioDao.get_instance().atualizar_Usuario(usuario)
    def deletarUsuario(self,email):
        return UsuarioDao.deletar_usuario(email)




    