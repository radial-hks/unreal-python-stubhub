## MaterialExpressionSceneTexture Objects

```python
class MaterialExpressionSceneTexture(MaterialExpression)
```

Material Expression Scene Texture

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionSceneTexture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``filtered`` (bool):  [Read-Write] Whether to use point sampled texture lookup (default) or using [bi-linear] filtered (can be slower, avoid faceted lock with distortions), some SceneTextures cannot be filtered
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``scene_texture_id`` (SceneTextureId):  [Read-Write] Which scene texture (screen aligned texture) we want to make a lookup into

<a id="unreal.MaterialExpressionScreenPosition"></a>