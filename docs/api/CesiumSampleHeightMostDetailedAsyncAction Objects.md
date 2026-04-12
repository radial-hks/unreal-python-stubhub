## CesiumSampleHeightMostDetailedAsyncAction Objects

```python
class CesiumSampleHeightMostDetailedAsyncAction(BlueprintAsyncActionBase)
```

Cesium Sample Height Most Detailed Async Action

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumSampleHeightMostDetailedAsyncAction.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_heights_sampled`` (CesiumSampleHeightMostDetailedComplete):  [Read-Write] Called when height has been sampled at all of the given positions. The
  Result property contains an element for each input position and in the same
  order. The Warnings property provides information about problems that were
  encountered while sampling heights.

<a id="unreal.CesiumSampleHeightMostDetailedAsyncAction.on_heights_sampled"></a>

#### on\_heights\_sampled

```python
@property
def on_heights_sampled() -> CesiumSampleHeightMostDetailedComplete
```

(CesiumSampleHeightMostDetailedComplete):  [Read-Write] Called when height has been sampled at all of the given positions. The
Result property contains an element for each input position and in the same
order. The Warnings property provides information about problems that were
encountered while sampling heights.

<a id="unreal.CesiumSampleHeightMostDetailedAsyncAction.on_heights_sampled"></a>

#### on\_heights\_sampled

```python
@on_heights_sampled.setter
def on_heights_sampled(value: CesiumSampleHeightMostDetailedComplete) -> None
```

<a id="unreal.CesiumSubLevelComponent"></a>