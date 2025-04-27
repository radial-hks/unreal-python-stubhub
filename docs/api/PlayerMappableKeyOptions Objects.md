## PlayerMappableKeyOptions Objects

```python
class PlayerMappableKeyOptions(StructBase)
```

A struct that represents player facing mapping options for an action key mapping.
Use this to set a unique FName for the mapping option to save it, as well as some FText options
for use in UI.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedActionKeyMapping.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display_category`` (Text):  [Read-Write] The category that this player mapping is in
- ``display_name`` (Text):  [Read-Write] The localized display name of this key mapping. Use this when displaying the mappings to a user.
- ``metadata`` (Object):  [Read-Write] Metadata that can used to store any other related items to this key mapping such as icons, ability assets, etc.
- ``name`` (Name):  [Read-Write] A unique name for this player mapping to be saved with.

<a id="unreal.PlayerMappableKeyOptions.__init__"></a>

#### __init__

```python
def __init__(metadata: Object = None,
             name: Name = "None",
             display_name: Text = "",
             display_category: Text = "") -> None
```

<a id="unreal.PlayerMappableKeyOptions.metadata"></a>

#### metadata

```python
@property
def metadata() -> Object
```

(Object):  [Read-Write] Metadata that can used to store any other related items to this key mapping such as icons, ability assets, etc.

<a id="unreal.PlayerMappableKeyOptions.metadata"></a>

#### metadata

```python
@metadata.setter
def metadata(value: Object) -> None
```

<a id="unreal.PlayerMappableKeyOptions.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] A unique name for this player mapping to be saved with.

<a id="unreal.PlayerMappableKeyOptions.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.PlayerMappableKeyOptions.display_name"></a>

#### display_name

```python
@property
def display_name() -> Text
```

(Text):  [Read-Write] The localized display name of this key mapping. Use this when displaying the mappings to a user.

<a id="unreal.PlayerMappableKeyOptions.display_name"></a>

#### display_name

```python
@display_name.setter
def display_name(value: Text) -> None
```

<a id="unreal.PlayerMappableKeyOptions.display_category"></a>

#### display_category

```python
@property
def display_category() -> Text
```

(Text):  [Read-Write] The category that this player mapping is in

<a id="unreal.PlayerMappableKeyOptions.display_category"></a>

#### display_category

```python
@display_category.setter
def display_category(value: Text) -> None
```

<a id="unreal.EnhancedActionKeyMapping"></a>