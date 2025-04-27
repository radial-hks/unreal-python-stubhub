## RigVMFunction_MathVectorSelectBool Objects

```python
class RigVMFunction_MathVectorSelectBool(RigVMFunction_MathVectorBase)
```

Return one of the two values based on the condition

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition`` (bool):  [Read-Write]
- ``if_false`` (Vector):  [Read-Write]
- ``if_true`` (Vector):  [Read-Write]
- ``result`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorSelectBool.__init__"></a>

#### __init__

```python
def __init__(condition: bool = False,
             if_true: Vector = [0.000000, 0.000000, 0.000000],
             if_false: Vector = [0.000000, 0.000000, 0.000000],
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathVectorSelectBool.condition"></a>

#### condition

```python
@property
def condition() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorSelectBool.condition"></a>

#### condition

```python
@condition.setter
def condition(value: bool) -> None
```

<a id="unreal.RigVMFunction_MathVectorSelectBool.if_true"></a>

#### if_true

```python
@property
def if_true() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorSelectBool.if_true"></a>

#### if_true

```python
@if_true.setter
def if_true(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorSelectBool.if_false"></a>

#### if_false

```python
@property
def if_false() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorSelectBool.if_false"></a>

#### if_false

```python
@if_false.setter
def if_false(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorSelectBool.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathVectorSelectBool"></a>