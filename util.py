#!/usr/bin/env python

# Copyright Dave Abrahams 2013. Distributed under the Boost
# Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
import subprocess, urlparse, urllib

def svn_head_revision(repo_url):
    log_line = subprocess.check_output(
        ['svn', 'log', '-rHEAD', '--quiet', repo_url]).split('\n')[1]
    return int( log_line.split()[0][1:] )

def path2url(path):
    return urlparse.urljoin(
      'file:', urllib.pathname2url(path))
    
if __name__ == '__main__':
    import sys
    print head_revision(sys.argv[1])
