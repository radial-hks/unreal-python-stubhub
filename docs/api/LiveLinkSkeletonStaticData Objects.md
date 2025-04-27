## LiveLinkSkeletonStaticData Objects

```python
class LiveLinkSkeletonStaticData(LiveLinkBaseStaticData)
```

Static data for Animation purposes. Contains data about bones that shouldn't change every frame.

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkAnimationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_names`` (Array[Name]):  [Read-Write] Names of each bone in the skeleton
- ``bone_parents`` (Array[int32]):  [Read-Write] Parent Indices: For each bone it specifies the index of its parent
- ``property_names`` (Array[Name]):  [Read-Write] Names for each curve values that will be sent for each frame

<a id="unreal.LiveLinkSkeletonStaticData.__init__"></a>

#### __init__

```python
def __init__(property_names: Array[Name] = [],
             bone_names: Array[Name] = [],
             bone_parents: Array[int] = []) -> None
```

<a id="unreal.LiveLinkSkeletonStaticData.bone_names"></a>

#### bone_names

```python
@property
def bone_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Names of each bone in the skeleton

<a id="unreal.LiveLinkSkeletonStaticData.bone_names"></a>

#### bone_names

```python
@bone_names.setter
def bone_names(value: Array[Name]) -> None
```

<a id="unreal.LiveLinkSkeletonStaticData.bone_parents"></a>

#### bone_parents

```python
@property
def bone_parents() -> Array[int]
```

(Array[int32]):  [Read-Write] Parent Indices: For each bone it specifies the index of its parent

<a id="unreal.LiveLinkSkeletonStaticData.bone_parents"></a>

#### bone_parents

```python
@bone_parents.setter
def bone_parents(value: Array[int]) -> None
```

<a id="unreal.LiveLinkBaseFrameData"></a>