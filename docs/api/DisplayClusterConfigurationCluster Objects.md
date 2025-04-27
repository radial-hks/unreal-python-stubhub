## DisplayClusterConfigurationCluster Objects

```python
class DisplayClusterConfigurationCluster(DisplayClusterConfigurationData_Base)
```

Display Cluster Configuration Cluster

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``failover`` (DisplayClusterConfigurationFailoverSettings):  [Read-Write]
- ``network`` (DisplayClusterConfigurationNetworkSettings):  [Read-Write]
- ``nodes`` (Map[str, DisplayClusterConfigurationClusterNode]):  [Read-Write]
- ``primary_node`` (DisplayClusterConfigurationPrimaryNode):  [Read-Write]
- ``sync`` (DisplayClusterConfigurationClusterSync):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationCluster.primary_node"></a>

#### primary_node

```python
@property
def primary_node() -> DisplayClusterConfigurationPrimaryNode
```

(DisplayClusterConfigurationPrimaryNode):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationCluster.master_node"></a>

#### master_node

```python
@property
def master_node() -> DisplayClusterConfigurationPrimaryNode
```

deprecated: 'master_node' was renamed to 'primary_node'.

<a id="unreal.DisplayClusterConfigurationCluster.sync"></a>

#### sync

```python
@property
def sync() -> DisplayClusterConfigurationClusterSync
```

(DisplayClusterConfigurationClusterSync):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationCluster.network"></a>

#### network

```python
@property
def network() -> DisplayClusterConfigurationNetworkSettings
```

(DisplayClusterConfigurationNetworkSettings):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationCluster.failover"></a>

#### failover

```python
@property
def failover() -> DisplayClusterConfigurationFailoverSettings
```

(DisplayClusterConfigurationFailoverSettings):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationCluster.nodes"></a>

#### nodes

```python
@property
def nodes() -> Map[str, DisplayClusterConfigurationClusterNode]
```

(Map[str, DisplayClusterConfigurationClusterNode]):  [Read-Only]

<a id="unreal.DisplayClusterConfigurationCluster.get_referenced_mesh_names"></a>

#### get_referenced_mesh_names

```python
def get_referenced_mesh_names() -> Array[str]
```

x.get_referenced_mesh_names() -> Array[str]
Return all references to meshes from policy, and other

Returns:
    Array[str]: 

    out_mesh_names (Array[str]):

<a id="unreal.DisplayClusterConfigurationCluster.get_node_ids"></a>

#### get_node_ids

```python
def get_node_ids() -> Array[str]
```

x.get_node_ids() -> Array[str]
Nodes API

Returns:
    Array[str]: 

    out_node_ids (Array[str]):

<a id="unreal.DisplayClusterConfigurationCluster.get_node"></a>

#### get_node

```python
def get_node(node_id: str) -> DisplayClusterConfigurationClusterNode
```

x.get_node(node_id) -> DisplayClusterConfigurationClusterNode
Get Node

Args:
    node_id (str): 

Returns:
    DisplayClusterConfigurationClusterNode:

<a id="unreal.DisplayClusterConfigurationData"></a>