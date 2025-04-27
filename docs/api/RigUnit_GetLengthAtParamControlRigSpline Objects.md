## RigUnit_GetLengthAtParamControlRigSpline Objects

```python
class RigUnit_GetLengthAtParamControlRigSpline(RigUnit)
```

* Retrieves the length from a given Splin

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``length`` (float):  [Read-Write]
- ``spline`` (ControlRigSpline):  [Read-Write]
- ``u`` (float):  [Read-Write]

<a id="unreal.RigUnit_GetLengthAtParamControlRigSpline.__init__"></a>

#### __init__

```python
def __init__(spline: ControlRigSpline = [],
             u: float = 0.000000,
             length: float = 0.000000) -> None
```

<a id="unreal.RigUnit_GetLengthAtParamControlRigSpline.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write]

<a id="unreal.RigUnit_GetLengthAtParamControlRigSpline.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_GetLengthAtParamControlRigSpline.u"></a>

#### u

```python
@property
def u() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_GetLengthAtParamControlRigSpline.u"></a>

#### u

```python
@u.setter
def u(value: float) -> None
```

<a id="unreal.RigUnit_GetLengthAtParamControlRigSpline.length"></a>

#### length

```python
@property
def length() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_FitChainToSplineCurve"></a>