## ControlRigSequencerLibrary Objects

```python
class ControlRigSequencerLibrary(BlueprintFunctionLibrary)
```

This is a set of helper functions to access various parts of the Sequencer and Control Rig API via Python and Blueprints.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: ControlRigSequencerEditorLibrary.h

<a id="unreal.ControlRigSequencerLibrary.tween_control_rig"></a>

#### tween_control_rig

```python
@classmethod
def tween_control_rig(cls, level_sequence: LevelSequence,
                      control_rig: ControlRig, tween_value: float) -> bool
```

X.tween_control_rig(level_sequence, control_rig, tween_value) -> bool
Peform a Tween operation on the current active sequencer time(must be visible).

Args:
    level_sequence (LevelSequence): The LevelSequence that's loaded in the editor
    control_rig (ControlRig): The Control Rig to tween.
    tween_value (float): The tween value to use, range from -1(blend to previous) to 1(blend to next)

Returns:
    bool:

<a id="unreal.ControlRigSequencerLibrary.space_compensate"></a>

#### space_compensate

```python
@classmethod
def space_compensate(
        cls,
        control_rig: ControlRig,
        time: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> bool
```

X.space_compensate(control_rig, time, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> bool
Perform compensation for any spaces at the specified time for the specified control rig

Args:
    control_rig (ControlRig): Control Rig to compensate
    time (FrameNumber): The time to look for a space key to compensate
    time_unit (MovieSceneTimeUnit): Unit for the InTime

Returns:
    bool: Will return false if function fails

<a id="unreal.ControlRigSequencerLibrary.snap_control_rig"></a>

#### snap_control_rig

```python
@classmethod
def snap_control_rig(
        cls,
        level_sequence: LevelSequence,
        start_frame: FrameNumber,
        end_frame: FrameNumber,
        children_to_snap: ControlRigSnapperSelection,
        parent_to_snap: ControlRigSnapperSelection,
        snap_settings: ControlRigSnapSettings,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> bool
```

X.snap_control_rig(level_sequence, start_frame, end_frame, children_to_snap, parent_to_snap, snap_settings, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> bool
Peform a Snap operation to snap the children to the parent.

Args:
    level_sequence (LevelSequence): Active Sequence to snap
    start_frame (FrameNumber): Beginning of the snap
    end_frame (FrameNumber): End of the snap
    children_to_snap (ControlRigSnapperSelection): The children objects that snap and get keys set onto. They need to live in an active Sequencer in the level editor
    parent_to_snap (ControlRigSnapperSelection): The parent object to snap relative to. If animated, it needs to live in an active Sequencer in the level editor
    snap_settings (ControlRigSnapSettings): Settings to use
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    bool:

<a id="unreal.ControlRigSequencerLibrary.smart_reduce"></a>

#### smart_reduce

```python
@classmethod
def smart_reduce(
        cls,
        movie_scene_section: MovieSceneSection) -> Optional[SmartReduceParams]
```

X.smart_reduce(movie_scene_section) -> SmartReduceParams or None
Peform new Smart Reduce filter over the specified control rig section in the current open level sequence. Note existing
functions like LoadAnimSequenceIntoControlRigSection and BakeToControlRig, will still use the old key reduction algorithm,
so if you want to bake and then key reduce with the new function, set the bKeyReduce param as false with those functions,
but then call this function after.

Args:
    movie_scene_section (MovieSceneSection): The Control rig section we want to reduce

Returns:
    SmartReduceParams or None: returns True if successful, False otherwise

    reduce_params (SmartReduceParams): Key reduction parameters

<a id="unreal.ControlRigSequencerLibrary.show_all_controls"></a>

#### show_all_controls

```python
@classmethod
def show_all_controls(cls, section: MovieSceneSection) -> None
```

X.show_all_controls(section) -> None
Shows all of the controls for the given section

Args:
    section (MovieSceneSection):

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_vector2_ds"></a>

#### set_local_control_rig_vector2_ds

```python
@classmethod
def set_local_control_rig_vector2_ds(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frames: Array[FrameNumber],
        values: Array[Vector2D],
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_local_control_rig_vector2_ds(level_sequence, control_rig, control_name, frames, values, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Set ControlRig Control's Vector2D values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Vector2D control
    frames (Array[FrameNumber]): Times to set the values
    values (Array[Vector2D]): The values to set at those times
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_vector2d"></a>

#### set_local_control_rig_vector2d

```python
@classmethod
def set_local_control_rig_vector2d(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        value: Vector2D,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        set_key: bool = True) -> None
```

X.set_local_control_rig_vector2d(level_sequence, control_rig, control_name, frame, value, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, set_key=True) -> None
Set ControlRig Control's Vector2D value at specific time

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Vector2D control
    frame (FrameNumber): Time to set the value
    value (Vector2D): The value to set
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution
    set_key (bool): If True set a key, if not just set the value

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_transforms"></a>

#### set_local_control_rig_transforms

```python
@classmethod
def set_local_control_rig_transforms(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frames: Array[FrameNumber],
        values: Array[Transform],
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_local_control_rig_transforms(level_sequence, control_rig, control_name, frames, values, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Set ControlRig Control's Transform values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Transform control
    frames (Array[FrameNumber]): Times to set the values
    values (Array[Transform]): The values to set at those times
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_transform_no_scales"></a>

#### set_local_control_rig_transform_no_scales

```python
@classmethod
def set_local_control_rig_transform_no_scales(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frames: Array[FrameNumber],
        values: Array[TransformNoScale],
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_local_control_rig_transform_no_scales(level_sequence, control_rig, control_name, frames, values, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Set ControlRig Control's TransformNoScale values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a TransformNoScale control
    frames (Array[FrameNumber]): Times to set the values
    values (Array[TransformNoScale]): The values to set at those times
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_transform_no_scale"></a>

#### set_local_control_rig_transform_no_scale

```python
@classmethod
def set_local_control_rig_transform_no_scale(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        value: TransformNoScale,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        set_key: bool = True) -> None
```

X.set_local_control_rig_transform_no_scale(level_sequence, control_rig, control_name, frame, value, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, set_key=True) -> None
Set ControlRig Control's TransformNoScale value at specific time

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a TransformNoScale control
    frame (FrameNumber): Time to set the value
    value (TransformNoScale): The value to set
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution
    set_key (bool): If True set a key, if not just set the value

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_transform"></a>

#### set_local_control_rig_transform

```python
@classmethod
def set_local_control_rig_transform(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        value: Transform,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        set_key: bool = True) -> None
```

X.set_local_control_rig_transform(level_sequence, control_rig, control_name, frame, value, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, set_key=True) -> None
Set ControlRig Control's Transform value at specific time

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Transform control
    frame (FrameNumber): Time to set the value
    value (Transform): The value to set
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution
    set_key (bool): If True set a key, if not just set the value

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_scales"></a>

#### set_local_control_rig_scales

```python
@classmethod
def set_local_control_rig_scales(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frames: Array[FrameNumber],
        values: Array[Vector],
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_local_control_rig_scales(level_sequence, control_rig, control_name, frames, values, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Set ControlRig Control's Scale values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Scale control
    frames (Array[FrameNumber]): Times to set the values
    values (Array[Vector]): The values to set at those times
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_scale"></a>

#### set_local_control_rig_scale

```python
@classmethod
def set_local_control_rig_scale(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        value: Vector,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        set_key: bool = True) -> None
```

X.set_local_control_rig_scale(level_sequence, control_rig, control_name, frame, value, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, set_key=True) -> None
Set ControlRig Control's Scale value at specific time

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Scale control
    frame (FrameNumber): Time to set the value
    value (Vector): The value to set
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution
    set_key (bool): If True set a key, if not just set the value

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_rotators"></a>

#### set_local_control_rig_rotators

```python
@classmethod
def set_local_control_rig_rotators(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frames: Array[FrameNumber],
        values: Array[Rotator],
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_local_control_rig_rotators(level_sequence, control_rig, control_name, frames, values, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Set ControlRig Control's Rotator values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Rotator control
    frames (Array[FrameNumber]): Times to set the values
    values (Array[Rotator]): The values to set at those times
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_rotator"></a>

#### set_local_control_rig_rotator

```python
@classmethod
def set_local_control_rig_rotator(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        value: Rotator,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        set_key: bool = True) -> None
```

X.set_local_control_rig_rotator(level_sequence, control_rig, control_name, frame, value, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, set_key=True) -> None
Set ControlRig Control's Rotator value at specific time

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Rotator control
    frame (FrameNumber): Time to set the value
    value (Rotator): The value to set
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution
    set_key (bool): If True set a key, if not just set the value

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_positions"></a>

#### set_local_control_rig_positions

```python
@classmethod
def set_local_control_rig_positions(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frames: Array[FrameNumber],
        values: Array[Vector],
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_local_control_rig_positions(level_sequence, control_rig, control_name, frames, values, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Set ControlRig Control's Position values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Position control
    frames (Array[FrameNumber]): Times to set the values
    values (Array[Vector]): The values to set at those times
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_position"></a>

#### set_local_control_rig_position

```python
@classmethod
def set_local_control_rig_position(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        value: Vector,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        set_key: bool = True) -> None
```

X.set_local_control_rig_position(level_sequence, control_rig, control_name, frame, value, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, set_key=True) -> None
Set ControlRig Control's Position value at specific time

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Position control
    frame (FrameNumber): Time to set the value
    value (Vector): The value to set
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution
    set_key (bool): If True set a key, if not just set the value

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_ints"></a>

#### set_local_control_rig_ints

```python
@classmethod
def set_local_control_rig_ints(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frames: Array[FrameNumber],
        values: Array[int],
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_local_control_rig_ints(level_sequence, control_rig, control_name, frames, values, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Set ControlRig Control's int values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a int control
    frames (Array[FrameNumber]): Times to set the values
    values (Array[int32]): The values to set at those times
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_int"></a>

#### set_local_control_rig_int

```python
@classmethod
def set_local_control_rig_int(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        value: int,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        set_key: bool = True) -> None
```

X.set_local_control_rig_int(level_sequence, control_rig, control_name, frame, value, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, set_key=True) -> None
Set ControlRig Control's int value at specific time

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a int control
    frame (FrameNumber): Time to set the value
    value (int32): The value to set
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution
    set_key (bool): If True set a key, if not just set the value

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_floats"></a>

#### set_local_control_rig_floats

```python
@classmethod
def set_local_control_rig_floats(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frames: Array[FrameNumber],
        values: Array[float],
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_local_control_rig_floats(level_sequence, control_rig, control_name, frames, values, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Set ControlRig Control's float values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a float control
    frames (Array[FrameNumber]): Times to set the values
    values (Array[float]): The values to set at those times
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_float"></a>

#### set_local_control_rig_float

```python
@classmethod
def set_local_control_rig_float(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        value: float,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        set_key: bool = True) -> None
```

X.set_local_control_rig_float(level_sequence, control_rig, control_name, frame, value, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, set_key=True) -> None
Set ControlRig Control's float value at specific time

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a float control
    frame (FrameNumber): Time to set the value
    value (float): The value to set
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution
    set_key (bool): If True set a key, if not just set the value

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_euler_transforms"></a>

#### set_local_control_rig_euler_transforms

```python
@classmethod
def set_local_control_rig_euler_transforms(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frames: Array[FrameNumber],
        values: Array[EulerTransform],
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_local_control_rig_euler_transforms(level_sequence, control_rig, control_name, frames, values, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Set ControlRig Control's EulerTransform values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a EulerTransform control
    frames (Array[FrameNumber]): Times to set the values
    values (Array[EulerTransform]): The values to set at those times
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_euler_transform"></a>

#### set_local_control_rig_euler_transform

```python
@classmethod
def set_local_control_rig_euler_transform(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        value: EulerTransform,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        set_key: bool = True) -> None
```

X.set_local_control_rig_euler_transform(level_sequence, control_rig, control_name, frame, value, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, set_key=True) -> None
Set ControlRig Control's EulerTransform value at specific time

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a EulerTransform control
    frame (FrameNumber): Time to set the value
    value (EulerTransform): The value to set
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution
    set_key (bool): If True set a key, if not just set the value

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_bools"></a>

#### set_local_control_rig_bools

```python
@classmethod
def set_local_control_rig_bools(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frames: Array[FrameNumber],
        values: Array[bool],
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_local_control_rig_bools(level_sequence, control_rig, control_name, frames, values, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Set ControlRig Control's bool values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a bool control
    frames (Array[FrameNumber]): Times to set the values
    values (Array[bool]): The values to set at those times
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

<a id="unreal.ControlRigSequencerLibrary.set_local_control_rig_bool"></a>

#### set_local_control_rig_bool

```python
@classmethod
def set_local_control_rig_bool(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        value: bool,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        set_key: bool = True) -> None
```

X.set_local_control_rig_bool(level_sequence, control_rig, control_name, frame, value, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, set_key=True) -> None
Set ControlRig Control's bool value at specific time

Args:
    level_sequence (LevelSequence): Active Sequence to set value on
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a bool control
    frame (FrameNumber): Time to set the value
    value (bool): The value to set
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution
    set_key (bool): If True set a key, if not just set the value

<a id="unreal.ControlRigSequencerLibrary.set_controls_mask"></a>

#### set_controls_mask

```python
@classmethod
def set_controls_mask(cls, section: MovieSceneSection,
                      control_names: Array[Name], visible: bool) -> None
```

X.set_controls_mask(section, control_names, visible) -> None
Set the controls mask for the given ControlNames

Args:
    section (MovieSceneSection): 
    control_names (Array[Name]): 
    visible (bool):

<a id="unreal.ControlRigSequencerLibrary.set_control_rig_world_transforms"></a>

#### set_control_rig_world_transforms

```python
@classmethod
def set_control_rig_world_transforms(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frames: Array[FrameNumber],
        world_transforms: Array[Transform],
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

X.set_control_rig_world_transforms(level_sequence, control_rig, control_name, frames, world_transforms, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Set ControlRig Control's World Transforms at a specific times.

Args:
    level_sequence (LevelSequence): Active Sequence to set transforms for. Must be loaded in Level Editor.
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control
    frames (Array[FrameNumber]): Times to set the transform
    world_transforms (Array[Transform]): 
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

<a id="unreal.ControlRigSequencerLibrary.set_control_rig_world_transform"></a>

#### set_control_rig_world_transform

```python
@classmethod
def set_control_rig_world_transform(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        world_transform: Transform,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        set_key: bool = True) -> None
```

X.set_control_rig_world_transform(level_sequence, control_rig, control_name, frame, world_transform, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, set_key=True) -> None
Set ControlRig Control's World Transform at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to set transforms for. Must be loaded in Level Editor.
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control
    frame (FrameNumber): Time to set the transform
    world_transform (Transform): World Transform to set
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution
    set_key (bool): Whether or not to set a key.

<a id="unreal.ControlRigSequencerLibrary.set_control_rig_space"></a>

#### set_control_rig_space

```python
@classmethod
def set_control_rig_space(
        cls,
        sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        space_key: RigElementKey,
        time: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> bool
```

X.set_control_rig_space(sequence, control_rig, control_name, space_key, time, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> bool
* Set the a key for the Control Rig Space for the Control at the specified time. If space is the same as the current no key witll be set.
*
*

Args:
    sequence (LevelSequence): Sequence to set the space *
    control_rig (ControlRig): ControlRig with the Control *
    control_name (Name): The name of the Control *
    space_key (RigElementKey): The new space for the Control *
    time (FrameNumber): Time to change the space. *
    time_unit (MovieSceneTimeUnit): Unit for the InTime, either in display rate or tick resolution

Returns:
    bool:

<a id="unreal.ControlRigSequencerLibrary.set_control_rig_priority_order"></a>

#### set_control_rig_priority_order

```python
@classmethod
def set_control_rig_priority_order(cls, section: MovieSceneTrack,
                                   priority_order: int) -> None
```

X.set_control_rig_priority_order(section, priority_order) -> None
Set Control Rig priority order

Args:
    section (MovieSceneTrack): 
    priority_order (int32):

<a id="unreal.ControlRigSequencerLibrary.set_control_rig_layered_mode"></a>

#### set_control_rig_layered_mode

```python
@classmethod
def set_control_rig_layered_mode(cls,
                                 track: MovieSceneControlRigParameterTrack,
                                 set_is_layered: bool) -> bool
```

X.set_control_rig_layered_mode(track, set_is_layered) -> bool
* Convert the control rig track into absolute or layered rig
*
*

Args:
    track (MovieSceneControlRigParameterTrack): Control rig track to convert *
    set_is_layered (bool): Convert to layered rig if true, or absolute if false

Returns:
    bool:

<a id="unreal.ControlRigSequencerLibrary.set_control_rig_apply_mode"></a>

#### set_control_rig_apply_mode

```python
@classmethod
def set_control_rig_apply_mode(cls, control_rig: ControlRig,
                               apply_mode: ControlRigFKRigExecuteMode) -> bool
```

X.set_control_rig_apply_mode(control_rig, apply_mode) -> bool
Set the FK Control Rig to apply mode

Args:
    control_rig (ControlRig): Rig to set
    apply_mode (ControlRigFKRigExecuteMode): Set the EControlRigFKRigExecuteMode mode (Replace,Addtiive or Direct)

Returns:
    bool: returns True if the mode was set, may not be set if the Control Rig doesn't support these modes currently only FKControlRig's do.

<a id="unreal.ControlRigSequencerLibrary.set_constraint_active_key"></a>

#### set_constraint_active_key

```python
@classmethod
def set_constraint_active_key(
        cls,
        constraint: TickableConstraint,
        active: bool,
        frame: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> bool
```

X.set_constraint_active_key(constraint, active, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> bool
Set the constraint active key in the current open Sequencer

Args:
    constraint (TickableConstraint): The constraint to set the key
    active (bool): Whether or not it's active
    frame (FrameNumber): 
    time_unit (MovieSceneTimeUnit): Unit for the time params, either in display rate or tick resolution

Returns:
    bool: Returns true if we set the constraint to be the passed in value, false if not. We may not do so if the value is the same.

<a id="unreal.ControlRigSequencerLibrary.rename_control_rig_control_channels"></a>

#### rename_control_rig_control_channels

```python
@classmethod
def rename_control_rig_control_channels(
        cls, sequence: LevelSequence, control_rig: ControlRig,
        old_control_names: Array[Name],
        new_control_names: Array[Name]) -> bool
```

X.rename_control_rig_control_channels(sequence, control_rig, old_control_names, new_control_names) -> bool
Rename the Control Rig Channels in Sequencer to the specified new control names, which should be present on the Control Rig

Args:
    sequence (LevelSequence): Sequence to rename controls
    control_rig (ControlRig): ControlRig to rename controls
    old_control_names (Array[Name]): The name of the old Control Rig Control Channels to change. Will be replaced by the corresponding name in the InNewControlNames array
    new_control_names (Array[Name]): The name of the new Control Rig Channels

Returns:
    bool: Return true if the function succeeds, false if it doesn't which can happen if the name arrays don't match in size or any of the new Control Names aren't valid

<a id="unreal.ControlRigSequencerLibrary.move_control_rig_space"></a>

#### move_control_rig_space

```python
@classmethod
def move_control_rig_space(
        cls,
        sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        time: FrameNumber,
        new_time: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> bool
```

X.move_control_rig_space(sequence, control_rig, control_name, time, new_time, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> bool
Move the Control Rig Space Key for the Control at the specified time to the new time. This will also move any Control Rig keys at this space switch boundary.

Args:
    sequence (LevelSequence): Sequence to set the space
    control_rig (ControlRig): ControlRig with the Control
    control_name (Name): The name of the Control
    time (FrameNumber): Original time of the space key
    new_time (FrameNumber): New time for the space key
    time_unit (MovieSceneTimeUnit): Unit for the time params, either in display rate or tick resolution

Returns:
    bool: Will return false if function fails, for example if there is no key at this time it will fail, or if the new time is invalid it could fail also

<a id="unreal.ControlRigSequencerLibrary.move_constraint_key"></a>

#### move_constraint_key

```python
@classmethod
def move_constraint_key(
        cls,
        constraint: TickableConstraint,
        constraint_section: MovieSceneSection,
        time: FrameNumber,
        new_time: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> bool
```

X.move_constraint_key(constraint, constraint_section, time, new_time, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> bool
Move the constraint active key in the current open Sequencer

Args:
    constraint (TickableConstraint): 
    constraint_section (MovieSceneSection): Section containing Cosntraint Key
    time (FrameNumber): Original time of the constraint key
    new_time (FrameNumber): New time for the constraint key
    time_unit (MovieSceneTimeUnit): Unit for the time params, either in display rate or tick resolution

Returns:
    bool: Will return false if function fails, for example if there is no key at this time it will fail, or if the new time is invalid it could fail also

<a id="unreal.ControlRigSequencerLibrary.merge_anim_layers"></a>

#### merge_anim_layers

```python
@classmethod
def merge_anim_layers(cls, indices: Array[int]) -> bool
```

X.merge_anim_layers(indices) -> bool
Merge specified anim layers into one layer. Will merge onto the anim layer with the lowest index

Args:
    indices (Array[int32]): The indices to merge

Returns:
    bool: Returns true if successful, false otherwise

<a id="unreal.ControlRigSequencerLibrary.load_anim_sequence_into_control_rig_section"></a>

#### load_anim_sequence_into_control_rig_section

```python
@classmethod
def load_anim_sequence_into_control_rig_section(
        cls,
        movie_scene_section: MovieSceneSection,
        anim_sequence: AnimSequence,
        skel_mesh_comp: SkeletalMeshComponent,
        start_frame: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        key_reduce: bool = False,
        tolerance: float = 0.001000,
        interpolation: MovieSceneKeyInterpolation = MovieSceneKeyInterpolation.
    SMART_AUTO,
        reset_controls: bool = True) -> bool
```

X.load_anim_sequence_into_control_rig_section(movie_scene_section, anim_sequence, skel_mesh_comp, start_frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, key_reduce=False, tolerance=0.001000, interpolation=MovieSceneKeyInterpolation.SMART_AUTO, reset_controls=True) -> bool
Load anim sequence into this control rig section

Args:
    movie_scene_section (MovieSceneSection): The MovieSceneSectionto load into
    anim_sequence (AnimSequence): The Sequence to load
    skel_mesh_comp (SkeletalMeshComponent): 
    start_frame (FrameNumber): Frame to insert the animation
    time_unit (MovieSceneTimeUnit): Unit for all frame and time values, either in display rate or tick resolution
    key_reduce (bool): If true do key reduction based upon Tolerance, if false don't
    tolerance (float): If reducing keys, tolerance about which keys will be removed, smaller tolerance, more keys usually.
    interpolation (MovieSceneKeyInterpolation): The key interpolation type to set the keys, defaults to EMovieSceneKeyInterpolation::SmartAuto
    reset_controls (bool): If true will reset all controls to initial value on every frame

Returns:
    bool: returns True if successful, False otherwise

<a id="unreal.ControlRigSequencerLibrary.is_layered_control_rig"></a>

#### is_layered_control_rig

```python
@classmethod
def is_layered_control_rig(cls, control_rig: ControlRig) -> bool
```

X.is_layered_control_rig(control_rig) -> bool
Whether or not the control rig is an Layered Control Rig.

Args:
    control_rig (ControlRig): Rig to test to see if Layered Control Rig

Returns:
    bool:

<a id="unreal.ControlRigSequencerLibrary.is_fk_control_rig"></a>

#### is_fk_control_rig

```python
@classmethod
def is_fk_control_rig(cls, control_rig: ControlRig) -> bool
```

X.is_fk_control_rig(control_rig) -> bool
Whether or not the control rig is an FK Control Rig.

Args:
    control_rig (ControlRig): Rig to test to see if FK Control Rig

Returns:
    bool:

<a id="unreal.ControlRigSequencerLibrary.import_fbx_to_control_rig_track"></a>

#### import_fbx_to_control_rig_track

```python
@classmethod
def import_fbx_to_control_rig_track(
        cls, world: World, sequence: LevelSequence,
        track: MovieSceneControlRigParameterTrack,
        section: MovieSceneControlRigParameterSection,
        selected_control_rig_names: Array[str],
        import_fbx_control_rig_settings:
    MovieSceneUserImportFBXControlRigSettings, import_filename: str) -> bool
```

X.import_fbx_to_control_rig_track(world, sequence, track, section, selected_control_rig_names, import_fbx_control_rig_settings, import_filename) -> bool
* Import FBX onto a control rig with the specified track and section
*
*

Args:
    world (World): 
    sequence (LevelSequence): Sequence to import *
    track (MovieSceneControlRigParameterTrack): Track to import onto *
    section (MovieSceneControlRigParameterSection): Section to import onto, may be null in which case we use the track's section to key *
    selected_control_rig_names (Array[str]): List of selected control rig names. Will use them if  ImportFBXControlRigSettings->bImportOntoSelectedControls is true *
    import_fbx_control_rig_settings (MovieSceneUserImportFBXControlRigSettings): Settings to control import. *
    import_filename (str): 

Returns:
    bool:

<a id="unreal.ControlRigSequencerLibrary.hide_all_controls"></a>

#### hide_all_controls

```python
@classmethod
def hide_all_controls(cls, section: MovieSceneSection) -> None
```

X.hide_all_controls(section) -> None
Hides all of the controls for the given section

Args:
    section (MovieSceneSection):

<a id="unreal.ControlRigSequencerLibrary.get_world_space_reference_key"></a>

#### get_world_space_reference_key

```python
@classmethod
def get_world_space_reference_key(cls) -> RigElementKey
```

X.get_world_space_reference_key() -> RigElementKey
* Get the default world space key, can be used a world space.

Returns:
    RigElementKey:

<a id="unreal.ControlRigSequencerLibrary.get_visible_control_rigs"></a>

#### get_visible_control_rigs

```python
@classmethod
def get_visible_control_rigs(cls) -> Array[ControlRig]
```

X.get_visible_control_rigs() -> Array[ControlRig]
Get all of the visible control rigs in the level

Returns:
    Array[ControlRig]: returns list of visible Control Rigs

<a id="unreal.ControlRigSequencerLibrary.get_skeletal_mesh_component_world_transforms"></a>

#### get_skeletal_mesh_component_world_transforms

```python
@classmethod
def get_skeletal_mesh_component_world_transforms(
        cls,
        level_sequence: LevelSequence,
        skeletal_mesh_component: SkeletalMeshComponent,
        frames: Array[FrameNumber],
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        reference_name: Name = "None") -> Array[Transform]
```

X.get_skeletal_mesh_component_world_transforms(level_sequence, skeletal_mesh_component, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, reference_name="None") -> Array[Transform]
Get SkeletalMeshComponents World Transforms at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to get transform for
    skeletal_mesh_component (SkeletalMeshComponent): The SkeletalMeshComponent
    frames (Array[FrameNumber]): Times to get the transform
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution
    reference_name (Name): Optional name of the referencer

Returns:
    Array[Transform]: Returns World Transforms

<a id="unreal.ControlRigSequencerLibrary.get_skeletal_mesh_component_world_transform"></a>

#### get_skeletal_mesh_component_world_transform

```python
@classmethod
def get_skeletal_mesh_component_world_transform(
        cls,
        level_sequence: LevelSequence,
        skeletal_mesh_component: SkeletalMeshComponent,
        frame: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE,
        reference_name: Name = "None") -> Transform
```

X.get_skeletal_mesh_component_world_transform(level_sequence, skeletal_mesh_component, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE, reference_name="None") -> Transform
Get SkeletalMeshComponent World Transform at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to get transform for
    skeletal_mesh_component (SkeletalMeshComponent): The SkeletalMeshComponent
    frame (FrameNumber): Time to get the transform
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution
    reference_name (Name): Optional name of the referencer

Returns:
    Transform: Returns World Transform

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_vector2_ds"></a>

#### get_local_control_rig_vector2_ds

```python
@classmethod
def get_local_control_rig_vector2_ds(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frames: Array[FrameNumber],
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[Vector2D]
```

X.get_local_control_rig_vector2_ds(level_sequence, control_rig, control_name, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Vector2D]
Get ControlRig Control's Vector2D values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Vector2D control
    frames (Array[FrameNumber]): Times to get the values
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Array[Vector2D]: Returns Values at those times

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_vector2d"></a>

#### get_local_control_rig_vector2d

```python
@classmethod
def get_local_control_rig_vector2d(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frame: FrameNumber,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Vector2D
```

X.get_local_control_rig_vector2d(level_sequence, control_rig, control_name, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Vector2D
Get ControlRig Control's Vector2D value at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Vector2D control
    frame (FrameNumber): Time to get the value
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Vector2D: Returns Value at that time

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_transforms"></a>

#### get_local_control_rig_transforms

```python
@classmethod
def get_local_control_rig_transforms(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frames: Array[FrameNumber],
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[Transform]
```

X.get_local_control_rig_transforms(level_sequence, control_rig, control_name, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Transform]
Get ControlRig Control's Transform values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Transform control
    frames (Array[FrameNumber]): Times to get the values
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Array[Transform]: Returns Values at those times

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_transform_no_scales"></a>

#### get_local_control_rig_transform_no_scales

```python
@classmethod
def get_local_control_rig_transform_no_scales(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frames: Array[FrameNumber],
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[TransformNoScale]
```

X.get_local_control_rig_transform_no_scales(level_sequence, control_rig, control_name, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[TransformNoScale]
Get ControlRig Control's TransformNoScale values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a TransformNoScale control
    frames (Array[FrameNumber]): Times to get the values
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Array[TransformNoScale]: Returns Values at those times

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_transform_no_scale"></a>

#### get_local_control_rig_transform_no_scale

```python
@classmethod
def get_local_control_rig_transform_no_scale(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frame: FrameNumber,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> TransformNoScale
```

X.get_local_control_rig_transform_no_scale(level_sequence, control_rig, control_name, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> TransformNoScale
Get ControlRig Control's TransformNoScale value at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a TransformNoScale control
    frame (FrameNumber): Time to get the value
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    TransformNoScale: Returns Value at that time

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_transform"></a>

#### get_local_control_rig_transform

```python
@classmethod
def get_local_control_rig_transform(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frame: FrameNumber,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Transform
```

X.get_local_control_rig_transform(level_sequence, control_rig, control_name, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Transform
Get ControlRig Control's Transform value at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Transform control
    frame (FrameNumber): Time to get the value
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Transform: Returns Value at that time

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_scales"></a>

#### get_local_control_rig_scales

```python
@classmethod
def get_local_control_rig_scales(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frames: Array[FrameNumber],
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[Vector]
```

X.get_local_control_rig_scales(level_sequence, control_rig, control_name, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Vector]
Get ControlRig Control's Scale values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Scale control
    frames (Array[FrameNumber]): Times to get the values
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Array[Vector]: Returns Values at those times

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_scale"></a>

#### get_local_control_rig_scale

```python
@classmethod
def get_local_control_rig_scale(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Vector
```

X.get_local_control_rig_scale(level_sequence, control_rig, control_name, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Vector
Get ControlRig Control's Scale value at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Scale control
    frame (FrameNumber): Time to get the value
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Vector: Returns Value at that time

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_rotators"></a>

#### get_local_control_rig_rotators

```python
@classmethod
def get_local_control_rig_rotators(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frames: Array[FrameNumber],
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[Rotator]
```

X.get_local_control_rig_rotators(level_sequence, control_rig, control_name, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Rotator]
Get ControlRig Control's Rotator values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Rotator control
    frames (Array[FrameNumber]): Times to get the values
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Array[Rotator]: Returns Values at those times

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_rotator"></a>

#### get_local_control_rig_rotator

```python
@classmethod
def get_local_control_rig_rotator(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frame: FrameNumber,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Rotator
```

X.get_local_control_rig_rotator(level_sequence, control_rig, control_name, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Rotator
Get ControlRig Control's Rotator value at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Rotator control
    frame (FrameNumber): Time to get the value
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Rotator: Returns Value at that time

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_positions"></a>

#### get_local_control_rig_positions

```python
@classmethod
def get_local_control_rig_positions(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frames: Array[FrameNumber],
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[Vector]
```

X.get_local_control_rig_positions(level_sequence, control_rig, control_name, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Vector]
Get ControlRig Control's Position values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Position control
    frames (Array[FrameNumber]): Times to get the values
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Array[Vector]: Returns Values at those times

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_position"></a>

#### get_local_control_rig_position

```python
@classmethod
def get_local_control_rig_position(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Vector
```

X.get_local_control_rig_position(level_sequence, control_rig, control_name, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Vector
Get ControlRig Control's Position value at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a Position control
    frame (FrameNumber): Time to get the value
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Vector: Returns Value at that time

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_ints"></a>

#### get_local_control_rig_ints

```python
@classmethod
def get_local_control_rig_ints(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frames: Array[FrameNumber],
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[int]
```

X.get_local_control_rig_ints(level_sequence, control_rig, control_name, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[int32]
Get ControlRig Control's integer values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a intteger control
    frames (Array[FrameNumber]): Times to get the values
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Array[int32]: Returns Values at those times

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_int"></a>

#### get_local_control_rig_int

```python
@classmethod
def get_local_control_rig_int(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> int
```

X.get_local_control_rig_int(level_sequence, control_rig, control_name, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> int32
Get ControlRig Control's integer value at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a integer control
    frame (FrameNumber): Time to get the value
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    int32: Returns Value at that time

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_floats"></a>

#### get_local_control_rig_floats

```python
@classmethod
def get_local_control_rig_floats(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frames: Array[FrameNumber],
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[float]
```

X.get_local_control_rig_floats(level_sequence, control_rig, control_name, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[float]
Get ControlRig Control's float values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a float control
    frames (Array[FrameNumber]): Times to get the values
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Array[float]: Returns Values at those times

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_float"></a>

#### get_local_control_rig_float

```python
@classmethod
def get_local_control_rig_float(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> float
```

X.get_local_control_rig_float(level_sequence, control_rig, control_name, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> float
Get ControlRig Control's float value at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a float control
    frame (FrameNumber): Time to get the value
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    float: Returns Value at that time

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_euler_transforms"></a>

#### get_local_control_rig_euler_transforms

```python
@classmethod
def get_local_control_rig_euler_transforms(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frames: Array[FrameNumber],
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[EulerTransform]
```

X.get_local_control_rig_euler_transforms(level_sequence, control_rig, control_name, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[EulerTransform]
Get ControlRig Control's EulerTransform values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a EulerTransform control
    frames (Array[FrameNumber]): Times to get the values
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Array[EulerTransform]: Returns Values at those times

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_euler_transform"></a>

#### get_local_control_rig_euler_transform

```python
@classmethod
def get_local_control_rig_euler_transform(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frame: FrameNumber,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> EulerTransform
```

X.get_local_control_rig_euler_transform(level_sequence, control_rig, control_name, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> EulerTransform
Get ControlRig Control's EulerTransform value at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a EulerTransfom control
    frame (FrameNumber): Time to get the value
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    EulerTransform: Returns Value at that time

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_bools"></a>

#### get_local_control_rig_bools

```python
@classmethod
def get_local_control_rig_bools(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frames: Array[FrameNumber],
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[bool]
```

X.get_local_control_rig_bools(level_sequence, control_rig, control_name, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[bool]
Get ControlRig Control's bool values at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a bool control
    frames (Array[FrameNumber]): Times to get the values
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Array[bool]: Returns Values at those times

<a id="unreal.ControlRigSequencerLibrary.get_local_control_rig_bool"></a>

#### get_local_control_rig_bool

```python
@classmethod
def get_local_control_rig_bool(
        cls,
        level_sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        frame: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> bool
```

X.get_local_control_rig_bool(level_sequence, control_rig, control_name, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> bool
Get ControlRig Control's bool value at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to get value for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control, should be a bool control
    frame (FrameNumber): Time to get the value
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    bool: Returns Value at that time

<a id="unreal.ControlRigSequencerLibrary.get_fk_control_rig_apply_mode"></a>

#### get_fk_control_rig_apply_mode

```python
@classmethod
def get_fk_control_rig_apply_mode(
        cls, control_rig: ControlRig) -> ControlRigFKRigExecuteMode
```

X.get_fk_control_rig_apply_mode(control_rig) -> ControlRigFKRigExecuteMode
Get FKControlRig Apply Mode.

Args:
    control_rig (ControlRig): Rig to test

Returns:
    ControlRigFKRigExecuteMode: The EControlRigFKRigExecuteMode mode it is in, either Replace,Additive or Direct

<a id="unreal.ControlRigSequencerLibrary.get_default_parent_key"></a>

#### get_default_parent_key

```python
@classmethod
def get_default_parent_key(cls) -> RigElementKey
```

X.get_default_parent_key() -> RigElementKey
* Get the default parent key, can be used a parent space.

Returns:
    RigElementKey:

<a id="unreal.ControlRigSequencerLibrary.get_controls_mask"></a>

#### get_controls_mask

```python
@classmethod
def get_controls_mask(cls, section: MovieSceneSection,
                      control_name: Name) -> bool
```

X.get_controls_mask(section, control_name) -> bool
Get the controls mask for the given ControlName

Args:
    section (MovieSceneSection): 
    control_name (Name): 

Returns:
    bool:

<a id="unreal.ControlRigSequencerLibrary.get_control_rig_world_transforms"></a>

#### get_control_rig_world_transforms

```python
@classmethod
def get_control_rig_world_transforms(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frames: Array[FrameNumber],
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[Transform]
```

X.get_control_rig_world_transforms(level_sequence, control_rig, control_name, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Transform]
Get ControlRig Control's World Transforms at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to get transform for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control
    frames (Array[FrameNumber]): Times to get the transform
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Array[Transform]: Returns World Transforms

<a id="unreal.ControlRigSequencerLibrary.get_control_rig_world_transform"></a>

#### get_control_rig_world_transform

```python
@classmethod
def get_control_rig_world_transform(
    cls,
    level_sequence: LevelSequence,
    control_rig: ControlRig,
    control_name: Name,
    frame: FrameNumber,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Transform
```

X.get_control_rig_world_transform(level_sequence, control_rig, control_name, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Transform
Get ControlRig Control's World Transform at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to get transform for
    control_rig (ControlRig): The ControlRig
    control_name (Name): Name of the Control
    frame (FrameNumber): Time to get the transform
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Transform: Returns World Transform

<a id="unreal.ControlRigSequencerLibrary.get_control_rigs"></a>

#### get_control_rigs

```python
@classmethod
def get_control_rigs(
        cls, level_sequence: LevelSequence
) -> Array[ControlRigSequencerBindingProxy]
```

X.get_control_rigs(level_sequence) -> Array[ControlRigSequencerBindingProxy]
Get all of the control rigs and their bindings in the level sequence

Args:
    level_sequence (LevelSequence): The movie scene sequence to look for Control Rigs

Returns:
    Array[ControlRigSequencerBindingProxy]: returns list of Control Rigs in the level sequence.

<a id="unreal.ControlRigSequencerLibrary.get_control_rig_priority_order"></a>

#### get_control_rig_priority_order

```python
@classmethod
def get_control_rig_priority_order(cls, section: MovieSceneTrack) -> int
```

X.get_control_rig_priority_order(section) -> int32
Get Control Rig prirority order

Args:
    section (MovieSceneTrack): 

Returns:
    int32:

<a id="unreal.ControlRigSequencerLibrary.get_constraints_for_handle"></a>

#### get_constraints_for_handle

```python
@classmethod
def get_constraints_for_handle(
        cls, world: World,
        child: TransformableHandle) -> Array[TickableConstraint]
```

X.get_constraints_for_handle(world, child) -> Array[TickableConstraint]
Get all constraints for this object, which is described by a transformable handle

Args:
    world (World): 
    child (TransformableHandle): The handle to look for constraints controlling it

Returns:
    Array[TickableConstraint]: Returns array of Constraints this handle is constrained to.

<a id="unreal.ControlRigSequencerLibrary.get_constraint_keys"></a>

#### get_constraint_keys

```python
@classmethod
def get_constraint_keys(
    cls,
    constraint: TickableConstraint,
    constraint_section: MovieSceneSection,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Optional[Tuple[Array[bool], Array[FrameNumber]]]
```

X.get_constraint_keys(constraint, constraint_section, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> (out_bools=Array[bool], out_frames=Array[FrameNumber]) or None
Get the constraint keys for the specified constraint

Args:
    constraint (TickableConstraint): The constraint to get
    constraint_section (MovieSceneSection): Section containing Cosntraint Key
    time_unit (MovieSceneTimeUnit): Unit for the time params, either in display rate or tick resolution

Returns:
    tuple or None: Returns true if we got the keys from this constraint

    out_bools (Array[bool]): Array of whether or not it's active at the specified times

    out_frames (Array[FrameNumber]): The Times for the keys

<a id="unreal.ControlRigSequencerLibrary.get_anim_layers"></a>

#### get_anim_layers

```python
@classmethod
def get_anim_layers(cls) -> Array[AnimLayer]
```

X.get_anim_layers() -> Array[AnimLayer]
Get the animation layer objects

Returns:
    Array[AnimLayer]: Returns array of anim layer objects if they exist on active Sequencer

<a id="unreal.ControlRigSequencerLibrary.get_anim_layer_index"></a>

#### get_anim_layer_index

```python
@classmethod
def get_anim_layer_index(cls, anim_layer: AnimLayer) -> int
```

X.get_anim_layer_index(anim_layer) -> int32
Helper function to get the index in the anim layer array from the anim layer

Args:
    anim_layer (AnimLayer): 

Returns:
    int32: Returns index for the anim layer or INDEX_NONE(-1) if it doesn't exist

<a id="unreal.ControlRigSequencerLibrary.get_actor_world_transforms"></a>

#### get_actor_world_transforms

```python
@classmethod
def get_actor_world_transforms(
    cls,
    level_sequence: LevelSequence,
    actor: Actor,
    frames: Array[FrameNumber],
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Array[Transform]
```

X.get_actor_world_transforms(level_sequence, actor, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Transform]
Get Actors World Transforms at specific times

Args:
    level_sequence (LevelSequence): Active Sequence to get transform for
    actor (Actor): The actor
    frames (Array[FrameNumber]): Times to get the transform
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Array[Transform]: Returns World Transforms

<a id="unreal.ControlRigSequencerLibrary.get_actor_world_transform"></a>

#### get_actor_world_transform

```python
@classmethod
def get_actor_world_transform(
    cls,
    level_sequence: LevelSequence,
    actor: Actor,
    frame: FrameNumber,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> Transform
```

X.get_actor_world_transform(level_sequence, actor, frame, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> Transform
Get Actors World Transform at a specific time

Args:
    level_sequence (LevelSequence): Active Sequence to get transform for
    actor (Actor): The actor
    frame (FrameNumber): Time to get the transform
    time_unit (MovieSceneTimeUnit): Unit for frame values, either in display rate or tick resolution

Returns:
    Transform: Returns World Transform

<a id="unreal.ControlRigSequencerLibrary.find_or_create_control_rig_track"></a>

#### find_or_create_control_rig_track

```python
@classmethod
def find_or_create_control_rig_track(
        cls,
        world: World,
        level_sequence: LevelSequence,
        control_rig_class: Class,
        binding: MovieSceneBindingProxy,
        is_layered_control_rig: bool = False) -> MovieSceneTrack
```

X.find_or_create_control_rig_track(world, level_sequence, control_rig_class, binding, is_layered_control_rig=False) -> MovieSceneTrack
Find or create a Control Rig track of a specific class based upon the binding

Args:
    world (World): The world used to spawn into temporarily if binding is a spawnable
    level_sequence (LevelSequence): The LevelSequence to find or create
    control_rig_class (type(Class)): The class of the Control Rig
    binding (MovieSceneBindingProxy): The binding (actor or component binding) to find or create the Control Rig track
    is_layered_control_rig (bool): 

Returns:
    MovieSceneTrack: returns Return the found or created track

<a id="unreal.ControlRigSequencerLibrary.find_or_create_control_rig_component_track"></a>

#### find_or_create_control_rig_component_track

```python
@classmethod
def find_or_create_control_rig_component_track(
        cls, world: World, level_sequence: LevelSequence,
        binding: MovieSceneBindingProxy) -> Array[MovieSceneTrack]
```

X.find_or_create_control_rig_component_track(world, level_sequence, binding) -> Array[MovieSceneTrack]
Find or create a Control Rig Component

Args:
    world (World): The world used to spawn into temporarily if binding is a spawnable
    level_sequence (LevelSequence): The LevelSequence to find or create
    binding (MovieSceneBindingProxy): The binding (actor or component binding) to find or create the Control Rig tracks

Returns:
    Array[MovieSceneTrack]: returns Find array of component Control Rigs that were found or created

<a id="unreal.ControlRigSequencerLibrary.export_fbx_from_control_rig_section"></a>

#### export_fbx_from_control_rig_section

```python
@classmethod
def export_fbx_from_control_rig_section(
    cls, sequence: LevelSequence,
    section: MovieSceneControlRigParameterSection,
    export_fbx_control_rig_settings: MovieSceneUserExportFBXControlRigSettings
) -> bool
```

X.export_fbx_from_control_rig_section(sequence, section, export_fbx_control_rig_settings) -> bool
Exports an FBX from the given control rig section.

Args:
    sequence (LevelSequence): 
    section (MovieSceneControlRigParameterSection): 
    export_fbx_control_rig_settings (MovieSceneUserExportFBXControlRigSettings): 

Returns:
    bool:

<a id="unreal.ControlRigSequencerLibrary.duplicate_anim_layer"></a>

#### duplicate_anim_layer

```python
@classmethod
def duplicate_anim_layer(cls, index: int) -> int
```

X.duplicate_anim_layer(index) -> int32
Duplicate anim layer at specified index

Args:
    index (int32): The index where the anim layer exists

Returns:
    int32: Returns index of new layer, -1 if none created

<a id="unreal.ControlRigSequencerLibrary.delete_control_rig_space"></a>

#### delete_control_rig_space

```python
@classmethod
def delete_control_rig_space(
        cls,
        sequence: LevelSequence,
        control_rig: ControlRig,
        control_name: Name,
        time: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> bool
```

X.delete_control_rig_space(sequence, control_rig, control_name, time, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> bool
Delete the Control Rig Space Key for the Control at the specified time. This will delete any attached Control Rig keys at this time and will perform any needed compensation to the new space.

Args:
    sequence (LevelSequence): Sequence to set the space
    control_rig (ControlRig): ControlRig with the Control
    control_name (Name): The name of the Control
    time (FrameNumber): Time to delete the space.
    time_unit (MovieSceneTimeUnit): Unit for the InTime, either in display rate or tick resolution

Returns:
    bool: Will return false if function fails,  for example if there is no key at this time it will fail.

<a id="unreal.ControlRigSequencerLibrary.delete_constraint_key"></a>

#### delete_constraint_key

```python
@classmethod
def delete_constraint_key(
        cls,
        constraint: TickableConstraint,
        constraint_section: MovieSceneSection,
        time: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> bool
```

X.delete_constraint_key(constraint, constraint_section, time, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> bool
Delete the Key for the Constraint at the specified time.

Args:
    constraint (TickableConstraint): 
    constraint_section (MovieSceneSection): Section containing Cosntraint Key
    time (FrameNumber): Time to delete the constraint.
    time_unit (MovieSceneTimeUnit): Unit for the InTime, either in display rate or tick resolution

Returns:
    bool: Will return false if function fails,  for example if there is no key at this time it will fail.

<a id="unreal.ControlRigSequencerLibrary.delete_anim_layer"></a>

#### delete_anim_layer

```python
@classmethod
def delete_anim_layer(cls, index: int) -> bool
```

X.delete_anim_layer(index) -> bool
Delete anim layer at specified index

Args:
    index (int32): The index where the anim layer exists

Returns:
    bool: Returns true if successful, false otherwise

<a id="unreal.ControlRigSequencerLibrary.compensate_all"></a>

#### compensate_all

```python
@classmethod
def compensate_all(cls, constraint: TickableConstraint) -> bool
```

X.compensate_all(constraint) -> bool
Compensate constraint at all keys

Args:
    constraint (TickableConstraint): The constraint to compensate

Returns:
    bool: Returns true if it can compensate

<a id="unreal.ControlRigSequencerLibrary.compensate"></a>

#### compensate

```python
@classmethod
def compensate(
        cls,
        constraint: TickableConstraint,
        time: FrameNumber,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> bool
```

X.compensate(constraint, time, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> bool
Compensate constraint at the specfied time

Args:
    constraint (TickableConstraint): The constraint to compensate
    time (FrameNumber): Time to compensate
    time_unit (MovieSceneTimeUnit): Unit for the InTime, either in display rate or tick resolution

Returns:
    bool: Returns true if it can compensate

<a id="unreal.ControlRigSequencerLibrary.collapse_control_rig_anim_layers_with_settings"></a>

#### collapse_control_rig_anim_layers_with_settings

```python
@classmethod
def collapse_control_rig_anim_layers_with_settings(
        cls, sequence: LevelSequence,
        track: MovieSceneControlRigParameterTrack,
        settings: BakingAnimationKeySettings) -> bool
```

X.collapse_control_rig_anim_layers_with_settings(sequence, track, settings) -> bool
* Collapse and bake all sections and layers on a control rig track to just one section using passed in settings.
*
*

Args:
    sequence (LevelSequence): Sequence that has track to collapse *
    track (MovieSceneControlRigParameterTrack): Track for layers to collapse *
    settings (BakingAnimationKeySettings): Settings that determine how to collapse

Returns:
    bool:

<a id="unreal.ControlRigSequencerLibrary.collapse_control_rig_anim_layers"></a>

#### collapse_control_rig_anim_layers

```python
@classmethod
def collapse_control_rig_anim_layers(cls,
                                     sequence: LevelSequence,
                                     track: MovieSceneControlRigParameterTrack,
                                     key_reduce: bool = False,
                                     tolerance: float = 0.001000) -> bool
```

X.collapse_control_rig_anim_layers(sequence, track, key_reduce=False, tolerance=0.001000) -> bool
* Collapse and bake all sections and layers on a control rig track to just one section.
*
*

Args:
    sequence (LevelSequence): Sequence that has track to collapse *
    track (MovieSceneControlRigParameterTrack): Track for layers to collapse *
    key_reduce (bool): If true do key reduction based upon Tolerance, if false don't *
    tolerance (float): If reducing keys, tolerance about which keys will be removed, smaller tolerance, more keys usually.

Returns:
    bool:

<a id="unreal.ControlRigSequencerLibrary.blend_values_on_selected"></a>

#### blend_values_on_selected

```python
@classmethod
def blend_values_on_selected(cls, level_sequence: LevelSequence,
                             blend_operation: AnimToolBlendOperation,
                             blend_value: float) -> bool
```

X.blend_values_on_selected(level_sequence, blend_operation, blend_value) -> bool
Peform specified blend operation based upon selected keys in the curve editor or selected control rig controls

Args:
    level_sequence (LevelSequence): The LevelSequence that's loaded in the editor
    blend_operation (AnimToolBlendOperation): 
    blend_value (float): The blend value to use, range from -1(blend to previous) to 1(blend to next)

Returns:
    bool:

<a id="unreal.ControlRigSequencerLibrary.bake_to_control_rig"></a>

#### bake_to_control_rig

```python
@classmethod
def bake_to_control_rig(cls,
                        world: World,
                        level_sequence: LevelSequence,
                        control_rig_class: Class,
                        export_options: AnimSeqExportOption,
                        reduce_keys: bool,
                        tolerance: float,
                        binding: MovieSceneBindingProxy,
                        reset_controls: bool = True) -> bool
```

X.bake_to_control_rig(world, level_sequence, control_rig_class, export_options, reduce_keys, tolerance, binding, reset_controls=True) -> bool
Bake the current animation in the binding to a Control Rig track

Args:
    world (World): The active world
    level_sequence (LevelSequence): The LevelSequence we are baking
    control_rig_class (type(Class)): The class of the Control Rig
    export_options (AnimSeqExportOption): Export options for creating an animation sequence
    reduce_keys (bool): 
    tolerance (float): If reducing keys, tolerance about which keys will be removed, smaller tolerance, more keys usually.
    binding (MovieSceneBindingProxy): The binding upon which to bake
    reset_controls (bool): If true will reset all controls to initial value on every frame

Returns:
    bool: returns True if successful, False otherwise

<a id="unreal.ControlRigSequencerLibrary.bake_control_rig_space"></a>

#### bake_control_rig_space

```python
@classmethod
def bake_control_rig_space(
        cls,
        sequence: LevelSequence,
        control_rig: ControlRig,
        control_names: Array[Name],
        settings: RigSpacePickerBakeSettings,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> bool
```

X.bake_control_rig_space(sequence, control_rig, control_names, settings, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> bool
Bake specified Control Rig Controls to a specified Space based upon the current settings

Args:
    sequence (LevelSequence): Sequence to bake
    control_rig (ControlRig): ControlRig to bake
    control_names (Array[Name]): The name of the Controls to bake
    settings (RigSpacePickerBakeSettings): The settings for the bake, e.g, how long to bake, to key reduce etc.
    time_unit (MovieSceneTimeUnit): Unit for the start and end times in the InSettings parameter.

Returns:
    bool:

<a id="unreal.ControlRigSequencerLibrary.bake_constraints"></a>

#### bake_constraints

```python
@classmethod
def bake_constraints(
    cls, world: World, settings: BakingAnimationKeySettings
) -> Optional[Array[TickableConstraint]]
```

X.bake_constraints(world, settings) -> Array[TickableConstraint] or None
Bake the constraint to keys based on the passed in settings. This will use the open sequencer to bake. See ConstraintsScriptingLibrary to get the list of available constraints

Args:
    world (World): The active world
    settings (BakingAnimationKeySettings): Settings to use for baking

Returns:
    Array[TickableConstraint] or None: Returns True if successful, False otherwise

    constraints (Array[TickableConstraint]): The Constraints tobake.  After baking they will be keyed to be inactive of the range of frames that are baked

<a id="unreal.ControlRigSequencerLibrary.bake_constraint"></a>

#### bake_constraint

```python
@classmethod
def bake_constraint(
        cls,
        world: World,
        constraint: TickableConstraint,
        frames: Array[FrameNumber],
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> bool
```

X.bake_constraint(world, constraint, frames, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> bool
Bake the constraint to keys based on the passed in frames. This will use the open sequencer to bake. See ConstraintsScriptingLibrary to get the list of available constraints

Args:
    world (World): The active world
    constraint (TickableConstraint): The Constraint to bake. After baking it will be keyed to be inactive of the range of frames that are baked
    frames (Array[FrameNumber]): The frames to bake, if the array is empty it will use the active time ranges of the constraint to determine where it should bake
    time_unit (MovieSceneTimeUnit): Unit for all frame and time values, either in display rate or tick resolution

Returns:
    bool: Returns True if successful, False otherwise

<a id="unreal.ControlRigSequencerLibrary.add_constraint"></a>

#### add_constraint

```python
@classmethod
def add_constraint(cls, world: World, type: TransformConstraintType,
                   child: TransformableHandle, parent: TransformableHandle,
                   maintain_offset: bool) -> TickableConstraint
```

X.add_constraint(world, type, child, parent, maintain_offset) -> TickableConstraint
Add a constraint possibly adding to sequencer also if one is open.

Args:
    world (World): The active world
    type (TransformConstraintType): Type of constraint to create
    child (TransformableHandle): The handle to the transormable to be constrainted
    parent (TransformableHandle): The handle to the parent of the constraint
    maintain_offset (bool): Whether to maintain offset between child and parent when setting the constraint

Returns:
    TickableConstraint: Returns the constraint if created all nullptr if not

<a id="unreal.ControlRigSequencerLibrary.add_anim_layer_from_selection"></a>

#### add_anim_layer_from_selection

```python
@classmethod
def add_anim_layer_from_selection(cls) -> int
```

X.add_anim_layer_from_selection() -> int32
Add anim layer from objects selected in Sequencer

Returns:
    int32: Returns Index of created anim layer

<a id="unreal.ControlRigControlsProxy"></a>