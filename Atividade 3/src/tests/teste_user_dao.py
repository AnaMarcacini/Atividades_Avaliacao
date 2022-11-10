from src.dao.usuario_dao import UsuarioDao
from src.models.user import User



##Ver todos os usuarios
print("OIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
usuarios = UsuarioDao.get_instance().get_all()

for usuario in usuarios:
    print(usuarios)

print(50*"#")




user = User(email="souNovo@gmail.com",name = "AcabeiDeChegar", password= "password")
UsuarioDao.get_instance().inserir_usuario(user)

usuarios = UsuarioDao.get_instance().get_all()
for usuario in usuarios:
    print(usuarios)

print(50*"#")





usuario = UsuarioDao.get_instance().pegar_item(user.email)
usuario.nome = "EstouVelho"
usuario.password = "senha"
print(UsuarioDao.get_instance().atualizar_item(usuario))

usuarios = UsuarioDao.get_instance().get_all()
for usuario in usuarios:
    print(usuarios)

print(50*"#")




print(UsuarioDao.get_instance().deletar_item(usuario.email))

print(50*"#")

usuarios = UsuarioDao.get_instance().get_all()
for usuario in usuarios:
    print(usuarios)