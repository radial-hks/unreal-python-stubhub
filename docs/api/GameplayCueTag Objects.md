## GameplayCueTag Objects

```python
class GameplayCueTag(StructBase)
```

Wrapper struct around a gameplaytag with the GameplayCue category. This also allows for a details customization

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gameplay_cue_tag`` (GameplayTag):  [Read-Write]

<a id="unreal.GameplayCueTag.__init__"></a>

#### \_\_init\_\_

```python
def __init__(gameplay_cue_tag: GameplayTag = ["None"]) -> None
```

<a id="unreal.GameplayCueTag.gameplay_cue_tag"></a>

#### gameplay\_cue\_tag

```python
@property
def gameplay_cue_tag() -> GameplayTag
```

(GameplayTag):  [Read-Write]

<a id="unreal.GameplayCueTag.gameplay_cue_tag"></a>

#### gameplay\_cue\_tag

```python
@gameplay_cue_tag.setter
def gameplay_cue_tag(value: GameplayTag) -> None
```

<a id="unreal.GameplayCueNotify_SpawnCondition"></a>