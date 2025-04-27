## HairCollisionConstraint Objects

```python
class HairCollisionConstraint(StructBase)
```

Hair Collision Constraint

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetPhysics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_radius`` (float):  [Read-Write] Radius that will be used for the collision detection against the physics asset
- ``grid_dimension`` (IntVector):  [Read-Write] Dimension of the grid used to compute the viscosity force
- ``kinetic_friction`` (float):  [Read-Write] Kinetic friction used for collision against the physics asset
- ``project_collision`` (bool):  [Read-Write] Enable ther projection of the collision constraint after the xpbd loop
- ``radius_scale`` (RuntimeFloatCurve):  [Read-Write] This curve determines how much the collision radius will be scaled along each strand. 
   The X axis range is [0,1], 0 mapping the root and 1 the tip
- ``solve_collision`` (bool):  [Read-Write] Enable the solve of the collision constraint during the xpbd loop
- ``static_friction`` (float):  [Read-Write] Static friction used for collision against the physics asset
- ``strands_viscosity`` (float):  [Read-Write] Viscosity parameter between 0 and 1 that will be used for self collision

<a id="unreal.HairCollisionConstraint.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.HairMaterialConstraints"></a>