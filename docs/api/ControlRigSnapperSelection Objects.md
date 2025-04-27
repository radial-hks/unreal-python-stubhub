## ControlRigSnapperSelection Objects

```python
class ControlRigSnapperSelection(StructBase)
```

Selection from the UI to Snap To. Contains a set of Actors and/or Control Rigs to snap onto or from.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: ControlRigSnapper.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actors`` (Array[ActorForWorldTransforms]):  [Read-Write]
- ``control_rigs`` (Array[ControlRigForWorldTransforms]):  [Read-Write]

<a id="unreal.ControlRigSnapperSelection.__init__"></a>

#### __init__

```python
def __init__(actors: Array[ActorForWorldTransforms] = [],
             control_rigs: Array[ControlRigForWorldTransforms] = []) -> None
```

<a id="unreal.ControlRigSnapperSelection.actors"></a>

#### actors

```python
@property
def actors() -> Array[ActorForWorldTransforms]
```

(Array[ActorForWorldTransforms]):  [Read-Write]

<a id="unreal.ControlRigSnapperSelection.actors"></a>

#### actors

```python
@actors.setter
def actors(value: Array[ActorForWorldTransforms]) -> None
```

<a id="unreal.ControlRigSnapperSelection.control_rigs"></a>

#### control_rigs

```python
@property
def control_rigs() -> Array[ControlRigForWorldTransforms]
```

(Array[ControlRigForWorldTransforms]):  [Read-Write]

<a id="unreal.ControlRigSnapperSelection.control_rigs"></a>

#### control_rigs

```python
@control_rigs.setter
def control_rigs(value: Array[ControlRigForWorldTransforms]) -> None
```

<a id="unreal.PreviewableWidgetVariant"></a>