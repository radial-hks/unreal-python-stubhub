## AnimLayerObjects Objects

```python
class AnimLayerObjects(StructBase)
```

Anim Layer Objects

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: AnimLayers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_rig_objects`` (Array[AnimLayerControlRigObject]):  [Read-Write]
- ``scene_objects`` (Array[AnimLayerSceneObject]):  [Read-Write]

<a id="unreal.AnimLayerObjects.__init__"></a>

#### \_\_init\_\_

```python
def __init__(control_rig_objects: Array[AnimLayerControlRigObject] = [],
             scene_objects: Array[AnimLayerSceneObject] = []) -> None
```

<a id="unreal.AnimLayerObjects.control_rig_objects"></a>

#### control\_rig\_objects

```python
@property
def control_rig_objects() -> Array[AnimLayerControlRigObject]
```

(Array[AnimLayerControlRigObject]):  [Read-Write]

<a id="unreal.AnimLayerObjects.control_rig_objects"></a>

#### control\_rig\_objects

```python
@control_rig_objects.setter
def control_rig_objects(value: Array[AnimLayerControlRigObject]) -> None
```

<a id="unreal.AnimLayerObjects.scene_objects"></a>

#### scene\_objects

```python
@property
def scene_objects() -> Array[AnimLayerSceneObject]
```

(Array[AnimLayerSceneObject]):  [Read-Write]

<a id="unreal.AnimLayerObjects.scene_objects"></a>

#### scene\_objects

```python
@scene_objects.setter
def scene_objects(value: Array[AnimLayerSceneObject]) -> None
```

<a id="unreal.RigSpacePickerBakeSettings"></a>