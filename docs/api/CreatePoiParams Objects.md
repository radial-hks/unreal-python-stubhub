## CreatePoiParams Objects

```python
class CreatePoiParams(ParamsBase)
```

USTRUCT(BlueprintType)
struct COVERINGAPIDEFINE_API FpoiPolicy
{
       GENERATED_USTRUCT_BODY()

       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "poiStyle")
               bool adaptive = false;
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "poiStyle")
               bool always_show_label = false;
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "poiStyle")
               FString show_label_range = TEXT("0,6000");
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "poiStyle")
               FString animation_type = TEXT("bounce");
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "poiStyle")
               float animation_duration_time = 0.7f;

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: PoiAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Api Param")
                 FpoiPolicy poiPolicy;
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``poi_style`` (poiStyle):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]

<a id="unreal.CreatePoiParams.__init__"></a>

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

<a id="unreal.CreatePoiParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.CreatePoiParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.CreatePoiParams.poi_style"></a>

#### poi\_style

```python
@property
def poi_style() -> poiStyle
```

(poiStyle):  [Read-Write]

<a id="unreal.CreatePoiParams.poi_style"></a>

#### poi\_style

```python
@poi_style.setter
def poi_style(value: poiStyle) -> None
```

<a id="unreal.CreatePoiParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Api Param")
               FpoiPolicy poiPolicy;

<a id="unreal.CreatePoiParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.GetPoiParams"></a>