commands = [
    # Acc-S2
    "fvctl -n add-flowspace purp1 0200000000000002 1 in_port=1,nw_src=10.0.0.5 nw_src=10.0.0.6 nw_dst=10.0.0.3 nw_dst=10.0.0.4 purple=7",
    "fvctl -n add-flowspace purp2 0200000000000002 1 in_port=3,nw_src=10.0.0.3 nw_dst=10.0.0.4 nw_dst=10.0.0.5 nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp3 0200000000000002 1 in_port=4,nw_src=10.0.0.4 nw_dst=10.0.0.3 nw_dst=10.0.0.5 nw_dst=10.0.0.6 purple=7",

    # Agg-S1
    "fvctl -n add-flowspace purp4 0100000000000001 1 in_port=1,nw_src=10.0.0.5 nw_src=10.0.0.6 nw_dst=10.0.0.3 nw_dst=10.0.0.4 purple=7",
    "fvctl -n add-flowspace purp5 0100000000000001 1 in_port=4,nw_src=10.0.0.3 nw_src=10.0.0.4 nw_dst=10.0.0.5 nw_dst=10.0.0.6 purple=7",

    # Core-S1
    "fvctl -n add-flowspace purp6 0000000000000001 1 in_port=1,nw_src=10.0.0.3 nw_src=10.0.0.4 nw_dst=10.0.0.5 nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp7 0000000000000001 1 in_port=2,nw_src=10.0.0.5 nw_src=10.0.0.6 nw_dst=10.0.0.3 nw_dst=10.0.0.4 purple=7",

    # Agg-S3
    "fvctl -n add-flowspace purp8 0100000000000003 1 in_port=1,nw_src=10.0.0.3 nw_src=10.0.0.4 nw_dst=10.0.0.5 nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp9 0100000000000003 1 in_port=3,nw_src=10.0.0.5 nw_src=10.0.0.6 nw_dst=10.0.0.3 nw_dst=10.0.0.4 purple=7",

    # Acc-S3
    "fvctl -n add-flowspace purp10 0200000000000003 1 in_port=1,nw_src=10.0.0.3 nw_src=10.0.0.4 nw_dst=10.0.0.5 nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp11 0200000000000003 1 in_port=3,nw_src=10.0.0.5 nw_dst=10.0.0.3 nw_dst=10.0.0.4 nw_dst=10.0.0.6 purple=7",
    "fvctl -n add-flowspace purp12 0200000000000003 1 in_port=4,nw_src=10.0.0.6 nw_dst=10.0.0.3 nw_dst=10.0.0.4 nw_dst=10.0.0.5 purple=7"
]

for cmd in commands:
    os.system(cmd)
