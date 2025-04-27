## MovieScene3DPathSection Objects

```python
class MovieScene3DPathSection(MovieScene3DConstraintSection)
```

A 3D Path section

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieScene3DPathSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``constraint_binding_id`` (MovieSceneObjectBindingID):  [Read-Write] The constraint binding that this movie Constraint uses
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``follow`` (bool):  [Read-Write] Follow Curve
- ``force_upright`` (bool):  [Read-Write] Force Upright
- ``front_axis_enum`` (MovieScene3DPathSection_Axis):  [Read-Write] Front Axis
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``reverse`` (bool):  [Read-Write] Reverse Timing
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)
- ``up_axis_enum`` (MovieScene3DPathSection_Axis):  [Read-Write] Up Axis

<a id="unreal.MovieScene3DPathSection.front_axis_enum"></a>

#### front_axis_enum

```python
@property
def front_axis_enum() -> MovieScene3DPathSection_Axis
```

(MovieScene3DPathSection_Axis):  [Read-Write] Front Axis

<a id="unreal.MovieScene3DPathSection.front_axis_enum"></a>

#### front_axis_enum

```python
@front_axis_enum.setter
def front_axis_enum(value: MovieScene3DPathSection_Axis) -> None
```

<a id="unreal.MovieScene3DPathSection.up_axis_enum"></a>

#### up_axis_enum

```python
@property
def up_axis_enum() -> MovieScene3DPathSection_Axis
```

(MovieScene3DPathSection_Axis):  [Read-Write] Up Axis

<a id="unreal.MovieScene3DPathSection.up_axis_enum"></a>

#### up_axis_enum

```python
@up_axis_enum.setter
def up_axis_enum(value: MovieScene3DPathSection_Axis) -> None
```

<a id="unreal.MovieScene3DPathSection.follow"></a>

#### follow

```python
@property
def follow() -> bool
```

(bool):  [Read-Write] Follow Curve

<a id="unreal.MovieScene3DPathSection.follow"></a>

#### follow

```python
@follow.setter
def follow(value: bool) -> None
```

<a id="unreal.MovieScene3DPathSection.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write] Reverse Timing

<a id="unreal.MovieScene3DPathSection.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.MovieScene3DPathSection.force_upright"></a>

#### force_upright

```python
@property
def force_upright() -> bool
```

(bool):  [Read-Write] Force Upright

<a id="unreal.MovieScene3DPathSection.force_upright"></a>

#### force_upright

```python
@force_upright.setter
def force_upright(value: bool) -> None
```

<a id="unreal.MovieScene3DTransformSection"></a>