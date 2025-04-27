## QuartzTransportTimeStamp Objects

```python
class QuartzTransportTimeStamp(StructBase)
```

Transport Time stamp, used for tracking the musical time stamp on a clock

**C++ Source:**

- **Module**: Engine
- **File**: QuartzQuantizationUtilities.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bars`` (int32):  [Read-Write] The current bar this clock is on
- ``beat`` (int32):  [Read-Write] The current beat this clock is on
- ``beat_fraction`` (float):  [Read-Write] A fractional representation of the time that's played since the last bear
- ``seconds`` (float):  [Read-Write] The time in seconds that this TimeStamp occured at

<a id="unreal.QuartzTransportTimeStamp.__init__"></a>

#### __init__

```python
def __init__(bars: int = 0,
             beat: int = 0,
             beat_fraction: float = 0.000000,
             seconds: float = 0.000000) -> None
```

<a id="unreal.QuartzTransportTimeStamp.bars"></a>

#### bars

```python
@property
def bars() -> int
```

(int32):  [Read-Only] The current bar this clock is on

<a id="unreal.QuartzTransportTimeStamp.beat"></a>

#### beat

```python
@property
def beat() -> int
```

(int32):  [Read-Only] The current beat this clock is on

<a id="unreal.QuartzTransportTimeStamp.beat_fraction"></a>

#### beat_fraction

```python
@property
def beat_fraction() -> float
```

(float):  [Read-Only] A fractional representation of the time that's played since the last bear

<a id="unreal.QuartzTransportTimeStamp.seconds"></a>

#### seconds

```python
@property
def seconds() -> float
```

(float):  [Read-Only] The time in seconds that this TimeStamp occured at

<a id="unreal.QuartzClockSettings"></a>