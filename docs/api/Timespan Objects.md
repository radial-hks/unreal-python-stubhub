## Timespan Objects

```python
class Timespan(StructBase)
```

A time span value, which is the difference between two dates and times.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Misc\Timespan.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

<a id="unreal.Timespan.__init__"></a>

#### __init__

```python
def __init__(days: int = 0,
             hours: int = 0,
             minutes: int = 0,
             seconds: int = 0,
             milliseconds: int = 0) -> None
```

<a id="unreal.Timespan.ZERO"></a>

#### ZERO

(Timespan): Returns a zero time span value

<a id="unreal.Timespan.MIN_VALUE"></a>

#### MIN_VALUE

(Timespan): Returns the minimum time span value

<a id="unreal.Timespan.MAX_VALUE"></a>

#### MAX_VALUE

(Timespan): Returns the maximum time span value

<a id="unreal.Transform"></a>