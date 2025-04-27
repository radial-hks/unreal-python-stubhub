## SelectedActorIterator Objects

```python
class SelectedActorIterator(object)
```

Type for iterating selected Unreal actor instances

<a id="unreal.SelectedActorIterator.__init__"></a>

#### __init__

```python
def __init__(world: World, type: Union[Class, type] = ...) -> None
```

<a id="unreal.SelectedActorIterator.__iter__"></a>

#### __iter__

```python
def __iter__() -> Iterator[Any]
```

<a id="unreal.get_engine_subsystem"></a>

#### get_engine_subsystem

```python
def get_engine_subsystem(
    subsystem: Union[Class, type[_EngineSubsystemTypeVar]]
) -> Optional[_EngineSubsystemTypeVar]
```

get_engine_subsystem(subsystem : Union[Class, type[_EngineSubsystemTypeVar]]) -> Optional[_EngineSubsystemTypeVar] -- returns the requested Engine subsystem or None

<a id="unreal.get_editor_subsystem"></a>

#### get_editor_subsystem

```python
def get_editor_subsystem(
    subsystem: Union[Class, type[_EditorSubsystemTypeVar]]
) -> Optional[_EditorSubsystemTypeVar]
```

get_editor_subsystem(subsystem : Union[Class, type[_EditorSubsystemTypeVar]]) -> Optional[_EditorSubsystemTypeVar] -- returns the requested Editor subsystem or None

<a id="unreal.ScopedEditorTransaction"></a>