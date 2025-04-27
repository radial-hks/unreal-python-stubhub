## SubobjectDataBlueprintFunctionLibrary Objects

```python
class SubobjectDataBlueprintFunctionLibrary(BlueprintFunctionLibrary)
```

A function library with wrappers around the getter/setter functions for FSubobjectData
that will make it easier to use within blueprint contexts.

**C++ Source:**

- **Module**: SubobjectDataInterface
- **File**: SubobjectDataBlueprintFunctionLibrary.h

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_valid"></a>

#### is_valid

```python
@classmethod
def is_valid(cls, data: SubobjectData) -> bool
```

X.is_valid(data) -> bool
Is Valid

Args:
    data (SubobjectData): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_scene_component"></a>

#### is_scene_component

```python
@classmethod
def is_scene_component(cls, data: SubobjectData) -> bool
```

X.is_scene_component(data) -> bool
Is Scene Component

Args:
    data (SubobjectData): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_root_component"></a>

#### is_root_component

```python
@classmethod
def is_root_component(cls, data: SubobjectData) -> bool
```

X.is_root_component(data) -> bool
Is Root Component

Args:
    data (SubobjectData): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_root_actor"></a>

#### is_root_actor

```python
@classmethod
def is_root_actor(cls, data: SubobjectData) -> bool
```

X.is_root_actor(data) -> bool
Is Root Actor

Args:
    data (SubobjectData): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_native_component"></a>

#### is_native_component

```python
@classmethod
def is_native_component(cls, data: SubobjectData) -> bool
```

X.is_native_component(data) -> bool
Is Native Component

Args:
    data (SubobjectData): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_instanced_component"></a>

#### is_instanced_component

```python
@classmethod
def is_instanced_component(cls, data: SubobjectData) -> bool
```

X.is_instanced_component(data) -> bool
Is Instanced Component

Args:
    data (SubobjectData): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_instanced_actor"></a>

#### is_instanced_actor

```python
@classmethod
def is_instanced_actor(cls, data: SubobjectData) -> bool
```

X.is_instanced_actor(data) -> bool
Is Instanced Actor

Args:
    data (SubobjectData): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_inherited_component"></a>

#### is_inherited_component

```python
@classmethod
def is_inherited_component(cls, data: SubobjectData) -> bool
```

X.is_inherited_component(data) -> bool
Is Inherited Component

Args:
    data (SubobjectData): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_handle_valid"></a>

#### is_handle_valid

```python
@classmethod
def is_handle_valid(cls, data_handle: SubobjectDataHandle) -> bool
```

X.is_handle_valid(data_handle) -> bool
Is Handle Valid

Args:
    data_handle (SubobjectDataHandle): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_default_scene_root"></a>

#### is_default_scene_root

```python
@classmethod
def is_default_scene_root(cls, data: SubobjectData) -> bool
```

X.is_default_scene_root(data) -> bool
Is Default Scene Root

Args:
    data (SubobjectData): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_component"></a>

#### is_component

```python
@classmethod
def is_component(cls, data: SubobjectData) -> bool
```

X.is_component(data) -> bool
Returns true if this subobject is a component.

Args:
    data (SubobjectData): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_child_actor"></a>

#### is_child_actor

```python
@classmethod
def is_child_actor(cls, data: SubobjectData) -> bool
```

X.is_child_actor(data) -> bool
Is Child Actor

Args:
    data (SubobjectData): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_attached_to"></a>

#### is_attached_to

```python
@classmethod
def is_attached_to(cls, data: SubobjectData,
                   handle: SubobjectDataHandle) -> bool
```

X.is_attached_to(data, handle) -> bool
Is Attached To

Args:
    data (SubobjectData): 
    handle (SubobjectDataHandle): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.is_actor"></a>

#### is_actor

```python
@classmethod
def is_actor(cls, data: SubobjectData) -> bool
```

X.is_actor(data) -> bool
Is Actor

Args:
    data (SubobjectData): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.get_variable_name"></a>

#### get_variable_name

```python
@classmethod
def get_variable_name(cls, data: SubobjectData) -> Name
```

X.get_variable_name(data) -> Name
Get Variable Name

Args:
    data (SubobjectData): 

