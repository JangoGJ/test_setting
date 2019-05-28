from os import system as cmd_run

File_folder = "C:/Users/XXX/Downloads/platform-tools_r28.0.3-windows/platform-tools/"
goto_enviroment="C:\Windows\System32\cmd.exe /K "+'"'+"cd /d "+str(File_folder)+'"'
print(goto_enviroment)
cmd_run(goto_enviroment)
print('xxxxxxxxxxxxxxxxxxxx')
cmd_run('".\adb -d shell sh /data/data/me.piebridge.brevent/brevent.sh"')

