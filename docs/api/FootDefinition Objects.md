## FootDefinition Objects

```python
class FootDefinition(StructBase)
```

Foot Definition

**C++ Source:**

- **Plugin**: AnimationModifierLibrary
- **Module**: AnimationModifierLibrary
- **File**: FootstepAnimEventsModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``foot_bone_name`` (Name):  [Read-Write]
- ``footstep_notify`` (type(Class)):  [Read-Write]
- ``footstep_notify_detection_technique`` (DetectionTechnique):  [Read-Write]
- ``footstep_notify_track_name`` (Name):  [Read-Write]
- ``reference_bone_name`` (Name):  [Read-Write]
- ``should_generate_notifies`` (bool):  [Read-Write]
- ``should_generate_sync_markers`` (bool):  [Read-Write]
- ``should_skip_notify_if_foot_bone_speed_starts_below_threshold`` (bool):  [Read-Write]
- ``should_skip_sync_marker_if_foot_bone_speed_starts_below_threshold`` (bool):  [Read-Write]
- ``sync_marker_detection_technique`` (DetectionTechnique):  [Read-Write]
- ``sync_marker_name`` (Name):  [Read-Write]
- ``sync_marker_track_name`` (Name):  [Read-Write]

<a id="unreal.FootDefinition.__init__"></a>

#### __init__

```python
def __init__(reference_bone_name: Name = "None") -> None
```

<a id="unreal.FootDefinition.reference_bone_name"></a>

#### reference_bone_name

```python
@property
def reference_bone_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.ControlRigSpline"></a>