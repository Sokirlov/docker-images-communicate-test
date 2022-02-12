# import best
import subprocess, os


directoru = os.listdir('/app')
print('It`s run A - ', directoru)



subprocess.run(['curl', 'best'])

