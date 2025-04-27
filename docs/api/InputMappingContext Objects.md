## InputMappingContext Objects

```python
class InputMappingContext(DataAsset)
```

UInputMappingContext : A collection of key to action mappings for a specific input context
Could be used to:
     Store predefined controller mappings (allow switching between controller config variants). TODO: Build a system allowing redirects of UInputMappingContexts to handle this.
     Define per-vehicle control mappings
     Define context specific mappings (e.g. I switch from a gun (shoot action) to a grappling hook (reel in, reel out, disconnect actions).
     Define overlay mappings to be applied on top of existing control mappings (e.g. Hero specific action mappings in a MOBA)

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputMappingContext.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``context_description`` (Text):  [Read-Write] Localized context descriptor
- ``mappings`` (Array[EnhancedActionKeyMapping]):  [Read-Write] List of key to action mappings.

<a id="unreal.InputMappingContext.mappings"></a>

#### mappings

```python
@property
def mappings() -> Array[EnhancedActionKeyMapping]
```

(Array[EnhancedActionKeyMapping]):  [Read-Only] List of key to action mappings.

<a id="unreal.InputMappingContext.context_description"></a>

#### context_description

```python
@property
def context_description() -> Text
```

(Text):  [Read-Only] Localized context descriptor

<a id="unreal.InputMappingContext.unmap_key"></a>

#### unmap_key

```python
def unmap_key(action: InputAction, key: Key) -> None
```

x.unmap_key(action, key) -> None
Unmap a key from an action within the mapping context.

Args:
    action (InputAction): 
    key (Key):

<a id="unreal.InputMappingContext.unmap_all_keys_from_action"></a>

#### unmap_all_keys_from_action

```python
def unmap_all_keys_from_action(action: InputAction) -> None
```

x.unmap_all_keys_from_action(action) -> None
Unmap all key maps to an action within the mapping context.

Args:
    action (InputAction):

<a id="unreal.InputMappingContext.unmap_all"></a>

#### unmap_all

```python
def unmap_all() -> None
```

x.unmap_all() -> None
Unmap everything within the mapping context.

<a id="unreal.InputMappingContext.unmap_action"></a>

#### unmap_action

```python
def unmap_action(action: InputAction) -> None
```

x.unmap_action(action) -> None
Unmap Action
deprecated: Function 'UnmapAction' is deprecated.

Args:
    action (InputAction):

<a id="unreal.InputMappingContext.map_key"></a>

#### map_key

```python
def map_key(action: InputAction, to_key: Key) -> EnhancedActionKeyMapping
```

x.map_key(action, to_key) -> EnhancedActionKeyMapping
Map a key to an action within the mapping context.

Args:
    action (InputAction): 
    to_key (Key): 

Returns:
    EnhancedActionKeyMapping:

<a id="unreal.InputModifier"></a>