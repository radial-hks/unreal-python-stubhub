## PhysicalMaterial Objects

```python
class PhysicalMaterial(Object)
```

Physical materials are used to define the response of a physical object when interacting dynamically with the world.

**C++ Source:**

- **Module**: PhysicsCore
- **File**: PhysicalMaterial.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_friction_impulse`` (float):  [Read-Write] A friction (positional) impulse of at least this magnitude may be applied,
                regardless the normal force. This is analogous to adding only the lateral part of a
                "stickiness" to a material
- ``damage_modifier`` (PhysicalMaterialDamageModifier):  [Read-Write]
- ``density`` (float):  [Read-Write] Used with the shape of the object to calculate its mass properties. The higher the number, the heavier the object. g per cubic cm.
- ``friction`` (float):  [Read-Write] Friction value of surface, controls how easily things can slide on this surface (0 is frictionless, higher values increase the amount of friction)
- ``friction_combine_mode`` (FrictionCombineMode):  [Read-Write] Friction combine mode, controls how friction is computed for multiple materials.
- ``override_friction_combine_mode`` (bool):  [Read-Write] If set we will use the FrictionCombineMode of this material, instead of the FrictionCombineMode found in the project settings.
- ``override_restitution_combine_mode`` (bool):  [Read-Write] If set we will use the RestitutionCombineMode of this material, instead of the RestitutionCombineMode found in the project settings.
- ``raise_mass_to_power`` (float):  [Read-Write] Used to adjust the way that mass increases as objects get larger. This is applied to the mass as calculated based on a 'solid' object.
  In actuality, larger objects do not tend to be solid, and become more like 'shells' (e.g. a car is not a solid piece of metal).
  Values are clamped to 1 or less.
- ``restitution`` (float):  [Read-Write] Restitution or 'bounciness' of this surface, between 0 (no bounce) and 1 (outgoing velocity is same as incoming).
- ``restitution_combine_mode`` (FrictionCombineMode):  [Read-Write] Restitution combine mode, controls how restitution is computed for multiple materials.
- ``show_experimental_properties`` (bool):  [Read-Only] Experimental material properties are enabled via the p.PhysicalMaterial.ShowExperimentalProperties console variable.
                NOTE: These are _experimental_ properties which may change. Use at your own risk!
- ``sleep_angular_velocity_threshold`` (float):  [Read-Write] How low the angular velocity can be before solver puts body to sleep.
- ``sleep_counter_threshold`` (int32):  [Read-Write] How many ticks we can be under thresholds for before solver puts body to sleep.
- ``sleep_linear_velocity_threshold`` (float):  [Read-Write] How low the linear velocity can be before solver puts body to sleep.
- ``soft_collision_mode`` (PhysicalMaterialSoftCollisionMode):  [Read-Write] For enable soft collision shell thickness mode
- ``soft_collision_thickness`` (float):  [Read-Write] Thickness of the layer just inside the collision shape in which contact is considered "soft".
                The units depend on SoftCollisionMode
- ``static_friction`` (float):  [Read-Write] Static Friction value of surface, controls how easily things can slide on this surface (0 is frictionless, higher values increase the amount of friction)
- ``strength`` (PhysicalMaterialStrength):  [Read-Write]
- ``surface_type`` (PhysicalSurface):  [Read-Write] To edit surface type for your project, use ProjectSettings/Physics/PhysicalSurface section

<a id="unreal.PhysicalMaterial.friction"></a>

#### friction

```python
@property
def friction() -> float
```

(float):  [Read-Only] Friction value of surface, controls how easily things can slide on this surface (0 is frictionless, higher values increase the amount of friction)

<a id="unreal.PhysicalMaterial.static_friction"></a>

#### static_friction

```python
@property
def static_friction() -> float
```

(float):  [Read-Only] Static Friction value of surface, controls how easily things can slide on this surface (0 is frictionless, higher values increase the amount of friction)

<a id="unreal.PhysicalMaterial.friction_combine_mode"></a>

#### friction_combine_mode

```python
@property
def friction_combine_mode() -> FrictionCombineMode
```

