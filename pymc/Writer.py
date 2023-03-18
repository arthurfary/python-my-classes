import os

class Writer:

    def __init__(self, classes):
        self.__classes = classes

    def write(self):
        for classname, variables in self.__classes.items():
            folders, filename, fclassname = self._format_classname(classname)

            if not os.path.exists(os.path.join(folders, filename)):
                self._create_directory(folders)
                self._create_class_file(fclassname, variables, folders, filename)

    def _format_classname(self, classname):
        folders = classname.rsplit('<', 1)[0].replace('<', '\\') if '<' in classname else ''
        filename = classname.rsplit('<', 1)[1] + '.py' if '<' in classname else classname + '.py'
        fclassname = classname.rsplit('<', 1)[1] if '<' in classname else classname

        return folders, filename, fclassname

    def _create_directory(self, folders):
        if folders:
            try:
                os.makedirs(folders)
            except FileExistsError:
                pass

    def _create_class_file(self, fclassname, variables, folders, filename):
        with open(os.path.join(folders, filename), 'w') as classfile:
            classfile.write(f'class {fclassname}:\n\n')
            classfile.write('\tdef __init__(self):\n\n')

            for variable, value in variables.items():
                classfile.write(f'\t\tself.{variable} = {value}\n')

            for variable, value in variables.items():
                if variable.startswith('_'):
                    method_name = f'get{variable[1:].capitalize()}'
                    classfile.write(f'\n\tdef {method_name}(self):\n')
                    classfile.write(f'\t\treturn self.{variable}\n')
