## MassEntityConfig Objects

```python
class MassEntityConfig(StructBase)
```

Describes a Mass agent to spawn. The struct can be embedded to allow last minute changes to the agent (i.e. for debugging).
The agent config describes a unique list of features which are used to create an entity template.
Derived configs can override parent features.

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassSpawner
- **File**: MassEntityConfigAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``config_guid`` (Guid):  [Read-Only]
- ``parent`` (MassEntityConfigAsset):  [Read-Write] Reference to parent config asset
- ``traits`` (Array[MassEntityTraitBase]):  [Read-Write] Array of unique traits of this config

<a id="unreal.MassEntityConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.EQSParametrizedQueryExecutionRequest"></a>