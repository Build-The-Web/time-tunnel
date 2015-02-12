#! /usr/bin/env python
# -*- coding: utf-8 -*-
""" timetunnel – An event collection and dispatching µservice.

    Copyright ⓒ  2015 1&1 Group

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import os
import re

# Project data (the rest is parsed from __init__.py and other project files)
name = 'timetunnel'

# Import setuptools
try:
    from setuptools import setup, find_packages
except ImportError, exc:
    raise RuntimeError("Cannot install '{0}', setuptools is missing ({1})".format(name, exc))

# Helpers
project_root = os.path.abspath(os.path.dirname(__file__))
def srcfile(*args):
    "Helper for path building."
    return os.path.join(*((project_root,) + args))

def _build_metadata():
    "Return project's metadata as a dict."
    # Handle metadata in package source
    expected_keys = ('url', 'version', 'license', 'author', 'author_email', 'long_description')
    metadata = {}
    with open(srcfile('src', name, '__init__.py')) as handle:
        pkg_init = handle.read()
        # Get default long description from docstring
        metadata['long_description'] = re.search(r'^"""(.+?)^"""$', pkg_init, re.DOTALL|re.MULTILINE).group(1).strip()
        for line in pkg_init.splitlines():
            match = re.match(r"""^__({0})__ += (?P<q>['"])(.+?)(?P=q)$""".format('|'.join(expected_keys)), line)
            if match:
                metadata[match.group(1)] = match.group(3)

    if not all(i in metadata for i in expected_keys):
        raise RuntimeError("Missing or bad metadata in '{0}' package".format(name))

    # Load requirements files
    requirements_files = dict(
        install = 'requirements.txt',
        setup = 'setup-requirements.txt',
        test = 'test-requirements.txt',
    )
    requires = {}
    for key, filename in requirements_files.iteritems():
        requires[key] = []
        if os.path.exists(srcfile(filename)):
            with open(srcfile(filename), 'r') as handle:
                requires[key] = [i.strip() for i in handle if i.strip() and not i.startswith('#')]

    # Complete project metadata
    with open(srcfile('classifiers.txt'), 'r') as handle:
        classifiers = [i.strip() for i in handle if i.strip() and not i.startswith('#')]

    metadata.update(dict(
        name = name,
        description = metadata['long_description'].split('.')[0],
        url = metadata['url'],
        package_dir = {'': 'src'},
        packages = find_packages(srcfile('src'), exclude=['tests']),
        zip_safe = False,
        include_package_data = True,
        install_requires = requires['install'],
        setup_requires = requires['setup'],
        tests_require =  requires['test'],
        classifiers = classifiers,
        entry_points = dict(
            console_scripts = [
                'tictoc = timetunnel.__main__:cli',
            ],
        ),
    ))
    return metadata

# Ensure "setup.py" is importable by other tools, to access the project's metadata
project = _build_metadata()
__all__ = ['project', 'project_root', 'srcfile']
if __name__ == '__main__':
    setup(**project)
