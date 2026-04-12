## GameplayCueNotify\_PlacementInfo Objects

```python
class GameplayCueNotify_PlacementInfo(StructBase)
```

FGameplayCueNotify_PlacementInfo

    Specifies how the gameplay cue notify will be positioned in the world.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotifyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attach_policy`` (GameplayCueNotify_AttachPolicy):  [Read-Write] Whether to attach to the target actor or not attach.
- ``attachment_rule`` (AttachmentRule):  [Read-Write] How the transform is handled when attached.
- ``override_rotation`` (bool):  [Read-Write] If enabled, will always spawn using rotation override.
- ``override_scale`` (bool):  [Read-Write] If enabled, will always spawn using the scale override.
- ``rotation_override`` (Rotator):  [Read-Write] If enabled, will always spawn using rotation override.
  This will also set the rotation to be absolute, so any changes to the parent's rotation will be ignored after attachment.
- ``scale_override`` (Vector):  [Read-Write] If enabled, will always spawn using scale override.
  This will also set the scale to be absolute, so any changes to the parent's scale will be ignored after attachment.
- ``socket_name`` (Name):  [Read-Write] Target's socket (or bone) used for location and rotation.  If "None", it uses the target's root.

<a id="unreal.GameplayCueNotify_PlacementInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(socket_name: Name = "None",
             attach_policy:
             GameplayCueNotify_AttachPolicy = GameplayCueNotify_AttachPolicy.
             DO_NOT_ATTACH,
             attachment_rule: AttachmentRule = AttachmentRule.KEEP_RELATIVE,
             override_rotation: bool = False,
             override_scale: bool = False,
             rotation_override: Rotator = [0.000000, 0.000000, 0.000000],
             scale_override: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.GameplayCueNotify_PlacementInfo.socket_name"></a>

#### socket\_name

```python
@property
def socket_name() -> Name
```

(Name):  [Read-Only] Target's socket (or bone) used for location and rotation.  If "None", it uses the target's root.

<a id="unreal.GameplayCueNotify_PlacementInfo.attach_policy"></a>

#### attach\_policy

```python
@property
def attach_policy() -> GameplayCueNotify_AttachPolicy
```

(GameplayCueNotify_AttachPolicy):  [Read-Only] Whether to attach to the target actor or not attach.

<a id="unreal.GameplayCueNotify_PlacementInfo.attachment_rule"></a>

#### attachment\_rule

```python
@property
def attachment_rule() -> AttachmentRule
```

(AttachmentRule):  [Read-Only] How the transform is handled when attached.

<a id="unreal.GameplayCueNotify_PlacementInfo.override_rotation"></a>

#### override\_rotation

```python
@property
def override_rotation() -> bool
```

(bool):  [Read-Only] If enabled, will always spawn using rotation override.

<a id="unreal.GameplayCueNotify_PlacementInfo.override_scale"></a>

#### override\_scale

```python
@property
def override_scale() -> bool
```

(bool):  [Read-Only] If enabled, will always spawn using the scale override.

<a id="unreal.GameplayCueNotify_PlacementInfo.rotation_override"></a>

#### rotation\_override

```python
@property
def rotation_override() -> Rotator
```

(Rotator):  [Read-Only] If enabled, will always spawn using rotation override.
This will also set the rotation to be absolute, so any changes to the parent's rotation will be ignored after attachment.

<a id="unreal.GameplayCueNotify_PlacementInfo.scale_override"></a>

#### scale\_override

```python
@property
def scale_override() -> Vector
```

(Vector):  [Read-Only] If enabled, will always spawn using scale override.
This will also set the scale to be absolute, so any changes to the parent's scale will be ignored after attachment.

<a id="unreal.GameplayCueNotify_SpawnResult"></a>