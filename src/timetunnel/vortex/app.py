# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation
""" Main web application.
"""
# Copyright ⓒ  2015 1&1 Group
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """The root page."""
    return '<h1>Move Along, Nothing to See Here!</h1>'
