## InheritedTagContainer Objects

```python
class InheritedTagContainer(StructBase)
```

Structure that is used to combine tags from parent and child blueprints in a safe way

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``added`` (GameplayTagContainer):  [Read-Write] Tags that I have (in addition to my parent's tags)
- ``combined_tags`` (GameplayTagContainer):  [Read-Only] CombinedTags = Inherited - Removed + Added
- ``removed`` (GameplayTagContainer):  [Read-Write] Tags that should be removed (only if my parent had them).  Note: we cannot use this to remove a tag that exists on a target. It only modifies the result of CombinedTags.

<a id="unreal.InheritedTagContainer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(combined_tags: GameplayTagContainer = [[]],
             added: GameplayTagContainer = [[]],
             removed: GameplayTagContainer = [[]]) -> None
```

<a id="unreal.InheritedTagContainer.combined_tags"></a>

#### combined\_tags

```python
@property
def combined_tags() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Only] CombinedTags = Inherited - Removed + Added

<a id="unreal.InheritedTagContainer.added"></a>

#### added

```python
@property
def added() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Only] Tags that I have (in addition to my parent's tags)

<a id="unreal.InheritedTagContainer.removed"></a>

#### removed

```python
@property
def removed() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Only] Tags that should be removed (only if my parent had them).  Note: we cannot use this to remove a tag that exists on a target. It only modifies the result of CombinedTags.

<a id="unreal.GameplayEffectCustomExecutionParameters"></a>