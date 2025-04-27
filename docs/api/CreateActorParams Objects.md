## CreateActorParams Objects

```python
class CreateActorParams(StructBase)
```

FCreateActorParams is a collection of input data intended to be passed to
UModelingObjectsCreationAPI::CreateNewActor().

**C++ Source:**

- **Plugin**: MeshModelingToolset
- **Module**: ModelingComponents
- **File**: ModelingObjectsCreationAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_name`` (str):  [Read-Write] The base name of the new Actor
- ``target_world`` (World):  [Read-Write] The World/Level the new Actor should be created in (if known).
- ``template_actor`` (Actor):  [Read-Write] input data
  deprecated: TemplateActor is being deprecated. Please use TemplateAsset instead.
- ``template_asset`` (Object):  [Read-Write] A template Asset used to determine the type of Actor to spawn.
- ``transform`` (Transform):  [Read-Write] The 3D local-to-world transform for the new actor

<a id="unreal.CreateActorParams.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.CreateActorParams.template_actor"></a>

#### template_actor

```python
@property
def template_actor() -> Actor
```

(Actor):  [Read-Write] input data
deprecated: TemplateActor is being deprecated. Please use TemplateAsset instead.

<a id="unreal.CreateActorParams.template_actor"></a>

#### template_actor

```python
@template_actor.setter
def template_actor(value: Actor) -> None
```

<a id="unreal.CreateActorResult"></a>