## UpdateCustomPoiParams Objects

```python
class UpdateCustomPoiParams(ParamsBase)
```

Update Custom Poi Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CustomPoiAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Api Param")
                 FcustompoiPolicy poiPolicy;
- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``poi_style`` (custompoiStyle):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]

<a id="unreal.UpdateCustomPoiParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             point_entity_eid: str = "",
             poi_style: custompoiStyle = [[[0.000000, 0.000000], ["", ""]],
                                          [
                                              "", [0.000000, 0.000000],
                                              [0.000000, 0.000000],
                                              ["", "", 0]
                                          ]],
             coord_z_ref: int = 0) -> None
```

<a id="unreal.UpdateCustomPoiParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateCustomPoiParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.UpdateCustomPoiParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateCustomPoiParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.UpdateCustomPoiParams.poi_style"></a>

#### poi\_style

```python
@property
def poi_style() -> custompoiStyle
```

(custompoiStyle):  [Read-Write]

<a id="unreal.UpdateCustomPoiParams.poi_style"></a>

#### poi\_style

```python
@poi_style.setter
def poi_style(value: custompoiStyle) -> None
```

<a id="unreal.UpdateCustomPoiParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Api Param")
               FcustompoiPolicy poiPolicy;

<a id="unreal.UpdateCustomPoiParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.HeatMapStyle"></a>