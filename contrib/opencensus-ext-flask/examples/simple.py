# Copyright 2017, OpenCensus Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.propagation.trace_context_http_header_format \
    import TraceContextPropagator

app = Flask(__name__)
middleware = FlaskMiddleware(app, propagator=TraceContextPropagator())


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    import logging
    logger = logging.getLogger('werkzeug')
    logger.setLevel(logging.ERROR)
    app.run(host='localhost', port=8080, threaded=True)
