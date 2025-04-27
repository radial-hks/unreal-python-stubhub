## RigUnit_AimBoneMath Objects

```python
class RigUnit_AimBoneMath(RigUnit_HighlevelBase)
```

Outputs an aligned transform of a primary and secondary axis of an input transform to a world target.
Note: This node operates in world space!

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_AimBone.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_settings`` (RigUnit_AimBone_DebugSettings):  [Read-Write] The debug setting for the node
- ``input_transform`` (Transform):  [Read-Write] The transform (in global space) before the aim was applied (optional)
- ``primary`` (RigUnit_AimItem_Target):  [Read-Write] The primary target for the aim
- ``result`` (Transform):  [Read-Write] The resulting transform
- ``secondary`` (RigUnit_AimItem_Target):  [Read-Write] The secondary target for the aim - also referred to as PoleVector / UpVector
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_AimBoneMath.__init__"></a>

#### __init__

```python
def __init__(
    input_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                  [-0.000000, 0.000000, 0.000000],
                                  [1.000000, 1.000000, 1.000000]],
    primary: RigUnit_AimItem_Target = [
        1.000000, [1.000000, 0.000000, 0.000000],
        [1.000000, 0.000000, 0.000000], ControlRigVectorKind.LOCATION,
        [RigElementType.BONE, "None"]
    ],
    secondary: RigUnit_AimItem_Target = [
        1.000000, [1.000000, 0.000000, 0.000000],
        [1.000000, 0.000000, 0.000000], ControlRigVectorKind.LOCATION,
        [RigElementType.BONE, "None"]
    ],
    weight: float = 0.000000,
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]],
    debug_settings: RigUnit_AimBone_DebugSettings = [
        False, 10.000000,
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]]
    ]
) -> None
```

<a id="unreal.RigUnit_AimBoneMath.input_transform"></a>

#### input_transform

```python
@property
def input_transform() -> Transform
```

(Transform):  [Read-Write] The transform (in global space) before the aim was applied (optional)

<a id="unreal.RigUnit_AimBoneMath.input_transform"></a>

#### input_transform

```python
@input_transform.setter
def input_transform(value: Transform) -> None
```

<a id="unreal.RigUnit_AimBoneMath.primary"></a>

#### primary

```python
@property
def primary() -> RigUnit_AimItem_Target
```

(RigUnit_AimItem_Target):  [Read-Write] The primary target for the aim

<a id="unreal.RigUnit_AimBoneMath.primary"></a>

#### primary

```python
@primary.setter
def primary(value: RigUnit_AimItem_Target) -> None
```

<a id="unreal.RigUnit_AimBoneMath.secondary"></a>

#### secondary

```python
@property
def secondary() -> RigUnit_AimItem_Target
```

(RigUnit_AimItem_Target):  [Read-Write] The secondary target for the aim - also referred to as PoleVector / UpVector

<a id="unreal.RigUnit_AimBoneMath.secondary"></a>

#### secondary

```python
@secondary.setter
def secondary(value: RigUnit_AimItem_Target) -> None
```

<a id="unreal.RigUnit_AimBoneMath.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_AimBoneMath.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_AimBoneMath.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only] The resulting transform

<a id="unreal.RigUnit_AimBoneMath.debug_settings"></a>

#### debug_settings

```python
@property
def debug_settings() -> RigUnit_AimBone_DebugSettings
```

(RigUnit_AimBone_DebugSettings):  [Read-Write] The debug setting for the node

<a id="unreal.RigUnit_AimBoneMath.debug_settings"></a>

#### debug_settings

```python
@debug_settings.setter
def debug_settings(value: RigUnit_AimBone_DebugSettings) -> None
```

<a id="unreal.RigUnit_AimBone"></a>