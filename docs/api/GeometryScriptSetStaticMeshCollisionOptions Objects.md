## GeometryScriptSetStaticMeshCollisionOptions Objects

```python
class GeometryScriptSetStaticMeshCollisionOptions(StructBase)
```

Geometry Script Set Static Mesh Collision Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: CollisionFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``mark_as_customized`` (bool):  [Read-Write] Whether to mark the static mesh collision as customized when it is set, so that it will not be overwritten on next import.
  If false, Static Mesh collision will not be un-marked as Customized; its state will just be left unchanged.

<a id="unreal.GeometryScriptSetStaticMeshCollisionOptions.__init__"></a>

#### __init__

```python
def __init__(mark_as_customized: bool = False) -> None
```

<a id="unreal.GeometryScriptSetStaticMeshCollisionOptions.mark_as_customized"></a>

#### mark_as_customized

```python
@property
def mark_as_customized() -> bool
```

(bool):  [Read-Write] Whether to mark the static mesh collision as customized when it is set, so that it will not be overwritten on next import.
If false, Static Mesh collision will not be un-marked as Customized; its state will just be left unchanged.

<a id="unreal.GeometryScriptSetStaticMeshCollisionOptions.mark_as_customized"></a>

#### mark_as_customized

```python
@mark_as_customized.setter
def mark_as_customized(value: bool) -> None
```

<a id="unreal.ComputeNegativeSpaceOptions"></a>