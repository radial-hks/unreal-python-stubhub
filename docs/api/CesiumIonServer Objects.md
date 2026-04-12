## CesiumIonServer Objects

```python
class CesiumIonServer(DataAsset)
```

Defines a Cesium ion Server. This may be the public (SaaS) Cesium ion server
at ion.cesium.com, or it may be a self-hosted instance.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumIonServer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``api_url`` (str):  [Read-Write] The URL of the main API endpoint of the Cesium ion server. For example, for
  the default, public Cesium ion server, this is `https://api.cesium.com`. If
  left blank, the API URL is automatically inferred from the Server URL.
- ``default_ion_access_token`` (str):  [Read-Write] The default token used to access Cesium ion assets at runtime. This token
  is embedded in packaged games for use at runtime.
- ``default_ion_access_token_id`` (str):  [Read-Write] The ID of the default access token to use to access Cesium ion assets at
  runtime. This property may be an empty string, in which case the ID is
  found by searching the logged-in Cesium ion account for the
  DefaultIonAccessToken.
- ``display_name`` (str):  [Read-Write] The name to display for this server.
- ``o_auth2_application_id`` (int64):  [Read-Write] The application ID to use to log in to this server using OAuth2. This
  OAuth2 application must be configured on the server with the exact URL
  `http://127.0.0.1/cesium-for-unreal/oauth2/callback`.
- ``server_url`` (str):  [Read-Write] The main URL of the Cesium ion server. For example, the server URL for the
  public Cesium ion is https://ion.cesium.com.

<a id="unreal.WidgetBlueprintGeneratedClass"></a>