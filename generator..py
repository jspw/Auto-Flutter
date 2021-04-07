import subprocess as sp
import os


def createDir(dir_name):
    sp.call(['mkdir', dir_name])


def createStructure():
    print("Creating Project Structure folders...")
    createDir('src')
    createDir('src/config')
    createDir('src/config/routes')
    createDir('src/config/themes')
    createDir('src/constats')
    createDir('src/core')
    createDir('src/core/auth')
    createDir('src/core/auth/forgot_password')
    createDir('src/core/auth/login')
    createDir('src/core/auth/register')
    createDir('src/core/modules')
    createDir('src/core/modules/dashboard')
    createDir('src/core/modules/dashboard/bloc')
    createDir('src/core/modules/dashboard/models')
    createDir('src/core/modules/dashboard/repository')
    createDir('src/core/modules/dashboard/screens')
    createDir('src/ui')
    createDir('src/utils')
    createDir('src/utils/helpers')
    createDir('src/utils/mixin')
    createDir('src/utils/services')
    createDir('src/utils/ui')
    createDir('src/widgets')
    print("Project Structuring Done!")


def changeDir(dir_name):
    current_path = os.getcwd()
    new_path = os.path.join(current_path, dir_name)
    os.chdir(new_path)


def createFlutterProject(project_name):

    create_flutter_project = ["flutter", "create",
                              "-i", "objc", "-a", "java", project_name]

    sp.call(create_flutter_project)
    changeDir(project_name + '/lib')


if __name__ == '__main__':
    project_name = input("Enter Flutter Application Name : ")
    try:
        createFlutterProject(project_name)
        createStructure()

    except Exception as e:
        print(e)
