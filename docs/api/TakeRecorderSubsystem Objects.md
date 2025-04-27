## TakeRecorderSubsystem Objects

```python
class TakeRecorderSubsystem(EngineSubsystem)
```

UTakeRecorderSubsystem
Subsystem for Take Recorder

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorder
- **File**: TakeRecorderSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``take_recorder_cancelled`` (TakeRecorderCancelled):  [Read-Write] Called when take recorder is cancelled
- ``take_recorder_finished`` (TakeRecorderFinished):  [Read-Write] Called when take recorder has finished
- ``take_recorder_marked_frame_added`` (TakeRecorderMarkedFrameAdded):  [Read-Write] Called when a marked frame is added to take recorder
- ``take_recorder_pre_initialize`` (TakeRecorderPreInitialize):  [Read-Write] Called before initialization occurs (ie. when the recording button is pressed and before the countdown starts)
- ``take_recorder_started`` (TakeRecorderStarted):  [Read-Write] Called when take recorder is started
- ``take_recorder_stopped`` (TakeRecorderStopped):  [Read-Write] Called when take recorder is stopped

<a id="unreal.TakeRecorderSubsystem.take_recorder_pre_initialize"></a>

#### take_recorder_pre_initialize

```python
@property
def take_recorder_pre_initialize() -> TakeRecorderPreInitialize
```

(TakeRecorderPreInitialize):  [Read-Write] Called before initialization occurs (ie. when the recording button is pressed and before the countdown starts)

<a id="unreal.TakeRecorderSubsystem.take_recorder_pre_initialize"></a>

#### take_recorder_pre_initialize

```python
@take_recorder_pre_initialize.setter
def take_recorder_pre_initialize(value: TakeRecorderPreInitialize) -> None
```

<a id="unreal.TakeRecorderSubsystem.take_recorder_started"></a>

#### take_recorder_started

```python
@property
def take_recorder_started() -> TakeRecorderStarted
```

(TakeRecorderStarted):  [Read-Write] Called when take recorder is started

<a id="unreal.TakeRecorderSubsystem.take_recorder_started"></a>

#### take_recorder_started

```python
@take_recorder_started.setter
def take_recorder_started(value: TakeRecorderStarted) -> None
```

<a id="unreal.TakeRecorderSubsystem.take_recorder_stopped"></a>

#### take_recorder_stopped

```python
@property
def take_recorder_stopped() -> TakeRecorderStopped
```

(TakeRecorderStopped):  [Read-Write] Called when take recorder is stopped

<a id="unreal.TakeRecorderSubsystem.take_recorder_stopped"></a>

#### take_recorder_stopped

```python
@take_recorder_stopped.setter
def take_recorder_stopped(value: TakeRecorderStopped) -> None
```

<a id="unreal.TakeRecorderSubsystem.take_recorder_finished"></a>

#### take_recorder_finished

```python
@property
def take_recorder_finished() -> TakeRecorderFinished
```

(TakeRecorderFinished):  [Read-Write] Called when take recorder has finished

<a id="unreal.TakeRecorderSubsystem.take_recorder_finished"></a>

#### take_recorder_finished

```python
@take_recorder_finished.setter
def take_recorder_finished(value: TakeRecorderFinished) -> None
```

<a id="unreal.TakeRecorderSubsystem.take_recorder_cancelled"></a>

#### take_recorder_cancelled

```python
@property
def take_recorder_cancelled() -> TakeRecorderCancelled
```

(TakeRecorderCancelled):  [Read-Write] Called when take recorder is cancelled

<a id="unreal.TakeRecorderSubsystem.take_recorder_cancelled"></a>

#### take_recorder_cancelled

```python
@take_recorder_cancelled.setter
def take_recorder_cancelled(value: TakeRecorderCancelled) -> None
```

<a id="unreal.TakeRecorderSubsystem.take_recorder_marked_frame_added"></a>

#### take_recorder_marked_frame_added

```python
@property
def take_recorder_marked_frame_added() -> TakeRecorderMarkedFrameAdded
```

(TakeRecorderMarkedFrameAdded):  [Read-Write] Called when a marked frame is added to take recorder

<a id="unreal.TakeRecorderSubsystem.take_recorder_marked_frame_added"></a>

#### take_recorder_marked_frame_added

```python
@take_recorder_marked_frame_added.setter
def take_recorder_marked_frame_added(
        value: TakeRecorderMarkedFrameAdded) -> None
```

<a id="unreal.TakeRecorder"></a>