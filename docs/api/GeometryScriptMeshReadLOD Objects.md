## GeometryScriptMeshReadLOD Objects

```python
class GeometryScriptMeshReadLOD(StructBase)
```

Geometry Script Mesh Read LOD

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lod_index`` (int32):  [Read-Write]
- ``lod_type`` (GeometryScriptLODType):  [Read-Write]

<a id="unreal.GeometryScriptMeshReadLOD.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        lod_type: GeometryScriptLODType = GeometryScriptLODType.MAX_AVAILABLE,
        lod_index: int = 0) -> None
```

<a id="unreal.GeometryScriptMeshReadLOD.lod_type"></a>

#### lod\_type

```python
@property
def lod_type() -> GeometryScriptLODType
```

(GeometryScriptLODType):  [Read-Write]

<a id="unreal.GeometryScriptMeshReadLOD.lod_type"></a>

#### lod\_type

```python
@lod_type.setter
def lod_type(value: GeometryScriptLODType) -> None
```

<a id="unreal.GeometryScriptMeshReadLOD.lod_index"></a>

#### lod\_index

```python
@property
def lod_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptMeshReadLOD.lod_index"></a>

#### lod\_index

```python
@lod_index.setter
def lod_index(value: int) -> None
```

<a id="unreal.GeometryScriptMeshWriteLOD"></a>