## GameplayTagContainer Objects

```python
class GameplayTagContainer(StructBase)
```

A Tag Container holds a collection of FGameplayTags, tags are included explicitly by adding them, and implicitly from adding child tags

**C++ Source:**

- **Module**: GameplayTags
- **File**: GameplayTagContainer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gameplay_tags`` (Array[GameplayTag]):  [Read-Only] Array of gameplay tags

<a id="unreal.GameplayTagContainer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(gameplay_tags: Array[GameplayTag] = []) -> None
```

<a id="unreal.GameplayTagContainer.gameplay_tags"></a>

#### gameplay\_tags

```python
@property
def gameplay_tags() -> Array[GameplayTag]
```

(Array[GameplayTag]):  [Read-Only] Array of gameplay tags

<a id="unreal.MapPlayerKeyArgs"></a>