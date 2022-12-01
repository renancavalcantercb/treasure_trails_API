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
        "quantity": "10001",
        "rank": "25"
      },
      {
        "tier": "Medium",
        "quantity": "822",
        "rank": "818"
      },
      {
        "tier": "Hard",
        "quantity": "2624",
        "rank": "2595"
      },
      {
        "tier": "Elite",
        "quantity": "1141",
        "rank": "2829"
      },
      {
        "tier": "Master",
        "quantity": "801",
        "rank": "1326"
      }
    ]
    ```
