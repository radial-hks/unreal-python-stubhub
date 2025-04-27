## GeometryCollectionSizeSpecificData Objects

```python
class GeometryCollectionSizeSpecificData(StructBase)
```

Geometry Collection Size Specific Data

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: GeometryCollectionObject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_object_reduction_percentage`` (int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 10)
  deprecated: Use Collision.CollisionObjectReductionPercentage instead.
- ``collision_particles_fraction`` (float):  [Read-Write] Number of particles on the triangulated surface to use for collisions.
  deprecated: Use Collision.CollisionParticlesFraction instead.
- ``collision_shapes`` (Array[GeometryCollectionCollisionTypeData]):  [Read-Write] * Collision Shapes allow kfor multiple collision types per rigid body.
- ``collision_type`` (CollisionTypeEnum):  [Read-Write] *  CollisionType defines how to initialize the rigid collision structures.
  deprecated: Use Collision.CollisionType instead.
- ``damage_threshold`` (int32):  [Read-Write] Max number of particles.
- ``implicit_type`` (ImplicitTypeEnum):  [Read-Write] *  CollisionType defines how to initialize the rigid collision structures.
  deprecated: Use Collision.ImplicitType instead.
- ``max_cluster_level_set_resolution`` (int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 10)
  deprecated: Use Collision.LevelSet.MaxClusterLevelSetResolution instead.
- ``max_level_set_resolution`` (int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 10)
  deprecated: Use Collision.LevelSet.MaxLevelSetResolution instead.
- ``max_size`` (float):  [Read-Write] The max size these settings apply to
- ``maximum_collision_particles`` (int32):  [Read-Write] Max number of particles.
  deprecated: Use Collision.MaximumCollisionParticles instead.
- ``min_cluster_level_set_resolution`` (int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 5)
  deprecated: Use Collision.LevelSet.MinClusterLevelSetResolution instead.
- ``min_level_set_resolution`` (int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 5)
  deprecated: Use Collision.LevelSet.MinLevelSetResolution instead.

<a id="unreal.GeometryCollectionSizeSpecificData.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GeometryCollectionSizeSpecificData.collision_type"></a>

#### collision_type

```python
@property
def collision_type() -> CollisionTypeEnum
```

(CollisionTypeEnum):  [Read-Write] *  CollisionType defines how to initialize the rigid collision structures.
deprecated: Use Collision.CollisionType instead.

<a id="unreal.GeometryCollectionSizeSpecificData.collision_type"></a>

#### collision_type

```python
@collision_type.setter
def collision_type(value: CollisionTypeEnum) -> None
```

<a id="unreal.GeometryCollectionSizeSpecificData.implicit_type"></a>

#### implicit_type

```python
@property
def implicit_type() -> ImplicitTypeEnum
```

(ImplicitTypeEnum):  [Read-Write] *  CollisionType defines how to initialize the rigid collision structures.
deprecated: Use Collision.ImplicitType instead.

<a id="unreal.GeometryCollectionSizeSpecificData.implicit_type"></a>

#### implicit_type

```python
@implicit_type.setter
def implicit_type(value: ImplicitTypeEnum) -> None
```

<a id="unreal.GeometryCollectionSizeSpecificData.min_level_set_resolution"></a>

#### min_level_set_resolution

```python
@property
def min_level_set_resolution() -> int
```

(int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 5)
deprecated: Use Collision.LevelSet.MinLevelSetResolution instead.

<a id="unreal.GeometryCollectionSizeSpecificData.min_level_set_resolution"></a>

#### min_level_set_resolution

```python
@min_level_set_resolution.setter
def min_level_set_resolution(value: int) -> None
```

<a id="unreal.GeometryCollectionSizeSpecificData.max_level_set_resolution"></a>

#### max_level_set_resolution

```python
@property
def max_level_set_resolution() -> int
```

(int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 10)
deprecated: Use Collision.LevelSet.MaxLevelSetResolution instead.

<a id="unreal.GeometryCollectionSizeSpecificData.max_level_set_resolution"></a>

#### max_level_set_resolution

```python
@max_level_set_resolution.setter
def max_level_set_resolution(value: int) -> None
```

<a id="unreal.GeometryCollectionSizeSpecificData.min_cluster_level_set_resolution"></a>

#### min_cluster_level_set_resolution

```python
@property
def min_cluster_level_set_resolution() -> int
```

(int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 5)
deprecated: Use Collision.LevelSet.MinClusterLevelSetResolution instead.

<a id="unreal.GeometryCollectionSizeSpecificData.min_cluster_level_set_resolution"></a>

#### min_cluster_level_set_resolution

```python
@min_cluster_level_set_resolution.setter
def min_cluster_level_set_resolution(value: int) -> None
```

<a id="unreal.GeometryCollectionSizeSpecificData.max_cluster_level_set_resolution"></a>

#### max_cluster_level_set_resolution

```python
@property
def max_cluster_level_set_resolution() -> int
```

(int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 10)
deprecated: Use Collision.LevelSet.MaxClusterLevelSetResolution instead.

<a id="unreal.GeometryCollectionSizeSpecificData.max_cluster_level_set_resolution"></a>

#### max_cluster_level_set_resolution

```python
@max_cluster_level_set_resolution.setter
def max_cluster_level_set_resolution(value: int) -> None
```

<a id="unreal.GeometryCollectionSizeSpecificData.collision_object_reduction_percentage"></a>

#### collision_object_reduction_percentage

```python
@property
def collision_object_reduction_percentage() -> int
```

(int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 10)
deprecated: Use Collision.CollisionObjectReductionPercentage instead.

<a id="unreal.GeometryCollectionSizeSpecificData.collision_object_reduction_percentage"></a>

#### collision_object_reduction_percentage

```python
@collision_object_reduction_percentage.setter
def collision_object_reduction_percentage(value: int) -> None
```

<a id="unreal.GeometryCollectionSizeSpecificData.collision_particles_fraction"></a>

#### collision_particles_fraction

```python
@property
def collision_particles_fraction() -> float
```

(float):  [Read-Write] Number of particles on the triangulated surface to use for collisions.
deprecated: Use Collision.CollisionParticlesFraction instead.

<a id="unreal.GeometryCollectionSizeSpecificData.collision_particles_fraction"></a>

#### collision_particles_fraction

```python
@collision_particles_fraction.setter
def collision_particles_fraction(value: float) -> None
```

<a id="unreal.GeometryCollectionSizeSpecificData.maximum_collision_particles"></a>

#### maximum_collision_particles

```python
@property
def maximum_collision_particles() -> int
```

(int32):  [Read-Write] Max number of particles.
deprecated: Use Collision.MaximumCollisionParticles instead.

<a id="unreal.GeometryCollectionSizeSpecificData.maximum_collision_particles"></a>

#### maximum_collision_particles

```python
@maximum_collision_particles.setter
def maximum_collision_particles(value: int) -> None
```

<a id="unreal.RecastNavMeshTileGenerationDebug"></a>