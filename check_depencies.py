import platform
import os
if str(platform.system()) == 'Windows':
    has_windows = True
else:
    has_windows = False
if not has_windows:
    Tk().withdraw()
    print('You do not have the reccomended OS for this program. Some features may work incorrectly.')
    os.system('python3 -m pip install playsound')
    os.system('python3 -m pip install requests')
    os.system('python3 -m pip install keyboard')
    os.system('python3 -m pip install termcolor')
    os.system('python3 -m pip install packaging')
else:
    os.system('py -m pip install playsound')
    os.system('py -m pip install requests')
    os.system('py -m pip install winsound')
    os.system('py -m pip install keyboard')
    os.system('py -m pip install termcolor')
    os.system('py -m pip install packaging')
input('All Finished! Press enter to complete source-code setup')
