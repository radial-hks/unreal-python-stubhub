## GameplayEffectRemovalInfo Objects

```python
class GameplayEffectRemovalInfo(StructBase)
```

Data struct for containing information pertinent to GameplayEffects as they are removed

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffectTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``effect_context`` (GameplayEffectContextHandle):  [Read-Only] Actor this gameplay effect was targeting.
- ``premature_removal`` (bool):  [Read-Only] True when the gameplay effect's duration has not expired, meaning the gameplay effect is being forcefully removed.
- ``stack_count`` (int32):  [Read-Only] Number of Stacks this gameplay effect had before it was removed.

<a id="unreal.GameplayEffectRemovalInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(premature_removal: bool = False,
             stack_count: int = 0,
             effect_context: GameplayEffectContextHandle = []) -> None
```

<a id="unreal.GameplayEffectRemovalInfo.premature_removal"></a>

#### premature\_removal

```python
@property
def premature_removal() -> bool
```

(bool):  [Read-Only] True when the gameplay effect's duration has not expired, meaning the gameplay effect is being forcefully removed.

<a id="unreal.GameplayEffectRemovalInfo.stack_count"></a>

#### stack\_count

```python
@property
def stack_count() -> int
```

(int32):  [Read-Only] Number of Stacks this gameplay effect had before it was removed.

<a id="unreal.GameplayEffectRemovalInfo.effect_context"></a>

#### effect\_context

```python
@property
def effect_context() -> GameplayEffectContextHandle
```

(GameplayEffectContextHandle):  [Read-Only] Actor this gameplay effect was targeting.

<a id="unreal.GameplayEventData"></a>