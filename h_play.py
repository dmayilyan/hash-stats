import os
import hashlib
import pprint

import numpy as np

let_dict = {}


def get_hash(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        file_content = f.read(65536)
        md5.update(file_content)

    return md5.hexdigest()


def to_hist(file_hash):
    for l in file_hash:
        if l in let_dict:
            let_dict[l] += 1
        else:
            let_dict[l] = 1


def main():
    home_path = os.path.expanduser('~')
    files_path = os.path.join(home_path, 'Documents')
    file_list = os.fwalk(files_path)
    counter = 0
    for loc_f in file_list:
        # print()

        for i_file in loc_f[2]:
            counter += 1
            file_path = os.path.join(loc_f[0], i_file)
            # print(file_path)
            file_hash = get_hash(file_path)
            # print(file_hash)
            to_hist(file_hash)

    pprint.pprint(let_dict)
    print('Overall count: ', counter)

    print('Std is: ', np.std([i for i in let_dict.values()]))


if __name__ == '__main__':
    main()
