## RigUnit_DrawControlRigSpline Objects

```python
class RigUnit_DrawControlRigSpline(RigUnitMutable)
```

* Draws the given spline in the viewport

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``detail`` (int32):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``spline`` (ControlRigSpline):  [Read-Write]
- ``thickness`` (float):  [Read-Write]

<a id="unreal.RigUnit_DrawControlRigSpline.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             spline: ControlRigSpline = [],
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             thickness: float = 0.000000,
             detail: int = 0) -> None
```

<a id="unreal.RigUnit_DrawControlRigSpline.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write]

<a id="unreal.RigUnit_DrawControlRigSpline.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_DrawControlRigSpline.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigUnit_DrawControlRigSpline.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_DrawControlRigSpline.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DrawControlRigSpline.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigUnit_DrawControlRigSpline.detail"></a>

#### detail

```python
@property
def detail() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigUnit_DrawControlRigSpline.detail"></a>

#### detail

```python
@detail.setter
def detail(value: int) -> None
```

<a id="unreal.RigUnit_GetLengthControlRigSpline"></a>