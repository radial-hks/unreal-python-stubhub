## ChaosPhysicalMaterial Objects

```python
class ChaosPhysicalMaterial(Object)
```

Physical materials are used to define the response of a physical object when
interacting dynamically with the world.

**C++ Source:**

- **Module**: PhysicsCore
- **File**: ChaosPhysicalMaterial.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_ether_drag`` (float):  [Read-Write] Uniform angular ether drag, the resistance a body experiences to its rotation.
- ``friction`` (float):  [Read-Write] Friction value of a surface in motion, controls how easily things can slide on this surface (0 is frictionless, higher values increase the amount of friction)
- ``linear_ether_drag`` (float):  [Read-Write] Uniform linear ether drag, the resistance a body experiences to its translation.
- ``restitution`` (float):  [Read-Write] Restitution or 'bounciness' of this surface, between 0 (no bounce) and 1 (outgoing velocity is same as incoming).
- ``sleeping_angular_velocity_threshold`` (float):  [Read-Write] How much to scale the damage threshold by on any destructible we are applied to
- ``sleeping_linear_velocity_threshold`` (float):  [Read-Write] How much to scale the damage threshold by on any destructible we are applied to
- ``static_friction`` (float):  [Read-Write] Friction value of surface at rest, controls how easily things can slide on this surface (0 is frictionless, higher values increase the amount of friction)

<a id="unreal.ChaosPhysicalMaterial.friction"></a>

#### friction

```python
@property
def friction() -> float
```

(float):  [Read-Only] Friction value of a surface in motion, controls how easily things can slide on this surface (0 is frictionless, higher values increase the amount of friction)

<a id="unreal.ChaosPhysicalMaterial.static_friction"></a>

#### static_friction

```python
@property
def static_friction() -> float
```

(float):  [Read-Only] Friction value of surface at rest, controls how easily things can slide on this surface (0 is frictionless, higher values increase the amount of friction)

<a id="unreal.ChaosPhysicalMaterial.restitution"></a>

#### restitution

```python
@property
def restitution() -> float
```

(float):  [Read-Only] Restitution or 'bounciness' of this surface, between 0 (no bounce) and 1 (outgoing velocity is same as incoming).

<a id="unreal.ChaosPhysicalMaterial.linear_ether_drag"></a>

#### linear_ether_drag

```python
@property
def linear_ether_drag() -> float
```

(float):  [Read-Only] Uniform linear ether drag, the resistance a body experiences to its translation.

<a id="unreal.ChaosPhysicalMaterial.angular_ether_drag"></a>

#### angular_ether_drag

```python
@property
def angular_ether_drag() -> float
```

(float):  [Read-Only] Uniform angular ether drag, the resistance a body experiences to its rotation.

<a id="unreal.ChaosPhysicalMaterial.sleeping_linear_velocity_threshold"></a>

#### sleeping_linear_velocity_threshold

```python
@property
def sleeping_linear_velocity_threshold() -> float
```

(float):  [Read-Only] How much to scale the damage threshold by on any destructible we are applied to

<a id="unreal.ChaosPhysicalMaterial.sleeping_angular_velocity_threshold"></a>

#### sleeping_angular_velocity_threshold

```python
@property
def sleeping_angular_velocity_threshold() -> float
```

(float):  [Read-Only] How much to scale the damage threshold by on any destructible we are applied to

<a id="unreal.PhysicalMaterial"></a>