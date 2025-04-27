## ActorModifierCoreLibrary Objects

```python
class ActorModifierCoreLibrary(BlueprintFunctionLibrary)
```

Blueprint Create/Read/Update/Delete operations for modifiers

**C++ Source:**

- **Plugin**: ActorModifierCore
- **Module**: ActorModifierCore
- **File**: ActorModifierCoreLibrary.h

<a id="unreal.ActorModifierCoreLibrary.set_modifier_metadata_name"></a>

#### set_modifier_metadata_name

```python
@classmethod
def set_modifier_metadata_name(
        cls, metadata: ActorModifierCoreMetadata, name: Name
) -> Tuple[ActorModifierCoreMetadata, ActorModifierCoreMetadata]
```

X.set_modifier_metadata_name(metadata, name) -> (ActorModifierCoreMetadata, metadata=ActorModifierCoreMetadata)
Sets the modifier metadata name

Args:
    metadata (ActorModifierCoreMetadata): The modifier metadata to use
    name (Name): The modifier name to set

Returns:
    ActorModifierCoreMetadata: The modifier metadata to chain operations

    metadata (ActorModifierCoreMetadata): The modifier metadata to use

<a id="unreal.ActorModifierCoreLibrary.set_modifier_metadata_display_name"></a>

#### set_modifier_metadata_display_name

```python
@classmethod
def set_modifier_metadata_display_name(
        cls, metadata: ActorModifierCoreMetadata, name: Text
) -> Tuple[ActorModifierCoreMetadata, ActorModifierCoreMetadata]
```

X.set_modifier_metadata_display_name(metadata, name) -> (ActorModifierCoreMetadata, metadata=ActorModifierCoreMetadata)
Sets the modifier metadata display name (EDITOR-ONLY)

Args:
    metadata (ActorModifierCoreMetadata): The modifier metadata to use
    name (Text): The modifier name to set

Returns:
    ActorModifierCoreMetadata: The modifier metadata to chain operations

    metadata (ActorModifierCoreMetadata): The modifier metadata to use

<a id="unreal.ActorModifierCoreLibrary.set_modifier_metadata_description"></a>

#### set_modifier_metadata_description

```python
@classmethod
def set_modifier_metadata_description(
    cls, metadata: ActorModifierCoreMetadata, description: Text
) -> Tuple[ActorModifierCoreMetadata, ActorModifierCoreMetadata]
```

X.set_modifier_metadata_description(metadata, description) -> (ActorModifierCoreMetadata, metadata=ActorModifierCoreMetadata)
Sets the modifier metadata description (EDITOR-ONLY)

Args:
    metadata (ActorModifierCoreMetadata): The modifier metadata to use
    description (Text): The modifier description to set

Returns:
    ActorModifierCoreMetadata: The modifier metadata to chain operations

    metadata (ActorModifierCoreMetadata): The modifier metadata to use

<a id="unreal.ActorModifierCoreLibrary.set_modifier_metadata_compatibility_rule"></a>

#### set_modifier_metadata_compatibility_rule

```python
@classmethod
def set_modifier_metadata_compatibility_rule(
    cls, metadata: ActorModifierCoreMetadata,
    delegate: ModifierCompatibilityRule
) -> Tuple[ActorModifierCoreMetadata, ActorModifierCoreMetadata]
```

X.set_modifier_metadata_compatibility_rule(metadata, delegate) -> (ActorModifierCoreMetadata, metadata=ActorModifierCoreMetadata)
Sets the modifier metadata compatibility rule

Args:
    metadata (ActorModifierCoreMetadata): The modifier metadata to use
    delegate (ModifierCompatibilityRule): The modifier rule to set

Returns:
    ActorModifierCoreMetadata: The modifier metadata to chain operations

    metadata (ActorModifierCoreMetadata): The modifier metadata to use

<a id="unreal.ActorModifierCoreLibrary.set_modifier_metadata_category"></a>

#### set_modifier_metadata_category

```python
@classmethod
def set_modifier_metadata_category(
    cls, metadata: ActorModifierCoreMetadata, category: Name
) -> Tuple[ActorModifierCoreMetadata, ActorModifierCoreMetadata]
```

X.set_modifier_metadata_category(metadata, category) -> (ActorModifierCoreMetadata, metadata=ActorModifierCoreMetadata)
Sets the modifier metadata category

Args:
    metadata (ActorModifierCoreMetadata): The modifier metadata to use
    category (Name): The modifier category to set

