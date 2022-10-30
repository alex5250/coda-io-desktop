import os,subprocess
import platform
import shutil
import pathlib

def run(command:str):
    output=subprocess.run(command,shell=True, check=True)
pass

def get_os():
    os=platform.system()
    if(os=="Windows"):
        return 'win32'
    if(os=="Linux"):
        return "linux"
    if(os=="Darwin"):
        return "darwin"
pass

def get_dir_with_app():
    for dir in os.listdir():
        if(dir.find("coda-electron-app") > -1):
            return dir
pass

def perpare_installer():
    input_string=open("installer.iss","r").read()
    print(str(pathlib.Path().resolve()))
    output=input_string.replace("_path_",str(pathlib.Path().resolve()))
    open("installer_build.iss","w").write(output)

    

def main():
    print("Coda Desktop app build tool. Now we will build an electron app for u")
    print("Getting an Node.js verison and Git version")
    run('node --version')
    run('git --version')
    run('git clone https://github.com/alex5250/coda-io-desktop.git')
    os.chdir('./coda-io-desktop')
    run('npm install ')
    run('npm install electron-packager --global ')
    run('npm start &')
    run(f'npx electron-packager . coda-electron-app --platform={get_os()} --icon {os.path.abspath("icon.ico")}')
    shutil.make_archive(f'coda_app_{get_os()}', 'zip', get_dir_with_app())
    perpare_installer()
    run(f'"C:\Program Files (x86)\Inno Setup 6\Compil32.exe" {os.path.abspath("installer_build.iss")}')
    

pass


main()
