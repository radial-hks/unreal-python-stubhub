## PhysicalMaterialDamageModifier Objects

```python
class PhysicalMaterialDamageModifier(StructBase)
```

Damage threshold modifiers, used by the Chaos destruction system

**C++ Source:**

- **Module**: PhysicsCore
- **File**: PhysicalMaterial.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``damage_threshold_multiplier`` (float):  [Read-Write] Multiplier for the geometry collection damage thresholds/ internal strain
  this allows for setting up unit damage threshold and use the material to scale them to the desired range of values
  Note that the geometry collection asset needs to opt-in for the material modifer to be able to use it

<a id="unreal.PhysicalMaterialDamageModifier.__init__"></a>

#### __init__

```python
def __init__(damage_threshold_multiplier: float = 0.000000) -> None
```

<a id="unreal.PhysicalMaterialDamageModifier.damage_threshold_multiplier"></a>

#### damage_threshold_multiplier

```python
@property
def damage_threshold_multiplier() -> float
```

(float):  [Read-Only] Multiplier for the geometry collection damage thresholds/ internal strain
this allows for setting up unit damage threshold and use the material to scale them to the desired range of values
Note that the geometry collection asset needs to opt-in for the material modifer to be able to use it

<a id="unreal.SoundGeneratorOutput"></a>