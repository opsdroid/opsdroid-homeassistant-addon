# Opsdroid Home Assistant

<!-- TODO: Badges -->

[Opsdroid](https://opsdroid.dev/) is a Python automation framework with a focus on chat and natural language. Connect your bot to a range of chat services and natural language APIs and build your own automations in Python.

With the [Home Assistant plugin for Opsdroid](https://home-assistant.opsdroid.dev) your bot can repond to state changes in Home Assistant and interact with your smart home.

When installing Opsdroid as an addon for Home Assistant it will automatically be configured to connect to your Home Assistant instance. An example skill will also be created within your config directory and configured automatically.

## Configuration

The following sections explain the default configuration for the Opsdroid Home Assistant addon. For full configuration information see the Opsdroid [configuration reference](https://docs.opsdroid.dev/en/stable/configuration.html). 

## Connecting to Home Assistant

Opsdroid will automatically be configured to connect to Home Assistant. You do not need to make any changes to the Home Assistant connector configuration.

You can of course connect opsdroid to additional connectors. See the [connector documentation](https://docs.opsdroid.dev/en/stable/connectors/index.html) for more information.

## Example skill

When you first install the Opsdroid addon an example skill will be created for you. Skills in opsdroid can be single Python files, a directory containing a `__init__.py` file (like the example), a Python module or even a Jupyter Notebook.

You can find the example skill in `/config/opsdroid/skills/example_skill/`.

You can get started by modifying the example skill or by creating your own. You will need to update the configuration and restart the addon for changes or new skills to be loaded.

See the [Opsdroid Home Assistant documentation](https://home-assistant.opsdroid.dev/en/latest/examples.html) for more information on building home automation skills and the main [Opsdroid documentation](https://docs.opsdroid.dev/en/stable/skills/index.html) for information on building skills in general.

## SSL

If you are using the [Let's Encrypt addon](https://github.com/home-assistant/hassio-addons/tree/master/letsencrypt) for Home Assistant you can tell Opsdroid to also use your SSL certificate by adding the following to your configuration.

```yaml
web:
  port: 8080
  ssl:
    cert: /ssl/fullchain.pem
    key: /ssl/privkey.pem
```

## Databases

Opsdroid skills can store key/value data in an external database. By default Opsdroid will store data in a sqlite database at `/config/opsdroid/opsdroid.db`.

See the [documentation](https://docs.opsdroid.dev/en/stable/databases/index.html) for alternate database configurations.