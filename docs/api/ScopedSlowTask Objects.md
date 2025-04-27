## ScopedSlowTask Objects

```python
class ScopedSlowTask(object)
```

Type used to create and managed a scoped slow task in Python

<a id="unreal.ScopedSlowTask.__init__"></a>

#### __init__

```python
def __init__(work: float,
             desc: Union[Text, str] = "",
             enabled: bool = True) -> None
```

<a id="unreal.ScopedSlowTask.__enter__"></a>

#### __enter__

```python
def __enter__() -> ScopedSlowTask
```

__enter__(self) -> ScopedSlowTask -- begin this slow task

<a id="unreal.ScopedSlowTask.__exit__"></a>

#### __exit__

```python
def __exit__(type: Optional[Type[BaseException]],
             value: Optional[BaseException],
             traceback: Optional[TracebackType]) -> bool
```

__exit__(self, type: Optional[Type[BaseException]], value: Optional[BaseException], traceback: Optional[TracebackType]) -> bool -- end this slow task

<a id="unreal.ScopedSlowTask.make_dialog_delayed"></a>

#### make_dialog_delayed

```python
def make_dialog_delayed(delay: float,
                        can_cancel: bool = False,
                        allow_in_pie: bool = False) -> None
```

make_dialog_delayed(self, delay: float, can_cancel: bool = False, allow_in_pie: bool = False) -> None -- creates a new dialog for this slow task after the given time delay (in seconds). If the task completes before this time, no dialog will be shown

<a id="unreal.ScopedSlowTask.make_dialog"></a>

#### make_dialog

```python
def make_dialog(can_cancel: bool = False, allow_in_pie: bool = False) -> None
```

make_dialog(self, can_cancel: bool = False, allow_in_pie: bool = False) -> None -- creates a new dialog for this slow task, if there is currently not one open

<a id="unreal.ScopedSlowTask.enter_progress_frame"></a>

#### enter_progress_frame

```python
def enter_progress_frame(work: float = 1.0,
                         desc: Union[Text, str] = "") -> None
```

enter_progress_frame(self, work: float = 1.0, desc: Union[Text, str] = "") -> None -- indicate that we are to enter a frame that will take up the specified amount of work (completes any previous frames)

<a id="unreal.ScopedSlowTask.should_cancel"></a>

#### should_cancel

```python
def should_cancel() -> bool
```

x.should_cancel() -> bool -- True if the user has requested that the slow task be canceled

<a id="unreal.ObjectIterator"></a>