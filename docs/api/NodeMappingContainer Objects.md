## NodeMappingContainer Objects

```python
class NodeMappingContainer(Object)
```

Node Mapping Container Class
* This saves source items, and target items, and mapping between
* Used by Retargeting, Control Rig mapping. Will need to improve interface better

**C++ Source:**

- **Module**: Engine
- **File**: NodeMappingContainer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``source_asset`` (Object):  [Read-Write] source asset that is used to create source
  should be UNodeMappingProviderInterface
- ``source_items`` (Map[Name, NodeItem]):  [Read-Only]
- ``source_to_target`` (Map[Name, Name]):  [Read-Write]
- ``target_asset`` (Object):  [Read-Write] source asset that is used to create target
  should be UNodeMappingProviderInterface
- ``target_items`` (Map[Name, NodeItem]):  [Read-Only]

<a id="unreal.PoseAsset"></a>