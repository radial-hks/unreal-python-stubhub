## GeometryScriptCalculateNormalsOptions Objects

```python
class GeometryScriptCalculateNormalsOptions(StructBase)
```

Geometry Script Calculate Normals Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshNormalsFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle_weighted`` (bool):  [Read-Write]
- ``area_weighted`` (bool):  [Read-Write]

<a id="unreal.GeometryScriptCalculateNormalsOptions.__init__"></a>

#### __init__

```python
def __init__(angle_weighted: bool = False,
             area_weighted: bool = False) -> None
```

<a id="unreal.GeometryScriptCalculateNormalsOptions.angle_weighted"></a>

#### angle_weighted

```python
@property
def angle_weighted() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCalculateNormalsOptions.angle_weighted"></a>

#### angle_weighted

```python
@angle_weighted.setter
def angle_weighted(value: bool) -> None
```

<a id="unreal.GeometryScriptCalculateNormalsOptions.area_weighted"></a>

#### area_weighted

```python
@property
def area_weighted() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCalculateNormalsOptions.area_weighted"></a>

#### area_weighted

```python
@area_weighted.setter
def area_weighted(value: bool) -> None
```

<a id="unreal.GeometryScriptSplitNormalsOptions"></a>