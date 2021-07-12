import subprocess

with open('out.txt', 'wb') as f:
    out = subprocess.run(['ls', '-l'], capture_output=True)
    f.write(out.stdout)
