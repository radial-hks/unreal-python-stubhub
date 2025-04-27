## AnimLayerControlRigObject Objects

```python
class AnimLayerControlRigObject(StructBase)
```

Anim Layer Control Rig Object

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: AnimLayers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_names`` (Array[Name]):  [Read-Write]
- ``control_rig`` (ControlRig):  [Read-Write]

<a id="unreal.AnimLayerControlRigObject.__init__"></a>

#### __init__

```python
def __init__(control_rig: ControlRig = None,
             control_names: Array[Name] = []) -> None
```

<a id="unreal.AnimLayerControlRigObject.control_rig"></a>

#### control_rig

```python
@property
def control_rig() -> ControlRig
```

(ControlRig):  [Read-Write]

<a id="unreal.AnimLayerControlRigObject.control_rig"></a>

#### control_rig

```python
@control_rig.setter
def control_rig(value: ControlRig) -> None
```

<a id="unreal.AnimLayerControlRigObject.control_names"></a>

#### control_names

```python
@property
def control_names() -> Array[Name]
```

(Array[Name]):  [Read-Write]

<a id="unreal.AnimLayerControlRigObject.control_names"></a>

#### control_names

```python
@control_names.setter
def control_names(value: Array[Name]) -> None
```

<a id="unreal.AnimLayerSceneObject"></a>