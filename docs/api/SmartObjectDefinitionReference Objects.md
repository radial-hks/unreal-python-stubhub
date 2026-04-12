## SmartObjectDefinitionReference Objects

```python
class SmartObjectDefinitionReference(StructBase)
```

Struct to hold reference to a SmartObjectDefinition asset along with values to parameterized it.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectDefinitionReference.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``parameters`` (InstancedPropertyBag):  [Read-Write]
- ``property_overrides`` (Array[Guid]):  [Read-Write] Array of overridden properties. Non-overridden properties will inherit the values from the SmartObjectDefintion default parameters.
- ``smart_object_definition`` (SmartObjectDefinition):  [Read-Write]

<a id="unreal.SmartObjectDefinitionReference.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.SmartObjectContainer"></a>