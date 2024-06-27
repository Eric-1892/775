import os

commands = [
    # Acc-S2
    "fvctl -n add-flowspace purp1 0200000000000002 1 in_port=1,nw_src=10.0.0.5,nw_dst=10.0.0.3 purple=7",
    "fvctl -n add-flowspace purp2 0200000000000002 1 in_port=1,nw_src=10.0.0.5,nw_dst=10.0.0.4 purple=7",
    "fvctl -n add-flowspace purp3 0200000000000002 1 in_port=1,nw_src=10.0.0.6,nw_dst=10.0.0.3 purple=7",
    "fvctl -n add-flowspace purp4 0200000000000002 1 in_port=1,nw_src=10.0.0.6,nw_dst=10.0.0.4 purple=7",
    "fvctl -n add-flowspace purp5 0200000000000002 1 in_port=3,nw_src=10.0.0.3,nw_dst=10.0.0.4 purple=7",
    "fvctl -n add-flowspace purp6 0200000000000002 1 in_port=3,nw_src=10.0.0.3,nw_dst=10.0.0.5 purple=7",
    "fvctl -n add-flowspace purp7 0200000000000002 1 in_port=3,nw_src=10.0.0.3,nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp8 0200000000000002 1 in_port=4,nw_src=10.0.0.4,nw_dst=10.0.0.3 purple=7",
    "fvctl -n add-flowspace purp9 0200000000000002 1 in_port=4,nw_src=10.0.0.4,nw_dst=10.0.0.5 purple=7",
    "fvctl -n add-flowspace purp10 0200000000000002 1 in_port=4,nw_src=10.0.0.4,nw_dst=10.0.0.6 purple=7",

    # Agg-S1
    "fvctl -n add-flowspace purp11 0100000000000001 1 in_port=1,nw_src=10.0.0.5,nw_dst=10.0.0.3 purple=7",
    "fvctl -n add-flowspace purp12 0100000000000001 1 in_port=1,nw_src=10.0.0.5,nw_dst=10.0.0.4 purple=7",
    "fvctl -n add-flowspace purp13 0100000000000001 1 in_port=1,nw_src=10.0.0.6,nw_dst=10.0.0.3 purple=7",
    "fvctl -n add-flowspace purp14 0100000000000001 1 in_port=1,nw_src=10.0.0.6,nw_dst=10.0.0.4 purple=7",
    "fvctl -n add-flowspace purp15 0100000000000001 1 in_port=4,nw_src=10.0.0.3,nw_dst=10.0.0.5 purple=7",
    "fvctl -n add-flowspace purp16 0100000000000001 1 in_port=4,nw_src=10.0.0.3,nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp17 0100000000000001 1 in_port=4,nw_src=10.0.0.4,nw_dst=10.0.0.5 purple=7",
    "fvctl -n add-flowspace purp18 0100000000000001 1 in_port=4,nw_src=10.0.0.4,nw_dst=10.0.0.6 purple=7",

    # Core-S1
    "fvctl -n add-flowspace purp19 0000000000000001 1 in_port=1,nw_src=10.0.0.3,nw_dst=10.0.0.5 purple=7",
    "fvctl -n add-flowspace purp20 0000000000000001 1 in_port=1,nw_src=10.0.0.3,nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp21 0000000000000001 1 in_port=1,nw_src=10.0.0.4,nw_dst=10.0.0.5 purple=7",
    "fvctl -n add-flowspace purp22 0000000000000001 1 in_port=1,nw_src=10.0.0.4,nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp23 0000000000000001 1 in_port=2,nw_src=10.0.0.5,nw_dst=10.0.0.3 purple=7",
    "fvctl -n add-flowspace purp24 0000000000000001 1 in_port=2,nw_src=10.0.0.5,nw_dst=10.0.0.4 purple=7",
    "fvctl -n add-flowspace purp25 0000000000000001 1 in_port=2,nw_src=10.0.0.6,nw_dst=10.0.0.3 purple=7",
    "fvctl -n add-flowspace purp26 0000000000000001 1 in_port=2,nw_src=10.0.0.6,nw_dst=10.0.0.4 purple=7",

    # Agg-S3
    "fvctl -n add-flowspace purp27 0100000000000003 1 in_port=1,nw_src=10.0.0.3,nw_dst=10.0.0.5 purple=7",
    "fvctl -n add-flowspace purp28 0100000000000003 1 in_port=1,nw_src=10.0.0.3,nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp29 0100000000000003 1 in_port=1,nw_src=10.0.0.4,nw_dst=10.0.0.5 purple=7",
    "fvctl -n add-flowspace purp30 0100000000000003 1 in_port=1,nw_src=10.0.0.4,nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp31 0100000000000003 1 in_port=3,nw_src=10.0.0.5,nw_dst=10.0.0.3 purple=7",
    "fvctl -n add-flowspace purp32 0100000000000003 1 in_port=3,nw_src=10.0.0.5,nw_dst=10.0.0.4 purple=7",
    "fvctl -n add-flowspace purp33 0100000000000003 1 in_port=3,nw_src=10.0.0.6,nw_dst=10.0.0.3 purple=7",
    "fvctl -n add-flowspace purp34 0100000000000003 1 in_port=3,nw_src=10.0.0.6,nw_dst=10.0.0.4 purple=7",

    # Acc-S3
    "fvctl -n add-flowspace purp35 0200000000000003 1 in_port=1,nw_src=10.0.0.3,nw_dst=10.0.0.5 purple=7",
    "fvctl -n add-flowspace purp36 0200000000000003 1 in_port=1,nw_src=10.0.0.3,nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp37 0200000000000003 1 in_port=1,nw_src=10.0.0.4,nw_dst=10.0.0.5 purple=7",
    "fvctl -n add-flowspace purp38 0200000000000003 1 in_port=1,nw_src=10.0.0.4,nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp39 0200000000000003 1 in_port=3,nw_src=10.0.0.5,nw_dst=10.0.0.3 purple=7",
    "fvctl -n add-flowspace purp40 0200000000000003 1 in_port=3,nw_src=10.0.0.5,nw_dst=10.0.0.4 purple=7",
    "fvctl -n add-flowspace purp41 0200000000000003 1 in_port=3,nw_src=10.0.0.5,nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp42 0200000000000003 1 in_port=4,nw_src=10.0.0.6,nw_dst=10.0.0.3 purple=7",
    "fvctl -n add-flowspace purp43 0200000000000003 1 in_port=4,nw_src=10.0.0.6,nw_dst=10.0.0.4 purple=7",
    "fvctl -n add-flowspace purp44 0200000000000003 1 in_port=4,nw_src=10.0.0.6,nw_dst=10.0.0.5 purple=7"
]

for cmd in commands:
    os.system(cmd)
