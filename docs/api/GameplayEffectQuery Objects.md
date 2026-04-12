## GameplayEffectQuery Objects

```python
class GameplayEffectQuery(StructBase)
```

Every set condition within this query must match in order for the query to match. i.e. individual query elements are ANDed together.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_match_delegate_bp`` (ActiveGameplayEffectQueryCustomMatch_Dynamic):  [Read-Write] BP-exposed delegate for providing custom matching conditions.
- ``effect_definition`` (type(Class)):  [Read-Write] Matches on GameplayEffects with this definition
- ``effect_source`` (Object):  [Read-Write] Matches on GameplayEffects which come from this source
- ``effect_tag_query`` (GameplayTagQuery):  [Read-Write] Query that is matched against tags this GE has
- ``modifying_attribute`` (GameplayAttribute):  [Read-Write] Matches on GameplayEffects which modify given attribute.
- ``owning_tag_query`` (GameplayTagQuery):  [Read-Write] Query that is matched against tags this GE gives
- ``source_aggregate_tag_query`` (GameplayTagQuery):  [Read-Write] Query that is matched against all tags the source of this GE has
- ``source_tag_query`` (GameplayTagQuery):  [Read-Write] Query that is matched against spec tags the source of this GE has

<a id="unreal.GameplayEffectQuery.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        custom_match_delegate_bp:
    ActiveGameplayEffectQueryCustomMatch_Dynamic = ActiveGameplayEffectQueryCustomMatch_Dynamic(
    ),
        owning_tag_query: GameplayTagQuery = [],
        effect_tag_query: GameplayTagQuery = [],
        source_tag_query: GameplayTagQuery = [],
        source_aggregate_tag_query: GameplayTagQuery = [],
        modifying_attribute: GameplayAttribute = [""],
        effect_source: Object = None,
        effect_definition: Class = None) -> None
```

<a id="unreal.GameplayEffectQuery.custom_match_delegate_bp"></a>

#### custom\_match\_delegate\_bp

```python
@property
def custom_match_delegate_bp() -> ActiveGameplayEffectQueryCustomMatch_Dynamic
```

(ActiveGameplayEffectQueryCustomMatch_Dynamic):  [Read-Write] BP-exposed delegate for providing custom matching conditions.

<a id="unreal.GameplayEffectQuery.custom_match_delegate_bp"></a>

#### custom\_match\_delegate\_bp

```python
@custom_match_delegate_bp.setter
def custom_match_delegate_bp(
        value: ActiveGameplayEffectQueryCustomMatch_Dynamic) -> None
```

<a id="unreal.GameplayEffectQuery.owning_tag_query"></a>

#### owning\_tag\_query

```python
@property
def owning_tag_query() -> GameplayTagQuery
```

(GameplayTagQuery):  [Read-Write] Query that is matched against tags this GE gives

<a id="unreal.GameplayEffectQuery.owning_tag_query"></a>

#### owning\_tag\_query

```python
@owning_tag_query.setter
def owning_tag_query(value: GameplayTagQuery) -> None
```

<a id="unreal.GameplayEffectQuery.effect_tag_query"></a>

#### effect\_tag\_query

```python
@property
def effect_tag_query() -> GameplayTagQuery
```

(GameplayTagQuery):  [Read-Write] Query that is matched against tags this GE has

<a id="unreal.GameplayEffectQuery.effect_tag_query"></a>

#### effect\_tag\_query

```python
@effect_tag_query.setter
def effect_tag_query(value: GameplayTagQuery) -> None
```

<a id="unreal.GameplayEffectQuery.source_tag_query"></a>

#### source\_tag\_query

```python
@property
def source_tag_query() -> GameplayTagQuery
```

(GameplayTagQuery):  [Read-Write] Query that is matched against spec tags the source of this GE has

<a id="unreal.GameplayEffectQuery.source_tag_query"></a>

#### source\_tag\_query

```python
@source_tag_query.setter
def source_tag_query(value: GameplayTagQuery) -> None
```

<a id="unreal.GameplayEffectQuery.source_aggregate_tag_query"></a>

#### source\_aggregate\_tag\_query

```python
@property
def source_aggregate_tag_query() -> GameplayTagQuery
```

(GameplayTagQuery):  [Read-Write] Query that is matched against all tags the source of this GE has

<a id="unreal.GameplayEffectQuery.source_aggregate_tag_query"></a>

#### source\_aggregate\_tag\_query

```python
@source_aggregate_tag_query.setter
def source_aggregate_tag_query(value: GameplayTagQuery) -> None
```

<a id="unreal.GameplayEffectQuery.modifying_attribute"></a>

#### modifying\_attribute

```python
@property
def modifying_attribute() -> GameplayAttribute
```

(GameplayAttribute):  [Read-Write] Matches on GameplayEffects which modify given attribute.

<a id="unreal.GameplayEffectQuery.modifying_attribute"></a>

#### modifying\_attribute

```python
@modifying_attribute.setter
def modifying_attribute(value: GameplayAttribute) -> None
```

<a id="unreal.GameplayEffectQuery.effect_source"></a>

#### effect\_source

```python
@property
def effect_source() -> Object
```

(Object):  [Read-Write] Matches on GameplayEffects which come from this source

<a id="unreal.GameplayEffectQuery.effect_source"></a>

#### effect\_source

```python
@effect_source.setter
def effect_source(value: Object) -> None
```

<a id="unreal.GameplayEffectQuery.effect_definition"></a>

#### effect\_definition

```python
@property
def effect_definition() -> Class
```

(type(Class)):  [Read-Write] Matches on GameplayEffects with this definition

<a id="unreal.GameplayEffectQuery.effect_definition"></a>

#### effect\_definition

```python
@effect_definition.setter
def effect_definition(value: Class) -> None
```

<a id="unreal.FastArraySerializer"></a>