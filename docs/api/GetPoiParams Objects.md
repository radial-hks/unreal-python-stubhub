## GetPoiParams Objects

```python
class GetPoiParams(ResultBase)
```

Get Poi Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: PoiAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Api Param")
                 FpoiPolicy poiPolicy;
- ``message`` (str):  [Read-Write]
- ``poi_style`` (poiStyle):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.GetPoiParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             point_entity_eid: str = "",
             poi_style: poiStyle = [[[0.000000, 0.000000], ["", ""]],
                                    [
                                        "", [0.000000, 0.000000],
                                        [0.000000, 0.000000], ["", "", 0]
                                    ]],
             coord_z_ref: int = 0) -> None
```

<a id="unreal.GetPoiParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.GetPoiParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.GetPoiParams.poi_style"></a>

#### poi\_style

```python
@property
def poi_style() -> poiStyle
```

(poiStyle):  [Read-Write]

<a id="unreal.GetPoiParams.poi_style"></a>

#### poi\_style

```python
@poi_style.setter
def poi_style(value: poiStyle) -> None
```

<a id="unreal.GetPoiParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Api Param")
               FpoiPolicy poiPolicy;

<a id="unreal.GetPoiParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.CreatePoisParams"></a>