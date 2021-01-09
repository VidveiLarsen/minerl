import abc
from abc import ABC

import minerl

from minerl.herobraine.hero import handlers
from minerl.herobraine.hero.mc import INVERSE_KEYMAP
from minerl.herobraine.env_spec import EnvSpec

from typing import List
from enum import Enum

class Resolution(Enum):
    """[Resolution constants]

    Args:
        Enum ([LOW]): [64 x 64 resolution]
        Enum ([HIGH]):[128 height, 256 width] 
    """
    LOW = 1
    HIGH = 2

class SimpleEnvSpec(EnvSpec, ABC):
    """
    A simple base environment from which all othe simple envs inherit.
    """
    STANDARD_KEYBOARD_ACTIONS = [
        "forward",
        "back",
        "left",
        "right",
        "jump",
        "sneak",
        "sprint",
        "attack"
    ]

    def __init__(self, name, xml, resolution: Resolution = Resolution.LOW, *args, **kwargs):
        if resolution == Resolution.LOW:
            self.resolution = tuple((64, 64))
        elif resolution == Resolution.HIGH:
            self.resolution = tuple((128,256))    
        else:
            raise ValueError(f"Invalid resolution {resolution}. 'Resolution.LOW:' or 'Resolution.HIGH' supported, corresponding to "
                            " (64,64) and (128,256)")
        super().__init__(name, xml, *args, **kwargs)

    def create_observables(self) -> List[minerl.herobraine.hero.AgentHandler]:
        return [
            handlers.POVObservation(self.resolution)
        ]

    def create_actionables(self) -> List[minerl.herobraine.hero.AgentHandler]:
        """
        Simple envs have some basic keyboard control functionality, but
        not all.
        """
        return [
            handlers.KeyboardAction(k, v) for k,v in INVERSE_KEYMAP.items()
            if k in SimpleEnvSpec.STANDARD_KEYBOARD_ACTIONS
        ] + [
            handlers.Camera()
        ]
