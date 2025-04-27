## DisplayClusterConfigurationMediaTiledOutputGroup Objects

```python
class DisplayClusterConfigurationMediaTiledOutputGroup(StructBase)
```

* Media output group (ICVFX, Tiled)

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Media.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cluster_nodes`` (DisplayClusterConfigurationClusterItemReferenceList):  [Read-Write] Cluster nodes that export media via MediaOutput below
- ``output_sync_policy`` (DisplayClusterMediaOutputSynchronizationPolicy):  [Read-Write] Media output synchronization policy
- ``tiles`` (Array[DisplayClusterConfigurationMediaUniformTileOutput]):  [Read-Write] Tile mapping. Maps tiles to media outputs.

<a id="unreal.DisplayClusterConfigurationMediaTiledOutputGroup.__init__"></a>

#### __init__

```python
def __init__(
    cluster_nodes: DisplayClusterConfigurationClusterItemReferenceList = [[]],
    tiles: Array[DisplayClusterConfigurationMediaUniformTileOutput] = [],
    output_sync_policy: DisplayClusterMediaOutputSynchronizationPolicy = None
) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaTiledOutputGroup.cluster_nodes"></a>

#### cluster_nodes

```python
@property
def cluster_nodes() -> DisplayClusterConfigurationClusterItemReferenceList
```

(DisplayClusterConfigurationClusterItemReferenceList):  [Read-Write] Cluster nodes that export media via MediaOutput below

<a id="unreal.DisplayClusterConfigurationMediaTiledOutputGroup.cluster_nodes"></a>

#### cluster_nodes

```python
@cluster_nodes.setter
def cluster_nodes(
        value: DisplayClusterConfigurationClusterItemReferenceList) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaTiledOutputGroup.tiles"></a>

#### tiles

```python
@property
def tiles() -> Array[DisplayClusterConfigurationMediaUniformTileOutput]
```

(Array[DisplayClusterConfigurationMediaUniformTileOutput]):  [Read-Write] Tile mapping. Maps tiles to media outputs.

<a id="unreal.DisplayClusterConfigurationMediaTiledOutputGroup.tiles"></a>

#### tiles

```python
@tiles.setter
def tiles(
        value: Array[DisplayClusterConfigurationMediaUniformTileOutput]
) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaTiledOutputGroup.output_sync_policy"></a>

#### output_sync_policy

```python
@property
def output_sync_policy() -> DisplayClusterMediaOutputSynchronizationPolicy
```

(DisplayClusterMediaOutputSynchronizationPolicy):  [Read-Write] Media output synchronization policy

<a id="unreal.DisplayClusterConfigurationMediaTiledOutputGroup.output_sync_policy"></a>

#### output_sync_policy

```python
@output_sync_policy.setter
def output_sync_policy(
        value: DisplayClusterMediaOutputSynchronizationPolicy) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaUniformTileOutput"></a>