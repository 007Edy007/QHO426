import os
def cwd():
    path = os.getcwd()
    print(f"Current working directory is {path}")
    print("the directory contains the next files:")
    for files in os.listdir(path):
        print(files)

def run():
    print("processing....")
    cwd()
if __name__ == "__main__":
    run()