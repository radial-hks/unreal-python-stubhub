## InterchangeTexture2DNode Objects

```python
class InterchangeTexture2DNode(InterchangeTextureNode)
```

ns UE::Interchange

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeTexture2DNode.h

<a id="unreal.InterchangeTexture2DNode.set_custom_wrap_v"></a>

#### set_custom_wrap_v

```python
def set_custom_wrap_v(attribute_value: InterchangeTextureWrapMode) -> bool
```

x.set_custom_wrap_v(attribute_value) -> bool
Set Custom Wrap V

Args:
    attribute_value (InterchangeTextureWrapMode): 

Returns:
    bool:

<a id="unreal.InterchangeTexture2DNode.set_custom_wrap_u"></a>

#### set_custom_wrap_u

```python
def set_custom_wrap_u(attribute_value: InterchangeTextureWrapMode) -> bool
```

x.set_custom_wrap_u(attribute_value) -> bool
Set Custom Wrap U

Args:
    attribute_value (InterchangeTextureWrapMode): 

Returns:
    bool:

<a id="unreal.InterchangeTexture2DNode.get_source_blocks"></a>

#### get_source_blocks

```python
def get_source_blocks() -> Map[int, str]
```

x.get_source_blocks() -> Map[int32, str]
Get the source blocks for the texture.
If the map is empty, the texture is imported as a normal texture using the payload key.

Returns:
    Map[int32, str]:

<a id="unreal.InterchangeTexture2DNode.get_custom_wrap_v"></a>

#### get_custom_wrap_v

```python
def get_custom_wrap_v() -> Optional[InterchangeTextureWrapMode]
```

x.get_custom_wrap_v() -> InterchangeTextureWrapMode or None
Get Custom Wrap V

Returns:
    InterchangeTextureWrapMode or None: 

    attribute_value (InterchangeTextureWrapMode):

<a id="unreal.InterchangeTexture2DNode.get_custom_wrap_u"></a>

#### get_custom_wrap_u

```python
def get_custom_wrap_u() -> Optional[InterchangeTextureWrapMode]
```

x.get_custom_wrap_u() -> InterchangeTextureWrapMode or None
Get Custom Wrap U

Returns:
    InterchangeTextureWrapMode or None: 

    attribute_value (InterchangeTextureWrapMode):

<a id="unreal.InterchangeTextureBlurNode"></a>