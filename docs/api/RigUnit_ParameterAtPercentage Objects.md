## RigUnit_ParameterAtPercentage Objects

```python
class RigUnit_ParameterAtPercentage(RigUnit_ControlRigSplineBase)
```

* Returns the U parameter of a spline given a length percentage (0.0 - 1.0)

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``percentage`` (float):  [Read-Write]
- ``spline`` (ControlRigSpline):  [Read-Write]
- ``u`` (float):  [Read-Write]

<a id="unreal.RigUnit_ParameterAtPercentage.__init__"></a>

#### __init__

```python
def __init__(spline: ControlRigSpline = [],
             percentage: float = 0.000000,
             u: float = 0.000000) -> None
```

<a id="unreal.RigUnit_ParameterAtPercentage.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write]

<a id="unreal.RigUnit_ParameterAtPercentage.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_ParameterAtPercentage.percentage"></a>

#### percentage

```python
@property
def percentage() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ParameterAtPercentage.percentage"></a>

#### percentage

```python
@percentage.setter
def percentage(value: float) -> None
```

<a id="unreal.RigUnit_ParameterAtPercentage.u"></a>

#### u

```python
@property
def u() -> float
```

(float):  [Read-Only]

<a id="unreal.ProviderPollResult"></a>