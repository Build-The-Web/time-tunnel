# -*- coding: utf-8 -*-
# pylint: disable=bad-whitespace
""" timetunnel – An event collection and dispatching µservice.

    time-tunnel accepts timestamped events with loosely defined semantics
    over a set of common APIs, and then dispatches those events on a
    best-effort basis to various event sinks according to a ruleset that
    is part of the configuration.

    The main goal is to offer clients a way to easily push their events to
    one uniform event submission API of their choosing, and then go back and
    concentrate on their actual task. Once those events hit the dispatcher,
    they can be filtered and duplicated according to the needs of the event sinks.

    There's a set of built-in implementations for both delivery APIs and
    event sinks, and they can be extended with custom ones via a plugin system.

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
__url__             = 'https://github.com/Feed-The-Web/time-tunnel'
__version__         = '0.1.0'
__license__         = 'Apache 2.0'
__author__          = 'Jürgen Hermann'
__author_email__    = 'jh@web.de'
__keywords__        = 'events dispatcher time-series restful flask webapp micro-service'


__all__ = [
    #'',
    #'EventSource',
    #'EventSink',
]
