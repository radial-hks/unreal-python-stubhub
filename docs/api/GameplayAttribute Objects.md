## GameplayAttribute Objects

```python
class GameplayAttribute(StructBase)
```

Describes a FGameplayAttributeData or float property inside an attribute set. Using this provides editor UI and helper functions

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AttributeSet.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute`` (FieldPath):  [Read-Write]
- ``attribute_name`` (str):  [Read-Only] Name of the attribute, usually the same as property name
- ``attribute_owner`` (Struct):  [Read-Only] FProperty*      Attribute;

<a id="unreal.GameplayAttribute.__init__"></a>

#### \_\_init\_\_

```python
def __init__(attribute_name: str = "") -> None
```

<a id="unreal.GameplayAttribute.attribute_name"></a>

#### attribute\_name

```python
@property
def attribute_name() -> str
```

(str):  [Read-Only] Name of the attribute, usually the same as property name

<a id="unreal.ActiveGameplayEffectHandle"></a>