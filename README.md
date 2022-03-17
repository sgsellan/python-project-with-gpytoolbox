# A template for a Python project 

Here's a template with (some) best practices on how to organize your python
project. I am new to python, so feel free to submit a PR if you know how to
improve this!

# Installation

If you create a new repository `repo_name` using this template, make sure to clone it and all its dependencies recursively:
```bash
git clone --recursive git@github.com:your_name/repo_name.git
cd repo_name
git submodule update --init --recursive
```

As an example of how to use submodules, this project template includes
`gpytoolbox` as a submodule in `ext/gpytoolbox`. If you want to use other
libraries that can't be installed through `pip` or `conda`, feel free to add
them as submodules in `ext/`. You can also
[delete](https://stackoverflow.com/questions/1260748/how-do-i-remove-a-submodule)
`gpytoolbox` if you just want to use this template for something else.

But if you do want to use this template with gpytoolbox, remember to install it by running
```bash
cd ext/gpytoolbox/
mkdir build
cd build
cmake ..
make
```

Then, you can test your installation by running
```bash
python scripts/sample_script.py
```

# Use this template for your own project

Add your project functionality in `utility/` following the example in
`utility/sample_fun.py`. Remember to update `utility/__init__.py` after adding
any new functions to `utility/`. Test your functionality with scripts following
the example of `scripts/sample_script.py`, using `scripts/context.py` to include
your functionality in a consistent way. Run any scripts with
```bash
python scripts/script_name.py
```