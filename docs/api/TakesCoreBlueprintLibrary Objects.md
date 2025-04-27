## TakesCoreBlueprintLibrary Objects

```python
class TakesCoreBlueprintLibrary(BlueprintFunctionLibrary)
```

Takes Core Blueprint Library

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakesCore
- **File**: TakesCoreBlueprintLibrary.h

<a id="unreal.TakesCoreBlueprintLibrary.set_on_take_recorder_take_number_changed"></a>

#### set_on_take_recorder_take_number_changed

```python
@classmethod
def set_on_take_recorder_take_number_changed(
    cls, on_take_recorder_take_number_changed: OnTakeRecorderTakeNumberChanged
) -> None
```

X.set_on_take_recorder_take_number_changed(on_take_recorder_take_number_changed) -> None
Called when the take number is changed.

Args:
    on_take_recorder_take_number_changed (OnTakeRecorderTakeNumberChanged):

<a id="unreal.TakesCoreBlueprintLibrary.set_on_take_recorder_slate_changed"></a>

#### set_on_take_recorder_slate_changed

```python
@classmethod
def set_on_take_recorder_slate_changed(
        cls,
        on_take_recorder_slate_changed: OnTakeRecorderSlateChanged) -> None
```

X.set_on_take_recorder_slate_changed(on_take_recorder_slate_changed) -> None
Called when the slate is changed.

Args:
    on_take_recorder_slate_changed (OnTakeRecorderSlateChanged):

<a id="unreal.TakesCoreBlueprintLibrary.find_takes"></a>

#### find_takes

```python
@classmethod
def find_takes(cls, slate: str, take_number: int = 0) -> Array[AssetData]
```

X.find_takes(slate, take_number=0) -> Array[AssetData]
Find all the existing takes that were recorded with the specified slate

Args:
    slate (str): The slate to filter by
    take_number (int32): The take number to filter by. <=0 denotes all takes

Returns:
    Array[AssetData]:

<a id="unreal.TakesCoreBlueprintLibrary.compute_next_take_number"></a>

#### compute_next_take_number

```python
@classmethod
def compute_next_take_number(cls, slate: str) -> int
```

X.compute_next_take_number(slate) -> int32
Compute the next unused sequential take number for the specified slate

Args:
    slate (str): 

Returns:
    int32:

<a id="unreal.MovieSceneTakeSection"></a>