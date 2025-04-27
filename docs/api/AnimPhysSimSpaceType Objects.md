## AnimPhysSimSpaceType Objects

```python
class AnimPhysSimSpaceType(EnumBase)
```

Anim Phys Sim Space Type

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_AnimDynamics.h

<a id="unreal.AnimPhysSimSpaceType.COMPONENT"></a>

#### COMPONENT

0: Sim origin is the location/orientation of the skeletal mesh component.

<a id="unreal.AnimPhysSimSpaceType.ACTOR"></a>

#### ACTOR

1: Sim origin is the location/orientation of the actor containing the skeletal mesh component.

<a id="unreal.AnimPhysSimSpaceType.WORLD"></a>

#### WORLD

2: Sim origin is the world origin. Teleporting characters is not recommended in this mode.

<a id="unreal.AnimPhysSimSpaceType.ROOT_RELATIVE"></a>

#### ROOT_RELATIVE

3: Sim origin is the location/orientation of the root bone.

<a id="unreal.AnimPhysSimSpaceType.BONE_RELATIVE"></a>

#### BONE_RELATIVE

4: Sim origin is the location/orientation of the bone specified in RelativeSpaceBone

<a id="unreal.ScaleChainInitialLength"></a>