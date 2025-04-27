## RigUnit_ParentConstraintMath Objects

```python
class RigUnit_ParentConstraintMath(RigUnit_HighlevelBase)
```

Computes the output transform by constraining the input transform to multiple parents

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TransformConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``advanced_settings`` (RigUnit_ParentConstraintMath_AdvancedSettings):  [Read-Write]
- ``input`` (Transform):  [Read-Write] Input is used to calculate offsets from parents' initial transform
- ``output`` (Transform):  [Read-Write]
- ``parents`` (Array[ConstraintParent]):  [Read-Write]

<a id="unreal.RigUnit_ParentConstraintMath.__init__"></a>

#### __init__

```python
def __init__(
    input: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]],
    parents: Array[ConstraintParent] = [],
    advanced_settings: RigUnit_ParentConstraintMath_AdvancedSettings = [
        ConstraintInterpType.AVERAGE
    ],
    output: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_ParentConstraintMath.input"></a>

#### input

```python
@property
def input() -> Transform
```

(Transform):  [Read-Write] Input is used to calculate offsets from parents' initial transform

<a id="unreal.RigUnit_ParentConstraintMath.input"></a>

#### input

```python
@input.setter
def input(value: Transform) -> None
```

<a id="unreal.RigUnit_ParentConstraintMath.parents"></a>

#### parents

```python
@property
def parents() -> Array[ConstraintParent]
```

(Array[ConstraintParent]):  [Read-Write]

<a id="unreal.RigUnit_ParentConstraintMath.parents"></a>

#### parents

```python
@parents.setter
def parents(value: Array[ConstraintParent]) -> None
```

<a id="unreal.RigUnit_ParentConstraintMath.advanced_settings"></a>

#### advanced_settings

```python
@property
def advanced_settings() -> RigUnit_ParentConstraintMath_AdvancedSettings
```

(RigUnit_ParentConstraintMath_AdvancedSettings):  [Read-Write]

<a id="unreal.RigUnit_ParentConstraintMath.advanced_settings"></a>

#### advanced_settings

```python
@advanced_settings.setter
def advanced_settings(
        value: RigUnit_ParentConstraintMath_AdvancedSettings) -> None
```

<a id="unreal.RigUnit_ParentConstraintMath.output"></a>

#### output

```python
@property
def output() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_PositionConstraint"></a>