## DCPSwitchSDKLibrary Objects

```python
class DCPSwitchSDKLibrary(BlueprintFunctionLibrary)
```

DCPSwitch SDKLibrary

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPSwitchSDKLibrary.h

<a id="unreal.DCPSwitchSDKLibrary.dcpsdk_set_node_response"></a>

#### dcpsdk\_set\_node\_response

```python
@classmethod
def dcpsdk_set_node_response(cls, open: bool) -> DCPSDKResult
```

X.dcpsdk_set_node_response(open) -> DCPSDKResult
DCPSDK Set Node Response

Args:
    open (bool): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPSwitchSDKLibrary.dcpsdk_set_hover_response"></a>

#### dcpsdk\_set\_hover\_response

```python
@classmethod
def dcpsdk_set_hover_response(cls, open: bool) -> DCPSDKResult
```

X.dcpsdk_set_hover_response(open) -> DCPSDKResult
DCPSDK Set Hover Response

Args:
    open (bool): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPSwitchSDKLibrary.dcpsdk_get_node_response"></a>

#### dcpsdk\_get\_node\_response

```python
@classmethod
def dcpsdk_get_node_response(cls) -> Tuple[DCPSDKResult, bool]
```

X.dcpsdk_get_node_response() -> (DCPSDKResult, open=bool)
DCPSDK Get Node Response

Returns:
    bool: 

    open (bool):

<a id="unreal.DCPSwitchSDKLibrary.dcpsdk_get_hover_response"></a>

#### dcpsdk\_get\_hover\_response

```python
@classmethod
def dcpsdk_get_hover_response(cls) -> Tuple[DCPSDKResult, bool]
```

X.dcpsdk_get_hover_response() -> (DCPSDKResult, open=bool)
DCPSDK Get Hover Response

Returns:
    bool: 

    open (bool):

<a id="unreal.DCPSwitchSDKLibrary.dcpsdk_get_click_open"></a>

#### dcpsdk\_get\_click\_open

```python
@classmethod
def dcpsdk_get_click_open(cls, in_asset_pick_type: AssetPickType) -> bool
```

X.dcpsdk_get_click_open(in_asset_pick_type) -> bool
DCPSDK Get Click Open

Args:
    in_asset_pick_type (AssetPickType): 

Returns:
    bool:

<a id="unreal.DCPSwitchSDKLibrary.dcpsdk_get_click_have"></a>

#### dcpsdk\_get\_click\_have

```python
@classmethod
def dcpsdk_get_click_have(cls, in_asset_pick_type: AssetPickType) -> bool
```

X.dcpsdk_get_click_have(in_asset_pick_type) -> bool
DCPSDK Get Click Have

Args:
    in_asset_pick_type (AssetPickType): 

Returns:
    bool:

<a id="unreal.DCPSwitchSDKLibrary.dcpsdk_click_point"></a>

#### dcpsdk\_click\_point

```python
@classmethod
def dcpsdk_click_point(cls, open: bool) -> DCPSDKResult
```

X.dcpsdk_click_point(open) -> DCPSDKResult
DCPSDK Click Point

Args:
    open (bool): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPSwitchSDKLibrary.dcpsdk_click_material"></a>

#### dcpsdk\_click\_material

```python
@classmethod
def dcpsdk_click_material(cls, open: bool) -> DCPSDKResult
```

X.dcpsdk_click_material(open) -> DCPSDKResult
DCPSDK Click Material

Args:
    open (bool): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPSwitchSDKLibrary.dcpsdk_click_high_light"></a>

#### dcpsdk\_click\_high\_light

```python
@classmethod
def dcpsdk_click_high_light(cls, open: bool) -> DCPSDKResult
```

X.dcpsdk_click_high_light(open) -> DCPSDKResult
DCPSDK Click High Light

Args:
    open (bool): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPSwitchSDKLibrary.dcpsdk_click_hidded"></a>

#### dcpsdk\_click\_hidded

```python
@classmethod
def dcpsdk_click_hidded(cls, open: bool) -> DCPSDKResult
```

X.dcpsdk_click_hidded(open) -> DCPSDKResult
DCPSDK Click Hidded

Args:
    open (bool): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPSwitchSDKLibrary.dcpsdk_click_building_layer"></a>

#### dcpsdk\_click\_building\_layer

```python
@classmethod
def dcpsdk_click_building_layer(cls, open: bool) -> DCPSDKResult
```

X.dcpsdk_click_building_layer(open) -> DCPSDKResult
DCPSDK Click Building Layer

Args:
    open (bool): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPWorldSubsystem"></a>