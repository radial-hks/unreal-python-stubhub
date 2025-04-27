## DisplayClusterBlueprintAPIImpl Objects

```python
class DisplayClusterBlueprintAPIImpl(Object)
```

Blueprint API interface implementation

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayCluster
- **File**: DisplayClusterBlueprintAPIImpl.h

<a id="unreal.DisplayClusterBlueprintAPIImpl.send_cluster_event_json_to"></a>

#### send_cluster_event_json_to

```python
def send_cluster_event_json_to(address: str, port: int,
                               event: DisplayClusterClusterEventJson,
                               primary_only: bool) -> None
```

x.send_cluster_event_json_to(address, port, event, primary_only) -> None
Send Cluster Event Json To
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Args:
    address (str): 
    port (int32): 
    event (DisplayClusterClusterEventJson): 
    primary_only (bool):

<a id="unreal.DisplayClusterBlueprintAPIImpl.send_cluster_event_binary_to"></a>

#### send_cluster_event_binary_to

```python
def send_cluster_event_binary_to(address: str, port: int,
                                 event: DisplayClusterClusterEventBinary,
                                 primary_only: bool) -> None
```

x.send_cluster_event_binary_to(address, port, event, primary_only) -> None
Send Cluster Event Binary To
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Args:
    address (str): 
    port (int32): 
    event (DisplayClusterClusterEventBinary): 
    primary_only (bool):

<a id="unreal.DisplayClusterBlueprintAPIImpl.remove_cluster_event_listener"></a>

#### remove_cluster_event_listener

```python
def remove_cluster_event_listener(
        listener: DisplayClusterClusterEventListener) -> None
```

x.remove_cluster_event_listener(listener) -> None
Remove Cluster Event Listener
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Args:
    listener (DisplayClusterClusterEventListener):

<a id="unreal.DisplayClusterBlueprintAPIImpl.is_secondary"></a>

#### is_secondary

```python
def is_secondary() -> bool
```

x.is_secondary() -> bool
Is Secondary
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Returns:
    bool:

<a id="unreal.DisplayClusterBlueprintAPIImpl.is_primary"></a>

#### is_primary

```python
def is_primary() -> bool
```

x.is_primary() -> bool
Is Primary
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Returns:
    bool:

<a id="unreal.DisplayClusterBlueprintAPIImpl.is_module_initialized"></a>

#### is_module_initialized

```python
def is_module_initialized() -> bool
```

x.is_module_initialized() -> bool
Is Module Initialized
deprecated: This function has been deprecated and will be removed soon.

Returns:
    bool:

<a id="unreal.DisplayClusterBlueprintAPIImpl.is_backup"></a>

#### is_backup

```python
def is_backup() -> bool
```

x.is_backup() -> bool
Is Backup
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Returns:
    bool:

<a id="unreal.DisplayClusterBlueprintAPIImpl.get_root_actor"></a>

#### get_root_actor

```python
def get_root_actor() -> DisplayClusterRootActor
```

x.get_root_actor() -> DisplayClusterRootActor
Get Root Actor
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Returns:
    DisplayClusterRootActor:

<a id="unreal.DisplayClusterBlueprintAPIImpl.get_operation_mode"></a>

#### get_operation_mode

```python
def get_operation_mode() -> DisplayClusterOperationMode
```

x.get_operation_mode() -> DisplayClusterOperationMode
Get Operation Mode
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Returns:
    DisplayClusterOperationMode:

<a id="unreal.DisplayClusterBlueprintAPIImpl.get_node_id"></a>

#### get_node_id

```python
def get_node_id() -> str
```

x.get_node_id() -> str
Get Node Id
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Returns:
    str:

<a id="unreal.DisplayClusterBlueprintAPIImpl.get_cluster_role"></a>

#### get_cluster_role

```python
def get_cluster_role() -> DisplayClusterNodeRole
```

x.get_cluster_role() -> DisplayClusterNodeRole
Get Cluster Role
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Returns:
    DisplayClusterNodeRole:

<a id="unreal.DisplayClusterBlueprintAPIImpl.get_active_nodes_amount"></a>

#### get_active_nodes_amount

```python
def get_active_nodes_amount() -> int
```

x.get_active_nodes_amount() -> int32
Get Active Nodes Amount
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Returns:
    int32:

<a id="unreal.DisplayClusterBlueprintAPIImpl.get_active_node_ids"></a>

#### get_active_node_ids

```python
def get_active_node_ids() -> Array[str]
```

x.get_active_node_ids() -> Array[str]
Get Active Node Ids
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Returns:
    Array[str]: 

    out_node_ids (Array[str]):

<a id="unreal.DisplayClusterBlueprintAPIImpl.emit_cluster_event_json"></a>

#### emit_cluster_event_json

```python
def emit_cluster_event_json(event: DisplayClusterClusterEventJson,
                            primary_only: bool) -> None
```

x.emit_cluster_event_json(event, primary_only) -> None
Emit Cluster Event Json
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Args:
    event (DisplayClusterClusterEventJson): 
    primary_only (bool):

<a id="unreal.DisplayClusterBlueprintAPIImpl.emit_cluster_event_binary"></a>

#### emit_cluster_event_binary

```python
def emit_cluster_event_binary(event: DisplayClusterClusterEventBinary,
                              primary_only: bool) -> None
```

x.emit_cluster_event_binary(event, primary_only) -> None
Emit Cluster Event Binary
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Args:
    event (DisplayClusterClusterEventBinary): 
    primary_only (bool):

<a id="unreal.DisplayClusterBlueprintAPIImpl.add_cluster_event_listener"></a>

#### add_cluster_event_listener

```python
def add_cluster_event_listener(
        listener: DisplayClusterClusterEventListener) -> None
```

x.add_cluster_event_listener(listener) -> None
Add Cluster Event Listener
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Args:
    listener (DisplayClusterClusterEventListener):

<a id="unreal.DisplayClusterBlueprintLib"></a>