## FrameRateChangedPayload Objects

```python
class FrameRateChangedPayload(EmptyPayload)
```

Frame Rate Changed Payload

**C++ Source:**

- **Module**: Engine
- **File**: AnimDataNotifications.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``previous_frame_rate`` (FrameRate):  [Read-Write] Previous sampling rate for the Model

<a id="unreal.FrameRateChangedPayload.__init__"></a>

#### __init__

```python
def __init__(previous_frame_rate: FrameRate = [60000, 1]) -> None
```

<a id="unreal.FrameRateChangedPayload.previous_frame_rate"></a>

#### previous_frame_rate

```python
@property
def previous_frame_rate() -> FrameRate
```

(FrameRate):  [Read-Only] Previous sampling rate for the Model

<a id="unreal.CurvePayload"></a>