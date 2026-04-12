## RangeStyle Objects

```python
class RangeStyle(StructBase)
```

Range Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RangeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (str):  [Read-Write]
- ``fill_area_type`` (str):  [Read-Write]
- ``height`` (float):  [Read-Write]
- ``stroke_weight`` (float):  [Read-Write]
- ``type`` (str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RangeStyle")
                 TArray<FVector> Points{ {0,0,0},{100,0,0},{100,100,0} };

<a id="unreal.RangeStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(type: str = "",
             fill_area_type: str = "",
             height: float = 0.000000,
             stroke_weight: float = 0.000000,
             color: str = "") -> None
```

<a id="unreal.RangeStyle.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RangeStyle")
               TArray<FVector> Points{ {0,0,0},{100,0,0},{100,100,0} };

<a id="unreal.RangeStyle.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.RangeStyle.fill_area_type"></a>

#### fill\_area\_type

```python
@property
def fill_area_type() -> str
```

(str):  [Read-Write]

<a id="unreal.RangeStyle.fill_area_type"></a>

#### fill\_area\_type

```python
@fill_area_type.setter
def fill_area_type(value: str) -> None
```

<a id="unreal.RangeStyle.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write]

<a id="unreal.RangeStyle.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.RangeStyle.stroke_weight"></a>

#### stroke\_weight

```python
@property
def stroke_weight() -> float
```

(float):  [Read-Write]

<a id="unreal.RangeStyle.stroke_weight"></a>

#### stroke\_weight

```python
@stroke_weight.setter
def stroke_weight(value: float) -> None
```

<a id="unreal.RangeStyle.color"></a>

#### color

```python
@property
def color() -> str
```

(str):  [Read-Write]

<a id="unreal.RangeStyle.color"></a>

#### color

```python
@color.setter
def color(value: str) -> None
```

<a id="unreal.CreateRangeParams"></a>