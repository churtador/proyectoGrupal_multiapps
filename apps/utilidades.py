import bcrypt


def encriptar(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verificarPassword(confirmPass, password):
    print(bcrypt.checkpw(confirmPass.encode(), password.encode()))
    return bcrypt.checkpw(confirmPass.encode(), password.encode())
def filtrarPorProfesor(acceso):
    if acceso == '9':
        return True
    return False