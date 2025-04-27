## RootMotionModifierState Objects

```python
class RootMotionModifierState(EnumBase)
```

The possible states of a Root Motion Modifier

**C++ Source:**

- **Plugin**: MotionWarping
- **Module**: MotionWarping
- **File**: RootMotionModifier.h

<a id="unreal.RootMotionModifierState.WAITING"></a>

#### WAITING

0: The modifier is waiting for the animation to hit the warping window

<a id="unreal.RootMotionModifierState.ACTIVE"></a>

#### ACTIVE

1: The modifier is active and currently affecting the final root motion

<a id="unreal.RootMotionModifierState.MARKED_FOR_REMOVAL"></a>

#### MARKED_FOR_REMOVAL

2: The modifier has been marked for removal. Usually because the warping window is done

<a id="unreal.RootMotionModifierState.DISABLED"></a>

#### DISABLED

3: The modifier will remain in the list (as long as the window is active) but will not modify the root motion

<a id="unreal.MotionWarpRotationType"></a>