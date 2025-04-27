## LevelSequenceCameraSettings Objects

```python
class LevelSequenceCameraSettings(StructBase)
```

Level Sequence Camera Settings

**C++ Source:**

- **Module**: LevelSequence
- **File**: LevelSequenceCameraSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aspect_ratio_axis_constraint`` (AspectRatioAxisConstraint):  [Read-Write]
- ``override_aspect_ratio_axis_constraint`` (bool):  [Read-Write]

<a id="unreal.LevelSequenceCameraSettings.__init__"></a>

#### __init__

```python
def __init__(
    override_aspect_ratio_axis_constraint: bool = False,
    aspect_ratio_axis_constraint:
    AspectRatioAxisConstraint = AspectRatioAxisConstraint.
    ASPECT_RATIO_MAINTAIN_YFOV
) -> None
```

<a id="unreal.LevelSequenceCameraSettings.override_aspect_ratio_axis_constraint"></a>

#### override_aspect_ratio_axis_constraint

```python
@property
def override_aspect_ratio_axis_constraint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LevelSequenceCameraSettings.override_aspect_ratio_axis_constraint"></a>

#### override_aspect_ratio_axis_constraint

```python
@override_aspect_ratio_axis_constraint.setter
def override_aspect_ratio_axis_constraint(value: bool) -> None
```

<a id="unreal.LevelSequenceCameraSettings.aspect_ratio_axis_constraint"></a>

#### aspect_ratio_axis_constraint

```python
@property
def aspect_ratio_axis_constraint() -> AspectRatioAxisConstraint
```

(AspectRatioAxisConstraint):  [Read-Write]

<a id="unreal.LevelSequenceCameraSettings.aspect_ratio_axis_constraint"></a>

#### aspect_ratio_axis_constraint

```python
@aspect_ratio_axis_constraint.setter
def aspect_ratio_axis_constraint(value: AspectRatioAxisConstraint) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem"></a>