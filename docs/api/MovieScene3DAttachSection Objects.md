## MovieScene3DAttachSection Objects

```python
class MovieScene3DAttachSection(MovieScene3DConstraintSection)
```

A 3D Attach section

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieScene3DAttachSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attach_component_name`` (Name):  [Read-Write]
- ``attach_socket_name`` (Name):  [Read-Write]
- ``attachment_location_rule`` (AttachmentRule):  [Read-Write]
- ``attachment_rotation_rule`` (AttachmentRule):  [Read-Write]
- ``attachment_scale_rule`` (AttachmentRule):  [Read-Write]
- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``constraint_binding_id`` (MovieSceneObjectBindingID):  [Read-Write] The constraint binding that this movie Constraint uses
- ``detachment_location_rule`` (DetachmentRule):  [Read-Write]
- ``detachment_rotation_rule`` (DetachmentRule):  [Read-Write]
- ``detachment_scale_rule`` (DetachmentRule):  [Read-Write]
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieScene3DAttachSection.attach_socket_name"></a>

#### attach_socket_name

```python
@property
def attach_socket_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.MovieScene3DAttachSection.attach_socket_name"></a>

#### attach_socket_name

```python
@attach_socket_name.setter
def attach_socket_name(value: Name) -> None
```

<a id="unreal.MovieScene3DAttachSection.attach_component_name"></a>

#### attach_component_name

```python
@property
def attach_component_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.MovieScene3DAttachSection.attach_component_name"></a>

#### attach_component_name

```python
@attach_component_name.setter
def attach_component_name(value: Name) -> None
```

<a id="unreal.MovieScene3DAttachSection.attachment_location_rule"></a>

#### attachment_location_rule

```python
@property
def attachment_location_rule() -> AttachmentRule
```

(AttachmentRule):  [Read-Write]

<a id="unreal.MovieScene3DAttachSection.attachment_location_rule"></a>

#### attachment_location_rule

```python
@attachment_location_rule.setter
def attachment_location_rule(value: AttachmentRule) -> None
```

<a id="unreal.MovieScene3DAttachSection.attachment_rotation_rule"></a>

#### attachment_rotation_rule

```python
@property
def attachment_rotation_rule() -> AttachmentRule
```

(AttachmentRule):  [Read-Write]

<a id="unreal.MovieScene3DAttachSection.attachment_rotation_rule"></a>

#### attachment_rotation_rule

```python
@attachment_rotation_rule.setter
def attachment_rotation_rule(value: AttachmentRule) -> None
```

<a id="unreal.MovieScene3DAttachSection.attachment_scale_rule"></a>

#### attachment_scale_rule

```python
@property
def attachment_scale_rule() -> AttachmentRule
```

(AttachmentRule):  [Read-Write]

<a id="unreal.MovieScene3DAttachSection.attachment_scale_rule"></a>

#### attachment_scale_rule

```python
@attachment_scale_rule.setter
def attachment_scale_rule(value: AttachmentRule) -> None
```

<a id="unreal.MovieScene3DAttachSection.detachment_location_rule"></a>

#### detachment_location_rule

```python
@property
def detachment_location_rule() -> DetachmentRule
```

(DetachmentRule):  [Read-Write]

<a id="unreal.MovieScene3DAttachSection.detachment_location_rule"></a>

#### detachment_location_rule

```python
@detachment_location_rule.setter
def detachment_location_rule(value: DetachmentRule) -> None
```

<a id="unreal.MovieScene3DAttachSection.detachment_rotation_rule"></a>

#### detachment_rotation_rule

```python
@property
def detachment_rotation_rule() -> DetachmentRule
```

(DetachmentRule):  [Read-Write]

<a id="unreal.MovieScene3DAttachSection.detachment_rotation_rule"></a>

#### detachment_rotation_rule

```python
@detachment_rotation_rule.setter
def detachment_rotation_rule(value: DetachmentRule) -> None
```

<a id="unreal.MovieScene3DAttachSection.detachment_scale_rule"></a>

#### detachment_scale_rule

```python
@property
def detachment_scale_rule() -> DetachmentRule
```

(DetachmentRule):  [Read-Write]

<a id="unreal.MovieScene3DAttachSection.detachment_scale_rule"></a>

#### detachment_scale_rule

```python
@detachment_scale_rule.setter
def detachment_scale_rule(value: DetachmentRule) -> None
```

<a id="unreal.MovieScene3DPathSection"></a>