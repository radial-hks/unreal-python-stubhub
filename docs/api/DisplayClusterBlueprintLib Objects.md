## DisplayClusterBlueprintLib Objects

```python
class DisplayClusterBlueprintLib(BlueprintFunctionLibrary)
```

Blueprint API function library

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayCluster
- **File**: DisplayClusterBlueprintLib.h

<a id="unreal.DisplayClusterBlueprintLib.send_cluster_event_json_to"></a>

#### send_cluster_event_json_to

```python
@classmethod
def send_cluster_event_json_to(cls, address: str, port: int,
                               event: DisplayClusterClusterEventJson,
                               primary_only: bool) -> None
```

X.send_cluster_event_json_to(address, port, event, primary_only) -> None
Sends JSON cluster event to a specific target (may be outside of the cluster).

Args:
    address (str): 
    port (int32): 
    event (DisplayClusterClusterEventJson): 
    primary_only (bool):

<a id="unreal.DisplayClusterBlueprintLib.send_cluster_event_binary_to"></a>

#### send_cluster_event_binary_to

```python
@classmethod
def send_cluster_event_binary_to(cls, address: str, port: int,
                                 event: DisplayClusterClusterEventBinary,
                                 primary_only: bool) -> None
```

X.send_cluster_event_binary_to(address, port, event, primary_only) -> None
Sends binary cluster event to a specific target (may be outside of the cluster).

Args:
    address (str): 
    port (int32): 
    event (DisplayClusterClusterEventBinary): 
    primary_only (bool):

<a id="unreal.DisplayClusterBlueprintLib.remove_cluster_event_listener"></a>

#### remove_cluster_event_listener

```python
@classmethod
def remove_cluster_event_listener(
        cls, listener: DisplayClusterClusterEventListener) -> None
```

X.remove_cluster_event_listener(listener) -> None
Removes cluster event listener.

Args:
    listener (DisplayClusterClusterEventListener):

<a id="unreal.DisplayClusterBlueprintLib.is_secondary"></a>

#### is_secondary

```python
@classmethod
def is_secondary(cls) -> bool
```

X.is_secondary() -> bool
Returns true if current node is a secondary node in a cluster.

Returns:
    bool:

<a id="unreal.DisplayClusterBlueprintLib.is_primary"></a>

#### is_primary

```python
@classmethod
def is_primary(cls) -> bool
```

X.is_primary() -> bool
Returns true if current node is a primary node in a cluster.

Returns:
    bool:

<a id="unreal.DisplayClusterBlueprintLib.is_backup"></a>

#### is_backup

```python
@classmethod
def is_backup(cls) -> bool
```

X.is_backup() -> bool
Returns true if current node is a backup node in a cluster.

Returns:
    bool:

<a id="unreal.DisplayClusterBlueprintLib.get_root_actor"></a>

#### get_root_actor

```python
@classmethod
def get_root_actor(cls) -> DisplayClusterRootActor
```

X.get_root_actor() -> DisplayClusterRootActor
Returns currently active root actor.

Returns:
    DisplayClusterRootActor:

<a id="unreal.DisplayClusterBlueprintLib.get_operation_mode"></a>

#### get_operation_mode

```python
@classmethod
def get_operation_mode(cls) -> DisplayClusterOperationMode
```

X.get_operation_mode() -> DisplayClusterOperationMode
Returns current operation mode.

Returns:
    DisplayClusterOperationMode:

<a id="unreal.DisplayClusterBlueprintLib.get_node_id"></a>

#### get_node_id

```python
@classmethod
def get_node_id(cls) -> str
```

X.get_node_id() -> str
Returns Id of the current node in a cluster.

Returns:
    str:

<a id="unreal.DisplayClusterBlueprintLib.get_cluster_role"></a>

#### get_cluster_role

```python
@classmethod
def get_cluster_role(cls) -> DisplayClusterNodeRole
```

X.get_cluster_role() -> DisplayClusterNodeRole
Returns the role of the current cluster node.

Returns:
    DisplayClusterNodeRole:

<a id="unreal.DisplayClusterBlueprintLib.get_api"></a>

#### get_api

```python
@classmethod
def get_api(cls) -> DisplayClusterBlueprintAPI
```

X.get_api() -> DisplayClusterBlueprintAPI
Get API
deprecated: GetAPI has been deprecated. All functions are now available in the main blueprint functions list under 'nDisplay' category.

Returns:
    DisplayClusterBlueprintAPI: 

    out_api (DisplayClusterBlueprintAPI):

<a id="unreal.DisplayClusterBlueprintLib.get_active_nodes_amount"></a>