Returns:
    ActorModifierCoreMetadata: The modifier metadata to chain operations

    metadata (ActorModifierCoreMetadata): The modifier metadata to use

<a id="unreal.ActorModifierCoreLibrary.remove_modifier"></a>

#### remove_modifier

```python
@classmethod
def remove_modifier(cls, modifier_stack: ActorModifierCoreStack,
                    operation: ActorModifierCoreRemoveOperation) -> bool
```

X.remove_modifier(modifier_stack, operation) -> bool
Removes an existing modifier from a modifier stack

Args:
    modifier_stack (ActorModifierCoreStack): The modifier stack to use for the operation
    operation (ActorModifierCoreRemoveOperation): The data for this operation

Returns:
    bool: true when the operation was successful

<a id="unreal.ActorModifierCoreLibrary.move_modifier"></a>

#### move_modifier

```python
@classmethod
def move_modifier(cls, modifier_stack: ActorModifierCoreStack,
                  operation: ActorModifierCoreMoveOperation) -> bool
```

X.move_modifier(modifier_stack, operation) -> bool
Moves an existing modifier into a modifier stack

Args:
    modifier_stack (ActorModifierCoreStack): The modifier stack to use for the operation
    operation (ActorModifierCoreMoveOperation): The data for this operation

Returns:
    bool: true when the operation was successful

<a id="unreal.ActorModifierCoreLibrary.is_modifier_enabled"></a>

#### is_modifier_enabled

```python
@classmethod
def is_modifier_enabled(cls,
                        modifier: ActorModifierCoreBase) -> Optional[bool]
```

X.is_modifier_enabled(modifier) -> bool or None
Checks the state of an existing modifier

Args:
    modifier (ActorModifierCoreBase): The modifier to read from

Returns:
    bool or None: true when the operation was successful

    out_enabled (bool): The modifier enabled state

<a id="unreal.ActorModifierCoreLibrary.insert_modifier"></a>

#### insert_modifier

```python
@classmethod
def insert_modifier(
    cls, modifier_stack: ActorModifierCoreStack,
    operation: ActorModifierCoreInsertOperation
) -> Optional[ActorModifierCoreBase]
```

X.insert_modifier(modifier_stack, operation) -> ActorModifierCoreBase or None
Creates and insert a new modifier into a modifier stack

Args:
    modifier_stack (ActorModifierCoreStack): The modifier stack to use for the operation
    operation (ActorModifierCoreInsertOperation): The data for this operation

Returns:
    ActorModifierCoreBase or None: true when a valid modifier is returned

    out_new_modifier (ActorModifierCoreBase): [Out] The newly created modifier

<a id="unreal.ActorModifierCoreLibrary.get_supported_modifiers"></a>

#### get_supported_modifiers

```python
@classmethod
def get_supported_modifiers(
        cls,
        actor: Actor,
        context_position:
    ActorModifierCoreStackPosition = ActorModifierCoreStackPosition.BEFORE,
        context_modifier: ActorModifierCoreBase = None
) -> Optional[Set[Class]]
```

X.get_supported_modifiers(actor, context_position=ActorModifierCoreStackPosition.BEFORE, context_modifier=None) -> Set[type(Class)] or None
Gets all modifier classes supported by this actor at a specific position

Args:
    actor (Actor): The actor to check for compatibility
    context_position (ActorModifierCoreStackPosition): The context position to insert the modifier
    context_modifier (ActorModifierCoreBase): The context modifier for insertion

Returns:
    Set[type(Class)] or None: true when the operation was successful

    out_supported_modifier_classes (Set[type(Class)]): [Out] The modifier classes available

<a id="unreal.ActorModifierCoreLibrary.get_stack_modifiers"></a>

#### get_stack_modifiers

```python
@classmethod
def get_stack_modifiers(
    cls, modifier_stack: ActorModifierCoreStack
) -> Optional[Array[ActorModifierCoreBase]]
```

X.get_stack_modifiers(modifier_stack) -> Array[ActorModifierCoreBase] or None
Retrieves all modifiers from a modifier stack

Args:
    modifier_stack (ActorModifierCoreStack): The modifier stack to read from

Returns:
    Array[ActorModifierCoreBase] or None: true when the operation was successful

    out_modifiers (Array[ActorModifierCoreBase]): [Out] The modifiers contained within the stack

<a id="unreal.ActorModifierCoreLibrary.get_required_modifiers"></a>

