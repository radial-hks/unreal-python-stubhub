## AvaSequencePlayAdvancedSettings Objects

```python
class AvaSequencePlayAdvancedSettings(StructBase)
```

Ava Sequence Play Advanced Settings

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheSequence
- **File**: AvaSequenceShared.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``loop_count`` (int32):  [Read-Write] Number of times to loop playback. -1 for infinite, else the number of times to loop before stopping
- ``playback_speed`` (float):  [Read-Write]
- ``restore_state`` (bool):  [Read-Write]

<a id="unreal.AvaSequencePlayAdvancedSettings.__init__"></a>

#### __init__

```python
def __init__(loop_count: int = 0,
             playback_speed: float = 0.000000,
             restore_state: bool = False) -> None
```

<a id="unreal.AvaSequencePlayAdvancedSettings.loop_count"></a>

#### loop_count

```python
@property
def loop_count() -> int
```

(int32):  [Read-Write] Number of times to loop playback. -1 for infinite, else the number of times to loop before stopping

<a id="unreal.AvaSequencePlayAdvancedSettings.loop_count"></a>

#### loop_count

```python
@loop_count.setter
def loop_count(value: int) -> None
```

<a id="unreal.AvaSequencePlayAdvancedSettings.playback_speed"></a>

#### playback_speed

```python
@property
def playback_speed() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaSequencePlayAdvancedSettings.playback_speed"></a>

#### playback_speed

```python
@playback_speed.setter
def playback_speed(value: float) -> None
```

<a id="unreal.AvaSequencePlayAdvancedSettings.restore_state"></a>

#### restore_state

```python
@property
def restore_state() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaSequencePlayAdvancedSettings.restore_state"></a>

#### restore_state

```python
@restore_state.setter
def restore_state(value: bool) -> None
```

<a id="unreal.AvaSequencePlayParams"></a>