#### get_active_nodes_amount

```python
@classmethod
def get_active_nodes_amount(cls) -> int
```

X.get_active_nodes_amount() -> int32
Returns amount of active nodes in a cluster.

Returns:
    int32:

<a id="unreal.DisplayClusterBlueprintLib.get_active_node_ids"></a>

#### get_active_node_ids

```python
@classmethod
def get_active_node_ids(cls) -> Array[str]
```

X.get_active_node_ids() -> Array[str]
Returns List of the active nodes in the runtime cluster node in a cluster.

Returns:
    Array[str]: 

    out_node_ids (Array[str]):

<a id="unreal.DisplayClusterBlueprintLib.find_light_cards_for_root_actor"></a>

#### find_light_cards_for_root_actor

```python
@classmethod
def find_light_cards_for_root_actor(
        cls, root_actor: DisplayClusterRootActor
) -> Set[DisplayClusterLightCardActor]
```

X.find_light_cards_for_root_actor(root_actor) -> Set[DisplayClusterLightCardActor]
Gets a list of all light card actors on the level linked to the specified root actor.

Args:
    root_actor (DisplayClusterRootActor): 

Returns:
    Set[DisplayClusterLightCardActor]: 

    out_light_cards (Set[DisplayClusterLightCardActor]):

<a id="unreal.DisplayClusterBlueprintLib.find_chromakey_cards_for_root_actor"></a>

#### find_chromakey_cards_for_root_actor

```python
@classmethod
def find_chromakey_cards_for_root_actor(
    cls, root_actor: DisplayClusterRootActor
) -> Set[DisplayClusterChromakeyCardActor]
```

X.find_chromakey_cards_for_root_actor(root_actor) -> Set[DisplayClusterChromakeyCardActor]
Gets a list of all chromakey card actors on the level linked to the specified root actor.

Args:
    root_actor (DisplayClusterRootActor): 

Returns:
    Set[DisplayClusterChromakeyCardActor]: 

    out_chromakey_cards (Set[DisplayClusterChromakeyCardActor]):

<a id="unreal.DisplayClusterBlueprintLib.emit_cluster_event_json"></a>

#### emit_cluster_event_json

```python
@classmethod
def emit_cluster_event_json(cls, event: DisplayClusterClusterEventJson,
                            primary_only: bool) -> None
```

X.emit_cluster_event_json(event, primary_only) -> None
Emits JSON cluster event.

Args:
    event (DisplayClusterClusterEventJson): 
    primary_only (bool):

<a id="unreal.DisplayClusterBlueprintLib.emit_cluster_event_binary"></a>

#### emit_cluster_event_binary

```python
@classmethod
def emit_cluster_event_binary(cls, event: DisplayClusterClusterEventBinary,
                              primary_only: bool) -> None
```

X.emit_cluster_event_binary(event, primary_only) -> None
Emits binary cluster event.

Args:
    event (DisplayClusterClusterEventBinary): 
    primary_only (bool):

<a id="unreal.DisplayClusterBlueprintLib.duplicate_light_cards"></a>

#### duplicate_light_cards

```python
@classmethod
def duplicate_light_cards(
    cls, original_lightcards: Array[DisplayClusterLightCardActor]
) -> Array[DisplayClusterLightCardActor]
```

X.duplicate_light_cards(original_lightcards) -> Array[DisplayClusterLightCardActor]
Create duplicates of a list of existing light cards.

Args:
    original_lightcards (Array[DisplayClusterLightCardActor]): 

Returns:
    Array[DisplayClusterLightCardActor]: 

    out_new_light_cards (Array[DisplayClusterLightCardActor]):

<a id="unreal.DisplayClusterBlueprintLib.create_light_card"></a>

#### create_light_card

```python
@classmethod
def create_light_card(
        cls,
        root_actor: DisplayClusterRootActor) -> DisplayClusterLightCardActor
```

X.create_light_card(root_actor) -> DisplayClusterLightCardActor
Create a new light card parented to the given nDisplay root actor.

Args:
    root_actor (DisplayClusterRootActor): 

Returns:
    DisplayClusterLightCardActor:

<a id="unreal.DisplayClusterBlueprintLib.add_cluster_event_listener"></a>

#### add_cluster_event_listener

```python
@classmethod
def add_cluster_event_listener(
        cls, listener: DisplayClusterClusterEventListener) -> None
```

X.add_cluster_event_listener(listener) -> None
Adds cluster event listener.

Args:
    listener (DisplayClusterClusterEventListener):

<a id="unreal.DisplayClusterCameraComponent"></a>