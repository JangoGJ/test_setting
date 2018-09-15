import os
#result = os.system("ipconfig")
p = Popen("ipconfig", shell=True, stdout=PIPE, stderr=PIPE)  
p.wait()
pause()