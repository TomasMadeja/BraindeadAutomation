from typing import Protocol

from ..artifacts.artifact_collection import ArtifactCollection

class Step(Protocol):

    def run(self) -> None:
        return

    def artifacts(self) -> ArtifactCollection:
        return

    def cleanup(self) -> None:
        return
