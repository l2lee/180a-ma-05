#!/usr/bin/env python

import sys
import os
import json

def main(target):
    test_dir = target
    test_file = os.path.join(test_dir, 'testdata', 'test_data.json')

    with open(test_file) as f:
        data = json.load(f)
        print(data)
    print(f'hello world, I am now running {test_file}')



if __name__ == '__main__':
    target = sys.argv[1]
    main(target)