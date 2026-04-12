## WorldConditionQueryDefinition Objects

```python
class WorldConditionQueryDefinition(StructBase)
```

Definition of a world condition.
The mutable state of the world condition is stored in FWorldConditionQueryState.
This allows to reuse the definitions and minimize the runtime memory needed to run queries.

**C++ Source:**

- **Plugin**: WorldConditions
- **Module**: WorldConditions
- **File**: WorldConditionQuery.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``editable_conditions`` (Array[WorldConditionEditable]):  [Read-Write] Conditions used while editing, converted in to Conditions via Initialize().

<a id="unreal.WorldConditionQueryDefinition.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.SmartObjectDefinitionDataProxy"></a>