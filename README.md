# Treasure Trails API

This is a API to get the stats of a Treasure Trails from a given username in RuneScape 3.

## Usage

`/treasure_trails/{nickname}`

| Parameter | Type | Description |
| --- | --- | --- |
| `username` | `string` | The username of the player you want to get the stats from. |

## Example

+ `/treasure_trails/cutguardlan`
  + `200 OK`
  ```json
    [
      {
        "tier": "Easy",
        "quantity": "7125",
        "rank": "47"
      },
      {
        "tier": "Medium",
        "quantity": "10",
        "rank": "62912"
      },
      {
        "tier": "Hard",
        "quantity": "5016",
        "rank": "1103"
      },
      {
        "tier": "Elite",
        "quantity": "512",
        "rank": "8614"
      },
      {
        "tier": "Master",
        "quantity": "808",
        "rank": "1300"
      }
    ]
  ```
