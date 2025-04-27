## TakeRecorderSource Objects

```python
class TakeRecorderSource(Object)
```

Base class for all sources that can be recorded with the Take Recorder. Custom recording sources can
be created by inheriting from this class and implementing the Start/Tick/Stop recording functions.
The level sequence that the recording is being placed into is provided so that the take can decide
to store the data directly in the resulting level sequence, but sources are not limited to generating
data in the specified Level Sequence. The source should be registered with the ITakeRecorderModule for
it to show up in the Take Recorder UI. If creating a recording setup via code you can just add instances
of your Source to the UTakeRecorderSources instance you're using to record and skip registering them with
the module.

Sources should reset their state before recording as there is not a guarantee that the object will be newly
created for each recording.

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakesCore
- **File**: TakeRecorderSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write] True if this source is cued for recording or not
- ``take_number`` (int32):  [Read-Write]
- ``track_tint`` (Color):  [Read-Write]

<a id="unreal.TakeRecorderSource.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] True if this source is cued for recording or not

<a id="unreal.TakeRecorderSource.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.TakeRecorderSource.take_number"></a>

#### take_number

```python
@property
def take_number() -> int
```

(int32):  [Read-Write]

<a id="unreal.TakeRecorderSource.take_number"></a>

#### take_number

```python
@take_number.setter
def take_number(value: int) -> None
```

<a id="unreal.TakeRecorderSource.track_tint"></a>

#### track_tint

```python
@property
def track_tint() -> Color
```

(Color):  [Read-Write]

<a id="unreal.TakeRecorderSource.track_tint"></a>

#### track_tint

```python
@track_tint.setter
def track_tint(value: Color) -> None
```

<a id="unreal.ActorRecorderPropertyMap"></a>