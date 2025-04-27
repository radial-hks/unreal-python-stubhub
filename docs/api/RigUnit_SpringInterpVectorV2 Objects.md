## RigUnit_SpringInterpVectorV2 Objects

```python
class RigUnit_SpringInterpVectorV2(RigVMFunction_SimBase)
```

Uses a simple spring model to interpolate a vector from Current to Target.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SpringInterp.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``critical_damping`` (float):  [Read-Write] The amount of damping in the spring.
  Set it smaller than 1 to make the spring oscillate before stabilizing on the target.
  Set it equal to 1 to reach the target without overshooting.
  Set it higher than one to make the spring take longer to reach the target.
- ``current`` (Vector):  [Read-Write] Current position of the spring.
- ``force`` (Vector):  [Read-Write] Extra force to apply (since the mass is 1, this is also the acceleration).
- ``initialize_from_target`` (bool):  [Read-Only] If true, then the initial value will be taken from the target value, and not from the current value.
- ``result`` (Vector):  [Read-Write] New position of the spring after delta time.
- ``strength`` (float):  [Read-Write] The spring strength determines how hard it will pull towards the target. The value is the frequency
  at which it will oscillate when there is no damping.
- ``target`` (Vector):  [Read-Write] Rest/target position of the spring.
- ``target_velocity_amount`` (float):  [Read-Write] The amount that the velocity should be passed through to the spring. A value of 1 will result in more
  responsive output, but if the input is noisy or has step changes, these discontinuities will be passed
  through to the output much more than if a smaller value such as 0 is used.
- ``use_current_input`` (bool):  [Read-Only] If true, then the Current input will be used to initialize the state, and is required to be a variable that
  holds the current state. If false then the Target value will be used to initialize the state and the Current
  input will be ignored/unnecessary as a state will be maintained by this node.
- ``velocity`` (Vector):  [Read-Write] Velocity

<a id="unreal.RigUnit_SpringInterpVectorV2.__init__"></a>

#### __init__

```python
def __init__(target: Vector = [0.000000, 0.000000, 0.000000],
             strength: float = 0.000000,
             critical_damping: float = 0.000000,
             force: Vector = [0.000000, 0.000000, 0.000000],
             use_current_input: bool = False,
             current: Vector = [0.000000, 0.000000, 0.000000],
             target_velocity_amount: float = 0.000000,
             initialize_from_target: bool = False,
             result: Vector = [0.000000, 0.000000, 0.000000],
             velocity: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_SpringInterpVectorV2.target"></a>

#### target

```python
@property
def target() -> Vector
```

(Vector):  [Read-Write] Rest/target position of the spring.

<a id="unreal.RigUnit_SpringInterpVectorV2.target"></a>

#### target

```python
@target.setter
def target(value: Vector) -> None
```

<a id="unreal.RigUnit_SpringInterpVectorV2.strength"></a>

#### strength

```python
@property
def strength() -> float
```

(float):  [Read-Write] The spring strength determines how hard it will pull towards the target. The value is the frequency
at which it will oscillate when there is no damping.

<a id="unreal.RigUnit_SpringInterpVectorV2.strength"></a>

#### strength

```python
@strength.setter
def strength(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterpVectorV2.critical_damping"></a>

#### critical_damping

```python
@property
def critical_damping() -> float
```

(float):  [Read-Write] The amount of damping in the spring.
Set it smaller than 1 to make the spring oscillate before stabilizing on the target.
Set it equal to 1 to reach the target without overshooting.
Set it higher than one to make the spring take longer to reach the target.

<a id="unreal.RigUnit_SpringInterpVectorV2.critical_damping"></a>

#### critical_damping

```python
@critical_damping.setter
def critical_damping(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterpVectorV2.force"></a>

#### force

```python
@property
def force() -> Vector
```

(Vector):  [Read-Write] Extra force to apply (since the mass is 1, this is also the acceleration).

<a id="unreal.RigUnit_SpringInterpVectorV2.force"></a>

#### force

```python
@force.setter
def force(value: Vector) -> None
```

<a id="unreal.RigUnit_SpringInterpVectorV2.use_current_input"></a>

#### use_current_input

```python
@property
def use_current_input() -> bool
```

(bool):  [Read-Only] If true, then the Current input will be used to initialize the state, and is required to be a variable that
holds the current state. If false then the Target value will be used to initialize the state and the Current
input will be ignored/unnecessary as a state will be maintained by this node.

<a id="unreal.RigUnit_SpringInterpVectorV2.current"></a>

#### current

```python
@property
def current() -> Vector
```

(Vector):  [Read-Write] Current position of the spring.

<a id="unreal.RigUnit_SpringInterpVectorV2.current"></a>

#### current

```python
@current.setter
def current(value: Vector) -> None
```

<a id="unreal.RigUnit_SpringInterpVectorV2.target_velocity_amount"></a>

#### target_velocity_amount

```python
@property
def target_velocity_amount() -> float
```

(float):  [Read-Write] The amount that the velocity should be passed through to the spring. A value of 1 will result in more
responsive output, but if the input is noisy or has step changes, these discontinuities will be passed
through to the output much more than if a smaller value such as 0 is used.

<a id="unreal.RigUnit_SpringInterpVectorV2.target_velocity_amount"></a>

#### target_velocity_amount

```python
@target_velocity_amount.setter
def target_velocity_amount(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterpVectorV2.initialize_from_target"></a>

#### initialize_from_target

```python
@property
def initialize_from_target() -> bool
```

(bool):  [Read-Only] If true, then the initial value will be taken from the target value, and not from the current value.

<a id="unreal.RigUnit_SpringInterpVectorV2.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only] New position of the spring after delta time.

<a id="unreal.RigUnit_SpringInterpVectorV2.velocity"></a>

#### velocity

```python
@property
def velocity() -> Vector
```

(Vector):  [Read-Only] Velocity

<a id="unreal.RigUnit_SpringInterpQuaternionV2"></a>