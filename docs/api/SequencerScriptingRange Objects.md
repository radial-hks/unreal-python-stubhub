## SequencerScriptingRange Objects

```python
class SequencerScriptingRange(StructBase)
```

Sequencer Scripting Range

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: SequencerScriptingRange.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``exclusive_end`` (int32):  [Read-Write]
- ``has_end_value`` (bool):  [Read-Write]
- ``has_start_value`` (bool):  [Read-Write]
- ``inclusive_start`` (int32):  [Read-Write]

<a id="unreal.SequencerScriptingRange.__init__"></a>

#### __init__

```python
def __init__(has_start_value: bool = False,
             has_end_value: bool = False,
             inclusive_start: int = 0,
             exclusive_end: int = 0) -> None
```

<a id="unreal.SequencerScriptingRange.has_start_value"></a>

#### has_start_value

```python
@property
def has_start_value() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SequencerScriptingRange.has_start_value"></a>

#### has_start_value

```python
@has_start_value.setter
def has_start_value(value: bool) -> None
```

<a id="unreal.SequencerScriptingRange.has_end_value"></a>

#### has_end_value

```python
@property
def has_end_value() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SequencerScriptingRange.has_end_value"></a>

#### has_end_value

```python
@has_end_value.setter
def has_end_value(value: bool) -> None
```

<a id="unreal.SequencerScriptingRange.inclusive_start"></a>

#### inclusive_start

```python
@property
def inclusive_start() -> int
```

(int32):  [Read-Write]

<a id="unreal.SequencerScriptingRange.inclusive_start"></a>

#### inclusive_start

```python
@inclusive_start.setter
def inclusive_start(value: int) -> None
```

<a id="unreal.SequencerScriptingRange.exclusive_end"></a>

#### exclusive_end

```python
@property
def exclusive_end() -> int
```

(int32):  [Read-Write]

<a id="unreal.SequencerScriptingRange.exclusive_end"></a>

#### exclusive_end

```python
@exclusive_end.setter
def exclusive_end(value: int) -> None
```

<a id="unreal.SequencerScriptingRange.set_start_seconds"></a>

#### set_start_seconds

```python
def set_start_seconds(start: float) -> None
```

x.set_start_seconds(start) -> None
Set the starting time for the specified range in seconds. Interpreted as the first valid time that is inside the range.

Args:
    start (float):

<a id="unreal.SequencerScriptingRange.set_start_frame"></a>

#### set_start_frame

```python
def set_start_frame(start: int) -> None
```

x.set_start_frame(start) -> None
Set the starting frame for the specified range. Interpreted as the first valid frame that is inside the range.

Args:
    start (int32):

<a id="unreal.SequencerScriptingRange.set_end_seconds"></a>

#### set_end_seconds

```python
def set_end_seconds(end: float) -> None
```

x.set_end_seconds(end) -> None
Set the ending time for the specified range in seconds. Interpreted as the first time that is outside of the range.

Args:
    end (float):

<a id="unreal.SequencerScriptingRange.set_end_frame"></a>

#### set_end_frame

```python
def set_end_frame(end: int) -> None
```

x.set_end_frame(end) -> None
Set the ending frame for the specified range. Interpreted as the first subsequent frame that is outside of the range.

Args:
    end (int32):

<a id="unreal.SequencerScriptingRange.remove_start"></a>

#### remove_start

```python
def remove_start() -> None
```

x.remove_start() -> None
Remove the start from this range, making it infinite

<a id="unreal.SequencerScriptingRange.remove_end"></a>

#### remove_end

```python
def remove_end() -> None
```

x.remove_end() -> None
Remove the end from this range, making it infinite

<a id="unreal.SequencerScriptingRange.has_start"></a>

#### has_start

```python
def has_start() -> bool
```

x.has_start() -> bool
Check whether this range has a start

Returns:
    bool:

<a id="unreal.SequencerScriptingRange.has_end"></a>

#### has_end

```python
def has_end() -> bool
```

x.has_end() -> bool
Check whether this range has an end

Returns:
    bool:

<a id="unreal.SequencerScriptingRange.get_start_seconds"></a>

#### get_start_seconds

```python
def get_start_seconds() -> float
```

x.get_start_seconds() -> float
Get the starting time for the specified range in seconds, if it has one. Defined as the first valid time that is inside the range.

Returns:
    float:

<a id="unreal.SequencerScriptingRange.get_start_frame"></a>

#### get_start_frame

```python
def get_start_frame() -> int
```

x.get_start_frame() -> int32
Get the starting frame for the specified range, if it has one. Defined as the first valid frame that is inside the range.

Returns:
    int32:

<a id="unreal.SequencerScriptingRange.get_end_seconds"></a>

#### get_end_seconds

```python
def get_end_seconds() -> float
```

x.get_end_seconds() -> float
Get the ending time for the specified range in seconds, if it has one. Defined as the first time that is outside of the range.

Returns:
    float:

<a id="unreal.SequencerScriptingRange.get_end_frame"></a>

#### get_end_frame

```python
def get_end_frame() -> int
```

x.get_end_frame() -> int32
Get the ending frame for the specified range, if it has one. Defined as the first subsequent frame that is outside of the range.

Returns:
    int32:

<a id="unreal.SequencerChannelProxy"></a>