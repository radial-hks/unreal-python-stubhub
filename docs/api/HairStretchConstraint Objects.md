## HairStretchConstraint Objects

```python
class HairStretchConstraint(StructBase)
```

Hair Stretch Constraint

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetPhysics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``project_stretch`` (bool):  [Read-Write] Enable ther projection of the stretch constraint after the xpbd loop
- ``solve_stretch`` (bool):  [Read-Write] Enable the solve of the stretch constraint during the xpbd loop
- ``stretch_damping`` (float):  [Read-Write] Damping for the stretch constraint between 0 and 1
- ``stretch_scale`` (RuntimeFloatCurve):  [Read-Write] This curve determines how much the stretch stiffness will be scaled along each strand. 
   The X axis range is [0,1], 0 mapping the root and 1 the tip
- ``stretch_stiffness`` (float):  [Read-Write] Stiffness for the stretch constraint in GPa

<a id="unreal.HairStretchConstraint.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.HairCollisionConstraint"></a>