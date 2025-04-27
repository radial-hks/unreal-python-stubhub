## LiveLinkAnimationAxisSwitchPreProcessor Objects

```python
class LiveLinkAnimationAxisSwitchPreProcessor(
        LiveLinkTransformAxisSwitchPreProcessor)
```

Allows to switch any axis of an incoming animation with another axis.
note: For example the Z-Axis of an incoming transform can be set to the (optionally negated) Y-Axis of the transform in UE.
note: This implies that translation, rotation and scale will be affected by switching an axis.

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLink
- **File**: LiveLinkAxisSwitchPreProcessor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``front_axis`` (LiveLinkAxis):  [Read-Write]
- ``offset_orientation`` (Rotator):  [Read-Write]
- ``offset_position`` (Vector):  [Read-Write]
- ``orientation_axis_x`` (LiveLinkAxis):  [Read-Write]
  deprecated: Use FrontAxis, RightAxis, UpAxis instead
- ``orientation_axis_y`` (LiveLinkAxis):  [Read-Write]
  deprecated: Use FrontAxis, RightAxis, UpAxis instead
- ``orientation_axis_z`` (LiveLinkAxis):  [Read-Write]
  deprecated: Use FrontAxis, RightAxis, UpAxis instead
- ``right_axis`` (LiveLinkAxis):  [Read-Write]
- ``translation_axis_x`` (LiveLinkAxis):  [Read-Write]
  deprecated: Use FrontAxis, RightAxis, UpAxis instead
- ``translation_axis_y`` (LiveLinkAxis):  [Read-Write]
  deprecated: Use FrontAxis, RightAxis, UpAxis instead
- ``translation_axis_z`` (LiveLinkAxis):  [Read-Write]
  deprecated: Use FrontAxis, RightAxis, UpAxis instead
- ``up_axis`` (LiveLinkAxis):  [Read-Write]
- ``use_offset_orientation`` (bool):  [Read-Write]
- ``use_offset_position`` (bool):  [Read-Write]

<a id="unreal.LiveLinkVirtualSubject"></a>