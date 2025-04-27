## CurveFlagsChangedPayload Objects

```python
class CurveFlagsChangedPayload(CurvePayload)
```

Curve Flags Changed Payload

**C++ Source:**

- **Module**: Engine
- **File**: AnimDataNotifications.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``identifier`` (AnimationCurveIdentifier):  [Read-Write] Identifier of the curve
- ``old_flags`` (int32):  [Read-Write] Old flags mask for the curve

<a id="unreal.CurveFlagsChangedPayload.__init__"></a>

#### __init__

```python
def __init__(identifier: AnimationCurveIdentifier = [],
             old_flags: int = 0) -> None
```

<a id="unreal.CurveFlagsChangedPayload.old_flags"></a>

#### old_flags

```python
@property
def old_flags() -> int
```

(int32):  [Read-Only] Old flags mask for the curve

<a id="unreal.AttributePayload"></a>