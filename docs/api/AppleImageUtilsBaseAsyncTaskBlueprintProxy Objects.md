## AppleImageUtilsBaseAsyncTaskBlueprintProxy Objects

```python
class AppleImageUtilsBaseAsyncTaskBlueprintProxy(Object)
```

Apple Image Utils Base Async Task Blueprint Proxy

**C++ Source:**

- **Plugin**: AppleImageUtils
- **Module**: AppleImageUtils
- **File**: AppleImageUtilsBlueprintProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``conversion_result`` (AppleImageUtilsImageConversionResult):  [Read-Write]
- ``on_failure`` (AppleImageConversionDelegate):  [Read-Write]
- ``on_success`` (AppleImageConversionDelegate):  [Read-Write]

<a id="unreal.AppleImageUtilsBaseAsyncTaskBlueprintProxy.on_success"></a>

#### on_success

```python
@property
def on_success() -> AppleImageConversionDelegate
```

(AppleImageConversionDelegate):  [Read-Write]

<a id="unreal.AppleImageUtilsBaseAsyncTaskBlueprintProxy.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: AppleImageConversionDelegate) -> None
```

<a id="unreal.AppleImageUtilsBaseAsyncTaskBlueprintProxy.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> AppleImageConversionDelegate
```

(AppleImageConversionDelegate):  [Read-Write]

<a id="unreal.AppleImageUtilsBaseAsyncTaskBlueprintProxy.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: AppleImageConversionDelegate) -> None
```

<a id="unreal.AppleImageUtilsBaseAsyncTaskBlueprintProxy.conversion_result"></a>

#### conversion_result

```python
@property
def conversion_result() -> AppleImageUtilsImageConversionResult
```

(AppleImageUtilsImageConversionResult):  [Read-Only]

<a id="unreal.AndroidPermissionCallbackProxy"></a>