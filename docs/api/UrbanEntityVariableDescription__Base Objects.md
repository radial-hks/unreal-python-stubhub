## UrbanEntityVariableDescription\_Base Objects

```python
class UrbanEntityVariableDescription_Base(StructBase)
```

Urban Entity Variable Description Base

**C++ Source:**

- **Plugin**: AesBuilderCommon
- **Module**: UrbanEntity
- **File**: UrbanEntityVariableDescription.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``category`` (Name):  [Read-Write] Is array fleid ?
- ``display_name`` (Name):  [Read-Write] Name of the variable
- ``is_advanced`` (bool):  [Read-Write]
- ``is_editable`` (bool):  [Read-Write]
- ``is_transit`` (bool):  [Read-Write] Set variable to sub-variabilization
- ``sub_variabilization`` (bool):  [Read-Write] Set variable to sub-variabilization
- ``tool_tip`` (str):  [Read-Write] Is array fleid ?
- ``var_name`` (Name):  [Read-Write] Name of the variable
- ``var_type`` (UrbanEntityVariableType):  [Read-Write] Type of the variable
  *      It should be any type in entity
  *      and only be basic type in nested

<a id="unreal.UrbanEntityVariableDescription_Base.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.UrbanEntityVariableDescription"></a>