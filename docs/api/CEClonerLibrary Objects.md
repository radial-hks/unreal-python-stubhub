## CEClonerLibrary Objects

```python
class CEClonerLibrary(BlueprintFunctionLibrary)
```

Blueprint operations for cloner

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerLibrary.h

<a id="unreal.CEClonerLibrary.set_cloner_layout_by_name"></a>

#### set_cloner_layout_by_name

```python
@classmethod
def set_cloner_layout_by_name(
        cls, world_context: Object, latent_info: LatentActionInfo,
        cloner: CEClonerComponent,
        layout_name: Name) -> Tuple[bool, CEClonerLayoutBase]
```

X.set_cloner_layout_by_name(world_context, latent_info, cloner, layout_name) -> (out_success=bool, out_layout=CEClonerLayoutBase)
Sets the active layout of a cloner and wait until the layout is loaded and active

Args:
    world_context (Object): World context object
    latent_info (LatentActionInfo): Latent action info
    cloner (CEClonerComponent): Target cloner component
    layout_name (Name): Cloner layout name

Returns:
    tuple: 

    out_success (bool): [Out] True when the layout class is set

    out_layout (CEClonerLayoutBase): [Out] Layout object corresponding to the layout class

<a id="unreal.CEClonerLibrary.set_cloner_layout_by_class"></a>

#### set_cloner_layout_by_class

```python
@classmethod
def set_cloner_layout_by_class(
        cls, world_context: Object, latent_info: LatentActionInfo,
        cloner: CEClonerComponent,
        layout_class: Class) -> Tuple[bool, CEClonerLayoutBase]
```

X.set_cloner_layout_by_class(world_context, latent_info, cloner, layout_class) -> (out_success=bool, out_layout=CEClonerLayoutBase)
Sets the active layout of a cloner and wait until the layout is loaded and active

Args:
    world_context (Object): World context object
    latent_info (LatentActionInfo): Latent action info
    cloner (CEClonerComponent): Target cloner component
    layout_class (type(Class)): Cloner layout class

Returns:
    tuple: 

    out_success (bool): [Out] True when the layout class is set

    out_layout (CEClonerLayoutBase): [Out] Layout object corresponding to the layout class

<a id="unreal.CEClonerLibrary.get_cloner_layout_name"></a>

#### get_cloner_layout_name

```python
@classmethod
def get_cloner_layout_name(cls, layout_class: Class) -> Optional[Name]
```

X.get_cloner_layout_name(layout_class) -> Name or None
Retrieves the layout name from a layout class

Args:
    layout_class (type(Class)): Layout class to get the name from

Returns:
    Name or None: true when the layout name was retrieved

    out_layout_name (Name): [Out] Layout name

<a id="unreal.CEClonerLibrary.get_cloner_layout_classes"></a>

#### get_cloner_layout_classes

```python
@classmethod
def get_cloner_layout_classes(cls) -> Set[Class]
```

X.get_cloner_layout_classes() -> Set[type(Class)]
Retrieves all layout classes available for a cloner

Returns:
    Set[type(Class)]: 

    out_layout_classes (Set[type(Class)]): [Out] Layout classes available

<a id="unreal.CEClonerLibrary.get_cloner_layout_class"></a>

#### get_cloner_layout_class

```python
@classmethod
def get_cloner_layout_class(cls, layout_name: Name) -> Optional[Class]
```

X.get_cloner_layout_class(layout_name) -> type(Class) or None
Retrieves the layout class from a layout name

Args:
    layout_name (Name): Layout name to get the class from

Returns:
    type(Class) or None: true when the layout class was retrieved

    out_layout_class (type(Class)): [Out] Layout class

<a id="unreal.CEClonerLibrary.get_cloner_extension_classes"></a>

#### get_cloner_extension_classes

```python
@classmethod
def get_cloner_extension_classes(cls) -> Set[Class]
```

X.get_cloner_extension_classes() -> Set[type(Class)]
Retrieves all extension classes available for a cloner

Returns:
    Set[type(Class)]: 

    out_extension_classes (Set[type(Class)]): [Out] Extension classes available

<a id="unreal.CEClonerLifetimeExtension"></a>