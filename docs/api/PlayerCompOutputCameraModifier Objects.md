## PlayerCompOutputCameraModifier Objects

```python
class PlayerCompOutputCameraModifier(CameraModifier)
```

UPlayerCompOutputCameraModifier

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: PlayerViewportCompositingOutput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current blend alpha.
- ``alpha_in_time`` (float):  [Read-Write] When blending in, alpha proceeds from 0 to 1 over this time
- ``alpha_out_time`` (float):  [Read-Write] When blending out, alpha proceeds from 1 to 0 over this time
- ``camera_owner`` (PlayerCameraManager):  [Read-Write] Camera this object is associated with.
- ``debug`` (bool):  [Read-Write] If true, enables certain debug visualization features.
- ``exclusive`` (bool):  [Read-Write] If true, no other modifiers of same priority allowed.
- ``priority`` (uint8):  [Read-Write] Priority value that determines the order in which modifiers are applied. 0 = highest priority, 255 = lowest.

<a id="unreal.ObjectMixerObjectFilter"></a>