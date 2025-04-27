## CurveScaledPayload Objects

```python
class CurveScaledPayload(CurvePayload)
```

Curve Scaled Payload

**C++ Source:**

- **Module**: Engine
- **File**: AnimDataNotifications.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``factor`` (float):  [Read-Write] Factor with which the curve was scaled
- ``identifier`` (AnimationCurveIdentifier):  [Read-Write] Identifier of the curve
- ``origin`` (float):  [Read-Write] Time used as the origin when scaling the curve

<a id="unreal.CurveScaledPayload.__init__"></a>

#### __init__

```python
def __init__(identifier: AnimationCurveIdentifier = [],
             factor: float = 0.000000,
             origin: float = 0.000000) -> None
```

<a id="unreal.CurveScaledPayload.factor"></a>

#### factor

```python
@property
def factor() -> float
```

(float):  [Read-Only] Factor with which the curve was scaled

<a id="unreal.CurveScaledPayload.origin"></a>

#### origin

```python
@property
def origin() -> float
```

(float):  [Read-Only] Time used as the origin when scaling the curve

<a id="unreal.CurveRenamedPayload"></a>