Returns:
    Name:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.get_parent_handle"></a>

#### get_parent_handle

```python
@classmethod
def get_parent_handle(cls, data: SubobjectData) -> SubobjectDataHandle
```

X.get_parent_handle(data) -> SubobjectDataHandle


Args:
    data (SubobjectData): 

Returns:
    SubobjectDataHandle: 

    out_handle (SubobjectDataHandle):

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.get_object_for_blueprint"></a>

#### get_object_for_blueprint

```python
@classmethod
def get_object_for_blueprint(cls, data: SubobjectData,
                             blueprint: Blueprint) -> Object
```

X.get_object_for_blueprint(data, blueprint) -> Object
Get Object for Blueprint

Args:
    data (SubobjectData): 
    blueprint (Blueprint): 

Returns:
    Object:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.get_object"></a>

#### get_object

```python
@classmethod
def get_object(cls,
               data: SubobjectData,
               even_if_pending_kill: bool = False) -> Object
```

X.get_object(data, even_if_pending_kill=False) -> Object
Get Object

Args:
    data (SubobjectData): 
    even_if_pending_kill (bool): 

Returns:
    Object:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.get_handle"></a>

#### get_handle

```python
@classmethod
def get_handle(cls, data: SubobjectData) -> SubobjectDataHandle
```

X.get_handle(data) -> SubobjectDataHandle


Args:
    data (SubobjectData): 

Returns:
    SubobjectDataHandle: 

    out_handle (SubobjectDataHandle):

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.get_display_name"></a>

#### get_display_name

```python
@classmethod
def get_display_name(cls, data: SubobjectData) -> Text
```

X.get_display_name(data) -> Text
Get Display Name

Args:
    data (SubobjectData): 

Returns:
    Text:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.get_data"></a>

#### get_data

```python
@classmethod
def get_data(cls, data_handle: SubobjectDataHandle) -> SubobjectData
```

X.get_data(data_handle) -> SubobjectData
Get Data

Args:
    data_handle (SubobjectDataHandle): 

Returns:
    SubobjectData: 

    out_data (SubobjectData):

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.get_blueprint"></a>

#### get_blueprint

```python
@classmethod
def get_blueprint(cls, data: SubobjectData) -> Blueprint
```

X.get_blueprint(data) -> Blueprint
Get Blueprint

Args:
    data (SubobjectData): 

Returns:
    Blueprint:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.can_reparent"></a>

#### can_reparent

```python
@classmethod
def can_reparent(cls, data: SubobjectData) -> bool
```

X.can_reparent(data) -> bool


Args:
    data (SubobjectData): 

Returns:
    bool: Whether or not this object represents a subobject that can be reparented to other subobjects based on its context.

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.can_rename"></a>

#### can_rename

```python
@classmethod
def can_rename(cls, data: SubobjectData) -> bool
```

X.can_rename(data) -> bool
Can Rename

Args:
    data (SubobjectData): 

Returns:
    bool:

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.can_edit"></a>

#### can_edit

```python
@classmethod
def can_edit(cls, data: SubobjectData) -> bool
```

X.can_edit(data) -> bool


Args:
    data (SubobjectData): 

Returns:
    bool: Whether or not we can edit properties for this subobject

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.can_duplicate"></a>

#### can_duplicate

```python
@classmethod
def can_duplicate(cls, data: SubobjectData) -> bool
```

X.can_duplicate(data) -> bool


Args:
    data (SubobjectData): 

Returns:
    bool: Whether or not this object represents a subobject that can be duplicated

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.can_delete"></a>

#### can_delete

```python
@classmethod
def can_delete(cls, data: SubobjectData) -> bool
```

X.can_delete(data) -> bool


Args:
    data (SubobjectData): 

Returns:
    bool: Whether or not this object represents a subobject that can be deleted

<a id="unreal.SubobjectDataBlueprintFunctionLibrary.can_copy"></a>

#### can_copy

```python
@classmethod
def can_copy(cls, data: SubobjectData) -> bool
```

X.can_copy(data) -> bool


Args:
    data (SubobjectData): 

Returns:
    bool: Whether or not this object represents a subobject that can be copied

<a id="unreal.SubobjectDataSubsystem"></a>