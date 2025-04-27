## TakeRecorderParameters Objects

```python
class TakeRecorderParameters(StructBase)
```

Structure housing all configurable parameters for a take recorder instance

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorder
- **File**: TakeRecorderParameters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``project`` (TakeRecorderProjectParameters):  [Read-Write]
- ``start_frame`` (FrameNumber):  [Read-Write]
- ``take_recorder_mode`` (TakeRecorderMode):  [Read-Write]
- ``user`` (TakeRecorderUserParameters):  [Read-Write]

<a id="unreal.TakeRecorderParameters.__init__"></a>

#### __init__

```python
def __init__(user: TakeRecorderUserParameters = [
    False, 0.000000, 1.000000, True, False, True, 0.000100, False, True, False
],
             project: TakeRecorderProjectParameters = [[
                 ""
             ], "", "", UpdateClockSource.RELATIVE_TIMECODE, True, False,
                                                       False, False, True],
             take_recorder_mode: TakeRecorderMode = TakeRecorderMode.
             RECORD_NEW_SEQUENCE,
             start_frame: FrameNumber = [0]) -> None
```

<a id="unreal.TakeRecorderParameters.user"></a>

#### user

```python
@property
def user() -> TakeRecorderUserParameters
```

(TakeRecorderUserParameters):  [Read-Write]

<a id="unreal.TakeRecorderParameters.user"></a>

#### user

```python
@user.setter
def user(value: TakeRecorderUserParameters) -> None
```

<a id="unreal.TakeRecorderParameters.project"></a>

#### project

```python
@property
def project() -> TakeRecorderProjectParameters
```

(TakeRecorderProjectParameters):  [Read-Write]

<a id="unreal.TakeRecorderParameters.project"></a>

#### project

```python
@project.setter
def project(value: TakeRecorderProjectParameters) -> None
```

<a id="unreal.TakeRecorderParameters.take_recorder_mode"></a>

#### take_recorder_mode

```python
@property
def take_recorder_mode() -> TakeRecorderMode
```

(TakeRecorderMode):  [Read-Write]

<a id="unreal.TakeRecorderParameters.take_recorder_mode"></a>

#### take_recorder_mode

```python
@take_recorder_mode.setter
def take_recorder_mode(value: TakeRecorderMode) -> None
```

<a id="unreal.TakeRecorderParameters.start_frame"></a>

#### start_frame

```python
@property
def start_frame() -> FrameNumber
```

(FrameNumber):  [Read-Write]

<a id="unreal.TakeRecorderParameters.start_frame"></a>

#### start_frame

```python
@start_frame.setter
def start_frame(value: FrameNumber) -> None
```

<a id="unreal.RigVMUserWorkflow"></a>