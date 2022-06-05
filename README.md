# Girls Talk Math 2021

Introducing high schoolers to cryptographic secret sharing and proofs.

## [Packet](./packet)
*[Girls Talk Math Camp 2021](http://gtm.math.umd.edu/virtualcamp2021.html) at UMD*

A (potentially outdated) version of the packet can also be found on the UMD Girls Talk Math GitHub [here](https://github.com/girlstalkmath-umd/secret-sharing). If I make any edits, they will show up in this repo before the other link (if they show up there at all).

## [Spring Activity](./spring)
*[Girls Talk Math Spring Event](spring/presentation/GTMSpring2021Program.pdf) held on May 22, 2021.*

---
## Installation
This repo uses a [pre-commit Git hook](https://githooks.com/) to clear the outputs of Jupyter notebook files in order to give easily legible `git diff`s. 

The pre-commit script (which is run before every `git commit`) is [pre-commit.sh](pre-commit.sh). If you clone this repo and wish to use this Git hook as well, "install" the hook by running
```
ln -s ../../pre-commit.sh .git/hooks/pre-commit
```
in the root of this repo.
