## RigUnit_VisualDebugVectorItemSpace Objects

```python
class RigUnit_VisualDebugVectorItemSpace(RigUnit_DebugBase)
```

Debug draw parameters for a Point or Vector given a vector

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_VisualDebug.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``mode`` (RigUnitVisualDebugPointMode):  [Read-Write]
- ``scale`` (float):  [Read-Write]
- ``space`` (RigElementKey):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.__init__"></a>

#### __init__

```python
def __init__(
        value: Vector = [0.000000, 0.000000, 0.000000],
        enabled: bool = False,
        mode: RigUnitVisualDebugPointMode = RigUnitVisualDebugPointMode.POINT,
        color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        thickness: float = 0.000000,
        scale: float = 0.000000,
        space: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.mode"></a>

#### mode

```python
@property
def mode() -> RigUnitVisualDebugPointMode
```

(RigUnitVisualDebugPointMode):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.mode"></a>

#### mode

```python
@mode.setter
def mode(value: RigUnitVisualDebugPointMode) -> None
```

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.space"></a>

#### space

```python
@property
def space() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugVectorItemSpace.space"></a>

#### space

```python
@space.setter
def space(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_VisualDebugQuat"></a>