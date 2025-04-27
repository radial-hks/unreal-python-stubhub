## ImportanceTexture Objects

```python
class ImportanceTexture(StructBase)
```

Texture processed for importance sampling
Holds marginal PDF of the rows, as well as the PDF of each row

**C++ Source:**

- **Module**: Engine
- **File**: ImportanceSamplingLibrary.h

<a id="unreal.ImportanceTexture.__init__"></a>

#### __init__

```python
def __init__(
        texture: Texture2D = None,
        weighting_func: ImportanceWeight = ImportanceWeight.LUMINANCE) -> None
```

<a id="unreal.ScalarParameterValue"></a>