#!/usr/bin/env python

# Copyright Dave Abrahams 2013. Distributed under the Boost
# Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

from util import svn_head_revision as head_rev
from paths import *
import sys

remote_repo_url = 'http://svn.boost.org/svn/boost'

if head_rev(remote_repo_url) == head_rev(local_repo_url):
    exit(1) # Only update if the remote and local URLs don't match
