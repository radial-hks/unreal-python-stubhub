## GroomCreateBindingOptions Objects

```python
class GroomCreateBindingOptions(Object)
```

Groom Create Binding Options

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomCreateBindingOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``groom_binding_type`` (GroomBindingMeshType):  [Read-Write] Type of mesh to create groom binding for
- ``matching_section`` (int32):  [Read-Write] Section to pick to transfer the position
- ``num_interpolation_points`` (int32):  [Read-Write] Number of points used for the rbf interpolation
- ``source_geometry_cache`` (GeometryCache):  [Read-Write] GeometryCache on which the groom has been authored
- ``source_skeletal_mesh`` (SkeletalMesh):  [Read-Write] Skeletal mesh on which the groom has been authored. This is optional, and used only if the hair
                binding is done a different mesh than the one which it has been authored, i.e., only if the curves
                roots and the surface geometry don't aligned and need to be wrapped/transformed.
- ``target_geometry_cache`` (GeometryCache):  [Read-Write] GeometryCache on which the groom is attached to.
- ``target_skeletal_mesh`` (SkeletalMesh):  [Read-Write] Skeletal mesh on which the groom is attached to.

<a id="unreal.GroomCreateBindingOptions.groom_binding_type"></a>

#### groom_binding_type

```python
@property
def groom_binding_type() -> GroomBindingMeshType
```

(GroomBindingMeshType):  [Read-Write] Type of mesh to create groom binding for

<a id="unreal.GroomCreateBindingOptions.groom_binding_type"></a>

#### groom_binding_type

```python
@groom_binding_type.setter
def groom_binding_type(value: GroomBindingMeshType) -> None
```

<a id="unreal.GroomCreateBindingOptions.source_skeletal_mesh"></a>

#### source_skeletal_mesh

```python
@property
def source_skeletal_mesh() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Write] Skeletal mesh on which the groom has been authored. This is optional, and used only if the hair
              binding is done a different mesh than the one which it has been authored, i.e., only if the curves
              roots and the surface geometry don't aligned and need to be wrapped/transformed.

<a id="unreal.GroomCreateBindingOptions.source_skeletal_mesh"></a>

#### source_skeletal_mesh

```python
@source_skeletal_mesh.setter
def source_skeletal_mesh(value: SkeletalMesh) -> None
```

<a id="unreal.GroomCreateBindingOptions.target_skeletal_mesh"></a>

#### target_skeletal_mesh

```python
@property
def target_skeletal_mesh() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Write] Skeletal mesh on which the groom is attached to.

<a id="unreal.GroomCreateBindingOptions.target_skeletal_mesh"></a>

#### target_skeletal_mesh

```python
@target_skeletal_mesh.setter
def target_skeletal_mesh(value: SkeletalMesh) -> None
```

<a id="unreal.GroomCreateBindingOptions.source_geometry_cache"></a>

#### source_geometry_cache

```python
@property
def source_geometry_cache() -> GeometryCache
```

(GeometryCache):  [Read-Write] GeometryCache on which the groom has been authored

<a id="unreal.GroomCreateBindingOptions.source_geometry_cache"></a>

#### source_geometry_cache

```python
@source_geometry_cache.setter
def source_geometry_cache(value: GeometryCache) -> None
```

<a id="unreal.GroomCreateBindingOptions.target_geometry_cache"></a>

#### target_geometry_cache

```python
@property
def target_geometry_cache() -> GeometryCache
```

(GeometryCache):  [Read-Write] GeometryCache on which the groom is attached to.

<a id="unreal.GroomCreateBindingOptions.target_geometry_cache"></a>

#### target_geometry_cache

```python
@target_geometry_cache.setter
def target_geometry_cache(value: GeometryCache) -> None
```

<a id="unreal.GroomCreateBindingOptions.num_interpolation_points"></a>

#### num_interpolation_points

```python
@property
def num_interpolation_points() -> int
```

(int32):  [Read-Write] Number of points used for the rbf interpolation

<a id="unreal.GroomCreateBindingOptions.num_interpolation_points"></a>

#### num_interpolation_points

```python
@num_interpolation_points.setter
def num_interpolation_points(value: int) -> None
```

<a id="unreal.GroomCreateBindingOptions.matching_section"></a>

#### matching_section

```python
@property
def matching_section() -> int
```

(int32):  [Read-Write] Section to pick to transfer the position

<a id="unreal.GroomCreateBindingOptions.matching_section"></a>

#### matching_section

```python
@matching_section.setter
def matching_section(value: int) -> None
```

<a id="unreal.GroomCreateFollicleMaskOptions"></a>