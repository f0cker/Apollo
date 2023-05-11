from mythic_container.MythicCommandBase import *
import json


class SleepArguments(TaskArguments):

    def __init__(self, command_line, **kwargs):
        super().__init__(command_line, **kwargs)
        self.args = []

    async def parse_arguments(self):
        if len(self.command_line) == 0:
            raise Exception("sleep requires an integer value (in seconds) to be passed on the command line to update the sleep value to.")
        parts = self.command_line.split(" ", maxsplit=1)
        try:
            int(parts[0])
        except:
            raise Exception("sleep requires an integer value (in seconds) to be passed on the command line to update the sleep value to.")
        if len(parts) == 2:
            try:
                int(parts[1])
            except:
                raise Exception("sleep requires an integer value for jitter, but received: {}".format(parts[1]))
        pass


class SleepCommand(CommandBase):
    cmd = "sleep"
    needs_admin = False
    help_cmd = "sleep [seconds] [jitter]"
    description = "Change the implant's sleep interval."
    version = 2
    author = "@djhohnstein"
    argument_class = SleepArguments
    attackmapping = ["T1029"]

    async def create_go_tasking(self, taskData: PTTaskMessageAllData) -> PTTaskCreateTaskingMessageResponse:
        response = PTTaskCreateTaskingMessageResponse(
            TaskID=taskData.Task.ID,
            Success=True,
        )
        return response

    async def process_response(self, task: PTTaskMessageAllData, response: any) -> PTTaskProcessResponseMessageResponse:
        resp = PTTaskProcessResponseMessageResponse(TaskID=task.Task.ID, Success=True)
        return resp