#### get_required_modifiers

```python
@classmethod
def get_required_modifiers(
        cls, modifier: ActorModifierCoreBase
) -> Optional[Set[ActorModifierCoreBase]]
```

X.get_required_modifiers(modifier) -> Set[ActorModifierCoreBase] or None
Retrieves all modifiers found before this one that are required for this modifier

Args:
    modifier (ActorModifierCoreBase): The modifier that requires other modifiers

Returns:
    Set[ActorModifierCoreBase] or None: true when the operation was successful

    out_modifiers (Set[ActorModifierCoreBase]): [Out] The required modifiers to use the modifier

<a id="unreal.ActorModifierCoreLibrary.get_modifier_stack"></a>

#### get_modifier_stack

```python
@classmethod
def get_modifier_stack(
        cls,
        modifier: ActorModifierCoreBase) -> Optional[ActorModifierCoreStack]
```

X.get_modifier_stack(modifier) -> ActorModifierCoreStack or None
Retrieves the modifier stack this modifier is in

Args:
    modifier (ActorModifierCoreBase): The modifier to read from

Returns:
    ActorModifierCoreStack or None: true when a valid stack is returned

    out_modifier_stack (ActorModifierCoreStack): [Out] The modifier stack this modifier belongs to

<a id="unreal.ActorModifierCoreLibrary.get_modifiers_by_category"></a>

#### get_modifiers_by_category

```python
@classmethod
def get_modifiers_by_category(cls, category: Name) -> Optional[Set[Class]]
```

X.get_modifiers_by_category(category) -> Set[type(Class)] or None
Retrieves the modifiers classes by a category

Args:
    category (Name): The modifier category to match

Returns:
    Set[type(Class)] or None: true when the operation was successful

    out_supported_modifier_classes (Set[type(Class)]): [Out] The modifier classes that match the category

<a id="unreal.ActorModifierCoreLibrary.get_modifier_name_by_class"></a>

#### get_modifier_name_by_class

```python
@classmethod
def get_modifier_name_by_class(cls, modifier_class: Class) -> Optional[Name]
```

X.get_modifier_name_by_class(modifier_class) -> Name or None
Retrieves the modifier name from a modifier class

Args:
    modifier_class (type(Class)): The modifier class to resolve the name from

Returns:
    Name or None: true when a valid name is returned

    out_modifier_name (Name): [Out] The modifier name

<a id="unreal.ActorModifierCoreLibrary.get_modifier_name"></a>

#### get_modifier_name

```python
@classmethod
def get_modifier_name(cls, modifier: ActorModifierCoreBase) -> Optional[Name]
```

X.get_modifier_name(modifier) -> Name or None
Retrieves the modifier name of an existing modifier

Args:
    modifier (ActorModifierCoreBase): The modifier to read from

Returns:
    Name or None: true when a valid name is returned

    out_modifier_name (Name): [Out] The modifier name

<a id="unreal.ActorModifierCoreLibrary.get_modifier_class"></a>

#### get_modifier_class

```python
@classmethod
def get_modifier_class(cls, modifier_name: Name) -> Optional[Class]
```

X.get_modifier_class(modifier_name) -> type(Class) or None
Retrieves the modifier class from a modifier name

Args:
    modifier_name (Name): The modifier name to resolve

Returns:
    type(Class) or None: true when the operation was successful

    out_modifier_class (type(Class)): [Out] The modifier class that matches the name

<a id="unreal.ActorModifierCoreLibrary.get_modifier_category_by_class"></a>

#### get_modifier_category_by_class

```python
@classmethod
def get_modifier_category_by_class(cls,
                                   modifier_class: Class) -> Optional[Name]
```

X.get_modifier_category_by_class(modifier_class) -> Name or None
Retrieves the modifier category from a modifier class

Args:
    modifier_class (type(Class)): The modifier class to resolve the category from

Returns:
    Name or None: true when a valid category is returned

    out_modifier_category (Name): [Out] The modifier category

<a id="unreal.ActorModifierCoreLibrary.get_modifier_category"></a>

#### get_modifier_category

```python
@classmethod
def get_modifier_category(cls,
                          modifier: ActorModifierCoreBase) -> Optional[Name]
```

X.get_modifier_category(modifier) -> Name or None
Retrieves the modifier category of an existing modifier

Args:
    modifier (ActorModifierCoreBase): The modifier to read from

