#!/usr/bin/env python3

import os
import sys
import argparse
from anytree import Node, RenderTree


def walk(path, depth):
    '''
    https://stackoverflow.com/questions/7159607/list-directories-with-a-specified-depth-in-python
    '''
    depth -= 1
    with os.scandir(path) as p:
        for entry in p:
            yield entry.path
            if entry.is_dir() and depth > 0:
                yield from walk(entry.path, depth)


def distus(args):
    pass


def main():
    parser = argparse.ArgumentParser(description="distk")
    parser.add_argument("--dir", help="scan directory")
    parser.add_argument("--depth", type=int, default=3,
                        help="max dir depth, default: 4")

    args = parser.parse_args()

    root = Node(args.dir)
    for i in walk(args.dir, args.depth):
        dirs = i.split("/")
        if len(dirs) > 0:
            Node(dirs[0], parent=root)


if __name__ == "__main__":
    main()
