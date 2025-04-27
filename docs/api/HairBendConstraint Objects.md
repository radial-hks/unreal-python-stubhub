## HairBendConstraint Objects

```python
class HairBendConstraint(StructBase)
```

Hair Bend Constraint

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetPhysics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bend_damping`` (float):  [Read-Write] Damping for the bend constraint between 0 and 1
- ``bend_scale`` (RuntimeFloatCurve):  [Read-Write] This curve determines how much the bend stiffness will be scaled along each strand. 
   The X axis range is [0,1], 0 mapping the root and 1 the tip
- ``bend_stiffness`` (float):  [Read-Write] Stiffness for the bend constraint in GPa
- ``project_bend`` (bool):  [Read-Write] Enable ther projection of the bend constraint after the xpbd loop
- ``solve_bend`` (bool):  [Read-Write] Enable the solve of the bend constraint during the xpbd loop

<a id="unreal.HairBendConstraint.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.HairStretchConstraint"></a>