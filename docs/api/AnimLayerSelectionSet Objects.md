## AnimLayerSelectionSet Objects

```python
class AnimLayerSelectionSet(StructBase)
```

Bound object/control rig and the properties/channels it is made of
A layer will consist of a bunch of these

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: AnimLayers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bound_object`` (Object):  [Read-Write]
- ``names`` (Map[Name, AnimLayerPropertyAndChannels]):  [Read-Write] bound object is either a CR or a bound sequencer object

<a id="unreal.AnimLayerSelectionSet.__init__"></a>

#### __init__

```python
def __init__(bound_object: Object = None,
             names: Map[Name, AnimLayerPropertyAndChannels] = {}) -> None
```

<a id="unreal.AnimLayerSelectionSet.bound_object"></a>

#### bound_object

```python
@property
def bound_object() -> Object
```

(Object):  [Read-Write]

<a id="unreal.AnimLayerSelectionSet.bound_object"></a>

#### bound_object

```python
@bound_object.setter
def bound_object(value: Object) -> None
```

<a id="unreal.AnimLayerSelectionSet.names"></a>

#### names

```python
@property
def names() -> Map[Name, AnimLayerPropertyAndChannels]
```

(Map[Name, AnimLayerPropertyAndChannels]):  [Read-Write] bound object is either a CR or a bound sequencer object

<a id="unreal.AnimLayerSelectionSet.names"></a>

#### names

```python
@names.setter
def names(value: Map[Name, AnimLayerPropertyAndChannels]) -> None
```

<a id="unreal.AnimLayerSectionItem"></a>