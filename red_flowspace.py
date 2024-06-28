import os

commands = [
    # Acc-S7
    "fvctl -n add-flowspace red1 0200000000000007 3 in_port=3,nw_src=10.0.0.13,nw_dst=10.0.0.12 red=7",
    "fvctl -n add-flowspace red2 0200000000000007 3 in_port=3,nw_src=10.0.0.13,nw_dst=10.0.0.14 red=7",
    "fvctl -n add-flowspace red3 0200000000000007 3 in_port=4,nw_src=10.0.0.14,nw_dst=10.0.0.12 red=7",
    "fvctl -n add-flowspace red4 0200000000000007 3 in_port=4,nw_src=10.0.0.14,nw_dst=10.0.0.13 red=7",
    "fvctl -n add-flowspace red5 0200000000000007 3 in_port=2,nw_src=10.0.0.12,nw_dst=10.0.0.13 red=7",
    "fvctl -n add-flowspace red6 0200000000000007 3 in_port=2,nw_src=10.0.0.12,nw_dst=10.0.0.14 red=7",

    # Agg-S8
    "fvctl -n add-flowspace red7 0100000000000008 3 in_port=3,nw_src=10.0.0.13,nw_dst=10.0.0.12 red=7",
    "fvctl -n add-flowspace red8 0100000000000008 3 in_port=3,nw_src=10.0.0.14,nw_dst=10.0.0.12 red=7",
    "fvctl -n add-flowspace red9 0100000000000008 3 in_port=2,nw_src=10.0.0.12,nw_dst=10.0.0.13 red=7",
    "fvctl -n add-flowspace red10 0100000000000008 3 in_port=2,nw_src=10.0.0.12,nw_dst=10.0.0.14 red=7",

    # Core-S4
    "fvctl -n add-flowspace red11 0000000000000004 3 in_port=4,nw_src=10.0.0.13,nw_dst=10.0.0.12 red=7",
    "fvctl -n add-flowspace red12 0000000000000004 3 in_port=4,nw_src=10.0.0.14,nw_dst=10.0.0.12 red=7",
    "fvctl -n add-flowspace red13 0000000000000004 3 in_port=3,nw_src=10.0.0.12,nw_dst=10.0.0.13 red=7",
    "fvctl -n add-flowspace red14 0000000000000004 3 in_port=3,nw_src=10.0.0.12,nw_dst=10.0.0.14 red=7",

    # Agg-S6
    "fvctl -n add-flowspace red15 0100000000000006 3 in_port=2,nw_src=10.0.0.13,nw_dst=10.0.0.12 red=7",
    "fvctl -n add-flowspace red16 0100000000000006 3 in_port=2,nw_src=10.0.0.14,nw_dst=10.0.0.12 red=7",
    "fvctl -n add-flowspace red17 0100000000000006 3 in_port=4,nw_src=10.0.0.12,nw_dst=10.0.0.13 red=7",
    "fvctl -n add-flowspace red18 0100000000000006 3 in_port=4,nw_src=10.0.0.12,nw_dst=10.0.0.14 red=7",

    # Acc-S6
    "fvctl -n add-flowspace red19 0200000000000006 3 in_port=2,nw_src=10.0.0.13,nw_dst=10.0.0.12 red=7",
    "fvctl -n add-flowspace red20 0200000000000006 3 in_port=2,nw_src=10.0.0.14,nw_dst=10.0.0.12 red=7",
    "fvctl -n add-flowspace red21 0200000000000006 3 in_port=4,nw_src=10.0.0.12,nw_dst=10.0.0.13 red=7",
    "fvctl -n add-flowspace red22 0200000000000006 3 in_port=4,nw_src=10.0.0.12,nw_dst=10.0.0.14 red=7"
]

for command in commands:
    os.system(command)
