# time-tunnel

![logo](https://raw.githubusercontent.com/Feed-The-Web/time-tunnel/master/static/img/logo-160.png)
An event collection and dispatching µservice.

![Apache 2.0 licensed](http://img.shields.io/badge/license-Apache_2.0-red.svg)


## Overview

`time-tunnel` accepts timestamped events with loosely defined semantics over a set of common APIs,
and then dispatches those events on a best-effort basis
to various event sinks according to a ruleset that is part of the configuration.


## Events

The canonical representation of an event is a flat JSON object with the following fields.

* `timestamp` – The timestamp of this event in ISO-8601 format.
* `kind` – An URN specifying the type of this event.
* `message` – Human readable description.
* `source` – An URN or URL specifying the exact location of the event source (e.g. a deployed webapp).
* `severity` – Importance of alarms or log entries.
* `view_link` – URL of a view in the source system.
* `ack_link` – URL for acknowledging alarm events.

`timestamp` and `message` are obligatory, but `timestamp` is added server-side when it's missing.
All other fields are optional, but if the semantics fit, the field name as defined above should be used.
Any additional number of fields can be added.


## Installation
**TODO**


## Usage
**TODO**


## Contributing
**TODO**


## Acknowledgements

[![1&1](https://raw.githubusercontent.com/1and1/1and1.github.io/master/images/1and1-logo-42.png)](https://github.com/1and1)  Project sponsored by [1&1](https://github.com/1and1).
