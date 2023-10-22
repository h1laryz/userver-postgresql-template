#!/bin/bash

BASEDIR=$(dirname $(readlink -f "$0"))

find $BASEDIR/../ -maxdepth 1 -type d -name "*build*" -print0 | while IFS= read -r -d '' dir; do
    echo "Successfully configured static config from template into directory: $dir"
    $BASEDIR/config_from_template.py -i $BASEDIR/../configs/static_config.yaml -e $BASEDIR/../configs/config_vars.yaml -o $dir/config_dev.yaml
done


DYNAMIC_CONFIG_DIRECTORY="/usr/local/etc/userver-postgresql-template"
if [ ! -d $DYNAMIC_CONFIG_DIRECTORY ]; then
  mkdir -p $DYNAMIC_CONFIG_DIRECTORY
fi

cp $BASEDIR/../configs/dynamic_config_fallback.json $DYNAMIC_CONFIG_DIRECTORY/dynamic_config_fallback.json
echo "Successfully copied dynamic config into directory: $DYNAMIC_CONFIG_DIRECTORY"
