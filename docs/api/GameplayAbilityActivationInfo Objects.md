## GameplayAbilityActivationInfo Objects

```python
class GameplayAbilityActivationInfo(StructBase)
```

FGameplayAbilityActivationInfo

Data tied to a specific activation of an ability.
        -Tell us whether we are the authority, if we are predicting, confirmed, etc.
        -Holds current and previous PredictionKey
        -Generally not meant to be subclassed in projects.
        -Passed around by value since the struct is small.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilitySpec.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``activation_mode`` (GameplayAbilityActivationMode):  [Read-Write] Activation status of this ability

<a id="unreal.GameplayAbilityActivationInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    activation_mode:
    GameplayAbilityActivationMode = GameplayAbilityActivationMode.AUTHORITY
) -> None
```

<a id="unreal.GameplayAbilityActivationInfo.activation_mode"></a>

#### activation\_mode

```python
@property
def activation_mode() -> GameplayAbilityActivationMode
```

(GameplayAbilityActivationMode):  [Read-Only] Activation status of this ability

<a id="unreal.GameplayEffectQuery"></a>