(FrictionCombineMode):  [Read-Only] Friction combine mode, controls how friction is computed for multiple materials.

<a id="unreal.PhysicalMaterial.override_friction_combine_mode"></a>

#### override_friction_combine_mode

```python
@property
def override_friction_combine_mode() -> bool
```

(bool):  [Read-Write] If set we will use the FrictionCombineMode of this material, instead of the FrictionCombineMode found in the project settings.

<a id="unreal.PhysicalMaterial.override_friction_combine_mode"></a>

#### override_friction_combine_mode

```python
@override_friction_combine_mode.setter
def override_friction_combine_mode(value: bool) -> None
```

<a id="unreal.PhysicalMaterial.restitution"></a>

#### restitution

```python
@property
def restitution() -> float
```

(float):  [Read-Only] Restitution or 'bounciness' of this surface, between 0 (no bounce) and 1 (outgoing velocity is same as incoming).

<a id="unreal.PhysicalMaterial.restitution_combine_mode"></a>

#### restitution_combine_mode

```python
@property
def restitution_combine_mode() -> FrictionCombineMode
```

(FrictionCombineMode):  [Read-Only] Restitution combine mode, controls how restitution is computed for multiple materials.

<a id="unreal.PhysicalMaterial.override_restitution_combine_mode"></a>

#### override_restitution_combine_mode

```python
@property
def override_restitution_combine_mode() -> bool
```

(bool):  [Read-Write] If set we will use the RestitutionCombineMode of this material, instead of the RestitutionCombineMode found in the project settings.

<a id="unreal.PhysicalMaterial.override_restitution_combine_mode"></a>

#### override_restitution_combine_mode

```python
@override_restitution_combine_mode.setter
def override_restitution_combine_mode(value: bool) -> None
```

<a id="unreal.PhysicalMaterial.density"></a>

#### density

```python
@property
def density() -> float
```

(float):  [Read-Only] Used with the shape of the object to calculate its mass properties. The higher the number, the heavier the object. g per cubic cm.

<a id="unreal.PhysicalMaterial.sleep_linear_velocity_threshold"></a>

#### sleep_linear_velocity_threshold

```python
@property
def sleep_linear_velocity_threshold() -> float
```

(float):  [Read-Only] How low the linear velocity can be before solver puts body to sleep.

<a id="unreal.PhysicalMaterial.sleep_angular_velocity_threshold"></a>

#### sleep_angular_velocity_threshold

```python
@property
def sleep_angular_velocity_threshold() -> float
```

(float):  [Read-Only] How low the angular velocity can be before solver puts body to sleep.

<a id="unreal.PhysicalMaterial.sleep_counter_threshold"></a>

#### sleep_counter_threshold

```python
@property
def sleep_counter_threshold() -> int
```

(int32):  [Read-Only] How many ticks we can be under thresholds for before solver puts body to sleep.

<a id="unreal.PhysicalMaterial.raise_mass_to_power"></a>

#### raise_mass_to_power

```python
@property
def raise_mass_to_power() -> float
```

(float):  [Read-Only] Used to adjust the way that mass increases as objects get larger. This is applied to the mass as calculated based on a 'solid' object.
In actuality, larger objects do not tend to be solid, and become more like 'shells' (e.g. a car is not a solid piece of metal).
Values are clamped to 1 or less.

<a id="unreal.PhysicalMaterial.surface_type"></a>

#### surface_type

```python
@property
def surface_type() -> PhysicalSurface
```

(PhysicalSurface):  [Read-Only] To edit surface type for your project, use ProjectSettings/Physics/PhysicalSurface section

<a id="unreal.PhysicalMaterial.strength"></a>

#### strength

```python
@property
def strength() -> PhysicalMaterialStrength
```

(PhysicalMaterialStrength):  [Read-Only]

<a id="unreal.PhysicalMaterial.damage_modifier"></a>

#### damage_modifier

```python
@property
def damage_modifier() -> PhysicalMaterialDamageModifier
```

(PhysicalMaterialDamageModifier):  [Read-Only]

<a id="unreal.AudioPropertiesSheetAssetBase"></a>