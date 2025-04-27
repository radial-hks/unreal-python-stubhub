## MaterialExpressionTextureBase Objects

```python
class MaterialExpressionTextureBase(MaterialExpression)
```

Material Expression Texture Base

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionTextureBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``is_default_meshpaint_texture`` (bool):  [Read-Write] Is default selected texture when using mesh paint mode texture painting
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``sampler_type`` (MaterialSamplerType):  [Read-Write]
- ``texture`` (Texture):  [Read-Write]

<a id="unreal.MaterialExpressionTextureBase.texture"></a>

#### texture

```python
@property
def texture() -> Texture
```

(Texture):  [Read-Write]

<a id="unreal.MaterialExpressionTextureBase.texture"></a>

#### texture

```python
@texture.setter
def texture(value: Texture) -> None
```

<a id="unreal.MaterialExpressionTextureBase.sampler_type"></a>

#### sampler_type

```python
@property
def sampler_type() -> MaterialSamplerType
```

(MaterialSamplerType):  [Read-Write]

<a id="unreal.MaterialExpressionTextureBase.sampler_type"></a>

#### sampler_type

```python
@sampler_type.setter
def sampler_type(value: MaterialSamplerType) -> None
```

<a id="unreal.MaterialExpressionTextureSample"></a>