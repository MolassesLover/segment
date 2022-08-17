#region Modules

import os
import shutil

#endregion

#region Variables

targetDirectories = [
    'ass/textures/block', 
    'ass/textures/colormap'
]

#endregion

def Build():
    for targets in targetDirectories:
        for fileName in os.listdir(targets):
            # Create a full file path.
            source = targets + fileName
            destination = f'build/{targets/fileName}'
            # Only copy files.
            if os.path.isfile(source):
                shutil.copy(source, destination)
                print(f'Copied: {fileName}')

if __name__ == '__main__':
    Build()