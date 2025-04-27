## DamageType Objects

```python
class DamageType(Object)
```

A DamageType is intended to define and describe a particular form of damage and to provide an avenue
for customizing responses to damage from various sources.

For example, a game could make a DamageType_Fire set it up to ignite the damaged actor.

DamageTypes are never instanced and should be treated as immutable data holders with static code
functionality.  They should never be stateful.

**C++ Source:**

- **Module**: Engine
- **File**: DamageType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``caused_by_world`` (bool):  [Read-Write] True if this damagetype is caused by the world (falling off level, into lava, etc).
- ``damage_falloff`` (float):  [Read-Write] Damage fall-off for radius damage (exponent).  Default 1.0=linear, 2.0=square of distance, etc.
- ``damage_impulse`` (float):  [Read-Write] The magnitude of impulse to apply to the Actors damaged by this type.
- ``destructible_damage_spread_scale`` (float):  [Read-Write] How much the damage spreads on a destructible mesh
- ``destructible_impulse`` (float):  [Read-Write] How large the impulse should be applied to destructible meshes
- ``radial_damage_vel_change`` (bool):  [Read-Write] When applying radial impulses, whether to treat as impulse or velocity change.
- ``scale_momentum_by_mass`` (bool):  [Read-Write] True to scale imparted momentum by the receiving pawn's mass for pawns using character movement

<a id="unreal.DamageType.caused_by_world"></a>

#### caused_by_world

```python
@property
def caused_by_world() -> bool
```

(bool):  [Read-Only] True if this damagetype is caused by the world (falling off level, into lava, etc).

<a id="unreal.DamageType.scale_momentum_by_mass"></a>

#### scale_momentum_by_mass

```python
@property
def scale_momentum_by_mass() -> bool
```

(bool):  [Read-Only] True to scale imparted momentum by the receiving pawn's mass for pawns using character movement

<a id="unreal.DamageType.radial_damage_vel_change"></a>

#### radial_damage_vel_change

```python
@property
def radial_damage_vel_change() -> bool
```

(bool):  [Read-Only] When applying radial impulses, whether to treat as impulse or velocity change.

<a id="unreal.DamageType.damage_impulse"></a>

#### damage_impulse

```python
@property
def damage_impulse() -> float
```

(float):  [Read-Only] The magnitude of impulse to apply to the Actors damaged by this type.

<a id="unreal.DamageType.destructible_impulse"></a>

#### destructible_impulse

```python
@property
def destructible_impulse() -> float
```

(float):  [Read-Only] How large the impulse should be applied to destructible meshes

<a id="unreal.DamageType.destructible_damage_spread_scale"></a>

#### destructible_damage_spread_scale

```python
@property
def destructible_damage_spread_scale() -> float
```

(float):  [Read-Only] How much the damage spreads on a destructible mesh

<a id="unreal.DamageType.damage_falloff"></a>

#### damage_falloff

```python
@property
def damage_falloff() -> float
```

(float):  [Read-Only] Damage fall-off for radius damage (exponent).  Default 1.0=linear, 2.0=square of distance, etc.

<a id="unreal.PrimaryDataAsset"></a>