## MassSpawnedEntityType Objects

```python
class MassSpawnedEntityType(StructBase)
```

Describes an entity type to spawn.

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassSpawner
- **File**: MassSpawnerTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_config`` (MassEntityConfigAsset):  [Read-Write] Asset that describes the entity
- ``proportion`` (float):  [Read-Write] Proportion of the count that should be this agent type, (the proportions will be normalized with other sibling agent types)

<a id="unreal.MassSpawnedEntityType.__init__"></a>

#### \_\_init\_\_

```python
def __init__(entity_config: MassEntityConfigAsset = None,
             proportion: float = 0.000000) -> None
```

<a id="unreal.MassSpawnedEntityType.entity_config"></a>

#### entity\_config

```python
@property
def entity_config() -> MassEntityConfigAsset
```

(MassEntityConfigAsset):  [Read-Write] Asset that describes the entity

<a id="unreal.MassSpawnedEntityType.entity_config"></a>

#### entity\_config

```python
@entity_config.setter
def entity_config(value: MassEntityConfigAsset) -> None
```

<a id="unreal.MassSpawnedEntityType.proportion"></a>

#### proportion

```python
@property
def proportion() -> float
```

(float):  [Read-Write] Proportion of the count that should be this agent type, (the proportions will be normalized with other sibling agent types)

<a id="unreal.MassSpawnedEntityType.proportion"></a>

#### proportion

```python
@proportion.setter
def proportion(value: float) -> None
```

<a id="unreal.MassSpawnDataGenerator"></a>