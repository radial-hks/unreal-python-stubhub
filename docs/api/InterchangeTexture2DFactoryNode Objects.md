## InterchangeTexture2DFactoryNode Objects

```python
class InterchangeTexture2DFactoryNode(InterchangeTextureFactoryNode)
```

ns UE::Interchange

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeTexture2DFactoryNode.h

<a id="unreal.InterchangeTexture2DFactoryNode.set_source_blocks"></a>

#### set_source_blocks

```python
def set_source_blocks(source_blocks: Map[int, str]) -> None
```

x.set_source_blocks(source_blocks) -> None
Set the source blocks for the texture.
Using this suggests to the pipeline to consider this texture as a UDIM. The pipeline can choose whether to pass these blocks to the texture factory node.

Args:
    source_blocks (Map[int32, str]): The blocks and their source image that compose the whole texture. The textures must be of the same format and use the same pixel format. The first block in the map is used to determine the accepted texture format and pixel format.

<a id="unreal.InterchangeTexture2DFactoryNode.set_source_block_by_coordinates"></a>

#### set_source_block_by_coordinates

```python
def set_source_block_by_coordinates(x: int, y: int, source_file: str) -> None
```

x.set_source_block_by_coordinates(x, y, source_file) -> None
Set a source block for the texture.

Args:
    x (int32): The X coordinate of the block.
    y (int32): The Y coordinate of the block.
    source_file (str): The source file for that block. The textures must be of the same format and use the same pixel format. The first block in the map is used to determine the accepted texture format and pixel format.

<a id="unreal.InterchangeTexture2DFactoryNode.set_source_block"></a>

#### set_source_block

```python
def set_source_block(block_index: int, source_file: str) -> None
```

x.set_source_block(block_index, source_file) -> None
Set a source block for the texture.

Args:
    block_index (int32): The UDIM index of the block.
    source_file (str): The source file for that block. The textures must be of the same format and use the same pixel format. The first block in the map is used to determine the accepted texture format and pixel format.

<a id="unreal.InterchangeTexture2DFactoryNode.set_custom_address_y"></a>

#### set_custom_address_y

```python
def set_custom_address_y(attribute_value: TextureAddress,
                         add_apply_delegate: bool = True) -> bool
```

x.set_custom_address_y(attribute_value, add_apply_delegate=True) -> bool
Set Custom Address Y

Args:
    attribute_value (TextureAddress): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTexture2DFactoryNode.set_custom_address_x"></a>

#### set_custom_address_x

```python
def set_custom_address_x(attribute_value: TextureAddress,
                         add_apply_delegate: bool = True) -> bool
```

x.set_custom_address_x(attribute_value, add_apply_delegate=True) -> bool
Set Custom Address X

Args:
    attribute_value (TextureAddress): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeTexture2DFactoryNode.get_source_blocks"></a>

#### get_source_blocks

```python
def get_source_blocks() -> Map[int, str]
```

x.get_source_blocks() -> Map[int32, str]
Get the source blocks for the texture.
If the map is empty, the texture is imported as a normal texture using the payload key.

Returns:
    Map[int32, str]:

<a id="unreal.InterchangeTexture2DFactoryNode.get_source_block_by_coordinates"></a>

#### get_source_block_by_coordinates

```python
def get_source_block_by_coordinates(x: int, y: int) -> Optional[str]
```

x.get_source_block_by_coordinates(x, y) -> str or None
Get a source block from the texture.

Args:
    x (int32): The X coordinate of the block.
    y (int32): The Y coordinate of the block.

Returns:
    str or None: True if the source file for the block was found.

    out_source_file (str): The source file for that block if found.

<a id="unreal.InterchangeTexture2DFactoryNode.get_source_block"></a>

#### get_source_block

```python
def get_source_block(block_index: int) -> Optional[str]
```

x.get_source_block(block_index) -> str or None
Get a source block from the texture.

Args:
    block_index (int32): The UDIM Index of the block.

Returns:
    str or None: True if the source file for the block was found.

    out_source_file (str): The source file for that block if found.

<a id="unreal.InterchangeTexture2DFactoryNode.get_custom_address_y"></a>

#### get_custom_address_y

```python
def get_custom_address_y() -> Optional[TextureAddress]
```

x.get_custom_address_y() -> TextureAddress or None
Return false if the Attribute was not set previously.

Returns:
    TextureAddress or None: 

    attribute_value (TextureAddress):

<a id="unreal.InterchangeTexture2DFactoryNode.get_custom_address_x"></a>

#### get_custom_address_x

```python
def get_custom_address_x() -> Optional[TextureAddress]
```

x.get_custom_address_x() -> TextureAddress or None
Return false if the Attribute was not set previously.

Returns:
    TextureAddress or None: 

    attribute_value (TextureAddress):

<a id="unreal.InterchangeTextureCubeArrayFactoryNode"></a>