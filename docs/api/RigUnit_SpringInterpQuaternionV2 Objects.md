## RigUnit_SpringInterpQuaternionV2 Objects

```python
class RigUnit_SpringInterpQuaternionV2(RigVMFunction_SimBase)
```

Uses a simple spring model to interpolate a quaternion from Current to Target.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SpringInterp.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_velocity`` (Vector):  [Read-Write] Angular velocity
- ``critical_damping`` (float):  [Read-Write] The amount of damping in the spring.
  Set it smaller than 1 to make the spring oscillate before stabilizing on the target.
  Set it equal to 1 to reach the target without overshooting.
  Set it higher than one to make the spring take longer to reach the target.
- ``current`` (Quat):  [Read-Write] Current position of the spring.
- ``initialize_from_target`` (bool):  [Read-Only] If true, then the initial value will be taken from the target value, and not from the current value.
- ``result`` (Quat):  [Read-Write] New position of the spring after delta time.
- ``strength`` (float):  [Read-Write] The spring strength determines how hard it will pull towards the target. The value is the frequency
  at which it will oscillate when there is no damping.
- ``target`` (Quat):  [Read-Write] Rest/target position of the spring.
- ``target_velocity_amount`` (float):  [Read-Write] The amount that the velocity should be passed through to the spring. A value of 1 will result in more
  responsive output, but if the input is noisy or has step changes, these discontinuities will be passed
  through to the output much more than if a smaller value such as 0 is used.
- ``torque`` (Vector):  [Read-Write] Extra torque to apply (since the moment of inertia is 1, this is also the angular acceleration).
- ``use_current_input`` (bool):  [Read-Only] If true, then the Current input will be used to initialize the state, and is required to be a variable that
  holds the current state. If false then the Target value will be used to initialize the state and the Current
  input will be ignored/unnecessary as a state will be maintained by this node.

<a id="unreal.RigUnit_SpringInterpQuaternionV2.__init__"></a>

#### __init__

```python
def __init__(
        target: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
        strength: float = 0.000000,
        critical_damping: float = 0.000000,
        torque: Vector = [0.000000, 0.000000, 0.000000],
        use_current_input: bool = False,
        current: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
        target_velocity_amount: float = 0.000000,
        initialize_from_target: bool = False,
        result: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
        angular_velocity: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_SpringInterpQuaternionV2.target"></a>

#### target

```python
@property
def target() -> Quat
```

(Quat):  [Read-Write] Rest/target position of the spring.

<a id="unreal.RigUnit_SpringInterpQuaternionV2.target"></a>

#### target

```python
@target.setter
def target(value: Quat) -> None
```

<a id="unreal.RigUnit_SpringInterpQuaternionV2.strength"></a>

#### strength

```python
@property
def strength() -> float
```

(float):  [Read-Write] The spring strength determines how hard it will pull towards the target. The value is the frequency
at which it will oscillate when there is no damping.

<a id="unreal.RigUnit_SpringInterpQuaternionV2.strength"></a>

#### strength

```python
@strength.setter
def strength(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterpQuaternionV2.critical_damping"></a>

#### critical_damping

```python
@property
def critical_damping() -> float
```

(float):  [Read-Write] The amount of damping in the spring.
Set it smaller than 1 to make the spring oscillate before stabilizing on the target.
Set it equal to 1 to reach the target without overshooting.
Set it higher than one to make the spring take longer to reach the target.

<a id="unreal.RigUnit_SpringInterpQuaternionV2.critical_damping"></a>

#### critical_damping

```python
@critical_damping.setter
def critical_damping(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterpQuaternionV2.torque"></a>

#### torque

```python
@property
def torque() -> Vector
```

(Vector):  [Read-Write] Extra torque to apply (since the moment of inertia is 1, this is also the angular acceleration).

<a id="unreal.RigUnit_SpringInterpQuaternionV2.torque"></a>

#### torque

```python
@torque.setter
def torque(value: Vector) -> None
```

<a id="unreal.RigUnit_SpringInterpQuaternionV2.use_current_input"></a>

#### use_current_input

```python
@property
def use_current_input() -> bool
```

(bool):  [Read-Only] If true, then the Current input will be used to initialize the state, and is required to be a variable that
holds the current state. If false then the Target value will be used to initialize the state and the Current
input will be ignored/unnecessary as a state will be maintained by this node.

<a id="unreal.RigUnit_SpringInterpQuaternionV2.current"></a>

#### current

```python
@property
def current() -> Quat
```

(Quat):  [Read-Write] Current position of the spring.

<a id="unreal.RigUnit_SpringInterpQuaternionV2.current"></a>

#### current

```python
@current.setter
def current(value: Quat) -> None
```

<a id="unreal.RigUnit_SpringInterpQuaternionV2.target_velocity_amount"></a>

#### target_velocity_amount

```python
@property
def target_velocity_amount() -> float
```

(float):  [Read-Write] The amount that the velocity should be passed through to the spring. A value of 1 will result in more
responsive output, but if the input is noisy or has step changes, these discontinuities will be passed
through to the output much more than if a smaller value such as 0 is used.

<a id="unreal.RigUnit_SpringInterpQuaternionV2.target_velocity_amount"></a>

#### target_velocity_amount

```python
@target_velocity_amount.setter
def target_velocity_amount(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterpQuaternionV2.initialize_from_target"></a>

#### initialize_from_target

```python
@property
def initialize_from_target() -> bool
```

(bool):  [Read-Only] If true, then the initial value will be taken from the target value, and not from the current value.

<a id="unreal.RigUnit_SpringInterpQuaternionV2.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only] New position of the spring after delta time.

<a id="unreal.RigUnit_SpringInterpQuaternionV2.angular_velocity"></a>

#### angular_velocity

```python
@property
def angular_velocity() -> Vector
```

(Vector):  [Read-Only] Angular velocity

<a id="unreal.RigUnit_SpringInterpQuaternion"></a>