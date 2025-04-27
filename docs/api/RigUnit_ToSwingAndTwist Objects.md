## RigUnit_ToSwingAndTwist Objects

```python
class RigUnit_ToSwingAndTwist(RigUnit)
```

Rig Unit to Swing and Twist

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Converter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input`` (Quat):  [Read-Write]
- ``swing`` (Quat):  [Read-Write]
- ``twist`` (Quat):  [Read-Write]
- ``twist_axis`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_ToSwingAndTwist.__init__"></a>

#### __init__

```python
def __init__(input: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             twist_axis: Vector = [0.000000, 0.000000, 0.000000],
             swing: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             twist: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigUnit_ToSwingAndTwist.input"></a>

#### input

```python
@property
def input() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigUnit_ToSwingAndTwist.input"></a>

#### input

```python
@input.setter
def input(value: Quat) -> None
```

<a id="unreal.RigUnit_ToSwingAndTwist.twist_axis"></a>

#### twist_axis

```python
@property
def twist_axis() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ToSwingAndTwist.twist_axis"></a>

#### twist_axis

```python
@twist_axis.setter
def twist_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_ToSwingAndTwist.swing"></a>

#### swing

```python
@property
def swing() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_ToSwingAndTwist.twist"></a>

#### twist

```python
@property
def twist() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_BinaryFloatOp"></a>