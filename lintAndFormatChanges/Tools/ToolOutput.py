from dataclasses import dataclass


@dataclass
class ToolOutput:
    """
    This dataclass stores the information
    resulting from the output of a tool.

    Attributes:
        returnCode (int)         The return code of the tool that was ran.

        command (list[str]): The command that was used to run the tool,
                                 not including the file/code that the tool
                                 was run on.

        data (str):              Any relevant data related to the object.
                                 Typically, if returnCode is not that of a successful
                                 run, this contains the stdout of the tool that ran.
                                 Otherwise, it can contain code that has been processed
                                 by the tools.
    """

    return_code: int
    command: list[str]
    data: str
