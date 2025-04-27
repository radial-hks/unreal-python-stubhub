## TimeManagementLibrary Objects

```python
class TimeManagementLibrary(BlueprintFunctionLibrary)
```

Time Management Blueprint Library

**C++ Source:**

- **Module**: TimeManagement
- **File**: TimeManagementBlueprintLibrary.h

<a id="unreal.TimeManagementLibrary.transform_time"></a>

#### transform_time

```python
@classmethod
def transform_time(cls, source_time: FrameTime, source_rate: FrameRate,
                   destination_rate: FrameRate) -> FrameTime
```

X.transform_time(source_time, source_rate, destination_rate) -> FrameTime
Converts the specified time from one framerate to another framerate. This is useful for converting between tick resolution and display rate.

Args:
    source_time (FrameTime): 
    source_rate (FrameRate): 
    destination_rate (FrameRate): 

Returns:
    FrameTime:

<a id="unreal.TimeManagementLibrary.subtract_frame_number_integer"></a>

#### subtract_frame_number_integer

```python
@classmethod
def subtract_frame_number_integer(cls, a: FrameNumber, b: int) -> FrameNumber
```

X.subtract_frame_number_integer(a, b) -> FrameNumber
Subtraction (FrameNumber A - int B)

Args:
    a (FrameNumber): 
    b (int32): 

Returns:
    FrameNumber:

<a id="unreal.TimeManagementLibrary.subtract_frame_number_frame_number"></a>

#### subtract_frame_number_frame_number

```python
@classmethod
def subtract_frame_number_frame_number(cls, a: FrameNumber,
                                       b: FrameNumber) -> FrameNumber
```

X.subtract_frame_number_frame_number(a, b) -> FrameNumber
Subtraction (FrameNumber A - FrameNumber B)

Args:
    a (FrameNumber): 
    b (FrameNumber): 

Returns:
    FrameNumber:

<a id="unreal.TimeManagementLibrary.snap_frame_time_to_rate"></a>

#### snap_frame_time_to_rate

```python
@classmethod
def snap_frame_time_to_rate(cls, source_time: FrameTime,
                            source_rate: FrameRate,
                            snap_to_rate: FrameRate) -> FrameTime
```

X.snap_frame_time_to_rate(source_time, source_rate, snap_to_rate) -> FrameTime
Snaps the given SourceTime to the nearest frame in the specified Destination Framerate. Useful for determining the nearest frame for another resolution. Returns the frame time in the destination frame rate.

Args:
    source_time (FrameTime): 
    source_rate (FrameRate): 
    snap_to_rate (FrameRate): 

Returns:
    FrameTime:

<a id="unreal.TimeManagementLibrary.multiply_seconds_frame_rate"></a>

#### multiply_seconds_frame_rate

```python
@classmethod
def multiply_seconds_frame_rate(cls, time_in_seconds: float,
                                frame_rate: FrameRate) -> FrameTime
```

X.multiply_seconds_frame_rate(time_in_seconds, frame_rate) -> FrameTime
Multiplies a value in seconds against a FrameRate to get a new FrameTime.

Args:
    time_in_seconds (float): 
    frame_rate (FrameRate): 

Returns:
    FrameTime:

<a id="unreal.TimeManagementLibrary.multiply_frame_number_integer"></a>

#### multiply_frame_number_integer

```python
@classmethod
def multiply_frame_number_integer(cls, a: FrameNumber, b: int) -> FrameNumber
```

X.multiply_frame_number_integer(a, b) -> FrameNumber
Multiply (FrameNumber A * B)

Args:
    a (FrameNumber): 
    b (int32): 

Returns:
    FrameNumber:

<a id="unreal.TimeManagementLibrary.is_valid_multiple_of"></a>

#### is_valid_multiple_of

```python
@classmethod
def is_valid_multiple_of(cls, frame_rate: FrameRate,
                         other_framerate: FrameRate) -> bool
```

X.is_valid_multiple_of(frame_rate, other_framerate) -> bool
Checks if this framerate is an even multiple of another framerate, ie: 60 is a multiple of 30, but 59.94 is not.

Args:
    frame_rate (FrameRate): 
    other_framerate (FrameRate): 

Returns:
    bool:

<a id="unreal.TimeManagementLibrary.is_valid_framerate"></a>

#### is_valid_framerate

```python
@classmethod
def is_valid_framerate(cls, frame_rate: FrameRate) -> bool
```

X.is_valid_framerate(frame_rate) -> bool
Verifies that this is a valid framerate with a non-zero denominator.

Args:
    frame_rate (FrameRate): 

