# Realiza la importacion de la "InterfaceRepositorio"
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
# Realiza la importación del modelo "Estudiante"
from Modelos.Estudiante import Estudiante

# Se declara la calse "RepositorioEstudiante" heredando los metodos "InterfaceRepositorio"


class RepositorioEstudiante(InterfaceRepositorio[Estudiante]):
    pass
