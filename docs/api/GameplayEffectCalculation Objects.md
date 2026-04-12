## GameplayEffectCalculation Objects

```python
class GameplayEffectCalculation(Object)
```

Abstract base for specialized gameplay effect calculations; Capable of specifing attribute captures

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffectCalculation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``relevant_attributes_to_capture`` (Array[GameplayEffectAttributeCaptureDefinition]):  [Read-Write] Attributes to capture that are relevant to the calculation

<a id="unreal.GameplayEffectCalculation.relevant_attributes_to_capture"></a>

#### relevant\_attributes\_to\_capture

```python
@property
def relevant_attributes_to_capture(
) -> Array[GameplayEffectAttributeCaptureDefinition]
```

(Array[GameplayEffectAttributeCaptureDefinition]):  [Read-Only] Attributes to capture that are relevant to the calculation

<a id="unreal.GameplayEffectCustomApplicationRequirement"></a>