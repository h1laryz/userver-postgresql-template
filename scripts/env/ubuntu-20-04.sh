#!/bin/bash

BASEDIR=$(dirname $(readlink -f "$0"))

echo "============= Initing userver submodule ============="
cd $BASEDIR/../
git submodule update --init --recursive


echo "============= Installing userver dependecies ============="
sudo apt install $(cat $BASEDIR/../../third_party/userver/scripts/docs/en/deps/ubuntu-20.04.md | tr '\n' ' ')

echo "============= Installing project dependecies ============="
pip install pyyaml ruamel.yaml argparse

echo "============= Installing functional testing dependecies ============="
pip install -r $BASEDIR/../tests/requirements.txt

