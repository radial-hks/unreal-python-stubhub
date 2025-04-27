## GeometryCollectionCollisionTypeData Objects

```python
class GeometryCollectionCollisionTypeData(StructBase)
```

Geometry Collection Collision Type Data

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: GeometryCollectionObject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_margin_fraction`` (float):  [Read-Write] A collision margin is a fraction of size used by some boxes and convex shapes to improve collision detection results.
  The core geometry of shapes that support a margin are reduced in size by the margin, and the margin
  is added back on during collision detection. The net result is a shape of the same size but with rounded corners.
- ``collision_object_reduction_percentage`` (float):  [Read-Write] *  Uniform scale on the collision body. (def: 0)
- ``collision_particles`` (GeometryCollectionCollisionParticleData):  [Read-Write] *  Collision Particle data for surface samples during Particle-LevelSet collisions.
- ``collision_type`` (CollisionTypeEnum):  [Read-Write] *  CollisionType defines how to initialize the rigid collision structures.
- ``implicit_type`` (ImplicitTypeEnum):  [Read-Write] *  CollisionType defines how to initialize the rigid collision structures.
- ``level_set`` (GeometryCollectionLevelSetData):  [Read-Write] *  LevelSet Resolution data for rasterization.

<a id="unreal.GeometryCollectionCollisionTypeData.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.LightmassParameterValue"></a>