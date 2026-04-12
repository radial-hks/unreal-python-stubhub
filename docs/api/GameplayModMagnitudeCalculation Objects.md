## GameplayModMagnitudeCalculation Objects

```python
class GameplayModMagnitudeCalculation(GameplayEffectCalculation)
```

Class used to perform custom gameplay effect modifier calculations, either via blueprint or native code

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayModMagnitudeCalculation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_non_net_authority_dependency_registration`` (bool):  [Read-Write] Whether the calculation allows non-net authorities to register the external dependency multi-cast delegate or not; Effectively
  whether clients are allowed to perform the custom calculation themselves or not
  Note:: This is an advanced use case that should only be enabled under very specific circumstances. This is designed for games that are utilizing network dormancy and may want to trust the client to update non-gameplay critical attributes client-side without causing a network dormancy flush. Usage of this flag is *NOT* compatible with attribute capture within the calculation and will trigger an ensure if used in tandem. Clients are incapable of performing custom calculations that require attribute captures. In general, if your game is not using network dormancy, this should always remain disabled.
  Note:: If enabling this for a custom calculation, be sure that the external delegate is sourced from something guaranteed to be on the client to avoid timing issues. As an example, binding to a delegate on a GameState is potentially unreliable, as the client reference to that actor may not be available during registration.
- ``relevant_attributes_to_capture`` (Array[GameplayEffectAttributeCaptureDefinition]):  [Read-Write] Attributes to capture that are relevant to the calculation

<a id="unreal.GameplayModMagnitudeCalculation.get_captured_attribute_magnitude"></a>

#### get\_captured\_attribute\_magnitude

```python
def get_captured_attribute_magnitude(
        effect_spec: GameplayEffectSpec, attribute: GameplayAttribute,
        source_tags: GameplayTagContainer,
        target_tags: GameplayTagContainer) -> float
```

x.get_captured_attribute_magnitude(effect_spec, attribute, source_tags, target_tags) -> float
Gets the captured magnitude value for the given Attribute
For this to work correctly, the Attribute needs to be added to the Relevant Attributes to Capture array

Args:
    effect_spec (GameplayEffectSpec): The Gameplay Effect Spec to get the info from
    attribute (GameplayAttribute): The attribute to query
    source_tags (GameplayTagContainer): 
    target_tags (GameplayTagContainer): 

Returns:
    float: The magnitude value if found, zero otherwise

<a id="unreal.GameplayModMagnitudeCalculation.get_target_spec_tags"></a>

#### get\_target\_spec\_tags

```python
def get_target_spec_tags(
        effect_spec: GameplayEffectSpec) -> GameplayTagContainer
```

x.get_target_spec_tags(effect_spec) -> GameplayTagContainer
Returns the target spec tags from a Gameplay Effect Spec
Useful for Modifier Magnitude Calculations

Args:
    effect_spec (GameplayEffectSpec): The Gameplay Effect Spec to get the info from

Returns:
    GameplayTagContainer: Gameplay Tag Container with the copied tags. The container will be empty if no captured source tags exist.

<a id="unreal.GameplayModMagnitudeCalculation.get_target_aggregated_tags"></a>

#### get\_target\_aggregated\_tags

```python
def get_target_aggregated_tags(
        effect_spec: GameplayEffectSpec) -> GameplayTagContainer
```

x.get_target_aggregated_tags(effect_spec) -> GameplayTagContainer
Copies and returns the target aggregated tags from a Gameplay Effect Spec

Args:
    effect_spec (GameplayEffectSpec): The Gameplay Effect Spec to get the info from

Returns:
    GameplayTagContainer: Gameplay Tag Container with the copied tags. The container will be empty if no captured source tags exist.

<a id="unreal.GameplayModMagnitudeCalculation.get_target_actor_tags"></a>

#### get\_target\_actor\_tags

```python
def get_target_actor_tags(
        effect_spec: GameplayEffectSpec) -> GameplayTagContainer
```

x.get_target_actor_tags(effect_spec) -> GameplayTagContainer
Returns the target actor tags from a Gameplay Effect Spec
Useful for Modifier Magnitude Calculations

Args:
    effect_spec (GameplayEffectSpec): The Gameplay Effect Spec to get the info from

