## AesWaterEditorActionParams\_SplitContour Objects

```python
class AesWaterEditorActionParams_SplitContour(AesEditorSimpleActionParams)
```

轮廓线切割工具的参数类

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEditorMode
- **File**: AesWaterEditorAction_SplitContour.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``snap_distance`` (float):  [Read-Write] 吸附距离阈值（厘米）
  当鼠标靠近顶点时，自动吸附到顶点

<a id="unreal.AesWaterEditorActionParams_SplitContour.snap_distance"></a>

#### snap\_distance

```python
@property
def snap_distance() -> float
```

(float):  [Read-Write] 吸附距离阈值（厘米）
当鼠标靠近顶点时，自动吸附到顶点

<a id="unreal.AesWaterEditorActionParams_SplitContour.snap_distance"></a>

#### snap\_distance

```python
@snap_distance.setter
def snap_distance(value: float) -> None
```

<a id="unreal.AesWaterEditorCommandParams_SplitContour"></a>