Returns:
    bool:

<a id="unreal.TimeManagementLibrary.get_timecode_frame_rate"></a>

#### get_timecode_frame_rate

```python
@classmethod
def get_timecode_frame_rate(cls) -> FrameRate
```

X.get_timecode_frame_rate() -> FrameRate
Gets the current timecode frame rate.

Returns:
    FrameRate:

<a id="unreal.TimeManagementLibrary.get_timecode"></a>

#### get_timecode

```python
@classmethod
def get_timecode(cls) -> Timecode
```

X.get_timecode() -> Timecode
Get the current timecode of the engine.

Returns:
    Timecode:

<a id="unreal.TimeManagementLibrary.divide_frame_number_integer"></a>

#### divide_frame_number_integer

```python
@classmethod
def divide_frame_number_integer(cls, a: FrameNumber, b: int) -> FrameNumber
```

X.divide_frame_number_integer(a, b) -> FrameNumber
Divide (FrameNumber A / B)

Args:
    a (FrameNumber): 
    b (int32): 

Returns:
    FrameNumber:

<a id="unreal.TimeManagementLibrary.conv_timecode_to_string"></a>

#### conv_timecode_to_string

```python
@classmethod
def conv_timecode_to_string(cls,
                            timecode: Timecode,
                            force_sign_display: bool = False) -> str
```

X.conv_timecode_to_string(timecode, force_sign_display=False) -> str
Converts an Timecode to a string (hh:mm:ss:ff). If bForceSignDisplay then the number sign will always be prepended instead of just when expressing a negative time.

Args:
    timecode (Timecode): 
    force_sign_display (bool): 

Returns:
    str:

<a id="unreal.TimeManagementLibrary.conv_qualified_frame_time_to_seconds"></a>

#### conv_qualified_frame_time_to_seconds

```python
@classmethod
def conv_qualified_frame_time_to_seconds(cls,
                                         frame_time: QualifiedTime) -> float
```

X.conv_qualified_frame_time_to_seconds(frame_time) -> float
Converts an QualifiedFrameTime to seconds.

Args:
    frame_time (QualifiedTime): 

Returns:
    float:

<a id="unreal.TimeManagementLibrary.conv_frame_rate_to_seconds"></a>

#### conv_frame_rate_to_seconds

```python
@classmethod
def conv_frame_rate_to_seconds(cls, frame_rate: FrameRate) -> float
```

X.conv_frame_rate_to_seconds(frame_rate) -> float
Conv Frame Rate to Seconds
deprecated: FrameRateToInterval replaces this function, which returns the expected result of seconds per frame, rather than (incorrectly) frames per second.

Args:
    frame_rate (FrameRate): 

Returns:
    float:

<a id="unreal.TimeManagementLibrary.conv_frame_rate_to_interval"></a>

#### conv_frame_rate_to_interval

```python
@classmethod
def conv_frame_rate_to_interval(cls, frame_rate: FrameRate) -> float
```

X.conv_frame_rate_to_interval(frame_rate) -> float
Converts a FrameRate to an interval float representing the frame time in seconds ie: 1/30 returns 0.0333333

Args:
    frame_rate (FrameRate): 

Returns:
    float:

<a id="unreal.TimeManagementLibrary.frame_number_to_integer"></a>

#### frame_number_to_integer

```python
@classmethod
def frame_number_to_integer(cls, frame_number: FrameNumber) -> int
```

X.frame_number_to_integer(frame_number) -> int32
Converts a FrameNumber to an int32 for use in functions that take int32 frame counts for convenience.

Args:
    frame_number (FrameNumber): 

Returns:
    int32:

<a id="unreal.TimeManagementLibrary.add_frame_number_integer"></a>

#### add_frame_number_integer

```python
@classmethod
def add_frame_number_integer(cls, a: FrameNumber, b: int) -> FrameNumber
```

X.add_frame_number_integer(a, b) -> FrameNumber
Addition (FrameNumber A + int B)

Args:
    a (FrameNumber): 
    b (int32): 

Returns:
    FrameNumber:

<a id="unreal.TimeManagementLibrary.add_frame_number_frame_number"></a>

#### add_frame_number_frame_number

```python
@classmethod
def add_frame_number_frame_number(cls, a: FrameNumber,
                                  b: FrameNumber) -> FrameNumber
```

X.add_frame_number_frame_number(a, b) -> FrameNumber
Addition (FrameNumber A + FrameNumber B)

Args:
    a (FrameNumber): 
    b (FrameNumber): 

Returns:
    FrameNumber:

<a id="unreal.MovieSceneBoundObjectProxy"></a>