import os
import subprocess
import shutil
import sys
import logging
import argparse

class cd:
    '''Context manager for changing the current working directory
    '''
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)
​
    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)
​
​
def is_package(path):
    '''This function returns whether the path passed is a 
        directory or not
​
        Arguments: path of file/folder
​
        Returns: True/False depending on whether it is a directory or not
​
    '''
    return (os.path.isdir(path))
        
​
def iterate_folder(path, skip_folder=[], skip_files=[],pattern=[]):
​
    ''' This function converts all python files into it's shared 
        executable format, skips specified files and directories and
        removes all pyc files.
​
        Arguments:  path:path of file/folder
                    skip_folder: directory to be skipped
                    skip_files: files to be skipped
                    pattern: pattern of file names to be skipped
​
    '''
​
    for item in os.listdir(path):
​
        
​
        if item in skip_folder or item[0] == '.':
            logger.info("Skippping directory:%s "%item)
            continue
        entry = os.path.join(path, item)
​
        if is_package(entry):
            try:
                iterate_folder(entry, skip_folder, skip_files,pattern)
            except Exception as e:
                print(e)
​
        if item.endswith(".pyc"):
            logger.info("Removing: %s"%item)
            try:
                os.remove(entry)
            except Exception as e:
                print(e)
        
        elif (item in skip_files or (not item.endswith(".py")) 
              or any(item.startswith(str(i)) for i in pattern)):
​
            logger.info("***Skippping file: %s ***"%item)
        else:
            with cd(path): 
                logger.info("Compiling: %s " %entry)
                cmd = "python -m nuitka --module --recurse-none " + item
​
                try:
                    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
                    stdout, stderr = proc.communicate()
                    os.remove(entry)
                    if os.path.exists(entry + "c"):
                        os.remove(entry + "c")
                    shutil.rmtree(".".join(item.split(".")[:-1]) + ".build")
                    logger.info("done")
                except Exception as e:
                    print(e)
                
​
​
def main():
    '''This function passes the path, folders and files, and patterns
        of text files to skip to the iterate_folder function.
    '''
    parser = argparse.ArgumentParser(description='Passing arguments')
    parser.add_argument('--paths', dest='paths', type=str, nargs='*',
                    help='list of paths')
    parser.add_argument('--skip_files', dest='sfile', default=[], type=str, nargs='*',
                    help='list of files to skip')
    parser.add_argument('--skip_folder', dest='sfold', type=str, nargs='*',
                    help='list of folders to skip')
    parser.add_argument('--pattern', dest='pattern', type=str, nargs='*',
                    help='list of patterns')
​
​
    results = parser.parse_args()
    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    
    
​
    for path in results.paths:
        path=path.strip("[").strip("]")
        logger.info("***Processing:%s***"%path)
        compile_path = os.path.join(CUR_DIR, path)
        iterate_folder(compile_path, results.sfold[0], results.sfile[0],results.pattern[0])
        logger.info("***DONE***")
​
​
​
if __name__ == '__main__':
​
    logger = logging.getLogger("__name__")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    file_handler = logging.FileHandler("preprocessing_and_OCR_report.log")
    file_handler.setFormatter(formatter)
    st_hndle = logging.StreamHandler()
    st_hndle.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(st_hndle)
    
    main()
