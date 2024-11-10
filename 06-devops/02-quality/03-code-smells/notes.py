#!/usr/bin/env python3

# Reference:
# https://python3.info/devops/quality/code-smells.html

#%% Code Smells



#%% Bad practice



#%% ``range(len())``
# Very common bad practice
# poor variable naming and readability
# range(len(...)) will evaluate generator to calculate length
# DATA[i] lookups has O(n) complexity!!
# Does not use generator at all!