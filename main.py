import subprocess

if __name__ == '__main__':
    subprocess.run(['python', 'converter.py'] + sys.argv[1:])
