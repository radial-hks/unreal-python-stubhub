## CreateCustomPoiParams Objects

```python
class CreateCustomPoiParams(ParamsBase)
```

USTRUCT(BlueprintType)
struct COVERINGAPIDEFINE_API FcustompoiPolicy
{
       GENERATED_USTRUCT_BODY()

       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "custompoiStyle")
               bool adaptive = false;
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "custompoiStyle")
               bool always_show_label = false;
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "custompoiStyle")
               FString show_label_range = TEXT("0,6000");
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "custompoiStyle")
               FString animation_type = TEXT("bounce");
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "custompoiStyle")
               float animation_duration_time = 0.7f;

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CustomPoiAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Api Param")
                 FpoiPolicy poiPolicy;
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``poi_style`` (custompoiStyle):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]

<a id="unreal.CreateCustomPoiParams.__init__"></a>

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

<a id="unreal.CreateCustomPoiParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateCustomPoiParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.CreateCustomPoiParams.poi_style"></a>

#### poi\_style

```python
@property
def poi_style() -> custompoiStyle
```

(custompoiStyle):  [Read-Write]

<a id="unreal.CreateCustomPoiParams.poi_style"></a>

#### poi\_style

```python
@poi_style.setter
def poi_style(value: custompoiStyle) -> None
```

<a id="unreal.CreateCustomPoiParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Api Param")
               FpoiPolicy poiPolicy;

<a id="unreal.CreateCustomPoiParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.GetCustomPoiParams"></a>