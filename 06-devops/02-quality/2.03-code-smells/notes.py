#!/usr/bin/env python3
# https://python3.info/devops/quality/code-smells.html


# %% Quality Code Smells
# %%



# %% Bad practice
# %%



# %% range(len())
# - Very common bad practice
# - poor variable naming and readability
# - range(len(...)) will evaluate generator to calculate length
# - DATA[i] lookups has O(n) complexity!!
# - Does not use generator at all!
# %%



