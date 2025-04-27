## GeometryCollectionSource Objects

```python
class GeometryCollectionSource(StructBase)
```

Geometry Collection Source

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: GeometryCollectionObject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``add_internal_materials`` (bool):  [Read-Write] (Legacy) Whether source materials will be duplicated to create new slots for internal materials, or existing odd materials will be considered internal. (For non-Geometry Collection inputs only.)
- ``instance_custom_data`` (Array[float]):  [Read-Write]
- ``local_transform`` (Transform):  [Read-Write]
- ``set_internal_from_material_index`` (bool):  [Read-Write] Whether to set the 'internal' flag for faces with odd-numbered materials slots.
- ``source_geometry_object`` (SoftObjectPath):  [Read-Write]
- ``source_material`` (Array[MaterialInterface]):  [Read-Write]
- ``split_components`` (bool):  [Read-Write] Whether individual source mesh components should be split into separate pieces of geometry based on mesh connectivity. If checked, triangles that are not topologically connected will be assigned separate bones. (For non-Geometry Collection inputs only.)

<a id="unreal.GeometryCollectionSource.__init__"></a>

#### __init__

```python
def __init__(source_geometry_object: SoftObjectPath = [""],
             local_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                           [-0.000000, 0.000000, 0.000000],
                                           [1.000000, 1.000000, 1.000000]],
             source_material: Array[MaterialInterface] = [],
             instance_custom_data: Array[float] = [],
             add_internal_materials: bool = False,
             split_components: bool = False,
             set_internal_from_material_index: bool = False) -> None
```

<a id="unreal.GeometryCollectionSource.source_geometry_object"></a>

#### source_geometry_object

```python
@property
def source_geometry_object() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write]

<a id="unreal.GeometryCollectionSource.source_geometry_object"></a>

#### source_geometry_object

```python
@source_geometry_object.setter
def source_geometry_object(value: SoftObjectPath) -> None
```

<a id="unreal.GeometryCollectionSource.local_transform"></a>

#### local_transform

```python
@property
def local_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.GeometryCollectionSource.local_transform"></a>

#### local_transform

```python
@local_transform.setter
def local_transform(value: Transform) -> None
```

<a id="unreal.GeometryCollectionSource.source_material"></a>

#### source_material

```python
@property
def source_material() -> Array[MaterialInterface]
```

(Array[MaterialInterface]):  [Read-Write]

<a id="unreal.GeometryCollectionSource.source_material"></a>

#### source_material

```python
@source_material.setter
def source_material(value: Array[MaterialInterface]) -> None
```

<a id="unreal.GeometryCollectionSource.instance_custom_data"></a>

#### instance_custom_data

```python
@property
def instance_custom_data() -> Array[float]
```

(Array[float]):  [Read-Write]

<a id="unreal.GeometryCollectionSource.instance_custom_data"></a>

#### instance_custom_data

```python
@instance_custom_data.setter
def instance_custom_data(value: Array[float]) -> None
```

<a id="unreal.GeometryCollectionSource.add_internal_materials"></a>

#### add_internal_materials

```python
@property
def add_internal_materials() -> bool
```

(bool):  [Read-Write] (Legacy) Whether source materials will be duplicated to create new slots for internal materials, or existing odd materials will be considered internal. (For non-Geometry Collection inputs only.)

<a id="unreal.GeometryCollectionSource.add_internal_materials"></a>

#### add_internal_materials

```python
@add_internal_materials.setter
def add_internal_materials(value: bool) -> None
```

<a id="unreal.GeometryCollectionSource.split_components"></a>

#### split_components

```python
@property
def split_components() -> bool
```

(bool):  [Read-Write] Whether individual source mesh components should be split into separate pieces of geometry based on mesh connectivity. If checked, triangles that are not topologically connected will be assigned separate bones. (For non-Geometry Collection inputs only.)

<a id="unreal.GeometryCollectionSource.split_components"></a>

#### split_components

```python
@split_components.setter
def split_components(value: bool) -> None
```

<a id="unreal.GeometryCollectionSource.set_internal_from_material_index"></a>

#### set_internal_from_material_index

```python
@property
def set_internal_from_material_index() -> bool
```

(bool):  [Read-Write] Whether to set the 'internal' flag for faces with odd-numbered materials slots.

<a id="unreal.GeometryCollectionSource.set_internal_from_material_index"></a>

#### set_internal_from_material_index

```python
@set_internal_from_material_index.setter
def set_internal_from_material_index(value: bool) -> None
```

<a id="unreal.GeometryCollectionAutoInstanceMesh"></a>