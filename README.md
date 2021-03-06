# time-tunnel

![logo](https://raw.githubusercontent.com/Build-The-Web/time-tunnel/master/static/img/logo-160.png)
An event collection and dispatching µservice.

 [![Groups](https://img.shields.io/badge/Google_groups-btw--users-orange.svg)](https://groups.google.com/forum/#!forum/btw-users)
 ![Apache 2.0 licensed](http://img.shields.io/badge/license-Apache_2.0-red.svg)
 [![Travis CI](https://api.travis-ci.org/Build-The-Web/time-tunnel.svg)](https://travis-ci.org/Build-The-Web/time-tunnel)


## Overview

`time-tunnel` accepts timestamped events with loosely defined semantics over a set of common APIs,
and then dispatches those events on a best-effort basis
to various event sinks according to a ruleset that is part of the configuration.

The main goal is to offer clients a way to easily push their events to *one* uniform event submission API of their choosing,
and then go back and concentrate on their actual task. Once those events hit the dispatcher,
they can be filtered and duplicated according to the needs of the event sinks.

There's a set of built-in implementations for both delivery APIs and event sinks, and they can
be extended with custom ones via a plugin system.
`time-tunnel` is implemented using Python (tested on 2.7 and 3.4) and Flask+WSME.

![System Landscape](https://raw.githubusercontent.com/Build-The-Web/time-tunnel/master/static/img/system-landscape.png)


## Portals

Events enter or exit the system via portals, which normally take the form of some API endpoint implementation.
They adapt to/from the internal event model, so that (hopefully) any connection between them is possible.

### Entry Portals

 * :soon: GitLab Web Hook

### Exit Portals

 * :soon: HipChat
 * :soon: WebHooks (e.g. Jenkins Job triggers)


## Events

The canonical representation of an event is a flat JSON object with the following fields.

* `timestamp` – The timestamp of this event in ISO-8601 format.
* `kind` – An URN specifying the type of this event.
* `message` – Human readable description.
* `source` – An URN or URL specifying the exact location of the event source (e.g. a deployed webapp).
* `severity` – Importance of alarms or log entries.
* `view_link` – URL of a view in the source system.
* `ack_link` – URL for acknowledging alarm events.

`timestamp`, `kind` and `message` are obligatory,
but `timestamp` is added server-side when it's missing,
and `kind` defaults to `unknown`.
All other fields are optional, but if the semantics fit, the field name as defined above should be used.
Any additional number of fields can be included.


## Installation

To create a development environment, use these commands:

```sh
git clone "https://github.com/Build-The-Web/time-tunnel.git"
cd time-tunnel
. .env # answer the prompt with (y)es
invoke build --docs
```

See [CONTRIBUTING](https://github.com/Build-The-Web/time-tunnel/blob/master/CONTRIBUTING.md)
for details on how to give back your improvements and fixes to upstream, so every user can benefit from them.


## Usage
**TODO**


## Related Projects

**Event sources + sinks**

* [HipChat](https://github.com/hipchat)
* [InfluxDB](https://github.com/influxdb)
* [Sentry](https://github.com/getsentry/sentry)
* [StatsD](https://github.com/etsy/statsd)
* [Fluentd](https://github.com/fluent/fluentd)
* [feedr](https://github.com/nir0s/feedr)
* [python-beaver](https://github.com/josegonzalez/python-beaver)
* [TeaFiles](https://github.com/discretelogics/TeaFiles.Py)
* [Graphite Beacon](https://github.com/klen/graphite-beacon)

**Visualization / UI**

* [EventDrops](https://github.com/marmelab/EventDrops)
* [Timesketch](https://github.com/google/timesketch)
* [Anthracite](https://github.com/Dieterbe/anthracite)


## Acknowledgements

[![1&1](https://raw.githubusercontent.com/1and1/1and1.github.io/master/images/1and1-logo-42.png)](https://github.com/1and1)  Project sponsored by [1&1](https://github.com/1and1).
