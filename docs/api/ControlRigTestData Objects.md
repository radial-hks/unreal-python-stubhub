## ControlRigTestData Objects

```python
class ControlRigTestData(Object)
```

Control Rig Test Data

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigTestData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_rig_object_path`` (SoftObjectPath):  [Read-Only]
- ``frames_to_skip`` (Array[int32]):  [Read-Write]
- ``initial`` (ControlRigTestDataFrame):  [Read-Only]
- ``input_frames`` (Array[ControlRigTestDataFrame]):  [Read-Only]
- ``output_frames`` (Array[ControlRigTestDataFrame]):  [Read-Only]
- ``tolerance`` (double):  [Read-Write]

<a id="unreal.ControlRigTestData.control_rig_object_path"></a>

#### control_rig_object_path

```python
@property
def control_rig_object_path() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Only]

<a id="unreal.ControlRigTestData.initial"></a>

#### initial

```python
@property
def initial() -> ControlRigTestDataFrame
```

(ControlRigTestDataFrame):  [Read-Only]

<a id="unreal.ControlRigTestData.input_frames"></a>

#### input_frames

```python
@property
def input_frames() -> Array[ControlRigTestDataFrame]
```

(Array[ControlRigTestDataFrame]):  [Read-Only]

<a id="unreal.ControlRigTestData.output_frames"></a>

#### output_frames

```python
@property
def output_frames() -> Array[ControlRigTestDataFrame]
```

(Array[ControlRigTestDataFrame]):  [Read-Only]

<a id="unreal.ControlRigTestData.frames_to_skip"></a>

#### frames_to_skip

```python
@property
def frames_to_skip() -> Array[int]
```

(Array[int32]):  [Read-Only]

<a id="unreal.ControlRigTestData.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> float
```

(double):  [Read-Only]

<a id="unreal.ControlRigTestData.setup_replay"></a>

#### setup_replay

```python
def setup_replay(control_rig: ControlRig, ground_truth: bool = True) -> bool
```

x.setup_replay(control_rig, ground_truth=True) -> bool
Setup Replay

Args:
    control_rig (ControlRig): 
    ground_truth (bool): 

Returns:
    bool:

<a id="unreal.ControlRigTestData.release_replay"></a>

#### release_replay

```python
def release_replay() -> None
```

x.release_replay() -> None
Release Replay

<a id="unreal.ControlRigTestData.record"></a>

#### record

```python
def record(control_rig: ControlRig,
           recording_duration: float = 0.000000) -> bool
```

x.record(control_rig, recording_duration=0.000000) -> bool
Record

Args:
    control_rig (ControlRig): 
    recording_duration (double): 

Returns:
    bool:

<a id="unreal.ControlRigTestData.is_replaying"></a>

#### is_replaying

```python
def is_replaying() -> bool
```

x.is_replaying() -> bool
Is Replaying

Returns:
    bool:

<a id="unreal.ControlRigTestData.is_recording"></a>

#### is_recording

```python
def is_recording() -> bool
```

x.is_recording() -> bool
Is Recording

Returns:
    bool:

<a id="unreal.ControlRigTestData.get_time_range"></a>

#### get_time_range

```python
def get_time_range(input: bool = False) -> Vector2D
```

x.get_time_range(input=False) -> Vector2D
Get Time Range

Args:
    input (bool): 

Returns:
    Vector2D:

<a id="unreal.ControlRigTestData.get_playback_mode"></a>

#### get_playback_mode

```python
def get_playback_mode() -> ControlRigTestDataPlaybackMode
```

x.get_playback_mode() -> ControlRigTestDataPlaybackMode
Get Playback Mode

Returns:
    ControlRigTestDataPlaybackMode:

<a id="unreal.ControlRigTestData.get_frame_index_for_time"></a>

#### get_frame_index_for_time

```python
def get_frame_index_for_time(seconds: float, input: bool = False) -> int
```

x.get_frame_index_for_time(seconds, input=False) -> int32
Get Frame Index for Time

Args:
    seconds (double): 
    input (bool): 

Returns:
    int32:

<a id="unreal.ControlRigTestData.create_new_asset"></a>

#### create_new_asset

```python
@classmethod
def create_new_asset(cls, desired_package_path: str,
                     blueprint_path_name: str) -> ControlRigTestData
```

X.create_new_asset(desired_package_path, blueprint_path_name) -> ControlRigTestData
Create New Asset

Args:
    desired_package_path (str): 
    blueprint_path_name (str): 

Returns:
    ControlRigTestData:

<a id="unreal.ModularRigController"></a>