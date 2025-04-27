## GeometryScriptPolygroupSimplifyOptions Objects

```python
class GeometryScriptPolygroupSimplifyOptions(StructBase)
```

Geometry Script Polygroup Simplify Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSimplifyFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle_threshold`` (float):  [Read-Write]
- ``auto_compact`` (bool):  [Read-Write] If enabled, the simplified mesh is automatically compacted to remove gaps in the index space. This is expensive and can be disabled by advanced users.

<a id="unreal.GeometryScriptPolygroupSimplifyOptions.__init__"></a>

#### __init__

```python
def __init__(angle_threshold: float = 0.000000,
             auto_compact: bool = False) -> None
```

<a id="unreal.GeometryScriptPolygroupSimplifyOptions.angle_threshold"></a>

#### angle_threshold

```python
@property
def angle_threshold() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptPolygroupSimplifyOptions.angle_threshold"></a>

#### angle_threshold

```python
@angle_threshold.setter
def angle_threshold(value: float) -> None
```

<a id="unreal.GeometryScriptPolygroupSimplifyOptions.auto_compact"></a>

#### auto_compact

```python
@property
def auto_compact() -> bool
```

(bool):  [Read-Write] If enabled, the simplified mesh is automatically compacted to remove gaps in the index space. This is expensive and can be disabled by advanced users.

<a id="unreal.GeometryScriptPolygroupSimplifyOptions.auto_compact"></a>

#### auto_compact

```python
@auto_compact.setter
def auto_compact(value: bool) -> None
```

<a id="unreal.GeometryScriptSimplifyMeshOptions"></a>