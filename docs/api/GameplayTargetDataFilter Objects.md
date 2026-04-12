## GameplayTargetDataFilter Objects

```python
class GameplayTargetDataFilter(StructBase)
```

Simple actor target filter, games can subclass this

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTargetDataFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``required_actor_class`` (type(Class)):  [Read-Write] Subclass actors must be to pass the filter.
- ``reverse_filter`` (bool):  [Read-Write] Reverses the meaning of the filter, so it will exclude all actors that pass.
- ``self_filter`` (TargetDataFilterSelf):  [Read-Write] Filter based on whether or not this actor is "self."

<a id="unreal.GameplayTargetDataFilter.__init__"></a>

#### \_\_init\_\_

```python
def __init__(required_actor_class: Class = None,
             self_filter: TargetDataFilterSelf = TargetDataFilterSelf.TDFS_ANY,
             reverse_filter: bool = False) -> None
```

<a id="unreal.GameplayTargetDataFilter.required_actor_class"></a>

#### required\_actor\_class

```python
@property
def required_actor_class() -> Class
```

(type(Class)):  [Read-Write] Subclass actors must be to pass the filter.

<a id="unreal.GameplayTargetDataFilter.required_actor_class"></a>

#### required\_actor\_class

```python
@required_actor_class.setter
def required_actor_class(value: Class) -> None
```

<a id="unreal.GameplayTargetDataFilter.self_filter"></a>

#### self\_filter

```python
@property
def self_filter() -> TargetDataFilterSelf
```

(TargetDataFilterSelf):  [Read-Write] Filter based on whether or not this actor is "self."

<a id="unreal.GameplayTargetDataFilter.self_filter"></a>

#### self\_filter

```python
@self_filter.setter
def self_filter(value: TargetDataFilterSelf) -> None
```

<a id="unreal.GameplayTargetDataFilter.reverse_filter"></a>

#### reverse\_filter

```python
@property
def reverse_filter() -> bool
```

(bool):  [Read-Write] Reverses the meaning of the filter, so it will exclude all actors that pass.

<a id="unreal.GameplayTargetDataFilter.reverse_filter"></a>

#### reverse\_filter

```python
@reverse_filter.setter
def reverse_filter(value: bool) -> None
```

<a id="unreal.WorldReticleParameters"></a>