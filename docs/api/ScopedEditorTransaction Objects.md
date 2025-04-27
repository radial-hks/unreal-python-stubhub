## ScopedEditorTransaction Objects

```python
class ScopedEditorTransaction(object)
```

Type used to create and managed a scoped editor transaction in Python

<a id="unreal.ScopedEditorTransaction.__init__"></a>

#### __init__

```python
def __init__(desc: Union[Text, str]) -> None
```

<a id="unreal.ScopedEditorTransaction.__enter__"></a>

#### __enter__

```python
def __enter__() -> ScopedEditorTransaction
```

__enter__(self) -> ScopedEditorTransaction -- begin this transaction

<a id="unreal.ScopedEditorTransaction.__exit__"></a>

#### __exit__

```python
def __exit__(type: Optional[Type[BaseException]],
             value: Optional[BaseException],
             traceback: Optional[TracebackType]) -> bool
```

__exit__(self, type: Optional[Type[BaseException]], value: Optional[BaseException], traceback: Optional[TracebackType]) -> bool -- end this transaction

<a id="unreal.ScopedEditorTransaction.cancel"></a>

#### cancel

```python
def cancel() -> None
```

cancel(self) -> None -- cancel this transaction

<a id="unreal.RangeBoundTypes"></a>