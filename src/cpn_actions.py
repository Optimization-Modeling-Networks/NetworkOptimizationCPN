from math import ceil

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
        all_modes_size = len(cpn.transition(f'Select_Router_{router_list[0][0]}').modes())
        for router in router_list:
            transition = f'Select_Router_{router[0]}'
            modes = cpn.transition(transition).modes()
            enabled_index = all_modes_size * probability
            enabled_modes = modes[:min(len(modes), ceil(enabled_index))]
            for sub in enabled_modes:
                cpn.transition(transition).fire(sub)

    tcp_routers = [r for r in routers if r[1] == PacketType.TCP]
    udp_routers = [r for r in routers if r[1] == PacketType.UDP]
    tcp_probability = 1 / len(tcp_routers)
    udp_probability = 1 / len(udp_routers)
    distribute_modes(tcp_routers, tcp_probability)
    distribute_modes(udp_routers, udp_probability)

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
