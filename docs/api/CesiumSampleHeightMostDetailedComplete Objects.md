## CesiumSampleHeightMostDetailedComplete Objects

```python
class CesiumSampleHeightMostDetailedComplete(MulticastDelegateBase)
```

The delegate used to asynchronously return sampled heights.

Args:
    result (Array[CesiumSampleHeightResult]): The result of the height sampling. This array contains the outputs for each input cartographic position. Each result has a HeightSampled property indicating whether the height was successfully sampled at that position, and a LongitudeLatitudeHeight property with the complete position, including the sampled height. If the sample was unsuccessful, the original position is returned.
    warnings (Array[str]): Provides information about problems, if any, that were encountered while sampling heights.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumSampleHeightMostDetailedAsyncAction.h

<a id="unreal.CesiumSampleHeightMostDetailedComplete.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.CompletedFlight"></a>