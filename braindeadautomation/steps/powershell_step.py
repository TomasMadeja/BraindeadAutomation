import subprocess, sys

from ..artifacts.artifact_collection import ArtifactCollection


class PowerShellStep:


    def __init__(
        self, *,
        command: str,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.command = command
        self.output = None


    def run(self) -> None:
        self.output = subprocess.run(
            ["powershell.exe", self.command], 
            capture_output=True
        )


    def artifacts(self) -> ArtifactCollection:
        return


    def logs(self):
        return


    def cleanup(self) -> None:
        return
