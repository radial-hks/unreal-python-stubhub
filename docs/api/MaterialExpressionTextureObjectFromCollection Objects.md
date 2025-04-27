## MaterialExpressionTextureObjectFromCollection Objects

```python
class MaterialExpressionTextureObjectFromCollection(MaterialExpression)
```

Material Expression Texture Object from Collection

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionTextureObjectFromCollection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``const_collection_index`` (int32):  [Read-Write]
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``texture_collection_object`` (TextureCollection):  [Read-Write]
- ``texture_type`` (TextureCollectionMemberType):  [Read-Write]

<a id="unreal.MaterialExpressionTextureObjectFromCollection.texture_collection_object"></a>

#### texture_collection_object

```python
@property
def texture_collection_object() -> TextureCollection
```

(TextureCollection):  [Read-Write]

<a id="unreal.MaterialExpressionTextureObjectFromCollection.texture_collection_object"></a>

#### texture_collection_object

```python
@texture_collection_object.setter
def texture_collection_object(value: TextureCollection) -> None
```

<a id="unreal.MaterialExpressionTextureObjectFromCollection.const_collection_index"></a>

#### const_collection_index

```python
@property
def const_collection_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.MaterialExpressionTextureObjectFromCollection.const_collection_index"></a>

#### const_collection_index

```python
@const_collection_index.setter
def const_collection_index(value: int) -> None
```

<a id="unreal.MaterialExpressionTextureObjectFromCollection.texture_type"></a>

#### texture_type

```python
@property
def texture_type() -> TextureCollectionMemberType
```

(TextureCollectionMemberType):  [Read-Write]

<a id="unreal.MaterialExpressionTextureObjectFromCollection.texture_type"></a>

#### texture_type

```python
@texture_type.setter
def texture_type(value: TextureCollectionMemberType) -> None
```

<a id="unreal.MaterialExpressionTextureObjectParameter"></a>