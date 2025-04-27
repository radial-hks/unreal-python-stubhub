## GroomBindingAsset Objects

```python
class GroomBindingAsset(Object)
```

Implements an asset that can be used to store binding information between a groom and a skeletal mesh

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomBindingAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``groom`` (GroomAsset):  [Read-Write]
- ``groom_binding_type`` (GroomBindingMeshType):  [Read-Only]
- ``group_infos`` (Array[GoomBindingGroupInfo]):  [Read-Write]
- ``matching_section`` (int32):  [Read-Only]
- ``num_interpolation_points`` (int32):  [Read-Only]
- ``source_geometry_cache`` (GeometryCache):  [Read-Only]
- ``source_skeletal_mesh`` (SkeletalMesh):  [Read-Write]
- ``target_geometry_cache`` (GeometryCache):  [Read-Only]
- ``target_skeletal_mesh`` (SkeletalMesh):  [Read-Write]

<a id="unreal.GroomBindingAsset.groom_binding_type"></a>

#### groom_binding_type

```python
@property
def groom_binding_type() -> GroomBindingMeshType
```

(GroomBindingMeshType):  [Read-Only]

<a id="unreal.GroomBindingAsset.groom"></a>

#### groom

```python
@property
def groom() -> GroomAsset
```

(GroomAsset):  [Read-Write]

<a id="unreal.GroomBindingAsset.groom"></a>

#### groom

```python
@groom.setter
def groom(value: GroomAsset) -> None
```

<a id="unreal.GroomBindingAsset.source_skeletal_mesh"></a>

#### source_skeletal_mesh

```python
@property
def source_skeletal_mesh() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Write]

<a id="unreal.GroomBindingAsset.source_skeletal_mesh"></a>

#### source_skeletal_mesh

```python
@source_skeletal_mesh.setter
def source_skeletal_mesh(value: SkeletalMesh) -> None
```

<a id="unreal.GroomBindingAsset.target_skeletal_mesh"></a>

#### target_skeletal_mesh

```python
@property
def target_skeletal_mesh() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Write]

<a id="unreal.GroomBindingAsset.target_skeletal_mesh"></a>

#### target_skeletal_mesh

```python
@target_skeletal_mesh.setter
def target_skeletal_mesh(value: SkeletalMesh) -> None
```

<a id="unreal.GroomBindingAsset.source_geometry_cache"></a>

#### source_geometry_cache

```python
@property
def source_geometry_cache() -> GeometryCache
```

(GeometryCache):  [Read-Only]

<a id="unreal.GroomBindingAsset.target_geometry_cache"></a>

#### target_geometry_cache

```python
@property
def target_geometry_cache() -> GeometryCache
```

(GeometryCache):  [Read-Only]

<a id="unreal.GroomBindingAsset.num_interpolation_points"></a>

#### num_interpolation_points

```python
@property
def num_interpolation_points() -> int
```

(int32):  [Read-Only]

<a id="unreal.GroomBindingAsset.matching_section"></a>

#### matching_section

```python
@property
def matching_section() -> int
```

(int32):  [Read-Only]

<a id="unreal.GroomBindingAsset.group_infos"></a>

#### group_infos

```python
@property
def group_infos() -> Array[GoomBindingGroupInfo]
```

(Array[GoomBindingGroupInfo]):  [Read-Write]

<a id="unreal.GroomBindingAsset.group_infos"></a>

#### group_infos

```python
@group_infos.setter
def group_infos(value: Array[GoomBindingGroupInfo]) -> None
```

<a id="unreal.GroomBindingAssetList"></a>