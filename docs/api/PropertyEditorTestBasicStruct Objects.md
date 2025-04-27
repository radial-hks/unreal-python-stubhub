## PropertyEditorTestBasicStruct Objects

```python
class PropertyEditorTestBasicStruct(StructBase)
```

This structs properties should be pushed out to categories inside its parent category unless it is in an array

**C++ Source:**

- **Module**: UnrealEd
- **File**: PropertyEditorTestObject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``float_property_inside_a_struct`` (float):  [Read-Write]
- ``inner_struct`` (PropertyEditorTestSubStruct):  [Read-Write]
- ``int_property_inside_a_struct`` (int32):  [Read-Write]
- ``object_property_inside_a_struct`` (Object):  [Read-Write]

<a id="unreal.PropertyEditorTestBasicStruct.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PropertyEditorTestInstancedStruct"></a>