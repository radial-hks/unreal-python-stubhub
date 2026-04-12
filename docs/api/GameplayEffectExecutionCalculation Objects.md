## GameplayEffectExecutionCalculation Objects

```python
class GameplayEffectExecutionCalculation(GameplayEffectCalculation)
```

Gameplay Effect Execution Calculation

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffectExecutionCalculation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``invalid_scoped_modifier_attributes`` (Array[GameplayEffectAttributeCaptureDefinition]):  [Read-Write] Any attribute in this list will not show up as a valid option for scoped modifiers; Used to allow attribute capture for internal calculation while preventing modification
- ``relevant_attributes_to_capture`` (Array[GameplayEffectAttributeCaptureDefinition]):  [Read-Write] Attributes to capture that are relevant to the calculation
- ``requires_passed_in_tags`` (bool):  [Read-Write] Used to indicate if this execution uses Passed In Tags
- ``valid_transient_aggregator_identifiers`` (GameplayTagContainer):  [Read-Write] Any tag in this container will show up as a valid "temporary variable" for scoped modifiers; Used to allow for data-driven variable support that doesn't rely on scoped modifiers

<a id="unreal.GameplayEffectExecutionCalculation.requires_passed_in_tags"></a>

#### requires\_passed\_in\_tags

```python
@property
def requires_passed_in_tags() -> bool
```

(bool):  [Read-Only] Used to indicate if this execution uses Passed In Tags

<a id="unreal.GameplayEffectExecutionCalculation.execute"></a>

#### execute

```python
def execute(
    execution_params: GameplayEffectCustomExecutionParameters
) -> GameplayEffectCustomExecutionOutput
```

x.execute(execution_params) -> GameplayEffectCustomExecutionOutput
Called whenever the owning gameplay effect is executed. Allowed to do essentially whatever is desired, including generating new
modifiers to instantly execute as well.
note:: Native subclasses should override the auto-generated Execute_Implementation function and NOT this one.

Args:
    execution_params (GameplayEffectCustomExecutionParameters): Parameters for the custom execution calculation

Returns:
    GameplayEffectCustomExecutionOutput: 

    out_execution_output (GameplayEffectCustomExecutionOutput): [OUT] Output data populated by the execution detailing further behavior or results of the execution

<a id="unreal.GameplayModMagnitudeCalculation"></a>