## SequencerScriptingRangeExtensions Objects

```python
class SequencerScriptingRangeExtensions(BlueprintFunctionLibrary)
```

Function library containing methods that should be hoisted onto FSequencerScriptingRanges

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: SequencerScriptingRangeExtensions.h

<a id="unreal.SequencerScriptingRangeExtensions.set_start_seconds"></a>

#### set_start_seconds

```python
@classmethod
def set_start_seconds(cls, range: SequencerScriptingRange,
                      start: float) -> SequencerScriptingRange
```

X.set_start_seconds(range, start) -> SequencerScriptingRange
Set the starting time for the specified range in seconds. Interpreted as the first valid time that is inside the range.

Args:
    range (SequencerScriptingRange): The range to set the start on
    start (float): 

Returns:
    SequencerScriptingRange: 

    range (SequencerScriptingRange): The range to set the start on

<a id="unreal.SequencerScriptingRangeExtensions.set_start_frame"></a>

#### set_start_frame

```python
@classmethod
def set_start_frame(cls, range: SequencerScriptingRange,
                    start: int) -> SequencerScriptingRange
```

X.set_start_frame(range, start) -> SequencerScriptingRange
Set the starting frame for the specified range. Interpreted as the first valid frame that is inside the range.

Args:
    range (SequencerScriptingRange): The range to set the start on
    start (int32): 

Returns:
    SequencerScriptingRange: 

    range (SequencerScriptingRange): The range to set the start on

<a id="unreal.SequencerScriptingRangeExtensions.set_end_seconds"></a>

#### set_end_seconds

```python
@classmethod
def set_end_seconds(cls, range: SequencerScriptingRange,
                    end: float) -> SequencerScriptingRange
```

X.set_end_seconds(range, end) -> SequencerScriptingRange
Set the ending time for the specified range in seconds. Interpreted as the first time that is outside of the range.

Args:
    range (SequencerScriptingRange): The range to set the end on
    end (float): 

Returns:
    SequencerScriptingRange: 

    range (SequencerScriptingRange): The range to set the end on

<a id="unreal.SequencerScriptingRangeExtensions.set_end_frame"></a>

#### set_end_frame

```python
@classmethod
def set_end_frame(cls, range: SequencerScriptingRange,
                  end: int) -> SequencerScriptingRange
```

X.set_end_frame(range, end) -> SequencerScriptingRange
Set the ending frame for the specified range. Interpreted as the first subsequent frame that is outside of the range.

Args:
    range (SequencerScriptingRange): The range to set the end on
    end (int32): 

Returns:
    SequencerScriptingRange: 

    range (SequencerScriptingRange): The range to set the end on

<a id="unreal.SequencerScriptingRangeExtensions.remove_start"></a>

#### remove_start

```python
@classmethod
def remove_start(cls,
                 range: SequencerScriptingRange) -> SequencerScriptingRange
```

X.remove_start(range) -> SequencerScriptingRange
Remove the start from this range, making it infinite

Args:
    range (SequencerScriptingRange): The range to remove the start from

Returns:
    SequencerScriptingRange: 

    range (SequencerScriptingRange): The range to remove the start from

<a id="unreal.SequencerScriptingRangeExtensions.remove_end"></a>

#### remove_end

```python
@classmethod
def remove_end(cls, range: SequencerScriptingRange) -> SequencerScriptingRange
```

X.remove_end(range) -> SequencerScriptingRange
Remove the end from this range, making it infinite

Args:
    range (SequencerScriptingRange): The range to remove the end from

Returns:
    SequencerScriptingRange: 

    range (SequencerScriptingRange): The range to remove the end from

<a id="unreal.SequencerScriptingRangeExtensions.has_start"></a>

#### has_start

```python
@classmethod
def has_start(cls, range: SequencerScriptingRange) -> bool
```

X.has_start(range) -> bool
Check whether this range has a start

Args:
    range (SequencerScriptingRange): The range to check

Returns:
    bool:

<a id="unreal.SequencerScriptingRangeExtensions.has_end"></a>

#### has_end

```python
@classmethod
def has_end(cls, range: SequencerScriptingRange) -> bool
```

X.has_end(range) -> bool
Check whether this range has an end

Args:
    range (SequencerScriptingRange): The range to check

Returns:
    bool:

<a id="unreal.SequencerScriptingRangeExtensions.get_start_seconds"></a>

#### get_start_seconds

```python
@classmethod
def get_start_seconds(cls, range: SequencerScriptingRange) -> float
```

X.get_start_seconds(range) -> float
Get the starting time for the specified range in seconds, if it has one. Defined as the first valid time that is inside the range.

Args:
    range (SequencerScriptingRange): The range to get the start from

Returns:
    float:

<a id="unreal.SequencerScriptingRangeExtensions.get_start_frame"></a>

#### get_start_frame

```python
@classmethod
def get_start_frame(cls, range: SequencerScriptingRange) -> int
```

X.get_start_frame(range) -> int32
Get the starting frame for the specified range, if it has one. Defined as the first valid frame that is inside the range.

Args:
    range (SequencerScriptingRange): The range to get the start from

Returns:
    int32:

<a id="unreal.SequencerScriptingRangeExtensions.get_end_seconds"></a>

#### get_end_seconds

```python
@classmethod
def get_end_seconds(cls, range: SequencerScriptingRange) -> float
```

X.get_end_seconds(range) -> float
Get the ending time for the specified range in seconds, if it has one. Defined as the first time that is outside of the range.

Args:
    range (SequencerScriptingRange): The range to get the end from

Returns:
    float:

<a id="unreal.SequencerScriptingRangeExtensions.get_end_frame"></a>

#### get_end_frame

```python
@classmethod
def get_end_frame(cls, range: SequencerScriptingRange) -> int
```

X.get_end_frame(range) -> int32
Get the ending frame for the specified range, if it has one. Defined as the first subsequent frame that is outside of the range.

Args:
    range (SequencerScriptingRange): The range to get the end from

Returns:
    int32:

<a id="unreal.SequencerCurveEditorObject"></a>