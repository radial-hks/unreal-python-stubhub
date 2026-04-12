## WdpPickResult Objects

```python
class WdpPickResult(StructBase)
```

Wdp Pick Result

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpPicker
- **File**: WdpPickResult.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_result`` (PrimitiveComponent):  [Read-Write]
- ``entity_result`` (WdpActorEntity):  [Read-Write]
- ``hit_result`` (HitResult):  [Read-Write]
- ``multi_trace_results`` (Array[HitResult]):  [Read-Write]
- ``point_result`` (Vector):  [Read-Write]

<a id="unreal.WdpPickResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(entity_result: WdpActorEntity = None,
             component_result: PrimitiveComponent = None,
             point_result: Vector = [0.000000, 0.000000, 0.000000],
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

<a id="unreal.WdpPickResult.entity_result"></a>

#### entity\_result

```python
@property
def entity_result() -> WdpActorEntity
```

(WdpActorEntity):  [Read-Only]

<a id="unreal.WdpPickResult.component_result"></a>

#### component\_result

```python
@property
def component_result() -> PrimitiveComponent
```

(PrimitiveComponent):  [Read-Only]

<a id="unreal.WdpPickResult.point_result"></a>

#### point\_result

```python
@property
def point_result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.WdpPickResult.hit_result"></a>

#### hit\_result

```python
@property
def hit_result() -> HitResult
```

(HitResult):  [Read-Only]

<a id="unreal.WdpPickResult.multi_trace_results"></a>

#### multi\_trace\_results

```python
@property
def multi_trace_results() -> Array[HitResult]
```

(Array[HitResult]):  [Read-Only]

<a id="unreal.WdpPickMaterialResult"></a>