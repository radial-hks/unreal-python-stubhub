## GeometryScriptRepackUVsOptions Objects

```python
class GeometryScriptRepackUVsOptions(StructBase)
```

Geometry Script Repack UVs Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshUVFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``optimize_island_rotation`` (bool):  [Read-Write]
- ``target_image_width`` (int32):  [Read-Write]

<a id="unreal.GeometryScriptRepackUVsOptions.__init__"></a>

#### __init__

```python
def __init__(target_image_width: int = 0,
             optimize_island_rotation: bool = False) -> None
```

<a id="unreal.GeometryScriptRepackUVsOptions.target_image_width"></a>

#### target_image_width

```python
@property
def target_image_width() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptRepackUVsOptions.target_image_width"></a>

#### target_image_width

```python
@target_image_width.setter
def target_image_width(value: int) -> None
```

<a id="unreal.GeometryScriptRepackUVsOptions.optimize_island_rotation"></a>

#### optimize_island_rotation

```python
@property
def optimize_island_rotation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptRepackUVsOptions.optimize_island_rotation"></a>

#### optimize_island_rotation

```python
@optimize_island_rotation.setter
def optimize_island_rotation(value: bool) -> None
```

<a id="unreal.GeometryScriptLayoutUVsOptions"></a>