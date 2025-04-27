## FIZEvaluationMode Objects

```python
class FIZEvaluationMode(EnumBase)
```

Mode that controls where FIZ inputs are sourced from and how they are used to evaluate the LensFile

**C++ Source:**

- **Plugin**: LensComponent
- **Module**: LensComponent
- **File**: LensComponent.h

<a id="unreal.FIZEvaluationMode.USE_LIVE_LINK"></a>

#### USE_LIVE_LINK

0: Evaluate the Lens File with the latest FIZ data received from LiveLink

<a id="unreal.FIZEvaluationMode.USE_CAMERA_SETTINGS"></a>

#### USE_CAMERA_SETTINGS

1: Evaluate the Lens File using the current FIZ settings of the target camera

<a id="unreal.FIZEvaluationMode.USE_RECORDED_VALUES"></a>

#### USE_RECORDED_VALUES

2: Evaluate the Lens File using values recorded in a level sequence (set automatically when the sequence is opened)

<a id="unreal.FIZEvaluationMode.MANUAL"></a>

#### MANUAL

3: Evaluate the Lens File using values set directly in the details panel or via BP/scripting

<a id="unreal.FIZEvaluationMode.DO_NOT_EVALUATE"></a>

#### DO_NOT_EVALUATE

4: Do not evaluate the Lens File

<a id="unreal.FilmbackOverrideSource"></a>