## MaterialExpressionPathTracingBufferTexture Objects

```python
class MaterialExpressionPathTracingBufferTexture(MaterialExpression)
```

Path tracing buffer is only accessable in postprocess material.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionPathTracingBufferTexture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``path_tracing_buffer_texture_id`` (PathTracingBufferTextureId):  [Read-Write] Which path tracing buffer texture we want to make a lookup into.

<a id="unreal.MaterialExpressionPathTracingQualitySwitch"></a>