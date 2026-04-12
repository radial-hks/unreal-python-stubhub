## CreateCustomPoisParams Objects

```python
class CreateCustomPoisParams(StructBase)
```

Create Custom Pois Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CustomPoiAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Api Param")
                 FcustompoiPolicy poiPolicy;
- ``poi_style`` (custompoiStyle):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]

<a id="unreal.CreateCustomPoisParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(point_entity_eid: str = "",
             poi_style: custompoiStyle = [[[0.000000, 0.000000], ["", ""]],
                                          [
                                              "", [0.000000, 0.000000],
                                              [0.000000, 0.000000],
                                              ["", "", 0]
                                          ]],
             coord_z_ref: int = 0) -> None
```

<a id="unreal.CreateCustomPoisParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateCustomPoisParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.CreateCustomPoisParams.poi_style"></a>

#### poi\_style

```python
@property
def poi_style() -> custompoiStyle
```

(custompoiStyle):  [Read-Write]

<a id="unreal.CreateCustomPoisParams.poi_style"></a>

#### poi\_style

```python
@poi_style.setter
def poi_style(value: custompoiStyle) -> None
```

<a id="unreal.CreateCustomPoisParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Api Param")
               FcustompoiPolicy poiPolicy;

<a id="unreal.CreateCustomPoisParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.CreateCustomPoiParams_Batch"></a>