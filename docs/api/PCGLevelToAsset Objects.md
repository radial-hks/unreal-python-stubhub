## PCGLevelToAsset Objects

```python
class PCGLevelToAsset(PCGAssetExporter)
```

PCGLevel to Asset

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCGEditor
- **File**: PCGLevelToAsset.h

<a id="unreal.PCGLevelToAsset.set_world"></a>

#### set_world

```python
def set_world(world: World) -> None
```

x.set_world(world) -> None
Set World

Args:
    world (World):

<a id="unreal.PCGLevelToAsset.get_world"></a>

#### get_world

```python
def get_world() -> World
```

x.get_world() -> World
Get World

Returns:
    World:

<a id="unreal.PCGLevelToAsset.bp_export_world"></a>

#### bp_export_world

```python
def bp_export_world(world: World, package_name: str,
                    asset: PCGDataAsset) -> bool
```

x.bp_export_world(world, package_name, asset) -> bool
Parses the world and fills in the provided data asset. Implement this in BP to drive the generation in a custom manner.

Args:
    world (World): 
    package_name (str): 
    asset (PCGDataAsset): 

Returns:
    bool:

<a id="unreal.TraceUtilLibrary"></a>