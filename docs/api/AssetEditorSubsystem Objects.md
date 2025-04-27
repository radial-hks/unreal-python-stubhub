## AssetEditorSubsystem Objects

```python
class AssetEditorSubsystem(EditorSubsystem)
```

UAssetEditorSubsystem

**C++ Source:**

- **Module**: UnrealEd
- **File**: AssetEditorSubsystem.h

<a id="unreal.AssetEditorSubsystem.open_editor_for_assets"></a>

#### open_editor_for_assets

```python
def open_editor_for_assets(
    assets: Array[Object],
    opened_method:
    AssetTypeActivationOpenedMethod = AssetTypeActivationOpenedMethod.EDIT
) -> bool
```

x.open_editor_for_assets(assets, opened_method=AssetTypeActivationOpenedMethod.EDIT) -> bool
Tries to open an editor for all of the specified assets.
If any of the assets are already open, it will not create a new editor for them.
If all assets are of the same type, the supporting AssetTypeAction (if it exists) is responsible for the details of how to handle opening multiple assets at once.

Args:
    assets (Array[Object]): 
    opened_method (AssetTypeActivationOpenedMethod): 

Returns:
    bool:

<a id="unreal.AssetEditorSubsystem.close_all_editors_for_asset"></a>

#### close_all_editors_for_asset

```python
def close_all_editors_for_asset(asset: Object) -> int
```

x.close_all_editors_for_asset(asset) -> int32
Close all active editors for the supplied asset and return the number of asset editors that were closed

Args:
    asset (Object): 

Returns:
    int32:

<a id="unreal.AssetEditorToolkitMenuContext"></a>