## RetargetAutoAlignMethod Objects

```python
class RetargetAutoAlignMethod(EnumBase)
```

A Note on Determining the "Direction" of a Bone...

What are we using to determine the "direction" of the source and target bones to align?
If chain only has one bone OR this bone is located at the end of a chain, then we cannot compute a tangent!
So we fallback to an analysis of the geometry... this is necessary because we cannot rely solely on the shape of the skeleton.
Any assumptions we make could be invalidated in different circumstances. For example,
1. we cannot assume the local axes are aligned in any meaningful way, and even if they are we cannot assume WHICH axis is the correct one
2. we cannot assume that any child bones are located in a position that would create a meaningful vector (ie twist bones in arbitrary locations)
3. we cannot assume that extrapolating the direction from the parent is meaningful. For example, feet are usually perpendicular to the knee.

Since the skeleton cannot be relied upon to provide robust directional information for individual and/or leaf bones, we must instead fallback
on looking at the mesh that is skinned to it and try to discern a direction vector from that. If there is no skinning data, then we simply
do NOT auto-align that bone.

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRigEditor
- **File**: IKRetargeterPoseGenerator.h

<a id="unreal.RetargetAutoAlignMethod.CHAIN_TO_CHAIN"></a>

#### CHAIN_TO_CHAIN

0: use the chain to determine the source and target directions to align

<a id="unreal.RetargetAutoAlignMethod.MESH_TO_MESH"></a>

#### MESH_TO_MESH

1: use mesh direction as source, and mesh direction as the target to align

<a id="unreal.ControlOutputFormat"></a>