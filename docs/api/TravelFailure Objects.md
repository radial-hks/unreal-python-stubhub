## TravelFailure Objects

```python
class TravelFailure(EnumBase)
```

Types of server travel failures broadcast by the engine

**C++ Source:**

- **Module**: Engine
- **File**: EngineBaseTypes.h

<a id="unreal.TravelFailure.NO_LEVEL"></a>

#### NO_LEVEL

0: No level found in the loaded package

<a id="unreal.TravelFailure.LOAD_MAP_FAILURE"></a>

#### LOAD_MAP_FAILURE

1: LoadMap failed on travel (about to Browse to default map)

<a id="unreal.TravelFailure.INVALID_URL"></a>

#### INVALID_URL

2: Invalid URL specified

<a id="unreal.TravelFailure.PACKAGE_MISSING"></a>

#### PACKAGE_MISSING

3: A package is missing on the client

<a id="unreal.TravelFailure.PACKAGE_VERSION"></a>

#### PACKAGE_VERSION

4: A package version mismatch has occurred between client and server

<a id="unreal.TravelFailure.NO_DOWNLOAD"></a>

#### NO_DOWNLOAD

5: A package is missing and the client is unable to download the file

<a id="unreal.TravelFailure.TRAVEL_FAILURE"></a>

#### TRAVEL_FAILURE

6: General travel failure

<a id="unreal.TravelFailure.CHEAT_COMMANDS"></a>

#### CHEAT_COMMANDS

7: Cheat commands have been used disabling travel

<a id="unreal.TravelFailure.PENDING_NET_GAME_CREATE_FAILURE"></a>

#### PENDING_NET_GAME_CREATE_FAILURE

8: Failed to create the pending net game for travel

<a id="unreal.TravelFailure.CLOUD_SAVE_FAILURE"></a>

#### CLOUD_SAVE_FAILURE

9: Failed to save before travel

<a id="unreal.TravelFailure.SERVER_TRAVEL_FAILURE"></a>

#### SERVER_TRAVEL_FAILURE

10: There was an error during a server travel to a new map

<a id="unreal.TravelFailure.CLIENT_TRAVEL_FAILURE"></a>

#### CLIENT_TRAVEL_FAILURE

11: There was an error during a client travel to a new map

<a id="unreal.ApplicationState"></a>