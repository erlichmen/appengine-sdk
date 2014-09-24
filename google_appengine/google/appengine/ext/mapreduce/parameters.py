#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
"""Parameters to control Mapreduce."""


__all__ = []

DEFAULT_SHARD_RETRY_LIMIT = 3
DEFAULT_QUEUE_NAME = "default"
DEFAULT_SHARD_COUNT = 8





_RETRY_SLICE_ERROR_MAX_RETRIES = 10


_MAX_TASK_RETRIES = 30




_SLICE_DURATION_SEC = 15


_LEASE_GRACE_PERIOD = 1


_REQUEST_EVENTUAL_TIMEOUT = 10 * 60 + 30


_CONTROLLER_PERIOD_SEC = 2



_DEFAULT_PROCESSING_RATE_PER_SEC = 1000000


_DEFAULT_BASE_PATH = "/_ah/mapreduce"
_DEFAULT_PIPELINE_BASE_PATH = _DEFAULT_BASE_PATH + "/pipeline"
