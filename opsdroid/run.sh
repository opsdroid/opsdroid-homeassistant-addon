#!/usr/bin/with-contenv bashio

# Create opsdroid config directory
mkdir -p /config/opsdroid > /dev/null 2>&1

# Create example skill
if [ ! -d "/config/opsdroid/skills" ] 
then
    # Create opsdroid skills directory
    mkdir -p /config/opsdroid/skills > /dev/null 2>&1
    # Copy example skill
    cp -R /usr/local/src/example_skill /config/opsdroid/skills/example_skill
fi

# Start opsdroid
opsdroid start -f /data/options.json