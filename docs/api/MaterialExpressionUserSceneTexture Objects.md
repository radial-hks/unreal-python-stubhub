## MaterialExpressionUserSceneTexture Objects

```python
class MaterialExpressionUserSceneTexture(MaterialExpression)
```

Material Expression User Scene Texture

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionUserSceneTexture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clamped`` (bool):  [Read-Write] Whether to clamp the texture lookup.  Necessary when sampling a UserSceneTexture at reduced resolution with filtering, to avoid blending out of bounds pixels.
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``filtered`` (bool):  [Read-Write] Whether to use point sampled texture lookup (default) or using [bi-linear] filtered (can be slower, avoid faceted lock with distortions)
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``user_scene_texture`` (Name):  [Read-Write] User Scene Texture (screen space texture with a user specified name, written by a previous PostProcess shader) to make a lookup into

<a id="unreal.MaterialExpressionVectorNoise"></a>