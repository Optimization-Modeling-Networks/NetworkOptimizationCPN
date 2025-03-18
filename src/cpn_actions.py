import math

from utils import log_state, PacketType
from cpn_config import cpn, MultiSet
from random import randint, random


def set_initial_marking():
    cpn.place('Created_File').tokens = MultiSet([(1, 'media'), (2, 'non-media')])  # Example files
    log_state("Initial State:")


def create_packets():
    for sub in cpn.transition('Break_Down_File').modes():
        cpn.transition('Break_Down_File').fire(sub)
    log_state("After Packet Creation:")


def select_router(routers):
    def distribute_modes(router_list, probability):
        remaining_modes = []
        for router in router_list:
            transition = f'Select_Router_{router[0]}'
            remaining_modes.append(cpn.transition(transition).modes())
        first_router_modes = remaining_modes[0]
        first_router_enabled = min(len(first_router_modes), math.ceil(len(first_router_modes) * probability))
        for sub in first_router_modes[:first_router_enabled]:
            cpn.transition(f'Select_Router_{router_list[0]}').fire(sub)
        remaining_substitutions = sum(len(modes) for modes in remaining_modes) - first_router_enabled
        remaining_routers = router_list[1:]
        for router, modes in zip(remaining_routers, remaining_modes[1:]):
            router_enabled = min(len(modes), math.ceil(remaining_substitutions / len(remaining_routers)))
            for sub in modes[:router_enabled]:
                cpn.transition(f'Select_Router_{router[0]}').fire(sub)
            remaining_substitutions -= router_enabled
            remaining_routers = remaining_routers[1:]

    tcp_probability = random()
    udp_probability = random()
    tcp_routers = [r for r in routers if r[1] == PacketType.TCP]
    udp_routers = [r for r in routers if r[1] == PacketType.UDP]
    distribute_modes(tcp_routers, tcp_probability)
    distribute_modes(udp_routers, udp_probability)

    # for router in routers:
    #     transition = f'Select_Router_{router[0]}'
    #     modes = cpn.transition(transition).modes()
    #     if router[1] == PacketType.TCP:
    #         enabled_modes = math.ceil(
    #             len(modes) * tcp_probability)
    #     else:
    #         enabled_modes = math.ceil(
    #             len(modes) * udp_probability)
    #     for sub in modes[:min(len(modes), enabled_modes)]:
    #         cpn.transition(transition).fire(sub)
    log_state("After Router Selection:")


def transmit_packets(routers):
    for router in routers:
        transition = f'Router_{router[0]}_Packet_Transmit'
        for sub in cpn.transition(transition).modes():
            cpn.transition(transition).fire(sub)
    log_state("After packet transmission:")


def route_selection(routes):
    top_routes = routes
    log_state("After route selection:")
    return top_routes


def congestion_control(first_tcp_route, second_tcp_route):
    log_state("After congestion control:")


def route_packets(first_tcp_route, second_tcp_route, udp_route):
    log_state("After packets routing:")


def check_packets_in_destination():
    log_state("After packet check in destination:")


def reconstruct_file():
    log_state("After file reconstruction")
