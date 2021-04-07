import subprocess as sp
import os


def createDir(dir_name):
    sp.call(['mkdir', dir_name])


def end(project_name):

    print("All done!")
    print("In order to run your application, type:\n")
    print("\t$ cd " + project_name)
    print("\t$ flutter run\n")

    print("To enable null safety, type:\n")
    print("\t$ cd", project_name)
    print("\t$ dart migrate --apply-changes\n")

    print("Project File Structure :")

    sp.call('tree')

    print("Your application code is in " + project_name + "/lib/main.dart.")

    print("Thanks for using.")


def createStructure():
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


def changeDir(dir_name):
    current_path = os.getcwd()
    new_path = os.path.join(current_path, dir_name)
    os.chdir(new_path)


def createFlutterProject(project_name):

    create_flutter_project = ["flutter", "create",
                              "-i", "objc", "-a", "java", project_name]

    print("Generating new flutter project......")

    sp.check_output(create_flutter_project)

    changeDir(project_name + '/lib')


def main():

    print("""
        _         _          _____ _       _   _            
       / \  _   _| |_ ___   |  ___| |_   _| |_| |_ ___ _ __ 
      / _ \| | | | __/ _ \  | |_  | | | | | __| __/ _ \ '__|
     / ___ \ |_| | || (_) | |  _| | | |_| | |_| ||  __/ |   
    /_/   \_\__,_|\__\___/  |_|   |_|\__,_|\__|\__\___|_| 

        """)

    project_name = input("Enter Flutter Application Name : ")
    try:
        createFlutterProject(project_name)
        createStructure()
        end(project_name)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
