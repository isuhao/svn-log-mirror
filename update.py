#!/usr/bin/env python

# Copyright Dave Abrahams 2013. Distributed under the Boost
# Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

from util import svn_head_revision as head_rev
from paths import *
import subprocess, os, sys

def run(dump = False):
    old_head = head_rev(local_repo_url)
    try:
        print ' === syncing local SVN repo ==='
        subprocess.check_call(
            ['svnsync', 'synchronize', '--non-interactive', local_repo_url])

        if not dump: return

        # If this fails, we'll rebuild the dump from scratch
        open(dump_file, 'r')

        if head_rev(local_repo_url) == old_head:
            print ' === Sync triggered, but found nothing to do === '
        else:
            print ' === updating dumpfile ==='
            subprocess.check_call(
                ['svnadmin', 'dump', local_repo_dir, '-r', str(old_head), '--incremental'],
                stdout=open(dump_file, 'ab'))
    except:
        # If anything went wrong, try to rebuild the dump file from the
        # beginning
        try:
            print ' === incremental update failed; rebuilding dumpfile... ==='
            subprocess.check_call(
                ['svnadmin', 'dump', '--quiet', local_repo_dir], 
                stdout=open(dump_file, 'wb'))
        except:
            if os.path.exists(dump_file):
                print ' === removing failed dump results ==='
                os.unlink(dump_file)
            raise # If that doesn't work either, finally, really fail.

if __name__ == '__main__':
    run('--dump' in sys.argv)
