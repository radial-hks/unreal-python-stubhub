## ColumnarHeatMapEntityAtom Objects

```python
class ColumnarHeatMapEntityAtom(EntityAtomBase)
```

USTRUCT(BlueprintType)
struct COVERINGAPIENTITY_API FColumnarData
{
       GENERATED_USTRUCT_BODY()
               UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "HeatMapStyle")
               FVector point;
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "HeatMapStyle")
               float value = 40;

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: ColumnarHeatMapEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``brush_diameter`` (float):  [Read-Write] cube:方柱, cylinder:圆柱, needle:针状, frame:线框
- ``columnar_width`` (float):  [Read-Write]
- ``enable_gap`` (bool):  [Read-Write]
- ``gradient_setting`` (Array[str]):  [Read-Write]
- ``mapping_height_range`` (Vector2D):  [Read-Write]
- ``mapping_value_range`` (Vector2D):  [Read-Write]
- ``type`` (str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ColumnarHeatMapAtom")
                 int CoordZRef = 0;
         UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ColumnarHeatMapAtom")
                 double CoordZ = 0;

<a id="unreal.ColumnarHeatMapEntityAtom.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ColumnarHeatMapAtom")
               int CoordZRef = 0;
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ColumnarHeatMapAtom")
               double CoordZ = 0;

<a id="unreal.ColumnarHeatMapEntityAtom.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.ColumnarHeatMapEntityAtom.brush_diameter"></a>

#### brush\_diameter

```python
@property
def brush_diameter() -> float
```

(float):  [Read-Write] cube:方柱, cylinder:圆柱, needle:针状, frame:线框

<a id="unreal.ColumnarHeatMapEntityAtom.brush_diameter"></a>

#### brush\_diameter

```python
@brush_diameter.setter
def brush_diameter(value: float) -> None
```

<a id="unreal.ColumnarHeatMapEntityAtom.mapping_value_range"></a>

#### mapping\_value\_range

```python
@property
def mapping_value_range() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.ColumnarHeatMapEntityAtom.mapping_value_range"></a>

#### mapping\_value\_range

```python
@mapping_value_range.setter
def mapping_value_range(value: Vector2D) -> None
```

<a id="unreal.ColumnarHeatMapEntityAtom.columnar_width"></a>

#### columnar\_width

```python
@property
def columnar_width() -> float
```

(float):  [Read-Write]

<a id="unreal.ColumnarHeatMapEntityAtom.columnar_width"></a>

#### columnar\_width

```python
@columnar_width.setter
def columnar_width(value: float) -> None
```

<a id="unreal.ColumnarHeatMapEntityAtom.mapping_height_range"></a>

#### mapping\_height\_range

```python
@property
def mapping_height_range() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.ColumnarHeatMapEntityAtom.mapping_height_range"></a>

#### mapping\_height\_range

```python
@mapping_height_range.setter
def mapping_height_range(value: Vector2D) -> None
```

<a id="unreal.ColumnarHeatMapEntityAtom.enable_gap"></a>

#### enable\_gap

```python
@property
def enable_gap() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ColumnarHeatMapEntityAtom.enable_gap"></a>

#### enable\_gap

```python
@enable_gap.setter
def enable_gap(value: bool) -> None
```

<a id="unreal.ColumnarHeatMapEntityAtom.gradient_setting"></a>

#### gradient\_setting

```python
@property
def gradient_setting() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.ColumnarHeatMapEntityAtom.gradient_setting"></a>

#### gradient\_setting

```python
@gradient_setting.setter
def gradient_setting(value: Array[str]) -> None
```

<a id="unreal.PointValueAtom"></a>