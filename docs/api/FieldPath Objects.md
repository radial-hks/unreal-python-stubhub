## FieldPath Objects

```python
class FieldPath(_WrapperBase)
```

Type for all Unreal exposed FieldPath instances

<a id="unreal.FieldPath.__init__"></a>

#### __init__

```python
def __init__(value: Union[FieldPath, str] = "") -> None
```

<a id="unreal.FieldPath.cast"></a>

#### cast

```python
@classmethod
def cast(cls, obj: object) -> FieldPath
```

cast(cls, obj: object) -> FieldPath -- cast the given object to this Unreal field path type

<a id="unreal.FieldPath.__copy__"></a>

#### __copy__

```python
def __copy__() -> FieldPath
```

__copy__(self) -> FieldPath -- copy this Unreal field path

<a id="unreal.FieldPath.copy"></a>

#### copy

```python
def copy() -> FieldPath
```

copy(self) -> FieldPath -- copy this Unreal field path

<a id="unreal.FieldPath.is_valid"></a>

#### is_valid

```python
def is_valid() -> bool
```

is_valid(self) -> bool -- whether this Unreal field path refers to an existing Unreal field

<a id="unreal.register_slate_pre_tick_callback"></a>

#### register_slate_pre_tick_callback

```python
def register_slate_pre_tick_callback(
        callable: Union[Callable[[float], None], DelegateBase]) -> object
```

x.register_slate_pre_tick_callback(callable: Union[Callable[[float], None], DelegateBase]) -> object -- register the given callable (taking a single float) as a pre-tick callback in Slate

<a id="unreal.unregister_slate_pre_tick_callback"></a>

#### unregister_slate_pre_tick_callback

```python
def unregister_slate_pre_tick_callback(handle: object) -> None
```

x.unregister_slate_pre_tick_callback(handle: object) -> None -- unregister the given handle from a previous call to register_slate_pre_tick_callback

<a id="unreal.register_slate_post_tick_callback"></a>

#### register_slate_post_tick_callback

```python
def register_slate_post_tick_callback(
        callable: Union[Callable[[float], None], DelegateBase]) -> object
```

x.register_slate_post_tick_callback(callable: Union[Callable[[float], None], DelegateBase]) -> object -- register the given callable (taking a single float) as a pre-tick callback in Slate

<a id="unreal.unregister_slate_post_tick_callback"></a>

#### unregister_slate_post_tick_callback

```python
def unregister_slate_post_tick_callback(handle: object) -> None
```

x.unregister_slate_post_tick_callback(handle: object) -> None -- unregister the given handle from a previous call to register_slate_post_tick_callback

<a id="unreal.parent_external_window_to_slate"></a>

#### parent_external_window_to_slate

```python
def parent_external_window_to_slate(
    external_window_handle: object,
    parent_search_method:
    SlateParentWindowSearchMethod = SlateParentWindowSearchMethod.ACTIVE_WINDOW
) -> None
```

x.parent_external_window_to_slate(external_window_handle: object, parent_search_method: SlateParentWindowSearchMethod = SlateParentWindowSearchMethod.ACTIVE_WINDOW) -> None -- parent the given OS specific external window handle to a suitable Slate window

<a id="unreal.get_blueprint_generated_types"></a>

#### get_blueprint_generated_types

```python
def get_blueprint_generated_types(
        paths: Iterable[str]) -> Optional[Union[type, Tuple[type, ...]]]
```

get_blueprint_generated_types(paths: Iterable[str]) -> Optional[Union[type, Tuple[type, ...]]] -- get the Python types (will return a tuple for multiple types) for the given set of Blueprint asset paths (may be a sequence type or set of arguments)

<a id="unreal.ActorIterator"></a>