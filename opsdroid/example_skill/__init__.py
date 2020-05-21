from opsdroid_homeassistant import HassSkill, match_sunrise, match_sunset


class SunriseSkill(HassSkill):

    @match_sunset
    async def lights_on_at_sunset(self, event):
        """This is an example automation for turning on an outside light at sunset.

        To enable this automation uncomment the line below and update the entity ID to
        match your outside light.

        Alternatively you can write your own automations. Opsdroid uses decorators to
        specify triggers like ``match_sunset`` in this example. You can then call functions
        like ``self.turn_on``, ``self.turn_off`` and ``self.notify`` to interact with
        Home Assistant.

        You can also create your own opsdroid skills. Just be sure to add it to your addon
        config in the Home Assistant Supervisor.

        Note that opsdroid uses asyncio so all function calls need to start with ``await``.

        For more examples and a full reference see https://home-assistant.opsdroid.dev.
        """

        # await self.turn_on("light.outside")