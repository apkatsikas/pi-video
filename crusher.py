import subprocess
import os

directory = '../Videos/frames/grb'

files = os.listdir(directory)

for filename in files:
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        cmd_array = [
            '..\\GBACrusher\\GBACrusherCL.exe',
            '-L',
            f,
            '-O',
            os.path.join(
                directory, '{}.lz'.format(os.path.splitext(filename)[0])
            )
        ]
        subprocess.run(cmd_array)