Returns:
    GameplayTagContainer: Gameplay Tag Container with the copied tags. The container will be empty if no captured source tags exist.

<a id="unreal.GameplayModMagnitudeCalculation.get_source_spec_tags"></a>

#### get\_source\_spec\_tags

```python
def get_source_spec_tags(
        effect_spec: GameplayEffectSpec) -> GameplayTagContainer
```

x.get_source_spec_tags(effect_spec) -> GameplayTagContainer
Returns the source spec tags from a Gameplay Effect Spec

Args:
    effect_spec (GameplayEffectSpec): The Gameplay Effect Spec to get the info from

Returns:
    GameplayTagContainer: Gameplay Tag Container with the copied tags. The container will be empty if no captured source tags exist.

<a id="unreal.GameplayModMagnitudeCalculation.get_source_aggregated_tags"></a>

#### get\_source\_aggregated\_tags

```python
def get_source_aggregated_tags(
        effect_spec: GameplayEffectSpec) -> GameplayTagContainer
```

x.get_source_aggregated_tags(effect_spec) -> GameplayTagContainer
Copies and returns the source aggregated tags from a Gameplay Effect Spec

Args:
    effect_spec (GameplayEffectSpec): The Gameplay Effect Spec to get the info from

Returns:
    GameplayTagContainer: Gameplay Tag Container with the copied tags. The container will be empty if no captured source tags exist.

<a id="unreal.GameplayModMagnitudeCalculation.get_source_actor_tags"></a>

#### get\_source\_actor\_tags

```python
def get_source_actor_tags(
        effect_spec: GameplayEffectSpec) -> GameplayTagContainer
```

x.get_source_actor_tags(effect_spec) -> GameplayTagContainer
Returns the source actor tags from a Gameplay Effect Spec

Args:
    effect_spec (GameplayEffectSpec): The Gameplay Effect Spec to get the info from

Returns:
    GameplayTagContainer: Gameplay Tag Container with the copied tags. The container will be empty if no captured source tags exist.

<a id="unreal.GameplayModMagnitudeCalculation.get_set_by_caller_magnitude_by_tag"></a>

#### get\_set\_by\_caller\_magnitude\_by\_tag

```python
def get_set_by_caller_magnitude_by_tag(effect_spec: GameplayEffectSpec,
                                       tag: GameplayTag) -> float
```

x.get_set_by_caller_magnitude_by_tag(effect_spec, tag) -> float
Extracts the Set by Caller Magnitude from a Gameplay Effect Spec

Args:
    effect_spec (GameplayEffectSpec): The Gameplay Effect Spec to get the info from
    tag (GameplayTag): The effect tag to query

Returns:
    float: The magnitude value if found, zero otherwise

<a id="unreal.GameplayModMagnitudeCalculation.get_set_by_caller_magnitude_by_name"></a>

#### get\_set\_by\_caller\_magnitude\_by\_name

```python
def get_set_by_caller_magnitude_by_name(effect_spec: GameplayEffectSpec,
                                        magnitude_name: Name) -> float
```

x.get_set_by_caller_magnitude_by_name(effect_spec, magnitude_name) -> float
Extracts the Set by Caller Magnitude from a Gameplay Effect Spec

Args:
    effect_spec (GameplayEffectSpec): The Gameplay Effect Spec to get the info from
    magnitude_name (Name): The effect name to query

Returns:
    float: The magnitude value if found, zero otherwise

<a id="unreal.GameplayModMagnitudeCalculation.calculate_base_magnitude"></a>

#### calculate\_base\_magnitude

```python
def calculate_base_magnitude(spec: GameplayEffectSpec) -> float
```

x.calculate_base_magnitude(spec) -> float
Calculate the base magnitude of the gameplay effect modifier, given the specified spec. Note that the owning spec def can still modify this base value
with a coeffecient and pre/post multiply adds. see FCustomCalculationBasedFloat::CalculateMagnitude for details.

Args:
    spec (GameplayEffectSpec): Gameplay effect spec to use to calculate the magnitude with

Returns:
    float: Computed magnitude of the modifier

<a id="unreal.MovieSceneGameplayCueTriggerSection"></a>