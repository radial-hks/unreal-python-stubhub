## AnimLayerSectionItem Objects

```python
class AnimLayerSectionItem(StructBase)
```

The set with it's section

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: AnimLayers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_layer_set`` (AnimLayerSelectionSet):  [Read-Write]
- ``section`` (MovieSceneSection):  [Read-Write]

<a id="unreal.AnimLayerSectionItem.__init__"></a>

#### __init__

```python
def __init__(anim_layer_set: AnimLayerSelectionSet = [None, {}],
             section: MovieSceneSection = None) -> None
```

<a id="unreal.AnimLayerSectionItem.anim_layer_set"></a>

#### anim_layer_set

```python
@property
def anim_layer_set() -> AnimLayerSelectionSet
```

(AnimLayerSelectionSet):  [Read-Write]

<a id="unreal.AnimLayerSectionItem.anim_layer_set"></a>

#### anim_layer_set

```python
@anim_layer_set.setter
def anim_layer_set(value: AnimLayerSelectionSet) -> None
```

<a id="unreal.AnimLayerSectionItem.section"></a>

#### section

```python
@property
def section() -> MovieSceneSection
```

(MovieSceneSection):  [Read-Write]

<a id="unreal.AnimLayerSectionItem.section"></a>

#### section

```python
@section.setter
def section(value: MovieSceneSection) -> None
```

<a id="unreal.AnimLayerItem"></a>