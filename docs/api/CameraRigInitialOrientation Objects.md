## CameraRigInitialOrientation Objects

```python
class CameraRigInitialOrientation(EnumBase)
```

Determines how a camera rig's initial orientation should be initialized.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: CameraRigTransition.h

<a id="unreal.CameraRigInitialOrientation.NONE"></a>

#### NONE

0: Leave the camera rig to its default orientation.

<a id="unreal.CameraRigInitialOrientation.CONTEXT_YAW_PITCH"></a>

#### CONTEXT_YAW_PITCH

1: Orient the camera rig in the same direction as its context's initial transform.

<a id="unreal.CameraRigInitialOrientation.PREVIOUS_YAW_PITCH"></a>

#### PREVIOUS_YAW_PITCH

2: Orient the camera rig in the same direction as the previously active camera rig.

<a id="unreal.CameraRigInitialOrientation.PREVIOUS_ABSOLUTE_TARGET"></a>

#### PREVIOUS_ABSOLUTE_TARGET

3: Make the camera rig point at the same target as the previously active camera rig's
last frame target.

<a id="unreal.CameraRigInitialOrientation.PREVIOUS_RELATIVE_TARGET"></a>

#### PREVIOUS_RELATIVE_TARGET

4: Make the camera rig point at the same target as the previously active camera rig.
Last frame's target will be moved and turned by an offset equal to how much the
active evaluation context has moved and turned since last frame.

<a id="unreal.WorldPartitionServerStreamingMode"></a>