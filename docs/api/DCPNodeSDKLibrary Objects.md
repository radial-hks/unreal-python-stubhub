## DCPNodeSDKLibrary Objects

```python
class DCPNodeSDKLibrary(BlueprintFunctionLibrary)
```

DCPNode SDKLibrary

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPNodeSDKLibrary.h

<a id="unreal.DCPNodeSDKLibrary.dcpsdk_show_all_node"></a>

#### dcpsdk\_show\_all\_node

```python
@classmethod
def dcpsdk_show_all_node(cls) -> DCPSDKResult
```

X.dcpsdk_show_all_node() -> DCPSDKResult
DCPSDK Show All Node

Returns:
    DCPSDKResult:

<a id="unreal.DCPNodeSDKLibrary.dcpsdk_set_other_nodes_visibility"></a>

#### dcpsdk\_set\_other\_nodes\_visibility

```python
@classmethod
def dcpsdk_set_other_nodes_visibility(cls,
                                      node_ids: Array[int],
                                      visible: bool = False) -> DCPSDKResult
```

X.dcpsdk_set_other_nodes_visibility(node_ids, visible=False) -> DCPSDKResult
DCPSDK Set Other Nodes Visibility

Args:
    node_ids (Array[int32]): 
    visible (bool): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPNodeSDKLibrary.dcpsdk_set_node_visibility_only"></a>

#### dcpsdk\_set\_node\_visibility\_only

```python
@classmethod
def dcpsdk_set_node_visibility_only(cls, node_id: int,
                                    visible: bool) -> DCPSDKResult
```

X.dcpsdk_set_node_visibility_only(node_id, visible) -> DCPSDKResult
DCPSDK Set Node Visibility Only

Args:
    node_id (int32): 
    visible (bool): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPNodeSDKLibrary.dcpsdk_set_node_visibility"></a>

#### dcpsdk\_set\_node\_visibility

```python
@classmethod
def dcpsdk_set_node_visibility(cls,
                               node_i_ds: Array[int],
                               visible: bool,
                               save: bool = False) -> DCPSDKResult
```

X.dcpsdk_set_node_visibility(node_i_ds, visible, save=False) -> DCPSDKResult
DCPSDK Set Node Visibility

Args:
    node_i_ds (Array[int32]): 
    visible (bool): 
    save (bool): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPNodeSDKLibrary.dcpsdk_set_node_location"></a>

#### dcpsdk\_set\_node\_location

```python
@classmethod
def dcpsdk_set_node_location(cls, node_id: int,
                             location: Vector) -> DCPSDKResult
```

X.dcpsdk_set_node_location(node_id, location) -> DCPSDKResult
DCPSDK Set Node Location

Args:
    node_id (int32): 
    location (Vector): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPNodeSDKLibrary.dcpsdk_set_node_highlight"></a>

#### dcpsdk\_set\_node\_highlight

```python
@classmethod
def dcpsdk_set_node_highlight(
        cls,
        node_id: int,
        hight_light: bool,
        exclusion: bool,
        hight_style: HierarchyMeshHighlightStyle = []) -> DCPSDKResult
```

X.dcpsdk_set_node_highlight(node_id, hight_light, exclusion, hight_style=[]) -> DCPSDKResult
DCPSDK Set Node Highlight

Args:
    node_id (int32): 
    hight_light (bool): 
    exclusion (bool): 
    hight_style (HierarchyMeshHighlightStyle): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPNodeSDKLibrary.dcpsdk_set_node_focused"></a>

#### dcpsdk\_set\_node\_focused

```python
@classmethod
def dcpsdk_set_node_focused(cls, node_id: int, camera_rotation: Rotator,
                            distance_factor: float,
                            fly_time: float) -> DCPSDKResult
```

X.dcpsdk_set_node_focused(node_id, camera_rotation, distance_factor, fly_time) -> DCPSDKResult
DCPSDK Set Node Focused

Args:
    node_id (int32): 
    camera_rotation (Rotator): 
    distance_factor (float): 
    fly_time (float): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPNodeSDKLibrary.dcpsdk_room_high_light"></a>

#### dcpsdk\_room\_high\_light

```python
@classmethod
def dcpsdk_room_high_light(
        cls,
        node_ids: Array[int],
        is_visible: bool,
        hight_style: HierarchyMeshHighlightStyle = []) -> DCPSDKResult
```

X.dcpsdk_room_high_light(node_ids, is_visible, hight_style=[]) -> DCPSDKResult
DCPSDK Room High Light

Args:
    node_ids (Array[int32]): 
    is_visible (bool): 
    hight_style (HierarchyMeshHighlightStyle): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPNodeSDKLibrary.dcpsdk_isolate_single_node"></a>

#### dcpsdk\_isolate\_single\_node

```python
@classmethod
def dcpsdk_isolate_single_node(cls, node_id: int) -> DCPSDKResult
```

X.dcpsdk_isolate_single_node(node_id) -> DCPSDKResult
DCPSDK Isolate Single Node

Args:
    node_id (int32): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPNodeSDKLibrary.dcpsdk_get_node_transform"></a>

#### dcpsdk\_get\_node\_transform

```python
@classmethod
def dcpsdk_get_node_transform(
        cls, node_id: int) -> Tuple[DCPSDKResult, Transform, Box]
```

X.dcpsdk_get_node_transform(node_id) -> (DCPSDKResult, trans=Transform, box=Box)
DCPSDK Get Node Transform

Args:
    node_id (int32): 

Returns:
    tuple: 

    trans (Transform): 

    box (Box):

<a id="unreal.DCPNodeSDKLibrary.dcpsdk_get_node_ids_by_label"></a>

#### dcpsdk\_get\_node\_ids\_by\_label

```python
@classmethod
def dcpsdk_get_node_ids_by_label(
        cls, label: str) -> Tuple[DCPSDKResult, Array[int]]
```

X.dcpsdk_get_node_ids_by_label(label) -> (DCPSDKResult, node_ids=Array[int32])
DCPSDK Get Node Ids by Label

Args:
    label (str): 

Returns:
    Array[int32]: 

    node_ids (Array[int32]):

<a id="unreal.DCPNodeSDKLibrary.dcpsdk_dcp_room_focus"></a>

#### dcpsdk\_dcp\_room\_focus

```python
@classmethod
def dcpsdk_dcp_room_focus(cls, node_ids: Array[int], camera_rotation: Rotator,
                          distance_factor: float,
                          fly_time: float) -> DCPSDKResult
```

X.dcpsdk_dcp_room_focus(node_ids, camera_rotation, distance_factor, fly_time) -> DCPSDKResult
DCPSDK Dcp Room Focus

Args:
    node_ids (Array[int32]): 
    camera_rotation (Rotator): 
    distance_factor (float): 
    fly_time (float): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPNodeSDKLibrary.dcpsdk_clear_room_high_light"></a>

#### dcpsdk\_clear\_room\_high\_light

```python
@classmethod
def dcpsdk_clear_room_high_light(cls) -> DCPSDKResult
```

X.dcpsdk_clear_room_high_light() -> DCPSDKResult
DCPSDK Clear Room High Light

Returns:
    DCPSDKResult:

<a id="unreal.DCPTransformAnchorObject"></a>