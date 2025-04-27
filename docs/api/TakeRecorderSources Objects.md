## TakeRecorderSources Objects

```python
class TakeRecorderSources(Object)
```

A list of sources to record for any given take. Stored as meta-data on ULevelSequence through ULevelSequence::FindMetaData<UTakeRecorderSources>

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakesCore
- **File**: TakeRecorderSources.h

<a id="unreal.TakeRecorderSources.start_recording_source"></a>

#### start_recording_source

```python
def start_recording_source(sources: Array[TakeRecorderSource],
                           current_frame_time: QualifiedTime) -> None
```

x.start_recording_source(sources, current_frame_time) -> None
Calls the recording initialization flows on each of the specified sources.

Args:
    sources (Array[TakeRecorderSource]): 
    current_frame_time (QualifiedTime):

<a id="unreal.TakeRecorderSources.remove_source"></a>

#### remove_source

```python
def remove_source(source: TakeRecorderSource) -> None
```

x.remove_source(source) -> None
Remove the specified source from this list

Args:
    source (TakeRecorderSource): The source to remove

<a id="unreal.TakeRecorderSources.get_sources_copy"></a>

#### get_sources_copy

```python
def get_sources_copy() -> Array[TakeRecorderSource]
```

x.get_sources_copy() -> Array[TakeRecorderSource]
Retrieves a copy of the list of sources that are being recorded. This is intended for Blueprint usages which cannot
use TArrayView.
DO NOT MODIFY THIS ARRAY, modifications will be lost.

Returns:
    Array[TakeRecorderSource]:

<a id="unreal.TakeRecorderSources.add_source"></a>

#### add_source

```python
def add_source(source_type: Class) -> TakeRecorderSource
```

x.add_source(source_type) -> TakeRecorderSource
Add a new source to this source list of the templated type

Args:
    source_type (type(Class)): The class type of the source to add

Returns:
    TakeRecorderSource: An instance of the specified source type

<a id="unreal.TakesCoreBlueprintLibrary"></a>