from __future__ import absolute_import

import sys
import os.path

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

# Run tests against sqlite for simplicity
import os
os.environ.setdefault('DB', 'sqlite')

pytest_plugins = [
    'sentry.utils.pytest'
]
