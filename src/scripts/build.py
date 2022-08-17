#region Modules

import os
import shutil

#endregion

#region Variables

targetDirectories = [
    'textures/block', 
    'textures/colormap'
]

#endregion

def Build():
    for targets in targetDirectories:
        shutil.copytree(
            f'ass/{targets}', 
            f'build/SegmentMC/assets/minecraft/{targets}', 
            symlinks=False, 
            ignore=None,
            ignore_dangling_symlinks=False,
            dirs_exist_ok=False
        )

    # Individual files
    shutil.copy('src/pack.mcmeta', 'build/SegmentMC/pack.mcmeta')

if __name__ == '__main__':
    Build()