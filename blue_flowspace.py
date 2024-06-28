import os

commands = [
    # Acc-S5
    "fvctl -n add-flowspace blue1 0200000000000005 2 in_port=3,nw_src=10.0.0.9,nw_dst=10.0.0.10 blue=7",
    "fvctl -n add-flowspace blue2 0200000000000005 2 in_port=3,nw_src=10.0.0.9,nw_dst=10.0.0.11 blue=7",
    "fvctl -n add-flowspace blue3 0200000000000005 2 in_port=3,nw_src=10.0.0.9,nw_dst=10.0.0.12 blue=7",
    "fvctl -n add-flowspace blue4 0200000000000005 2 in_port=4,nw_src=10.0.0.10,nw_dst=10.0.0.9 blue=7",
    "fvctl -n add-flowspace blue5 0200000000000005 2 in_port=4,nw_src=10.0.0.10,nw_dst=10.0.0.11 blue=7",
    "fvctl -n add-flowspace blue6 0200000000000005 2 in_port=4,nw_src=10.0.0.10,nw_dst=10.0.0.12 blue=7",
    "fvctl -n add-flowspace blue7 0200000000000005 2 in_port=1,nw_src=10.0.0.11,nw_dst=10.0.0.9 blue=7",
    "fvctl -n add-flowspace blue8 0200000000000005 2 in_port=1,nw_src=10.0.0.11,nw_dst=10.0.0.10 blue=7",
    "fvctl -n add-flowspace blue9 0200000000000005 2 in_port=1,nw_src=10.0.0.12,nw_dst=10.0.0.9 blue=7",
    "fvctl -n add-flowspace blue10 0200000000000005 2 in_port=1,nw_src=10.0.0.12,nw_dst=10.0.0.10 blue=7",

    # Agg-S5
    "fvctl -n add-flowspace blue11 0100000000000005 2 in_port=3,nw_src=10.0.0.9,nw_dst=10.0.0.11 blue=7",
    "fvctl -n add-flowspace blue12 0100000000000005 2 in_port=3,nw_src=10.0.0.9,nw_dst=10.0.0.12 blue=7",
    "fvctl -n add-flowspace blue13 0100000000000005 2 in_port=3,nw_src=10.0.0.10,nw_dst=10.0.0.11 blue=7",
    "fvctl -n add-flowspace blue14 0100000000000005 2 in_port=3,nw_src=10.0.0.10,nw_dst=10.0.0.12 blue=7",
    "fvctl -n add-flowspace blue15 0100000000000005 2 in_port=4,nw_src=10.0.0.11,nw_dst=10.0.0.9 blue=7",
    "fvctl -n add-flowspace blue16 0100000000000005 2 in_port=4,nw_src=10.0.0.11,nw_dst=10.0.0.10 blue=7",
    "fvctl -n add-flowspace blue17 0100000000000005 2 in_port=4,nw_src=10.0.0.12,nw_dst=10.0.0.9 blue=7",
    "fvctl -n add-flowspace blue18 0100000000000005 2 in_port=4,nw_src=10.0.0.12,nw_dst=10.0.0.10 blue=7",

    # Acc-S6
    "fvctl -n add-flowspace blue6_1 0200000000000006 2 in_port=1,nw_src=10.0.0.9,nw_dst=10.0.0.11 blue=7",
    "fvctl -n add-flowspace blue6_2 0200000000000006 2 in_port=1,nw_src=10.0.0.9,nw_dst=10.0.0.12 blue=7",
    "fvctl -n add-flowspace blue6_3 0200000000000006 2 in_port=1,nw_src=10.0.0.10,nw_dst=10.0.0.11 blue=7",
    "fvctl -n add-flowspace blue6_4 0200000000000006 2 in_port=1,nw_src=10.0.0.10,nw_dst=10.0.0.12 blue=7",
    "fvctl -n add-flowspace blue7_1 0200000000000006 2 in_port=3,nw_src=10.0.0.11,nw_dst=10.0.0.9 blue=7",
    "fvctl -n add-flowspace blue7_2 0200000000000006 2 in_port=3,nw_src=10.0.0.11,nw_dst=10.0.0.10 blue=7",
    "fvctl -n add-flowspace blue7_3 0200000000000006 2 in_port=3,nw_src=10.0.0.11,nw_dst=10.0.0.12 blue=7",
    "fvctl -n add-flowspace blue8_1 0200000000000006 2 in_port=4,nw_src=10.0.0.12,nw_dst=10.0.0.9 blue=7",
    "fvctl -n add-flowspace blue8_2 0200000000000006 2 in_port=4,nw_src=10.0.0.12,nw_dst=10.0.0.10 blue=7",
    "fvctl -n add-flowspace blue8_3 0200000000000006 2 in_port=4,nw_src=10.0.0.12,nw_dst=10.0.0.11 blue=7"
]

for command in commands:
    os.system(command)
