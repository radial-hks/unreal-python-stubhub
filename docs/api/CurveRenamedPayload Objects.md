## CurveRenamedPayload Objects

```python
class CurveRenamedPayload(CurvePayload)
```

Curve Renamed Payload

**C++ Source:**

- **Module**: Engine
- **File**: AnimDataNotifications.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``identifier`` (AnimationCurveIdentifier):  [Read-Write] Identifier of the curve
- ``new_identifier`` (AnimationCurveIdentifier):  [Read-Write] Identifier of the curve after it was renamed

<a id="unreal.CurveRenamedPayload.__init__"></a>

#### __init__

```python
def __init__(identifier: AnimationCurveIdentifier = [],
             new_identifier: AnimationCurveIdentifier = []) -> None
```

<a id="unreal.CurveRenamedPayload.new_identifier"></a>

#### new_identifier

```python
@property
def new_identifier() -> AnimationCurveIdentifier
```

(AnimationCurveIdentifier):  [Read-Only] Identifier of the curve after it was renamed

<a id="unreal.CurveFlagsChangedPayload"></a>