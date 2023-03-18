import os

class Writer:

    def __init__(self, classes) -> None:
        self.__classes = classes

    def write(self) -> None:
        classes = self.__classes                
        for classname in classes:

            # formatando o nome da classe, arquivo e pastas
            # (tirar '<', adicionar .py ...)
            folders = classname.rsplit('<', 1)[0].replace('<', '\\') if '<' in classname else ''
            filename = classname.rsplit('<', 1)[1] + '.py' if '<' in classname else classname + '.py' #need to change if wanna make for other languages
            fclassname = classname.rsplit('<', 1)[1] if '<' in classname else classname
            
            # se o arquivo nao existir:
            if not os.path.exists(os.path.join(folders, filename)):

                if folders:
                    # tenta criar o diretorio, se der windowsError é que ja existe 
                    try:
                        os.makedirs(folders)
                    except WindowsError:
                        pass
                
                # abre o arquivo
                with open(os.path.join(folders, filename), 'w') as classfile:

                    # escreve a classe e abre o init
                    classfile.write('class ' + fclassname + ':\n\n')
                    classfile.write('\tdef __init__(self):\n\n')

                    # adiciona as variaveis dentro do init
                    for variable in classes[classname]:
                        classfile.write(f'\t\tself.{variable} = {classes[classname][variable]}\n')

                    # adiciona gets se a variavel começar com _ (protegida)
                    for variable in classes[classname]:
                        if variable[0] == '_':
                            classfile.write(f'\n\tdef get{ (str(variable).replace("_", "").capitalize()) }(self):\n')
                            classfile.write(f'\t\treturn self.{variable}\n')
                    