## InterchangeCommonPipelineDataFactoryNode Objects

```python
class InterchangeCommonPipelineDataFactoryNode(InterchangeFactoryBaseNode)
```

This factory node is where pipelines can set global data that can be used by factories.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeCommonPipelineDataFactoryNode.h

<a id="unreal.InterchangeCommonPipelineDataFactoryNode.set_custom_global_offset_transform"></a>

#### set_custom_global_offset_transform

```python
def set_custom_global_offset_transform(
        node_container: InterchangeBaseNodeContainer,
        attribute_value: Transform) -> bool
```

x.set_custom_global_offset_transform(node_container, attribute_value) -> bool
Pipelines can set a global transform. Factories will use this global offset when importing assets.

Args:
    node_container (InterchangeBaseNodeContainer): 
    attribute_value (Transform): 

Returns:
    bool:

<a id="unreal.InterchangeCommonPipelineDataFactoryNode.set_bake_pivot_meshes"></a>

#### set_bake_pivot_meshes

```python
def set_bake_pivot_meshes(attribute_value: bool) -> bool
```

x.set_bake_pivot_meshes(attribute_value) -> bool
Pipelines can set this Bake Meshes setting. Factories use this to identify whether they should apply global transforms to static meshes and skeletal meshes.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeCommonPipelineDataFactoryNode.set_bake_meshes"></a>

#### set_bake_meshes

```python
def set_bake_meshes(attribute_value: bool) -> bool
```

x.set_bake_meshes(attribute_value) -> bool
Pipelines can set this Bake Meshes setting. Factories use this to identify whether they should apply global transforms to static meshes and skeletal meshes.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeCommonPipelineDataFactoryNode.get_custom_global_offset_transform"></a>

#### get_custom_global_offset_transform

```python
def get_custom_global_offset_transform() -> Optional[Transform]
```

x.get_custom_global_offset_transform() -> Transform or None
Return the global offset transform set by the pipelines.

Returns:
    Transform or None: 

    attribute_value (Transform):

<a id="unreal.InterchangeCommonPipelineDataFactoryNode.get_bake_pivot_meshes"></a>

#### get_bake_pivot_meshes

```python
def get_bake_pivot_meshes() -> Optional[bool]
```

x.get_bake_pivot_meshes() -> bool or None
Return the value of the Bake Meshes setting set by the pipelines.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeCommonPipelineDataFactoryNode.get_bake_meshes"></a>

#### get_bake_meshes

```python
def get_bake_meshes() -> Optional[bool]
```

x.get_bake_meshes() -> bool or None
Return the value of the Bake Meshes setting set by the pipelines.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMaterialFactoryNode"></a>