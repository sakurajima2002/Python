def verificarEmail(emailUser):
    """
    Evalua un email recibido en busca
    del @ , si tiene un @ es correcto
    , si tiene mas de un @ es incorrecto
    y si tiene  @ al final es incorrecto

    >>> verificarEmail('juan@cursor.com')
    True

    >>> verificarEmail('juancursor.com@')
    False

    >>> verificarEmail('juancursor.com')
    False

    >>> verificarEmail('juan@cursor@.com')
    False
    """

    arroba = emailUser.count('@')
    if (arroba != 1 or emailUser.rfind('@') == (len(emailUser)-1) or emailUser.find('@') == 0):
        return False
    else:
        return True

import doctest
doctest.testmod()