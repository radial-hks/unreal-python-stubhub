## RigUnit_FitSplineCurveToChainItemArray Objects

```python
class RigUnit_FitSplineCurveToChainItemArray(RigUnit_HighlevelBaseMutable)
```

Fits a given spline curve to a chain.

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``items`` (Array[RigElementKey]):  [Read-Write] The items to align to
- ``spline`` (ControlRigSpline):  [Read-Write] The curve to align

<a id="unreal.RigUnit_FitSplineCurveToChainItemArray.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             items: Array[RigElementKey] = [],
             spline: ControlRigSpline = []) -> None
```

<a id="unreal.RigUnit_FitSplineCurveToChainItemArray.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write] The items to align to

<a id="unreal.RigUnit_FitSplineCurveToChainItemArray.items"></a>

#### items

```python
@items.setter
def items(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_FitSplineCurveToChainItemArray.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write] The curve to align

<a id="unreal.RigUnit_FitSplineCurveToChainItemArray.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_ClosestParameterFromControlRigSpline"></a>