Returns:
    Name or None: true when a valid category is returned

    out_modifier_category (Name): [Out] The modifier category

<a id="unreal.ActorModifierCoreLibrary.get_modifier_categories"></a>

#### get_modifier_categories

```python
@classmethod
def get_modifier_categories(cls) -> Optional[Set[Name]]
```

X.get_modifier_categories() -> Set[Name] or None
Retrieves the modifier categories available

Returns:
    Set[Name] or None: true when the operation was successful

    out_modifier_categories (Set[Name]): [Out] The modifier categories registered

<a id="unreal.ActorModifierCoreLibrary.get_modifier_actor"></a>

#### get_modifier_actor

```python
@classmethod
def get_modifier_actor(cls,
                       modifier: ActorModifierCoreBase) -> Optional[Actor]
```

X.get_modifier_actor(modifier) -> Actor or None
Retrieves the actor modified by a modifier

Args:
    modifier (ActorModifierCoreBase): The modifier to read from

Returns:
    Actor or None: true when a valid actor is returned

    out_modified_actor (Actor): [Out] The actor modified by this modifier

<a id="unreal.ActorModifierCoreLibrary.get_dependent_modifiers"></a>

#### get_dependent_modifiers

```python
@classmethod
def get_dependent_modifiers(
        cls, modifier: ActorModifierCoreBase
) -> Optional[Set[ActorModifierCoreBase]]
```

X.get_dependent_modifiers(modifier) -> Set[ActorModifierCoreBase] or None
Retrieves all modifiers found after this one that depends on this modifier

Args:
    modifier (ActorModifierCoreBase): The modifier that is required by others

Returns:
    Set[ActorModifierCoreBase] or None: true when the operation was successful

    out_modifiers (Set[ActorModifierCoreBase]): [Out] The dependent modifiers that required the modifier

<a id="unreal.ActorModifierCoreLibrary.get_available_modifiers"></a>

#### get_available_modifiers

```python
@classmethod
def get_available_modifiers(cls) -> Optional[Set[Class]]
```

X.get_available_modifiers() -> Set[type(Class)] or None
Gets all available modifier classes registered

Returns:
    Set[type(Class)] or None: true when the operation was successful

    out_available_modifier_classes (Set[type(Class)]): [Out] The modifier classes registered and available to use

<a id="unreal.ActorModifierCoreLibrary.find_modifier_stack"></a>

#### find_modifier_stack

```python
@classmethod
def find_modifier_stack(
        cls,
        actor: Actor,
        create_if_none: bool = False) -> Optional[ActorModifierCoreStack]
```

X.find_modifier_stack(actor, create_if_none=False) -> ActorModifierCoreStack or None
Retrieves the modifier stack or create one if none is found

Args:
    actor (Actor): The actor to get the modifier stack from
    create_if_none (bool): Whether to create the modifier stack if none is found

Returns:
    ActorModifierCoreStack or None: true when a valid modifier stack is returned

    out_modifier_stack (ActorModifierCoreStack): [Out] The modifier stack for this actor

<a id="unreal.ActorModifierCoreLibrary.find_modifiers_by_name"></a>

#### find_modifiers_by_name

```python
@classmethod
def find_modifiers_by_name(
        cls, modifier_stack: ActorModifierCoreStack,
        modifier_name: Name) -> Array[ActorModifierCoreBase]
```

X.find_modifiers_by_name(modifier_stack, modifier_name) -> Array[ActorModifierCoreBase]
Finds all modifiers with specified class in the stack

Args:
    modifier_stack (ActorModifierCoreStack): The modifier stack to search
    modifier_name (Name): The name of the modifier to look for

Returns:
    Array[ActorModifierCoreBase]: the modifiers with specified name, if any.

<a id="unreal.ActorModifierCoreLibrary.find_modifiers_by_class"></a>

#### find_modifiers_by_class

```python
@classmethod
def find_modifiers_by_class(
        cls, modifier_stack: ActorModifierCoreStack,
        modifier_class: Class) -> Array[ActorModifierCoreBase]
```

X.find_modifiers_by_class(modifier_stack, modifier_class) -> Array[ActorModifierCoreBase]
Finds all modifiers with specified class in the stack

Args:
    modifier_stack (ActorModifierCoreStack): The modifier stack to search
    modifier_class (type(Class)): The class of the modifier to look for

Returns:
    Array[ActorModifierCoreBase]: the modifiers with specified class, if any.

<a id="unreal.ActorModifierCoreLibrary.find_modifier_by_name"></a>

