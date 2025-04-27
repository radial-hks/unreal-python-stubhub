## GeometryCollectionAutoInstanceMesh Objects

```python
class GeometryCollectionAutoInstanceMesh(StructBase)
```

Geometry Collection Auto Instance Mesh

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: GeometryCollectionObject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_data`` (Array[float]):  [Read-Only]
- ``materials`` (Array[MaterialInterface]):  [Read-Write]
- ``mesh`` (StaticMesh):  [Read-Write]
- ``num_instances`` (int32):  [Read-Only]
- ``static_mesh`` (SoftObjectPath):  [Read-Write]
  deprecated: Use Mesh instead.

<a id="unreal.GeometryCollectionAutoInstanceMesh.__init__"></a>

#### __init__

```python
def __init__(mesh: StaticMesh = None,
             materials: Array[MaterialInterface] = []) -> None
```

<a id="unreal.GeometryCollectionAutoInstanceMesh.static_mesh"></a>

#### static_mesh

```python
@property
def static_mesh() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write]
deprecated: Use Mesh instead.

<a id="unreal.GeometryCollectionAutoInstanceMesh.static_mesh"></a>

#### static_mesh

```python
@static_mesh.setter
def static_mesh(value: SoftObjectPath) -> None
```

<a id="unreal.GeometryCollectionAutoInstanceMesh.mesh"></a>

#### mesh

```python
@property
def mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write]

<a id="unreal.GeometryCollectionAutoInstanceMesh.mesh"></a>

#### mesh

```python
@mesh.setter
def mesh(value: StaticMesh) -> None
```

<a id="unreal.GeometryCollectionAutoInstanceMesh.materials"></a>

#### materials

```python
@property
def materials() -> Array[MaterialInterface]
```

(Array[MaterialInterface]):  [Read-Write]

<a id="unreal.GeometryCollectionAutoInstanceMesh.materials"></a>

#### materials

```python
@materials.setter
def materials(value: Array[MaterialInterface]) -> None
```

<a id="unreal.GeometryCollectionEmbeddedExemplar"></a>