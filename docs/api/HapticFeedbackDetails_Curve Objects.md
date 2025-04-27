## HapticFeedbackDetails_Curve Objects

```python
class HapticFeedbackDetails_Curve(StructBase)
```

Haptic Feedback Details Curve

**C++ Source:**

- **Module**: Engine
- **File**: HapticFeedbackEffect_Curve.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``amplitude`` (RuntimeFloatCurve):  [Read-Write] The amplitude to vibrate the haptic device at.  Amplitudes are normalized over the range [0.0, 1.0], with 1.0 being the max setting of the device
- ``frequency`` (RuntimeFloatCurve):  [Read-Write] The frequency to vibrate the haptic device at.  Frequency ranges vary by device!

<a id="unreal.HapticFeedbackDetails_Curve.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.HapticFeedbackDetails"></a>