#### find_modifier_by_name

```python
@classmethod
def find_modifier_by_name(cls, modifier_stack: ActorModifierCoreStack,
                          modifier_name: Name) -> ActorModifierCoreBase
```

X.find_modifier_by_name(modifier_stack, modifier_name) -> ActorModifierCoreBase
Returns the first modifier with specified name in the stack

Args:
    modifier_stack (ActorModifierCoreStack): The modifier stack to search
    modifier_name (Name): The name of the modifier to look for

Returns:
    ActorModifierCoreBase: the modifier with specified name, if any.

<a id="unreal.ActorModifierCoreLibrary.find_modifier_by_class"></a>

#### find_modifier_by_class

```python
@classmethod
def find_modifier_by_class(cls, modifier_stack: ActorModifierCoreStack,
                           modifier_class: Class) -> ActorModifierCoreBase
```

X.find_modifier_by_class(modifier_stack, modifier_class) -> ActorModifierCoreBase
Returns the first modifier of a specified class in the stack

Args:
    modifier_stack (ActorModifierCoreStack): The modifier stack to search
    modifier_class (type(Class)): The class of the modifier to look for

Returns:
    ActorModifierCoreBase: the modifier of the specified class, if any.

<a id="unreal.ActorModifierCoreLibrary.find_modifier_of_class"></a>

#### find_modifier_of_class

```python
@classmethod
def find_modifier_of_class(cls, modifier_stack: ActorModifierCoreStack,
                           modifier_class: Class) -> ActorModifierCoreBase
```

deprecated: 'find_modifier_of_class' was renamed to 'find_modifier_by_class'.

<a id="unreal.ActorModifierCoreLibrary.enable_modifier"></a>

#### enable_modifier

```python
@classmethod
def enable_modifier(cls, modifier: ActorModifierCoreBase, state: bool) -> bool
```

X.enable_modifier(modifier, state) -> bool
Sets the state of an existing modifier

Args:
    modifier (ActorModifierCoreBase): The modifier to use for the operation
    state (bool): The new state for the modifier

Returns:
    bool: true when the operation was successful

<a id="unreal.ActorModifierCoreLibrary.contains_modifier"></a>

#### contains_modifier

```python
@classmethod
def contains_modifier(cls, modifier_stack: ActorModifierCoreStack,
                      modifier: ActorModifierCoreBase) -> bool
```

X.contains_modifier(modifier_stack, modifier) -> bool
Checks if a modifier is contained in the stack

Args:
    modifier_stack (ActorModifierCoreStack): The modifier stack to search
    modifier (ActorModifierCoreBase): The modifier to look for

Returns:
    bool: true if the modifier is contained within that stack

<a id="unreal.ActorModifierCoreLibrary.clone_modifier"></a>

#### clone_modifier

```python
@classmethod
def clone_modifier(
    cls, modifier_stack: ActorModifierCoreStack,
    operation: ActorModifierCoreCloneOperation
) -> Optional[ActorModifierCoreBase]
```

X.clone_modifier(modifier_stack, operation) -> ActorModifierCoreBase or None
Clones an existing modifier into a modifier stack

Args:
    modifier_stack (ActorModifierCoreStack): The modifier stack to use for the operation
    operation (ActorModifierCoreCloneOperation): The data for this operation

Returns:
    ActorModifierCoreBase or None: true when a valid modifier is returned

    out_new_modifier (ActorModifierCoreBase): [Out] The newly created modifier

<a id="unreal.ActorModifierCoreLibrary.add_modifier_metadata_dependency"></a>

#### add_modifier_metadata_dependency

```python
@classmethod
def add_modifier_metadata_dependency(
    cls, metadata: ActorModifierCoreMetadata, modifier_class: Class
) -> Tuple[ActorModifierCoreMetadata, ActorModifierCoreMetadata]
```

X.add_modifier_metadata_dependency(metadata, modifier_class) -> (ActorModifierCoreMetadata, metadata=ActorModifierCoreMetadata)
Adds a modifier metadata dependency for this modifier

Args:
    metadata (ActorModifierCoreMetadata): The modifier metadata to use
    modifier_class (type(Class)): The modifier dependency to add

Returns:
    ActorModifierCoreMetadata: The modifier metadata to chain operations

    metadata (ActorModifierCoreMetadata): The modifier metadata to use

<a id="unreal.ActorModifierCoreSharedActor"></a>