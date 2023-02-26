#!/bin/python3

import os
import shutil


def copy_exactly(targetDirectories: list[str]):
    print(":: Copying texture images.")

    for targets in targetDirectories:
        shutil.copytree(
            f"ass/{targets}",
            f"build/SegmentMC/assets/minecraft/{targets}",
            symlinks=False,
            ignore=None,
            ignore_dangling_symlinks=False,
            dirs_exist_ok=False,
        )

    # Individual files
    shutil.copy("src/pack.mcmeta", "build/SegmentMC/pack.mcmeta")


if __name__ == "__main__":
    copy_exactly()
