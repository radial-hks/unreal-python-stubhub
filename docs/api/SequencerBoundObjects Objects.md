## SequencerBoundObjects Objects

```python
class SequencerBoundObjects(StructBase)
```

Sequencer Bound Objects

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScriptingEditor
- **File**: SequencerTools.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``binding_proxy`` (MovieSceneBindingProxy):  [Read-Write]
- ``bound_objects`` (Array[Object]):  [Read-Write]

<a id="unreal.SequencerBoundObjects.__init__"></a>

#### __init__

```python
def __init__(binding_proxy: MovieSceneBindingProxy = [[], None],
             bound_objects: Array[Object] = []) -> None
```

<a id="unreal.SequencerBoundObjects.binding_proxy"></a>

#### binding_proxy

```python
@property
def binding_proxy() -> MovieSceneBindingProxy
```

(MovieSceneBindingProxy):  [Read-Write]

<a id="unreal.SequencerBoundObjects.binding_proxy"></a>

#### binding_proxy

```python
@binding_proxy.setter
def binding_proxy(value: MovieSceneBindingProxy) -> None
```

<a id="unreal.SequencerBoundObjects.bound_objects"></a>

#### bound_objects

```python
@property
def bound_objects() -> Array[Object]
```

(Array[Object]):  [Read-Write]

<a id="unreal.SequencerBoundObjects.bound_objects"></a>

#### bound_objects

```python
@bound_objects.setter
def bound_objects(value: Array[Object]) -> None
```

<a id="unreal.SequencerQuickBindingResult"></a>