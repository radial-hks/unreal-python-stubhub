## CameraModifier_CameraShake Objects

```python
class CameraModifier_CameraShake(CameraModifier)
```

A UCameraModifier_CameraShake is a camera modifier that can apply a UCameraShakeBase to
the owning camera.

**C++ Source:**

- **Module**: Engine
- **File**: CameraModifier_CameraShake.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current blend alpha.
- ``alpha_in_time`` (float):  [Read-Write] When blending in, alpha proceeds from 0 to 1 over this time
- ``alpha_out_time`` (float):  [Read-Write] When blending out, alpha proceeds from 1 to 0 over this time
- ``camera_owner`` (PlayerCameraManager):  [Read-Write] Camera this object is associated with.
- ``debug`` (bool):  [Read-Write] If true, enables certain debug visualization features.
- ``exclusive`` (bool):  [Read-Write] If true, no other modifiers of same priority allowed.
- ``priority`` (uint8):  [Read-Write] Priority value that determines the order in which modifiers are applied. 0 = highest priority, 255 = lowest.
- ``split_screen_shake_scale`` (float):  [Read-Write] Scaling factor applied to all camera shakes in when in splitscreen mode. Normally used to reduce shaking, since shakes feel more intense in a smaller viewport.

<a id="unreal.CameraShakeBase"></a>