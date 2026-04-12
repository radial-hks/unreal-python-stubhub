## DCPBuildingLayerSDKLibrary Objects

```python
class DCPBuildingLayerSDKLibrary(BlueprintFunctionLibrary)
```

DCPBuilding Layer SDKLibrary

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPBuildingLayerSDKLibrary.h

<a id="unreal.DCPBuildingLayerSDKLibrary.dcpsdk_start_building_layer"></a>

#### dcpsdk\_start\_building\_layer

```python
@classmethod
def dcpsdk_start_building_layer(cls) -> DCPSDKResult
```

X.dcpsdk_start_building_layer() -> DCPSDKResult
DCPSDK Start Building Layer

Returns:
    DCPSDKResult:

<a id="unreal.DCPBuildingLayerSDKLibrary.dcpsdk_set_building_layer"></a>

#### dcpsdk\_set\_building\_layer

```python
@classmethod
def dcpsdk_set_building_layer(
        cls, building_layer: DCPBuildingLayers) -> DCPSDKResult
```

X.dcpsdk_set_building_layer(building_layer) -> DCPSDKResult
DCPSDK Set Building Layer

Args:
    building_layer (DCPBuildingLayers): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPBuildingLayerSDKLibrary.dcpsdk_move_building_layer"></a>

#### dcpsdk\_move\_building\_layer

```python
@classmethod
def dcpsdk_move_building_layer(cls, normal: Vector,
                               comp: SceneComponent) -> DCPSDKResult
```

X.dcpsdk_move_building_layer(normal, comp) -> DCPSDKResult
DCPSDK Move Building Layer

Args:
    normal (Vector): 
    comp (SceneComponent): 

Returns:
    DCPSDKResult:

<a id="unreal.DCPBuildingLayerSDKLibrary.dcpsdk_end_building_layer"></a>

#### dcpsdk\_end\_building\_layer

```python
@classmethod
def dcpsdk_end_building_layer(cls) -> DCPSDKResult
```

X.dcpsdk_end_building_layer() -> DCPSDKResult
DCPSDK End Building Layer

Returns:
    DCPSDKResult:

<a id="unreal.DCPBuildingLayerSDKLibrary.dcpsdk_clear_building_layer"></a>

#### dcpsdk\_clear\_building\_layer

```python
@classmethod
def dcpsdk_clear_building_layer(cls) -> DCPSDKResult
```

X.dcpsdk_clear_building_layer() -> DCPSDKResult
DCPSDK Clear Building Layer

Returns:
    DCPSDKResult:

<a id="unreal.DCPCommonLibrary"></a>