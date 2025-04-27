## RigUnit_FitSplineCurveToChain Objects

```python
class RigUnit_FitSplineCurveToChain(RigUnit_HighlevelBaseMutable)
```

Fits a given spline curve to a chain.

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``items`` (RigElementKeyCollection):  [Read-Write] The items to align to
- ``spline`` (ControlRigSpline):  [Read-Write] The curve to align

<a id="unreal.RigUnit_FitSplineCurveToChain.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             items: RigElementKeyCollection = [[]],
             spline: ControlRigSpline = []) -> None
```

<a id="unreal.RigUnit_FitSplineCurveToChain.items"></a>

#### items

```python
@property
def items() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write] The items to align to

<a id="unreal.RigUnit_FitSplineCurveToChain.items"></a>

#### items

```python
@items.setter
def items(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_FitSplineCurveToChain.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write] The curve to align

<a id="unreal.RigUnit_FitSplineCurveToChain.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_FitSplineCurveToChainItemArray"></a>