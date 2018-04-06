# bpy_lambda
🎥 A compiled binary of Blender-as-a-Python-Module (bpy) for use in AWS Lambda

[![PyPI version](https://badge.fury.io/py/bpy_lambda.svg)](https://badge.fury.io/py/bpy_lambda)

## Installation

```sh
pip install bpy_lambda
```

Works great with [Zappa](https://github.com/Miserlou/Zappa/)!

## Usage

`bpy_lambda` is a simple wrapper around the `bpy`. You can read more about `bpy` usage in the [Blender Documentation](https://docs.blender.org/api/current/).

```python
from bpy_lambda import bpy

# bpy can be used normally!
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
cube = bpy.context.scene.objects.active
cube.scale = (1, 2, 3)
bpy.ops.export_scene.obj(filepath='my_model.obj')
```

`bpy_lambda` will only work in a Lambda environment (perhaps some linux distros as well, if you have a similar set of library versions to AWS Lambda).

For local development, it will be useful to install `bpy` normally with the [instructions](https://wiki.blender.org/index.php/User:Ideasman42/BlenderAsPyModule) on the Blender website. (Unfortunately, this requires building from source).

With a local version of `bpy` installed, you can use this code to switch seamlessly between your local environment and Lambda: 

```python
try:
    import bpy
except ImportError:
    from bpy_lambda import bpy
```


## Contribution / Building from Source

The Dockerfile is the easiest way to create a version of `bpy` that works on Lambda. Building this docker image will download the necessary libraries and compile a minimal version of Blender that works in a Lambda environment.

For easy installation / local setup, run `./build.sh`. This will create a directory called `bpy_lambda` that contains all the necessary package files.

Running `./test.sh` will spin up a test Lambda invocation (using the excellent [lambci/docker-lambda](https://github.com/lambci/docker-lambda)). Any import or dependency errors should be caught by this test.
