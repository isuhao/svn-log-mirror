# Copyright Dave Abrahams 2013. Distributed under the Boost
# Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

import util, os

_home = '/home/svnsync' # not exported

dump_file = os.path.join(_home, 'boost.svndump')
local_repo_dir = os.path.join(_home, 'svn', 'boost')

# Don't change this line
local_repo_url = util.path2url(local_repo_dir)

if __name__ == '__main__':
    for v in ['dump_file', 'local_repo_dir', 'local_repo_url']:
        print v, '==', globals()[v]
