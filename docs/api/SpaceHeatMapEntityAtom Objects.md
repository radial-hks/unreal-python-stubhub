## SpaceHeatMapEntityAtom Objects

```python
class SpaceHeatMapEntityAtom(EntityAtomBase)
```

USTRUCT(BlueprintType)
struct COVERINGAPIENTITY_API FSpaceHeatMapData_Atom
{
       GENERATED_USTRUCT_BODY()
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "SpaceHeatMapEntityAtom")
               FVector point;
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "SpaceHeatMapEntityAtom")
               float value = 40;

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: SpaceHeatMapEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``brush_diameter`` (float):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "SpaceHeatMapEntityAtom")
                 int CoordZRef = 0;
- ``gradient_setting`` (Array[str]):  [Read-Write]
- ``mapping_value_range`` (Vector2D):  [Read-Write]

<a id="unreal.SpaceHeatMapEntityAtom.brush_diameter"></a>

#### brush\_diameter

```python
@property
def brush_diameter() -> float
```

(float):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "SpaceHeatMapEntityAtom")
               int CoordZRef = 0;

<a id="unreal.SpaceHeatMapEntityAtom.brush_diameter"></a>

#### brush\_diameter

```python
@brush_diameter.setter
def brush_diameter(value: float) -> None
```

<a id="unreal.SpaceHeatMapEntityAtom.mapping_value_range"></a>

#### mapping\_value\_range

```python
@property
def mapping_value_range() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.SpaceHeatMapEntityAtom.mapping_value_range"></a>

#### mapping\_value\_range

```python
@mapping_value_range.setter
def mapping_value_range(value: Vector2D) -> None
```

<a id="unreal.SpaceHeatMapEntityAtom.gradient_setting"></a>

#### gradient\_setting

```python
@property
def gradient_setting() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.SpaceHeatMapEntityAtom.gradient_setting"></a>

#### gradient\_setting

```python
@gradient_setting.setter
def gradient_setting(value: Array[str]) -> None
```

<a id="unreal.Text3DEntityAtom"></a>