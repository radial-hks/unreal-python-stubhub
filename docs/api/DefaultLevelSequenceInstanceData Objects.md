## DefaultLevelSequenceInstanceData Objects

```python
class DefaultLevelSequenceInstanceData(Object)
```

Default instance data class that level sequences understand. Implements IMovieSceneTransformOrigin.

**C++ Source:**

- **Module**: LevelSequence
- **File**: DefaultLevelSequenceInstanceData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``transform_origin`` (Transform):  [Read-Write] Specifies a transform that offsets all absolute transform sections in this sequence. Scale is ignored. Not applied to Relative or Additive sections.
- ``transform_origin_actor`` (Actor):  [Read-Write] When set, this actor's world position will be used as the transform origin for all absolute transform sections

<a id="unreal.DefaultLevelSequenceInstanceData.transform_origin_actor"></a>

#### transform_origin_actor

```python
@property
def transform_origin_actor() -> Actor
```

(Actor):  [Read-Write] When set, this actor's world position will be used as the transform origin for all absolute transform sections

<a id="unreal.DefaultLevelSequenceInstanceData.transform_origin_actor"></a>

#### transform_origin_actor

```python
@transform_origin_actor.setter
def transform_origin_actor(value: Actor) -> None
```

<a id="unreal.DefaultLevelSequenceInstanceData.transform_origin"></a>

#### transform_origin

```python
@property
def transform_origin() -> Transform
```

(Transform):  [Read-Write] Specifies a transform that offsets all absolute transform sections in this sequence. Scale is ignored. Not applied to Relative or Additive sections.

<a id="unreal.DefaultLevelSequenceInstanceData.transform_origin"></a>

#### transform_origin

```python
@transform_origin.setter
def transform_origin(value: Transform) -> None
```

<a id="unreal.DefaultLevelSequenceInstanceData.bp_get_transform_origin"></a>

#### bp_get_transform_origin

```python
def bp_get_transform_origin() -> Transform
```

x.bp_get_transform_origin() -> Transform
Get the transform from which all absolute component transform sections should be relative. Scale is ignored.

Returns:
    Transform:

<a id="unreal.AssetUserData"></a>