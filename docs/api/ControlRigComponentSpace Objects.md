## ControlRigComponentSpace Objects

```python
class ControlRigComponentSpace(EnumBase)
```

Enum for controlling which space a transform is applied in.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigComponent.h

<a id="unreal.ControlRigComponentSpace.WORLD_SPACE"></a>

#### WORLD\_SPACE

0: World space transform

<a id="unreal.ControlRigComponentSpace.ACTOR_SPACE"></a>

#### ACTOR\_SPACE

1: The space below the actor's root transform

<a id="unreal.ControlRigComponentSpace.COMPONENT_SPACE"></a>

#### COMPONENT\_SPACE

2: The space defined by the Control Rig Component

<a id="unreal.ControlRigComponentSpace.RIG_SPACE"></a>

#### RIG\_SPACE

3: The space within the rig. Currently the same as Component Space.
Inside of control rig this is called 'Global Space'.

<a id="unreal.ControlRigComponentSpace.LOCAL_SPACE"></a>

#### LOCAL\_SPACE

4: The space defined by each element's parent (bone, control etc)

<a id="unreal.CRSimSoftCollisionType"></a>