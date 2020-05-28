from symbot.chat.message import Message
from symbot.control.commands._base_command import BaseCommand
from symbot.control.control import Control


class Command(BaseCommand):

    def __init__(self, control: Control):
        self.control = control
        self.name = 'hey'
        self.author = 'fd_symbicort'
        self.permission_level = 3
        self.cooldown = 1

    @property
    def control(self) -> Control:
        return self._control

    @control.setter
    def control(self, value):
        self._control = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def permission_level(self) -> int:
        return self._permission_level

    @permission_level.setter
    def permission_level(self, value):
        self._permission_level = value

    @property
    def cooldown(self) -> float:
        return self._cooldown

    @cooldown.setter
    def cooldown(self, value):
        self._cooldown = value

    async def run(self, msg: Message):
        response = f'Hey there, {msg.user} HeyGuys'
        await self.control.respond(response)
