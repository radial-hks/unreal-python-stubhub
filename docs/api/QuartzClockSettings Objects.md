## QuartzClockSettings Objects

```python
class QuartzClockSettings(StructBase)
```

UStruct version of settings struct used to initialized a clock

**C++ Source:**

- **Module**: Engine
- **File**: QuartzQuantizationUtilities.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ignore_level_change`` (bool):  [Read-Write] should the clock start Ticking
- ``time_signature`` (QuartzTimeSignature):  [Read-Write] Time Signature (defaults to 4/4)

<a id="unreal.QuartzClockSettings.__init__"></a>

#### __init__

```python
def __init__(time_signature: QuartzTimeSignature = [
    4, QuartzTimeSignatureQuantization.QUARTER_NOTE, []
],
             ignore_level_change: bool = False) -> None
```

<a id="unreal.QuartzClockSettings.time_signature"></a>

#### time_signature

```python
@property
def time_signature() -> QuartzTimeSignature
```

(QuartzTimeSignature):  [Read-Write] Time Signature (defaults to 4/4)

<a id="unreal.QuartzClockSettings.time_signature"></a>

#### time_signature

```python
@time_signature.setter
def time_signature(value: QuartzTimeSignature) -> None
```

<a id="unreal.QuartzClockSettings.ignore_level_change"></a>

#### ignore_level_change

```python
@property
def ignore_level_change() -> bool
```

(bool):  [Read-Write] should the clock start Ticking

<a id="unreal.QuartzClockSettings.ignore_level_change"></a>

#### ignore_level_change

```python
@ignore_level_change.setter
def ignore_level_change(value: bool) -> None
```

<a id="unreal.QuartzQuantizationBoundary"></a>