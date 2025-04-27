## RigVMFunction_MathFloatSelectBool Objects

```python
class RigVMFunction_MathFloatSelectBool(RigVMFunction_MathFloatBase)
```

Return one of the two values based on the condition

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition`` (bool):  [Read-Write]
- ``if_false`` (float):  [Read-Write]
- ``if_true`` (float):  [Read-Write]
- ``result`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatSelectBool.__init__"></a>

#### __init__

```python
def __init__(condition: bool = False,
             if_true: float = 0.000000,
             if_false: float = 0.000000,
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathFloatSelectBool.condition"></a>

#### condition

```python
@property
def condition() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatSelectBool.condition"></a>

#### condition

```python
@condition.setter
def condition(value: bool) -> None
```

<a id="unreal.RigVMFunction_MathFloatSelectBool.if_true"></a>

#### if_true

```python
@property
def if_true() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatSelectBool.if_true"></a>

#### if_true

```python
@if_true.setter
def if_true(value: float) -> None
```

<a id="unreal.RigVMFunction_MathFloatSelectBool.if_false"></a>

#### if_false

```python
@property
def if_false() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathFloatSelectBool.if_false"></a>

#### if_false

```python
@if_false.setter
def if_false(value: float) -> None
```

<a id="unreal.RigVMFunction_MathFloatSelectBool.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_MathFloatSelectBool"></a>