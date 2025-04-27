## RigVMFunction_DebugRectangleNoSpace Objects

```python
class RigVMFunction_DebugRectangleNoSpace(RigVMFunction_DebugBaseMutable)
```

Draws a rectangle in the viewport given a transform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_DebugPrimitives.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together
- ``scale`` (float):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugRectangleNoSpace.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = [],
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             scale: float = 0.000000,
             thickness: float = 0.000000,
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigVMFunction_DebugRectangleNoSpace.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugRectangleNoSpace.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigVMFunction_DebugRectangleNoSpace.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigVMFunction_DebugRectangleNoSpace.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigVMFunction_DebugRectangleNoSpace.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugRectangleNoSpace.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugRectangleNoSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugRectangleNoSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugRectangleNoSpace.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugRectangleNoSpace.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigVMFunction_DebugRectangleNoSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_DebugRectangleNoSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigVMFunction_DebugArc"></a>