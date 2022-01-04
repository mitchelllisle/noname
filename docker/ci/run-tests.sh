#!/usr/bin/env sh
set -e

cd /source
make install-tests
make install
make test
