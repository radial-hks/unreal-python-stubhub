## GeometryScriptCreateNewVolumeFromMeshOptions Objects

```python
class GeometryScriptCreateNewVolumeFromMeshOptions(StructBase)
```

Geometry Script Create New Volume from Mesh Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingEditor
- **File**: CreateNewAssetUtilityFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_simplify`` (bool):  [Read-Write]
- ``max_triangles`` (int32):  [Read-Write]
- ``volume_type`` (type(Class)):  [Read-Write]

<a id="unreal.GeometryScriptCreateNewVolumeFromMeshOptions.__init__"></a>

#### __init__

```python
def __init__(volume_type: Class = None,
             auto_simplify: bool = False,
             max_triangles: int = 0) -> None
```

<a id="unreal.GeometryScriptCreateNewVolumeFromMeshOptions.volume_type"></a>

#### volume_type

```python
@property
def volume_type() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.GeometryScriptCreateNewVolumeFromMeshOptions.volume_type"></a>

#### volume_type

```python
@volume_type.setter
def volume_type(value: Class) -> None
```

<a id="unreal.GeometryScriptCreateNewVolumeFromMeshOptions.auto_simplify"></a>

#### auto_simplify

```python
@property
def auto_simplify() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCreateNewVolumeFromMeshOptions.auto_simplify"></a>

#### auto_simplify

```python
@auto_simplify.setter
def auto_simplify(value: bool) -> None
```

<a id="unreal.GeometryScriptCreateNewVolumeFromMeshOptions.max_triangles"></a>

#### max_triangles

```python
@property
def max_triangles() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptCreateNewVolumeFromMeshOptions.max_triangles"></a>

#### max_triangles

```python
@max_triangles.setter
def max_triangles(value: int) -> None
```

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions"></a>