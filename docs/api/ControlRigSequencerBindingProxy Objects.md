## ControlRigSequencerBindingProxy Objects

```python
class ControlRigSequencerBindingProxy(StructBase)
```

Control Rig Sequencer Binding Proxy

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: ControlRigSequencerEditorLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_rig`` (ControlRig):  [Read-Write]
- ``proxy`` (MovieSceneBindingProxy):  [Read-Write]
- ``track`` (MovieSceneControlRigParameterTrack):  [Read-Write]

<a id="unreal.ControlRigSequencerBindingProxy.__init__"></a>

#### __init__

```python
def __init__(proxy: MovieSceneBindingProxy = [[], None],
             control_rig: ControlRig = None,
             track: MovieSceneControlRigParameterTrack = None) -> None
```

<a id="unreal.ControlRigSequencerBindingProxy.proxy"></a>

#### proxy

```python
@property
def proxy() -> MovieSceneBindingProxy
```

(MovieSceneBindingProxy):  [Read-Only]

<a id="unreal.ControlRigSequencerBindingProxy.control_rig"></a>

#### control_rig

```python
@property
def control_rig() -> ControlRig
```

(ControlRig):  [Read-Only]

<a id="unreal.ControlRigSequencerBindingProxy.track"></a>

#### track

```python
@property
def track() -> MovieSceneControlRigParameterTrack
```

(MovieSceneControlRigParameterTrack):  [Read-Only]

<a id="unreal.AnimDetailProxyFloat"></a>