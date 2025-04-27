## Timecode Objects

```python
class Timecode(StructBase)
```

A timecode that stores time in HH:MM:SS format with the remainder of time represented by an integer frame count.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Misc\TimeCode.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``drop_frame_format`` (bool):  [Read-Write] If true, this Timecode represents a Drop Frame timecode used to account for fractional frame rates in NTSC play rates.
- ``frames`` (int32):  [Read-Write]
- ``hours`` (int32):  [Read-Write]
- ``minutes`` (int32):  [Read-Write]
- ``seconds`` (int32):  [Read-Write]
- ``subframe`` (float):  [Read-Write]

<a id="unreal.Timecode.__init__"></a>

#### __init__

```python
def __init__(hours: int = 0,
             minutes: int = 0,
             seconds: int = 0,
             frames: int = 0,
             subframe: float = 0.000000,
             drop_frame_format: bool = False) -> None
```

<a id="unreal.Timecode.hours"></a>

#### hours

```python
@property
def hours() -> int
```

(int32):  [Read-Write]

<a id="unreal.Timecode.hours"></a>

#### hours

```python
@hours.setter
def hours(value: int) -> None
```

<a id="unreal.Timecode.minutes"></a>

#### minutes

```python
@property
def minutes() -> int
```

(int32):  [Read-Write]

<a id="unreal.Timecode.minutes"></a>

#### minutes

```python
@minutes.setter
def minutes(value: int) -> None
```

<a id="unreal.Timecode.seconds"></a>

#### seconds

```python
@property
def seconds() -> int
```

(int32):  [Read-Write]

<a id="unreal.Timecode.seconds"></a>

#### seconds

```python
@seconds.setter
def seconds(value: int) -> None
```

<a id="unreal.Timecode.frames"></a>

#### frames

```python
@property
def frames() -> int
```

(int32):  [Read-Write]

<a id="unreal.Timecode.frames"></a>

#### frames

```python
@frames.setter
def frames(value: int) -> None
```

<a id="unreal.Timecode.subframe"></a>

#### subframe

```python
@property
def subframe() -> float
```

(float):  [Read-Write]

<a id="unreal.Timecode.subframe"></a>

#### subframe

```python
@subframe.setter
def subframe(value: float) -> None
```

<a id="unreal.Timecode.drop_frame_format"></a>

#### drop_frame_format

```python
@property
def drop_frame_format() -> bool
```

(bool):  [Read-Write] If true, this Timecode represents a Drop Frame timecode used to account for fractional frame rates in NTSC play rates.

<a id="unreal.Timecode.drop_frame_format"></a>

#### drop_frame_format

```python
@drop_frame_format.setter
def drop_frame_format(value: bool) -> None
```

<a id="unreal.Timespan"></a>