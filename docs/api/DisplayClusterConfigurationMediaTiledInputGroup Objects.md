## DisplayClusterConfigurationMediaTiledInputGroup Objects

```python
class DisplayClusterConfigurationMediaTiledInputGroup(StructBase)
```

* Media input group (ICVFX, Tiled)

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Media.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cluster_nodes`` (DisplayClusterConfigurationClusterItemReferenceList):  [Read-Write] Cluster nodes that use media source below
- ``tiles`` (Array[DisplayClusterConfigurationMediaUniformTileInput]):  [Read-Write] Tile mapping. Maps tiles to media sources.

<a id="unreal.DisplayClusterConfigurationMediaTiledInputGroup.__init__"></a>

#### __init__

```python
def __init__(
    cluster_nodes: DisplayClusterConfigurationClusterItemReferenceList = [[]],
    tiles: Array[DisplayClusterConfigurationMediaUniformTileInput] = []
) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaTiledInputGroup.cluster_nodes"></a>

#### cluster_nodes

```python
@property
def cluster_nodes() -> DisplayClusterConfigurationClusterItemReferenceList
```

(DisplayClusterConfigurationClusterItemReferenceList):  [Read-Write] Cluster nodes that use media source below

<a id="unreal.DisplayClusterConfigurationMediaTiledInputGroup.cluster_nodes"></a>

#### cluster_nodes

```python
@cluster_nodes.setter
def cluster_nodes(
        value: DisplayClusterConfigurationClusterItemReferenceList) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaTiledInputGroup.tiles"></a>

#### tiles

```python
@property
def tiles() -> Array[DisplayClusterConfigurationMediaUniformTileInput]
```

(Array[DisplayClusterConfigurationMediaUniformTileInput]):  [Read-Write] Tile mapping. Maps tiles to media sources.

<a id="unreal.DisplayClusterConfigurationMediaTiledInputGroup.tiles"></a>

#### tiles

```python
@tiles.setter
def tiles(
        value: Array[DisplayClusterConfigurationMediaUniformTileInput]
) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaUniformTileInput"></a>