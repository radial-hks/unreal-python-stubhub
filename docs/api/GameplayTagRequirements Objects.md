## GameplayTagRequirements Objects

```python
class GameplayTagRequirements(StructBase)
```

Encapsulate require and ignore tags

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffectTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ignore_tags`` (GameplayTagContainer):  [Read-Write] None of these tags may be present
- ``require_tags`` (GameplayTagContainer):  [Read-Write] All of these tags must be present
- ``tag_query`` (GameplayTagQuery):  [Read-Write] Build up a more complex query that can't be expressed with RequireTags/IgnoreTags alone

<a id="unreal.GameplayTagRequirements.__init__"></a>

#### \_\_init\_\_

```python
def __init__(require_tags: GameplayTagContainer = [[]],
             ignore_tags: GameplayTagContainer = [[]],
             tag_query: GameplayTagQuery = []) -> None
```

<a id="unreal.GameplayTagRequirements.require_tags"></a>

#### require\_tags

```python
@property
def require_tags() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Write] All of these tags must be present

<a id="unreal.GameplayTagRequirements.require_tags"></a>

#### require\_tags

```python
@require_tags.setter
def require_tags(value: GameplayTagContainer) -> None
```

<a id="unreal.GameplayTagRequirements.ignore_tags"></a>

#### ignore\_tags

```python
@property
def ignore_tags() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Write] None of these tags may be present

<a id="unreal.GameplayTagRequirements.ignore_tags"></a>

#### ignore\_tags

```python
@ignore_tags.setter
def ignore_tags(value: GameplayTagContainer) -> None
```

<a id="unreal.GameplayTagRequirements.tag_query"></a>

#### tag\_query

```python
@property
def tag_query() -> GameplayTagQuery
```

(GameplayTagQuery):  [Read-Write] Build up a more complex query that can't be expressed with RequireTags/IgnoreTags alone

<a id="unreal.GameplayTagRequirements.tag_query"></a>

#### tag\_query

```python
@tag_query.setter
def tag_query(value: GameplayTagQuery) -> None
```

<a id="unreal.GameplayTargetDataFilterHandle"></a>