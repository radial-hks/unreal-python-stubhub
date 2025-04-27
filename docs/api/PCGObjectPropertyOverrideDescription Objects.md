## PCGObjectPropertyOverrideDescription Objects

```python
class PCGObjectPropertyOverrideDescription(StructBase)
```

Represents the override source (to be read) and the object property (to be written).

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGObjectPropertyOverride.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input_source`` (PCGAttributePropertyInputSelector):  [Read-Write] Provide an attribute or property to read the override value from.
- ``property_target`` (str):  [Read-Write] Provide an object property name to be overridden. If you have a property "A" on your object, use "A" as the property target.

  For example, if you want to override the "Is Editor Only" flag, find it in the details panel, right-click, select 'Copy Internal Name', and paste that as the property target.

  If you have a component property, such as the static mesh of a static mesh component, use "StaticMeshComponent.StaticMesh".

<a id="unreal.PCGObjectPropertyOverrideDescription.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PCGActorPropertyOverrideDescription"></a>