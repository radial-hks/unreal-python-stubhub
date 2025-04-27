## MulticastDelegateBase Objects

```python
class MulticastDelegateBase(_WrapperBase)
```

Type for all Unreal exposed multicast delegate instances

<a id="unreal.MulticastDelegateBase.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.MulticastDelegateBase.cast"></a>

#### cast

```python
@classmethod
def cast(cls: Type[_T], object: object) -> _T
```

cast(cls: Type[_T], object: object) -> _T -- cast the given object to this Unreal delegate type

<a id="unreal.MulticastDelegateBase.__copy__"></a>

#### __copy__

```python
def __copy__() -> Any
```

__copy__(self) -> Any -- copy this Unreal delegate

<a id="unreal.MulticastDelegateBase.copy"></a>

#### copy

```python
def copy() -> Any
```

copy(self) -> Any -- copy this Unreal delegate

<a id="unreal.MulticastDelegateBase.is_bound"></a>

#### is_bound

```python
def is_bound() -> bool
```

is_bound(self) -> bool -- is this Unreal delegate bound to something?

<a id="unreal.MulticastDelegateBase.add_function"></a>

#### add_function

```python
def add_function(obj: Object, name: Union[Name, str]) -> None
```

add_function(self, obj: Object, name: Union[Name, str]) -> None -- add a binding to a named Unreal function on the given object instance to the invocation list of this Unreal delegate

<a id="unreal.MulticastDelegateBase.add_callable"></a>

#### add_callable

```python
def add_callable(callable: Callable[..., Any]) -> None
```

add_callable(self, callable: Callable[..., Any]) -> None -- add a binding to a Python callable to the invocation list of this Unreal delegate

<a id="unreal.MulticastDelegateBase.add_function_unique"></a>

#### add_function_unique

```python
def add_function_unique(obj: Object, name: Union[Name, str]) -> None
```

add_function_unique(self, obj: Object, name: Union[Name, str]) -> None -- add a unique binding to a named Unreal function on the given object instance to the invocation list of this Unreal delegate

<a id="unreal.MulticastDelegateBase.add_callable_unique"></a>

#### add_callable_unique

```python
def add_callable_unique(callable: Callable[..., Any]) -> None
```

add_callable_unique(self, callable: Callable[..., Any]) -> None -- add a unique binding to a Python callable to the invocation list of this Unreal delegate

<a id="unreal.MulticastDelegateBase.remove_function"></a>

#### remove_function

```python
def remove_function(obj: Object, name: Union[Name, str]) -> None
```

remove_function(self, obj: Object, name: Union[Name, str]) -> None -- remove a binding to a named Unreal function on the given object instance from the invocation list of this Unreal delegate

<a id="unreal.MulticastDelegateBase.remove_callable"></a>

#### remove_callable

```python
def remove_callable(callable: Callable[..., Any]) -> None
```

remove_callable(self, callable: Callable[..., Any]) -> None -- remove a binding to a Python callable from the invocation list of this Unreal delegate

<a id="unreal.MulticastDelegateBase.remove_object"></a>

#### remove_object

```python
def remove_object(obj: Object) -> None
```

remove_object(self, obj: Object) -> None -- remove all bindings for the given object instance from the invocation list of this Unreal delegate

<a id="unreal.MulticastDelegateBase.contains_function"></a>

#### contains_function

```python
def contains_function(obj: Object, name: Union[Name, str]) -> bool
```

contains_function(self, obj: Object, name: Union[Name, str]) -> bool -- does the invocation list of this Unreal delegate contain a binding to a named Unreal function on the given object instance

<a id="unreal.MulticastDelegateBase.contains_callable"></a>

#### contains_callable

```python
def contains_callable(callable: Callable[..., Any]) -> bool
```

contains_callable(self, callable: Callable[..., Any]) -> bool -- does the invocation list of this Unreal delegate contain a binding to a Python callable

<a id="unreal.MulticastDelegateBase.clear"></a>

#### clear

```python
def clear() -> None
```

x.clear() -> None -- clear the invocation list of this Unreal delegate

<a id="unreal.MulticastDelegateBase.broadcast"></a>

#### broadcast

```python
def broadcast(*args: Any) -> None
```

x.broadcast(*args: Any) -> None -- invoke this Unreal multicast delegate

<a id="unreal.Name"></a>