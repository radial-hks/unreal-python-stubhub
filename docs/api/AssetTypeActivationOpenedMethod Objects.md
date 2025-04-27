## AssetTypeActivationOpenedMethod Objects

```python
class AssetTypeActivationOpenedMethod(EnumBase)
```

(jcotton) This enum has been extracted into a separate header as it would ideally live in IAssetTypeActions.h or AssetTypeActions_Base.h,
however these files are included without module linking (IncludePathModuleNames) in several other modules which makes adding a UENUM() not
possible without refactoring.
// Types of permissions allowed when attempting to open an asset in editor via activation (EAssetTypeActivationMethod)

**C++ Source:**

- **Module**: AssetTools
- **File**: AssetTypeActivationOpenedMethod.h

<a id="unreal.AssetTypeActivationOpenedMethod.EDIT"></a>

#### EDIT

0

<a id="unreal.AssetTypeActivationOpenedMethod.VIEW"></a>

#### VIEW

1

<a id="unreal.ReloadPackagesInteractionMode"></a>