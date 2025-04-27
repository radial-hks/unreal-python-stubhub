## RigControlAnimationType Objects

```python
class RigControlAnimationType(EnumBase)
```

ERig Control Animation Type

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyDefines.h

<a id="unreal.RigControlAnimationType.ANIMATION_CONTROL"></a>

#### ANIMATION_CONTROL

0: A visible, animatable control.

<a id="unreal.RigControlAnimationType.ANIMATION_CHANNEL"></a>

#### ANIMATION_CHANNEL

1: An animation channel without a 3d shape

<a id="unreal.RigControlAnimationType.PROXY_CONTROL"></a>

#### PROXY_CONTROL

2: A control to drive other controls,
not animatable in sequencer.

<a id="unreal.RigControlAnimationType.VISUAL_CUE"></a>

#### VISUAL_CUE

3: Visual feedback only - the control is
neither animatable nor selectable.

<a id="unreal.ConnectorType"></a>