## HairStrandsParameters Objects

```python
class HairStrandsParameters(StructBase)
```

Hair Strands Parameters

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetPhysics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``strands_density`` (float):  [Read-Write] Density of the strands in g/cm3
- ``strands_size`` (GroomStrandsSize):  [Read-Write] Number of particles per guide that will be used for simulation
- ``strands_smoothing`` (float):  [Read-Write] Smoothing between 0 and 1 of the incoming guides curves for better stability
- ``strands_thickness`` (float):  [Read-Write] Strands thickness in cm that will be used for mass and inertia computation
- ``thickness_scale`` (RuntimeFloatCurve):  [Read-Write] This curve determines how much the strands thickness will be scaled along each strand. 
   The X axis range is [0,1], 0 mapping the root and 1 the tip

<a id="unreal.HairStrandsParameters.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.HairGroupsPhysics"></a>