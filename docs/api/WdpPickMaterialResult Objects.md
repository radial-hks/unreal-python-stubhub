## WdpPickMaterialResult Objects

```python
class WdpPickMaterialResult(StructBase)
```

Wdp Pick Material Result

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpPicker
- **File**: WdpPickResult.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_result`` (PrimitiveComponent):  [Read-Write]
- ``entity_result`` (IWdpEntity):  [Read-Write]
- ``hit_result`` (HitResult):  [Read-Write]
- ``material_index`` (int32):  [Read-Write]
- ``material_name`` (str):  [Read-Write]
- ``multi_trace_results`` (Array[HitResult]):  [Read-Write]

<a id="unreal.WdpPickMaterialResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(entity_result: IWdpEntity = None,
             component_result: PrimitiveComponent = None,
             material_name: str = "",
             material_index: int = 0,
             hit_result: HitResult = [
                 False, False, 1.000000, 0.000000,
                 [0.000000, 0.000000,
                  0.000000], [0.000000, 0.000000,
                              0.000000], [0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000, 0.000000], None, None, None, "None",
                 "None", 0, 0, 0, [0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000, 0.000000]
             ],
             multi_trace_results: Array[HitResult] = []) -> None
```

<a id="unreal.WdpPickMaterialResult.entity_result"></a>

#### entity\_result

```python
@property
def entity_result() -> IWdpEntity
```

(IWdpEntity):  [Read-Only]

<a id="unreal.WdpPickMaterialResult.component_result"></a>

#### component\_result

```python
@property
def component_result() -> PrimitiveComponent
```

(PrimitiveComponent):  [Read-Only]

<a id="unreal.WdpPickMaterialResult.material_name"></a>

#### material\_name

```python
@property
def material_name() -> str
```

(str):  [Read-Only]

<a id="unreal.WdpPickMaterialResult.material_index"></a>

#### material\_index

```python
@property
def material_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.WdpPickMaterialResult.hit_result"></a>

#### hit\_result

```python
@property
def hit_result() -> HitResult
```

(HitResult):  [Read-Only]

<a id="unreal.WdpPickMaterialResult.multi_trace_results"></a>

#### multi\_trace\_results

```python
@property
def multi_trace_results() -> Array[HitResult]
```

(Array[HitResult]):  [Read-Only]

<a id="unreal.WdpAssetDescription"></a>