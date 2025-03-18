from cpn_actions import set_initial_marking, create_packets, select_router, transmit_packets, route_selection, \
    congestion_control, route_packets, check_packets_in_destination, reconstruct_file
from clock import Clock
from utils import PacketType


def get_solver_results():
    return []


def start_simulation(simulation_clock):
    routers = [('A', PacketType.TCP), ('B', PacketType.TCP), ('C', PacketType.UDP), ('D', PacketType.UDP)]
    # Simulation
    set_initial_marking()
    print(simulation_clock)
    create_packets()
    select_router(routers)
    while simulation_clock.hasTime():
        print(simulation_clock)
        transmit_packets(routers)
        # routes = get_solver_results()
        # first_tcp_route, second_tcp_route, udp_route = route_selection(routes)
        # congestion_control(first_tcp_route, second_tcp_route)
        # route_packets(first_tcp_route, second_tcp_route, udp_route)
        # check_packets_in_destination()
        # reconstruct_file()
        # get_metrics()
        simulation_clock.increment()
    else:
        print('\nClock run out', end='\n')


if __name__ == '__main__':
    start_simulation(Clock(2))
