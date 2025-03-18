from enum import Enum

from cpn_config import cpn
import re


class PacketType(Enum):
    TCP = 1
    UDP = 2


def log_state(print_state):
    image_path = './images/'
    image_name = f"{image_path}{re.sub(r'[^a-zA-Z0-9 ]', '', print_state).lower().replace(' ', '_')}"
    print(print_state)
    print(cpn.get_marking(), end='\n')
    cpn.draw(f'{image_name}.png')
