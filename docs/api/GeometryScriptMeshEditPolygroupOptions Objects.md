## GeometryScriptMeshEditPolygroupOptions Objects

```python
class GeometryScriptMeshEditPolygroupOptions(StructBase)
```

Geometry Script Mesh Edit Polygroup Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshModelingFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``constant_group`` (int32):  [Read-Write]
- ``group_mode`` (GeometryScriptMeshEditPolygroupMode):  [Read-Write]

<a id="unreal.GeometryScriptMeshEditPolygroupOptions.__init__"></a>

#### __init__

```python
def __init__(
        group_mode:
    GeometryScriptMeshEditPolygroupMode = GeometryScriptMeshEditPolygroupMode.
    PRESERVE_EXISTING,
        constant_group: int = 0) -> None
```

<a id="unreal.GeometryScriptMeshEditPolygroupOptions.group_mode"></a>

#### group_mode

```python
@property
def group_mode() -> GeometryScriptMeshEditPolygroupMode
```

(GeometryScriptMeshEditPolygroupMode):  [Read-Write]

<a id="unreal.GeometryScriptMeshEditPolygroupOptions.group_mode"></a>

#### group_mode

```python
@group_mode.setter
def group_mode(value: GeometryScriptMeshEditPolygroupMode) -> None
```

<a id="unreal.GeometryScriptMeshEditPolygroupOptions.constant_group"></a>

#### constant_group

```python
@property
def constant_group() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptMeshEditPolygroupOptions.constant_group"></a>

#### constant_group

```python
@constant_group.setter
def constant_group(value: int) -> None
```

<a id="unreal.GeometryScriptMeshOffsetOptions"></a>