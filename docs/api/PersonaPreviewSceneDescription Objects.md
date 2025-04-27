## PersonaPreviewSceneDescription Objects

```python
class PersonaPreviewSceneDescription(Object)
```

Persona Preview Scene Description

**C++ Source:**

- **Module**: Persona
- **File**: PersonaPreviewSceneDescription.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_meshes`` (DataAsset):  [Read-Write]
- ``application_method`` (PreviewAnimationBlueprintApplicationMethod):  [Read-Write] The method by which a preview animation blueprint is applied, either as an overlay layer, or as a linked instance
- ``linked_anim_graph_tag`` (Name):  [Read-Write] The tag to use when applying a preview animation blueprint via LinkAnimGraphByTag
- ``preview_animation_blueprint`` (AnimBlueprint):  [Read-Write] The preview anim blueprint to use
- ``preview_controller`` (type(Class)):  [Read-Write] The method by which the preview is animated
- ``preview_mesh`` (SkeletalMesh):  [Read-Write] The preview mesh to use

<a id="unreal.PersonaPreviewSceneDescription.preview_controller"></a>

#### preview_controller

```python
@property
def preview_controller() -> Class
```

(type(Class)):  [Read-Only] The method by which the preview is animated

<a id="unreal.PersonaToolMenuContext"></a>