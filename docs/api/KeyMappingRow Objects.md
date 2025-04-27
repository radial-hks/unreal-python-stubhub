## KeyMappingRow Objects

```python
class KeyMappingRow(StructBase)
```

Stores all mappings bound to a single mapping name.

Since a single mapping can have multiple bindings to it and this system should be Blueprint friendly,
this needs to be a struct (blueprint don't support nested containers).

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedInputUserSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``mappings`` (Set[PlayerKeyMapping]):  [Read-Only]

<a id="unreal.KeyMappingRow.__init__"></a>

#### __init__

```python
def __init__(mappings: Set[PlayerKeyMapping] = []) -> None
```

<a id="unreal.KeyMappingRow.mappings"></a>

#### mappings

```python
@property
def mappings() -> Set[PlayerKeyMapping]
```

(Set[PlayerKeyMapping]):  [Read-Only]

<a id="unreal.PlayerMappableKeyQueryOptions"></a>