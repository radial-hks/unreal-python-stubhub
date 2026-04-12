## CreatePoisParams Objects

```python
class CreatePoisParams(StructBase)
```

Create Pois Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: PoiAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Api Param")
                 FpoiPolicy poiPolicy;
- ``poi_style`` (poiStyle):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]

<a id="unreal.CreatePoisParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(point_entity_eid: str = "",
             poi_style: poiStyle = [[[0.000000, 0.000000], ["", ""]],
                                    [
                                        "", [0.000000, 0.000000],
                                        [0.000000, 0.000000], ["", "", 0]
                                    ]],
             coord_z_ref: int = 0) -> None
```

<a id="unreal.CreatePoisParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.CreatePoisParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.CreatePoisParams.poi_style"></a>

#### poi\_style

```python
@property
def poi_style() -> poiStyle
```

(poiStyle):  [Read-Write]

<a id="unreal.CreatePoisParams.poi_style"></a>

#### poi\_style

```python
@poi_style.setter
def poi_style(value: poiStyle) -> None
```

<a id="unreal.CreatePoisParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Api Param")
               FpoiPolicy poiPolicy;

<a id="unreal.CreatePoisParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.CreatePoiParams_Batch"></a>