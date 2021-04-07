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
    createDir('assets')
    createDir("assets/images")
    createDir("assets/fonts")
    createDir('lib/src')
    createDir('lib/src/config')
    createDir('lib/src/config/routes')
    createDir('lib/src/config/themes')
    createDir('lib/src/constats')
    createDir('lib/src/core')
    createDir('lib/src/core/auth')
    createDir('lib/src/core/auth/forgot_password')
    createDir('lib/src/core/auth/login')
    createDir('lib/src/core/auth/register')
    createDir('lib/src/core/modules')
    createDir('lib/src/core/modules/dashboard')
    createDir('lib/src/core/modules/dashboard/bloc')
    createDir('lib/src/core/modules/dashboard/models')
    createDir('lib/src/core/modules/dashboard/repository')
    createDir('lib/src/core/modules/dashboard/screens')
    createDir('lib/src/ui')
    createDir('lib/src/utils')
    createDir('lib/src/utils/helpers')
    createDir('lib/src/utils/mixin')
    createDir('lib/src/utils/services')
    createDir('lib/src/utils/ui')
    createDir('lib/src/widgets')


def changeDir(dir_name):
    current_path = os.getcwd()
    new_path = os.path.join(current_path, dir_name)
    os.chdir(new_path)


def createFlutterProject(project_name):

    create_flutter_project = ["flutter", "create",
                              "-i", "objc", "-a", "java", project_name]

    print("Generating new flutter project......")

    sp.check_output(create_flutter_project)

    changeDir(project_name)


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
