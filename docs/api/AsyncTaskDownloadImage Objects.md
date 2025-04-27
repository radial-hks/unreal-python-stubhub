## AsyncTaskDownloadImage Objects

```python
class AsyncTaskDownloadImage(BlueprintAsyncActionBase)
```

Async Task Download Image

**C++ Source:**

- **Module**: UMG
- **File**: AsyncTaskDownloadImage.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_fail`` (DownloadImageDelegate):  [Read-Write]
- ``on_success`` (DownloadImageDelegate):  [Read-Write]

<a id="unreal.AsyncTaskDownloadImage.on_success"></a>

#### on_success

```python
@property
def on_success() -> DownloadImageDelegate
```

(DownloadImageDelegate):  [Read-Write]

<a id="unreal.AsyncTaskDownloadImage.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: DownloadImageDelegate) -> None
```

<a id="unreal.AsyncTaskDownloadImage.on_fail"></a>

#### on_fail

```python
@property
def on_fail() -> DownloadImageDelegate
```

(DownloadImageDelegate):  [Read-Write]

<a id="unreal.AsyncTaskDownloadImage.on_fail"></a>

#### on_fail

```python
@on_fail.setter
def on_fail(value: DownloadImageDelegate) -> None
```

<a id="unreal.GameViewportSubsystem"></a>