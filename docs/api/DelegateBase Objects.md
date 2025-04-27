## DelegateBase Objects

```python
class DelegateBase(_WrapperBase)
```

Type for all Unreal exposed delegate instances

<a id="unreal.DelegateBase.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.DelegateBase.cast"></a>

#### cast

```python
@classmethod
def cast(cls: Type[_T], object: object) -> _T
```

cast(cls: Type[_T], object: object) -> _T -- cast the given object to this Unreal delegate type

<a id="unreal.DelegateBase.__copy__"></a>

#### __copy__

```python
def __copy__() -> Any
```

__copy__(self) -> Any -- copy this Unreal delegate

<a id="unreal.DelegateBase.copy"></a>

#### copy

```python
def copy() -> Any
```

copy(self) -> Any -- copy this Unreal delegate

<a id="unreal.DelegateBase.is_bound"></a>

#### is_bound

```python
def is_bound() -> bool
```

is_bound(self) -> bool -- is this Unreal delegate bound to something?

<a id="unreal.DelegateBase.bind_delegate"></a>

#### bind_delegate

```python
def bind_delegate(delegate: DelegateBase) -> None
```

bind_delegate(self, delegate: DelegateBase) -> None -- bind this Unreal delegate to the same object and function as another delegate

<a id="unreal.DelegateBase.bind_function"></a>

#### bind_function

```python
def bind_function(obj: Object, name: Union[Name, str]) -> None
```

bind_function(self, obj: Object, name: Union[Name, str]) -> None -- bind this Unreal delegate to a named Unreal function on the given object instance

<a id="unreal.DelegateBase.bind_callable"></a>

#### bind_callable

```python
def bind_callable(callable: Callable[..., Any]) -> None
```

bind_callable(self, callable: Callable[..., Any]) -> None -- bind this Unreal delegate to a Python callable

<a id="unreal.DelegateBase.unbind"></a>

#### unbind

```python
def unbind() -> None
```

unbind(self) -> None -- unbind this Unreal delegate

<a id="unreal.DelegateBase.execute"></a>

#### execute

```python
def execute(*args: Any) -> Any
```

execute(self, *args: Any) -> Any -- call this Unreal delegate, but error if it's unbound

<a id="unreal.DelegateBase.execute_if_bound"></a>

#### execute_if_bound

```python
def execute_if_bound(*args: Any) -> Any
```

x.execute_if_bound(self, *args: Any) -> Any -- call this Unreal delegate, but only if it's bound to something

<a id="unreal.MulticastDelegateBase"></a>