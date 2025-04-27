## _ObjectBase Objects

```python
class _ObjectBase(_WrapperBase)
```

Type for all Unreal exposed object instances

<a id="unreal._ObjectBase.__init__"></a>

#### __init__

```python
def __init__(outer: Optional[Object] = None,
             name: Union[Name, str] = "None") -> None
```

<a id="unreal._ObjectBase._post_init"></a>

#### _post_init

```python
def _post_init() -> None
```

_post_init(self) -> None -- called during Unreal object initialization (equivalent to PostInitProperties in C++)

<a id="unreal._ObjectBase.cast"></a>

#### cast

```python
@classmethod
def cast(cls: Type[_T], object: object) -> _T
```

cast(cls: Type[_T], object: object) -> _T -- cast the given object to this Unreal object type or raise an exception if the cast is not possible

<a id="unreal._ObjectBase.get_default_object"></a>

#### get_default_object

```python
@classmethod
def get_default_object(cls: Type[_T]) -> _T
```

get_default_object(cls: Type[_T]) -> _T -- get the Unreal class default object (CDO) of this type

<a id="unreal._ObjectBase.static_class"></a>

#### static_class

```python
@classmethod
def static_class(cls) -> Class
```

static_class(cls) -> Class -- get the Unreal class of this type

<a id="unreal._ObjectBase.get_class"></a>

#### get_class

```python
def get_class() -> Class
```

get_class(self) -> Class -- get the Unreal class of this instance

<a id="unreal._ObjectBase.get_outer"></a>

#### get_outer

```python
def get_outer() -> Any
```

get_outer(self) -> Any -- get the outer object from this instance (if any)

<a id="unreal._ObjectBase.get_typed_outer"></a>

#### get_typed_outer

```python
def get_typed_outer(type: Union[Class, type]) -> Any
```

get_typed_outer(self, type: Union[Class, type]) -> Any -- get the first outer object of the given type from this instance (if any)

<a id="unreal._ObjectBase.get_outermost"></a>

#### get_outermost

```python
def get_outermost() -> Package
```

get_outermost(self) -> Package -- get the outermost object (the package) from this instance

<a id="unreal._ObjectBase.is_package_external"></a>

#### is_package_external

```python
def is_package_external() -> bool
```

is_package_external(self) -> bool -- returns true if this instance has a different package than its outer's package

<a id="unreal._ObjectBase.get_package"></a>

#### get_package

```python
def get_package() -> Package
```

get_package(self) -> Package -- get the package directly associated with this instance

<a id="unreal._ObjectBase.get_name"></a>

#### get_name

```python
def get_name() -> str
```

get_name(self) -> str -- get the name of this instance

<a id="unreal._ObjectBase.get_fname"></a>

#### get_fname

```python
def get_fname() -> Name
```

get_fname(self) -> Name -- get the name of this instance

<a id="unreal._ObjectBase.get_full_name"></a>

#### get_full_name

```python
def get_full_name() -> str
```

get_full_name(self) -> str -- get the full name (class name + full path) of this instance

<a id="unreal._ObjectBase.get_path_name"></a>

#### get_path_name

```python
def get_path_name() -> str
```

get_path_name(self) -> str -- get the path name of this instance

<a id="unreal._ObjectBase.get_world"></a>

#### get_world

```python
def get_world() -> Optional[World]
```

get_world(self) -> Optional[World] -- get the world associated with this instance (if any)

<a id="unreal._ObjectBase.modify"></a>

#### modify

```python
def modify(always_mark_dirty: bool = True) -> bool
```

modify(self, always_mark_dirty: bool = True) -> bool -- inform that this instance is about to be modified (tracks changes for undo/redo if transactional)

<a id="unreal._ObjectBase.rename"></a>

#### rename

```python
def rename(name: Union[Name, str] = "None",
           outer: Optional[Object] = None) -> bool
```

rename(self, name: Union[Name, str]="None", outer: Optional[Object]=None) -> bool -- rename this instance and/or change its outer

<a id="unreal._ObjectBase.get_editor_property"></a>

#### get_editor_property

```python
def get_editor_property(name: str) -> object
```

get_editor_property(self, name: str) -> object -- get the value of any property visible to the editor

<a id="unreal._ObjectBase.set_editor_property"></a>

#### set_editor_property

```python
def set_editor_property(
    name: str,
    value: object,
    notify_mode: PropertyAccessChangeNotifyMode = PropertyAccessChangeNotifyMode
    .DEFAULT
) -> None
```

set_editor_property(self, name: str, value: object, notify_mode: PropertyAccessChangeNotifyMode=PropertyAccessChangeNotifyMode.DEFAULT) -> None -- set the value of any property visible to the editor, ensuring that the pre/post change notifications are called

<a id="unreal._ObjectBase.set_editor_properties"></a>

#### set_editor_properties

```python
def set_editor_properties(properties: Mapping[str, object]) -> None
```

set_editor_properties(self, properties: Mapping[str, object]) -> None -- set the value of any properties visible to the editor (from a name->value dict), ensuring that the pre/post change notifications are called

<a id="unreal._ObjectBase.call_method"></a>

#### call_method

```python
def call_method(name: str, *args: Tuple[object, ...],
                **kwargs: Mapping[str, object]) -> Any
```

call_method(self, name: str, *args: Tuple[object, ...], **kwargs: Mapping[str, object]) -> Any -- call a method on this object via Unreal reflection using the given ordered (a tuple passed as args) or named (a dict passed as kwargs) argument data - allows calling methods that don't have Python glue

<a id="unreal.StructBase"></a>