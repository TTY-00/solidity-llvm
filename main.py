# coding:utf-8
#!/usr/bin/env python3

'''
This file is the entrance of the module.
'''

import src.util
import argparse
from src.ir_gen import *

if __name__ == '__main__':
    source_file = ''
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", type=str, help="source ast file")
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    
    if args.source:
        source_file = args.source
        # transfer relative path to absolute path
        if source_file[0] != "/":
            source_file=os.path.join(sys.path[0],source_file)
    else:
        print('No source file exit.')
        exit

    ap=AstParser()
    ap.run(source_file)
