## RigVMFunction_VerletIntegrateVector Objects

```python
class RigVMFunction_VerletIntegrateVector(RigVMFunction_SimBase)
```

Simulates a single position over time using Verlet integration. It is recommended to use SpringInterp instead as it
is more accurate and stable, and has more meaningful parameters.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Verlet.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``acceleration`` (Vector):  [Read-Write]
- ``blend`` (float):  [Read-Write] The amount of blending to apply per second
- ``damp`` (float):  [Read-Write] The amount of damping to apply ( 0.0 to 1.0, but usually really low like 0.005 )
- ``force`` (Vector):  [Read-Write] The force feeding into the solver. Can be used for gravity.
- ``position`` (Vector):  [Read-Write]
- ``strength`` (float):  [Read-Write] The strength of the verlet spring
- ``target`` (Vector):  [Read-Write]
- ``velocity`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_VerletIntegrateVector.__init__"></a>

#### __init__

```python
def __init__(target: Vector = [0.000000, 0.000000, 0.000000],
             strength: float = 0.000000,
             damp: float = 0.000000,
             blend: float = 0.000000,
             force: Vector = [0.000000, 0.000000, 0.000000],
             position: Vector = [0.000000, 0.000000, 0.000000],
             velocity: Vector = [0.000000, 0.000000, 0.000000],
             acceleration: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_VerletIntegrateVector.target"></a>

#### target

```python
@property
def target() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_VerletIntegrateVector.target"></a>

#### target

```python
@target.setter
def target(value: Vector) -> None
```

<a id="unreal.RigVMFunction_VerletIntegrateVector.strength"></a>

#### strength

```python
@property
def strength() -> float
```

(float):  [Read-Write] The strength of the verlet spring

<a id="unreal.RigVMFunction_VerletIntegrateVector.strength"></a>

#### strength

```python
@strength.setter
def strength(value: float) -> None
```

<a id="unreal.RigVMFunction_VerletIntegrateVector.damp"></a>

#### damp

```python
@property
def damp() -> float
```

(float):  [Read-Write] The amount of damping to apply ( 0.0 to 1.0, but usually really low like 0.005 )

<a id="unreal.RigVMFunction_VerletIntegrateVector.damp"></a>

#### damp

```python
@damp.setter
def damp(value: float) -> None
```

<a id="unreal.RigVMFunction_VerletIntegrateVector.blend"></a>

#### blend

```python
@property
def blend() -> float
```

(float):  [Read-Write] The amount of blending to apply per second

<a id="unreal.RigVMFunction_VerletIntegrateVector.blend"></a>

#### blend

```python
@blend.setter
def blend(value: float) -> None
```

<a id="unreal.RigVMFunction_VerletIntegrateVector.force"></a>

#### force

```python
@property
def force() -> Vector
```

(Vector):  [Read-Write] The force feeding into the solver. Can be used for gravity.

<a id="unreal.RigVMFunction_VerletIntegrateVector.force"></a>

#### force

```python
@force.setter
def force(value: Vector) -> None
```

<a id="unreal.RigVMFunction_VerletIntegrateVector.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_VerletIntegrateVector.velocity"></a>

#### velocity

```python
@property
def velocity() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_VerletIntegrateVector.acceleration"></a>

#### acceleration

```python
@property
def acceleration() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_VerletIntegrateVector"></a>