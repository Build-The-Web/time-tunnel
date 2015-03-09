# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, bad-continuation
""" Project automation for Invoke.
"""

from invoke import run, task
from rituals.invoke_tasks import * # pylint: disable=redefined-builtin


@task
def serve(browse=False):
    """Start development web server."""
    if browse:
        import webbrowser
        webbrowser.open("http://127.0.0.1:5000/")
    run("vortex runserver")

@task
def ci(): # pylint: disable=invalid-name
    """Perform continuous integration tasks."""
    run("invoke clean --all build --docs test check --reports")
